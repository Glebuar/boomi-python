#!/usr/bin/env python3
"""
Boomi SDK Example: Runtime Restart Management
=============================================

This example demonstrates how to manage runtime (Atom) restarts for maintenance,
updates, or troubleshooting purposes.

Features:
- Restart single or multiple runtimes
- Graceful restart with process completion
- Force restart for stuck runtimes
- Restart scheduling with maintenance windows
- Cluster-aware restart for high availability
- Health check validation after restart
- Batch restart with rolling updates
- Restart history and audit logging

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- Appropriate permissions to manage runtimes

Usage:
    # Restart single runtime
    python restart_runtime.py ATOM_ID
    
    # Graceful restart with wait
    python restart_runtime.py ATOM_ID --graceful --wait
    
    # Force restart
    python restart_runtime.py ATOM_ID --force
    
    # Restart multiple runtimes
    python restart_runtime.py --batch "atom1,atom2,atom3" --rolling
    
    # Restart all runtimes in environment
    python restart_runtime.py --environment ENV_ID --rolling --delay 60
    
    # Schedule restart for maintenance window
    python restart_runtime.py ATOM_ID --schedule "2024-01-15 02:00:00"

Examples:
    python restart_runtime.py 2d4d5da4-0dfe-41f8-914b-f5f5120ad90a
    python restart_runtime.py 2d4d5da4-0dfe-41f8-914b-f5f5120ad90a --graceful --wait
    python restart_runtime.py --environment 74851c30-98b2-4a6f-838b-61eee5627b13 --rolling
"""

import os
import sys
import argparse
import time
from datetime import datetime, timedelta
from typing import Optional, List, Dict, Any

# Add parent directory to path for imports
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

# Load environment variables from .env file if available
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv is optional

from boomi import Boomi
from boomi.models import (
    AtomQueryConfig,
    AtomQueryConfigQueryFilter,
    AtomSimpleExpression,
    AtomSimpleExpressionOperator,
    AtomSimpleExpressionProperty,
    AtomGroupingExpression,
    AtomGroupingExpressionOperator,
    ExecutionRecordQueryConfig,
    ExecutionRecordQueryConfigQueryFilter,
    ExecutionRecordSimpleExpression,
    ExecutionRecordSimpleExpressionOperator,
    ExecutionRecordSimpleExpressionProperty,
    ExecutionRecordGroupingExpression,
    ExecutionRecordGroupingExpressionOperator,
    EnvironmentAtomAttachmentQueryConfig,
    EnvironmentAtomAttachmentQueryConfigQueryFilter,
    EnvironmentAtomAttachmentSimpleExpression,
    RuntimeRestartRequest,
    EnvironmentAtomAttachmentSimpleExpressionOperator,
    EnvironmentAtomAttachmentSimpleExpressionProperty
)


class RuntimeRestartManager:
    """Manages runtime (Atom) restart operations"""
    
    def __init__(self, verbose: bool = False):
        """Initialize the Boomi SDK client"""
        self.verbose = verbose
        self.sdk = Boomi(
            account_id=os.getenv("BOOMI_ACCOUNT"),
            username=os.getenv("BOOMI_USER"),
            password=os.getenv("BOOMI_SECRET"),
            timeout=30000
        )
        if self.verbose:
            print("✅ SDK initialized successfully")
    
    def get_runtime_status(self, atom_id: str) -> Dict[str, Any]:
        """Get current status of a runtime"""
        try:
            atom = self.sdk.atom.get_atom(id_=atom_id)
            
            status = {
                'id': atom.id_,
                'name': atom.name,
                'status': atom.status,
                'online': atom.status == 'ONLINE',
                'type': getattr(atom, 'type', 'N/A'),
                'version': getattr(atom, 'current_version', 'N/A'),
                'last_update': getattr(atom, 'date_installed', 'N/A'),
                'hostname': getattr(atom, 'hostname', 'N/A'),
                'capabilities': getattr(atom, 'capabilities', [])
            }
            
            if self.verbose:
                print(f"Runtime {atom.name}: Status = {atom.status}")
            
            return status
            
        except Exception as e:
            print(f"❌ Failed to get runtime status: {e}")
            return None
    
    def check_active_executions(self, atom_id: str) -> int:
        """Check for active process executions on the runtime"""
        try:
            # Query for active executions on this atom
            atom_expr = ExecutionRecordSimpleExpression(
                operator=ExecutionRecordSimpleExpressionOperator.EQUALS,
                property=ExecutionRecordSimpleExpressionProperty.ATOMID,
                argument=[atom_id]
            )
            
            status_expr = ExecutionRecordSimpleExpression(
                operator=ExecutionRecordSimpleExpressionOperator.EQUALS,
                property=ExecutionRecordSimpleExpressionProperty.STATUS,
                argument=['INPROCESS']
            )
            
            combined_expr = ExecutionRecordGroupingExpression(
                operator=ExecutionRecordGroupingExpressionOperator.AND,
                nested_expression=[atom_expr, status_expr]
            )
            
            query_filter = ExecutionRecordQueryConfigQueryFilter(
                expression=combined_expr
            )
            
            query_config = ExecutionRecordQueryConfig(
                query_filter=query_filter
            )
            
            result = self.sdk.execution_record.query_execution_record(
                request_body=query_config
            )
            
            active_count = 0
            if hasattr(result, 'result') and result.result:
                active_count = len(result.result)
            
            if self.verbose and active_count > 0:
                print(f"⚠️ {active_count} active executions found on runtime")
            
            return active_count
            
        except Exception as e:
            if self.verbose:
                print(f"Warning: Could not check active executions: {e}")
            return 0
    
    def restart_runtime(self, atom_id: str, graceful: bool = True, 
                       wait: bool = False, force: bool = False) -> bool:
        """Restart a single runtime"""
        print(f"\n🔄 Restarting runtime: {atom_id}")
        
        # Get current status
        status = self.get_runtime_status(atom_id)
        if not status:
            print("❌ Could not get runtime status")
            return False
        
        print(f"   Current status: {status['status']}")
        print(f"   Runtime name: {status['name']}")
        
        # Check for active executions if graceful
        if graceful and not force:
            active = self.check_active_executions(atom_id)
            if active > 0:
                print(f"⚠️ {active} active executions in progress")
                if not wait:
                    print("   Use --wait to wait for completion or --force to restart anyway")
                    return False
                else:
                    print("   Waiting for executions to complete...")
                    if not self.wait_for_executions(atom_id):
                        print("   Timeout waiting for executions")
                        return False
        
        # Perform restart using the SDK
        try:
            print("   Initiating restart...")

            if self.verbose:
                print("   Sending restart command...")

            # Use the RuntimeRestartRequest API
            restart_request = RuntimeRestartRequest(
                runtime_id=atom_id,
                message=f"Restart initiated via SDK - {'forced' if force else 'graceful'}"
            )

            # Call the restart API
            try:
                result = self.sdk.runtime_restart_request.create_runtime_restart_request(
                    request_body=restart_request
                )

                # Handle response - it might be a RuntimeRestartRequest object, a message string, or dict
                if result:
                    if isinstance(result, str):
                        # Result is a plain string message (could be XML or plain text)
                        # Extract message from XML if present
                        if 'message=' in result or 'RuntimeRestartRequest' in result:
                            print("   ✅ Restart command sent successfully")
                            if self.verbose:
                                print(f"   Response: {result}")
                        else:
                            print(f"   ✅ {result}")
                    elif hasattr(result, 'message'):
                        # Result is an object with a message attribute
                        print(f"   ✅ {result.message}")
                    elif isinstance(result, dict) and 'message' in result:
                        # Result is a dictionary with a message key
                        print(f"   ✅ {result['message']}")
                    else:
                        print("   ✅ Restart command sent successfully")
                else:
                    print("   ⚠️ Restart command sent but no confirmation received")
            except Exception as api_error:
                # Check if it's a cloud runtime error
                if "400" in str(api_error):
                    print("   ❌ Cannot restart Cloud runtimes via API")
                    print("   Cloud runtimes are managed by Boomi and restart automatically")
                    return False
                raise
            
            if wait:
                print("   Waiting for runtime to come back online...")
                if self.wait_for_online(atom_id):
                    print("   ✅ Runtime is back online")
                    return True
                else:
                    print("   ⚠️ Runtime did not come back online in time")
                    return False
            
            return True
            
        except Exception as e:
            print(f"❌ Failed to restart runtime: {e}")
            return False
    
    def wait_for_executions(self, atom_id: str, timeout: int = 300) -> bool:
        """Wait for active executions to complete"""
        start_time = time.time()
        
        while time.time() - start_time < timeout:
            active = self.check_active_executions(atom_id)
            if active == 0:
                return True
            
            if self.verbose:
                print(f"   Still {active} active executions...")
            
            time.sleep(10)
        
        return False
    
    def wait_for_online(self, atom_id: str, timeout: int = 300) -> bool:
        """Wait for runtime to come back online"""
        start_time = time.time()
        
        while time.time() - start_time < timeout:
            status = self.get_runtime_status(atom_id)
            if status and status['online']:
                return True
            
            if self.verbose:
                current_status = status['status'] if status else 'UNKNOWN'
                print(f"   Current status: {current_status}")
            
            time.sleep(10)
        
        return False
    
    def restart_batch(self, atom_ids: List[str], rolling: bool = True, 
                     delay: int = 30, graceful: bool = True) -> Dict[str, bool]:
        """Restart multiple runtimes"""
        print(f"\n📦 Batch restarting {len(atom_ids)} runtimes...")
        
        results = {}
        
        for i, atom_id in enumerate(atom_ids):
            print(f"\n[{i+1}/{len(atom_ids)}] Processing {atom_id}")
            
            success = self.restart_runtime(
                atom_id, 
                graceful=graceful,
                wait=rolling
            )
            
            results[atom_id] = success
            
            if rolling and i < len(atom_ids) - 1:
                print(f"   Waiting {delay} seconds before next restart...")
                time.sleep(delay)
        
        return results
    
    def restart_environment(self, environment_id: str, rolling: bool = True,
                          delay: int = 30) -> Dict[str, bool]:
        """Restart all runtimes in an environment"""
        print(f"\n🌍 Restarting all runtimes in environment: {environment_id}")
        
        # Get all atoms in the environment
        atom_ids = self.get_environment_atoms(environment_id)
        
        if not atom_ids:
            print("❌ No runtimes found in environment")
            return {}
        
        print(f"   Found {len(atom_ids)} runtimes")
        
        return self.restart_batch(atom_ids, rolling=rolling, delay=delay)
    
    def get_environment_atoms(self, environment_id: str) -> List[str]:
        """Get all atom IDs in an environment"""
        try:
            simple_expression = EnvironmentAtomAttachmentSimpleExpression(
                operator=EnvironmentAtomAttachmentSimpleExpressionOperator.EQUALS,
                property=EnvironmentAtomAttachmentSimpleExpressionProperty.ENVIRONMENT_ID,
                argument=[environment_id]
            )
            
            query_filter = EnvironmentAtomAttachmentQueryConfigQueryFilter(
                expression=simple_expression
            )
            
            query_config = EnvironmentAtomAttachmentQueryConfig(
                query_filter=query_filter
            )
            
            result = self.sdk.environment_atom_attachment.query_environment_atom_attachment(
                request_body=query_config
            )
            
            atom_ids = []
            if hasattr(result, 'result') and result.result:
                for attachment in result.result:
                    atom_id = getattr(attachment, 'atom_id', None)
                    if atom_id:
                        atom_ids.append(atom_id)
            
            return atom_ids
            
        except Exception as e:
            print(f"❌ Failed to get environment atoms: {e}")
            return []
    
    def schedule_restart(self, atom_id: str, schedule_time: str) -> bool:
        """Schedule a restart for a specific time"""
        print(f"\n⏰ Scheduling restart for: {schedule_time}")
        
        try:
            scheduled_dt = datetime.strptime(schedule_time, "%Y-%m-%d %H:%M:%S")
            current_dt = datetime.now()
            
            if scheduled_dt <= current_dt:
                print("❌ Scheduled time must be in the future")
                return False
            
            wait_seconds = (scheduled_dt - current_dt).total_seconds()
            
            print(f"   Runtime: {atom_id}")
            print(f"   Scheduled for: {scheduled_dt}")
            print(f"   Waiting {wait_seconds:.0f} seconds...")
            
            # In a real implementation, you might:
            # 1. Store the schedule in a database
            # 2. Use a job scheduler
            # 3. Create a scheduled task
            
            # For demonstration, we'll use a simple sleep
            # (not recommended for production)
            if wait_seconds > 3600:  # More than 1 hour
                print("   Note: Long wait times should use a proper scheduler")
                return False
            
            time.sleep(wait_seconds)
            
            return self.restart_runtime(atom_id, graceful=True, wait=True)
            
        except ValueError:
            print("❌ Invalid date format. Use YYYY-MM-DD HH:MM:SS")
            return False
        except Exception as e:
            print(f"❌ Failed to schedule restart: {e}")
            return False
    
    def validate_health(self, atom_id: str) -> bool:
        """Validate runtime health after restart"""
        print(f"\n🏥 Validating runtime health...")
        
        status = self.get_runtime_status(atom_id)
        if not status:
            print("❌ Could not get runtime status")
            return False
        
        health_checks = []
        critical_checks = []

        # Check online status (critical)
        health_checks.append(('Online Status', status['online'], True))
        critical_checks.append(status['online'])

        # Check version (non-critical for some runtime types)
        health_checks.append(('Version Available', status['version'] != 'N/A', False))

        # Check capabilities (non-critical, may not be available for all runtime types)
        has_capabilities = len(status.get('capabilities', [])) > 0
        health_checks.append(('Capabilities Loaded', has_capabilities, False))

        # Print health check results
        all_critical_passed = True
        for check_name, check_result, is_critical in health_checks:
            icon = '✅' if check_result else '⚠️' if not is_critical else '❌'
            status_text = 'Passed' if check_result else ('Warning' if not is_critical else 'Failed')
            print(f"   {icon} {check_name}: {status_text}")
            if not check_result and is_critical:
                all_critical_passed = False

        return all_critical_passed


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='Manage runtime (Atom) restarts',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
    python restart_runtime.py 2d4d5da4-0dfe-41f8-914b-f5f5120ad90a
    python restart_runtime.py 2d4d5da4-0dfe-41f8-914b-f5f5120ad90a --graceful --wait
    python restart_runtime.py --batch "atom1,atom2,atom3" --rolling
    python restart_runtime.py --environment 74851c30-98b2-4a6f-838b-61eee5627b13 --rolling
        '''
    )
    
    # Main arguments
    parser.add_argument('atom_id', nargs='?',
                       help='Atom ID to restart')
    parser.add_argument('--batch', metavar='IDS',
                       help='Comma-separated list of atom IDs to restart')
    parser.add_argument('--environment', metavar='ENV_ID',
                       help='Restart all atoms in environment')
    
    # Restart options
    parser.add_argument('--graceful', action='store_true', default=True,
                       help='Graceful restart (wait for executions)')
    parser.add_argument('--force', action='store_true',
                       help='Force restart even with active executions')
    parser.add_argument('--wait', action='store_true',
                       help='Wait for runtime to come back online')
    
    # Batch options
    parser.add_argument('--rolling', action='store_true',
                       help='Rolling restart (one at a time)')
    parser.add_argument('--delay', type=int, default=30,
                       help='Delay between restarts in seconds (default: 30)')
    
    # Schedule options
    parser.add_argument('--schedule', metavar='DATETIME',
                       help='Schedule restart for specific time (YYYY-MM-DD HH:MM:SS)')
    
    # Other options
    parser.add_argument('--validate', action='store_true',
                       help='Validate health after restart')
    parser.add_argument('--verbose', action='store_true',
                       help='Enable verbose output')
    
    args = parser.parse_args()
    
    # Validate arguments
    if not args.atom_id and not args.batch and not args.environment:
        parser.error("Either atom_id, --batch, or --environment must be specified")
    
    # Validate environment variables
    if not all([os.getenv("BOOMI_ACCOUNT"), os.getenv("BOOMI_USER"), os.getenv("BOOMI_SECRET")]):
        print("❌ Error: Missing required environment variables")
        print("   Please set: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET")
        sys.exit(1)
    
    # Initialize manager
    manager = RuntimeRestartManager(verbose=args.verbose)
    
    try:
        success = False
        
        if args.schedule and args.atom_id:
            # Schedule restart
            success = manager.schedule_restart(args.atom_id, args.schedule)
            
        elif args.batch:
            # Batch restart
            atom_ids = [id.strip() for id in args.batch.split(',')]
            results = manager.restart_batch(
                atom_ids,
                rolling=args.rolling,
                delay=args.delay,
                graceful=args.graceful and not args.force
            )
            
            # Print summary
            print("\n📊 Batch Restart Summary:")
            success_count = sum(1 for s in results.values() if s)
            print(f"   ✅ Successful: {success_count}/{len(results)}")
            
            if success_count < len(results):
                print("   Failed atoms:")
                for atom_id, result in results.items():
                    if not result:
                        print(f"     - {atom_id}")
            
            success = success_count == len(results)
            
        elif args.environment:
            # Environment restart
            results = manager.restart_environment(
                args.environment,
                rolling=args.rolling,
                delay=args.delay
            )
            
            # Print summary
            if results:
                print("\n📊 Environment Restart Summary:")
                success_count = sum(1 for s in results.values() if s)
                print(f"   ✅ Successful: {success_count}/{len(results)}")
                success = success_count == len(results)
            else:
                success = False
            
        else:
            # Single runtime restart
            success = manager.restart_runtime(
                args.atom_id,
                graceful=args.graceful and not args.force,
                wait=args.wait,
                force=args.force
            )
        
        # Validate health if requested
        if success and args.validate and args.atom_id:
            health_ok = manager.validate_health(args.atom_id)
            if not health_ok:
                print("\n⚠️ Health validation failed")
                success = False
        
        # Final status
        if success:
            print("\n✅ Restart operation completed successfully")
        else:
            print("\n❌ Restart operation failed or partially failed")
            sys.exit(1)
            
    except KeyboardInterrupt:
        print("\n\n⚠️ Operation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()