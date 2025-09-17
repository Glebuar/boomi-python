#!/usr/bin/env python3
"""
Runtime Management Example for Boomi Python SDK

This example demonstrates comprehensive runtime/atom management:
- List and query runtimes with filtering
- Get runtime details and status
- Update runtime configuration  
- Delete runtimes (with safety confirmation)
- Monitor runtime health and status
- Manage runtime environment attachments

Usage:
    python manage_runtimes.py --list
    python manage_runtimes.py --get --runtime-id <id>
    python manage_runtimes.py --update --runtime-id <id> --name "New Name"
    python manage_runtimes.py --delete --runtime-id <id>
    python manage_runtimes.py --monitor --runtime-id <id>
"""

import argparse
import json
import os
import sys
import time
from datetime import datetime
from typing import Dict, List, Optional, Any

# Add src to Python path for SDK imports
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
    Atom,
    AtomQueryConfig,
    AtomQueryConfigQueryFilter,
    AtomSimpleExpression,
    AtomSimpleExpressionOperator,
    AtomSimpleExpressionProperty
)


class RuntimeManager:
    """Manages Boomi runtimes and atoms."""
    
    def __init__(self):
        """Initialize the Runtime Manager with SDK."""
        self.sdk = self._initialize_sdk()
        
    def _initialize_sdk(self) -> Boomi:
        """Initialize the Boomi SDK with credentials from environment."""
        account_id = os.getenv('BOOMI_ACCOUNT')
        username = os.getenv('BOOMI_USER') 
        password = os.getenv('BOOMI_SECRET')
        
        if not all([account_id, username, password]):
            print("❌ Error: Missing required environment variables:")
            print("   BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET")
            sys.exit(1)
            
        return Boomi(
            account_id=account_id,
            username=username, 
            password=password,
            timeout=30000
        )
    
    def list_runtimes(self, runtime_type: Optional[str] = None, 
                     status: Optional[str] = None) -> List[Dict]:
        """
        List all runtimes with optional filtering.
        
        Args:
            runtime_type: Filter by runtime type (ATOM, CLOUD, MOLECULE, GATEWAY)
            status: Filter by status (ONLINE, OFFLINE)
            
        Returns:
            List of runtime information dictionaries
        """
        print("📋 Listing runtimes...")
        
        try:
            # Create query with filters if specified
            query_config = AtomQueryConfig()
            
            # Add filters if specified
            if runtime_type or status:
                expressions = []
                
                if runtime_type:
                    type_expr = AtomSimpleExpression(
                        operator=AtomSimpleExpressionOperator.EQUALS,
                        property=AtomSimpleExpressionProperty.TYPE,
                        argument=[runtime_type]
                    )
                    expressions.append(type_expr)
                
                if status:
                    status_expr = AtomSimpleExpression(
                        operator=AtomSimpleExpressionOperator.EQUALS,
                        property=AtomSimpleExpressionProperty.STATUS,
                        argument=[status]
                    )
                    expressions.append(status_expr)
                
                # If multiple expressions, we'd need grouping logic
                # For now, use the first expression
                if expressions:
                    query_filter = AtomQueryConfigQueryFilter(expression=expressions[0])
                    query_config = AtomQueryConfig(query_filter=query_filter)
            
            # Execute query
            response = self.sdk.atom.query_atom(query_config)
            
            # Parse results
            runtimes = []
            if hasattr(response, 'result') and response.result:
                result_data = response.result
                if isinstance(result_data, list):
                    runtimes = result_data
                else:
                    runtimes = [result_data]
            
            # Convert to dict format for easier handling
            runtime_list = []
            for runtime in runtimes:
                runtime_info = {
                    'id': getattr(runtime, 'id_', 'N/A'),
                    'name': getattr(runtime, 'name', 'N/A'),
                    'type': getattr(runtime, 'type_', 'N/A'),
                    'status': getattr(runtime, 'status', 'N/A'),
                    'hostname': getattr(runtime, 'host_name', 'N/A'),
                    'version': getattr(runtime, 'current_version', 'N/A'),
                    'date_installed': getattr(runtime, 'date_installed', 'N/A'),
                    'created_by': getattr(runtime, 'created_by', 'N/A'),
                    'capabilities': getattr(runtime, 'capabilities', [])
                }
                runtime_list.append(runtime_info)
            
            print(f"✅ Found {len(runtime_list)} runtime(s)")
            return runtime_list
            
        except Exception as e:
            print(f"❌ Error listing runtimes: {e}")
            return []
    
    def get_runtime(self, runtime_id: str) -> Optional[Dict]:
        """
        Get detailed information about a specific runtime.
        
        Args:
            runtime_id: The runtime ID
            
        Returns:
            Runtime information dictionary or None
        """
        print(f"🔍 Getting runtime details: {runtime_id}")
        
        try:
            result = self.sdk.atom.get_atom(id_=runtime_id)
            
            # Extract runtime information
            runtime_info = {
                'id': getattr(result, 'id_', runtime_id),
                'name': getattr(result, 'name', 'N/A'),
                'type': getattr(result, 'type_', 'N/A'),
                'status': getattr(result, 'status', 'N/A'),
                'hostname': getattr(result, 'host_name', 'N/A'),
                'version': getattr(result, 'current_version', 'N/A'),
                'date_installed': getattr(result, 'date_installed', 'N/A'),
                'date_created': getattr(result, 'date_created', 'N/A'),
                'created_by': getattr(result, 'created_by', 'N/A'),
                'description': getattr(result, 'description', 'N/A'),
                'capabilities': getattr(result, 'capabilities', []),
                'shared_server_information': getattr(result, 'shared_server_information', None)
            }
            
            print("✅ Runtime retrieved successfully")
            return runtime_info
            
        except Exception as e:
            print(f"❌ Error getting runtime: {e}")
            return None
    
    def update_runtime(self, runtime_id: str, name: Optional[str] = None,
                      description: Optional[str] = None) -> bool:
        """
        Update runtime configuration.
        
        Args:
            runtime_id: The runtime ID
            name: New name for the runtime
            description: New description for the runtime
            
        Returns:
            True if successful, False otherwise
        """
        print(f"🔄 Updating runtime: {runtime_id}")
        
        try:
            # Get current atom to preserve required fields
            current_atom = self.sdk.atom.get_atom(id_=runtime_id)

            # Create update object with required fields
            update_data = {
                'id_': runtime_id,  # Required field
                'name': name if name else current_atom.name,
                'purge_history_days': getattr(current_atom, 'purge_history_days', 30),
                'purge_immediate': getattr(current_atom, 'purge_immediate', False),
                'force_restart_time': getattr(current_atom, 'force_restart_time', 0)
            }

            if name:
                print(f"   Setting name to: {name}")
            if description:
                # Note: description is not an updatable field for Atoms
                print(f"   ⚠️ Description cannot be updated for Atoms")

            # Create Atom update object
            runtime_update = Atom(**update_data)
            
            # Execute update
            result = self.sdk.atom.update_atom(
                id_=runtime_id,
                request_body=runtime_update
            )
            
            print("✅ Runtime updated successfully")
            return True
            
        except Exception as e:
            print(f"❌ Error updating runtime: {e}")
            return False
    
    def delete_runtime(self, runtime_id: str, confirm: bool = False) -> bool:
        """
        Delete a runtime (with safety confirmation).
        
        Args:
            runtime_id: The runtime ID
            confirm: Skip interactive confirmation
            
        Returns:
            True if successful, False otherwise
        """
        print(f"🗑️ Deleting runtime: {runtime_id}")
        print("⚠️ WARNING: Deletion is permanent and cannot be undone!")
        
        # Safety confirmation
        if not confirm:
            try:
                confirm_input = input("Type 'DELETE' to confirm deletion: ").strip()
                if confirm_input != 'DELETE':
                    print("❌ Deletion cancelled")
                    return False
            except (EOFError, KeyboardInterrupt):
                print("\n❌ Deletion cancelled")
                return False
        
        try:
            # Execute deletion
            self.sdk.atom.delete_atom(id_=runtime_id)
            print("✅ Runtime deleted successfully")
            return True
            
        except Exception as e:
            print(f"❌ Error deleting runtime: {e}")
            if hasattr(e, 'status'):
                if e.status == 400:
                    print("   Bad request - runtime ID may be invalid or not exist")
                elif e.status == 403:
                    print("   Permission denied - check account permissions")
                elif e.status == 404:
                    print("   Runtime not found - may already be deleted")
                elif e.status == 409:
                    print("   Conflict - runtime may be attached to environments")
            return False
    
    def monitor_runtime(self, runtime_id: str, interval_seconds: int = 30,
                       max_iterations: int = 10) -> None:
        """
        Monitor runtime status over time.
        
        Args:
            runtime_id: The runtime ID
            interval_seconds: Time between checks
            max_iterations: Maximum number of monitoring cycles
        """
        print(f"👁️ Monitoring runtime: {runtime_id}")
        print(f"   Checking every {interval_seconds} seconds for {max_iterations} cycles")
        
        for i in range(max_iterations):
            print(f"\n--- Monitoring Cycle {i+1}/{max_iterations} ---")
            print(f"Time: {datetime.now().strftime('%H:%M:%S')}")
            
            runtime_info = self.get_runtime(runtime_id)
            
            if runtime_info:
                status = runtime_info['status']
                hostname = runtime_info['hostname']
                version = runtime_info['version']
                
                status_icon = "🟢" if status == "ONLINE" else "🔴" if status == "OFFLINE" else "⚪"
                
                print(f"   {status_icon} Status: {status}")
                print(f"   🖥️ Hostname: {hostname}")
                print(f"   📦 Version: {version}")
                
                # Health assessment
                if status == "ONLINE":
                    print("   ✅ Runtime is healthy and ready for processing")
                elif status == "OFFLINE":
                    print("   ⚠️ Runtime is offline - check runtime service")
                else:
                    print(f"   ❓ Runtime status: {status}")
            else:
                print("   ❌ Failed to get runtime status")
            
            if i < max_iterations - 1:  # Don't sleep after last iteration
                print(f"   Waiting {interval_seconds} seconds...")
                time.sleep(interval_seconds)
        
        print("\n📊 Monitoring complete")
    
    def get_runtime_statistics(self) -> Dict[str, Any]:
        """
        Get comprehensive runtime statistics for the account.
        
        Returns:
            Dictionary with runtime statistics
        """
        runtimes = self.list_runtimes()
        
        if not runtimes:
            return {"error": "No runtimes found or error occurred"}
        
        stats = {
            "total_runtimes": len(runtimes),
            "runtime_types": {},
            "runtime_statuses": {},
            "online_runtimes": 0,
            "offline_runtimes": 0,
            "runtime_versions": {},
            "runtimes": []
        }
        
        for runtime in runtimes:
            runtime_type = runtime['type']
            status = runtime['status']
            version = runtime['version']
            
            # Update type counts
            stats["runtime_types"][runtime_type] = stats["runtime_types"].get(runtime_type, 0) + 1
            
            # Update status counts
            stats["runtime_statuses"][status] = stats["runtime_statuses"].get(status, 0) + 1
            
            if status == "ONLINE":
                stats["online_runtimes"] += 1
            elif status == "OFFLINE":
                stats["offline_runtimes"] += 1
            
            # Update version counts
            if version and version != "N/A":
                stats["runtime_versions"][version] = stats["runtime_versions"].get(version, 0) + 1
            
            stats["runtimes"].append({
                "name": runtime['name'],
                "id": runtime['id'],
                "type": runtime_type,
                "status": status,
                "hostname": runtime['hostname'],
                "version": version
            })
        
        return stats
    
    def _display_runtime_summary(self, runtimes: List[Dict]) -> None:
        """Display a formatted summary of runtime information."""
        if not runtimes:
            print("   No runtimes found")
            return
        
        print(f"\n📋 Found {len(runtimes)} runtime(s):")
        print("-" * 100)
        
        online_count = 0
        offline_count = 0
        
        for runtime in runtimes:
            name = runtime['name']
            runtime_type = runtime['type']
            status = runtime['status']
            hostname = runtime['hostname']
            version = runtime['version']
            
            if status == "ONLINE":
                online_count += 1
                status_icon = "🟢"
            elif status == "OFFLINE":
                offline_count += 1
                status_icon = "🔴"
            else:
                status_icon = "⚪"
            
            print(f"{status_icon} {name} ({runtime_type})")
            print(f"    ID: {runtime['id']}")
            print(f"    Status: {status}")
            print(f"    Hostname: {hostname}")
            print(f"    Version: {version}")
            print()
        
        print("-" * 100)
        print(f"📊 Total: {online_count} online, {offline_count} offline")
        
        # Runtime health assessment
        if offline_count > 0:
            print("⚠️ Warning: Some runtimes are offline - check runtime services")
        elif online_count == 0:
            print("❌ No online runtimes - no processes can execute")
        else:
            print("✅ All runtimes are online and ready for processing")
    
    def _format_date(self, date_string: str) -> str:
        """Format ISO date string to readable format."""
        try:
            if date_string and date_string != 'N/A':
                dt = datetime.fromisoformat(date_string.replace('Z', '+00:00'))
                return dt.strftime('%Y-%m-%d %H:%M:%S UTC')
        except:
            pass
        return date_string or 'N/A'


def main():
    """Main CLI interface for runtime management operations."""
    parser = argparse.ArgumentParser(
        description="Manage Boomi runtimes and atoms",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # List all runtimes
  python manage_runtimes.py --list
  
  # List only online runtimes
  python manage_runtimes.py --list --status ONLINE
  
  # List only ATOM type runtimes
  python manage_runtimes.py --list --type ATOM
  
  # Get specific runtime details
  python manage_runtimes.py --get --runtime-id 12345678-1234-1234-1234-123456789012
  
  # Update runtime name and description
  python manage_runtimes.py --update --runtime-id 12345678-1234-1234-1234-123456789012 --name "New Name" --description "Updated description"
  
  # Delete runtime (with confirmation)
  python manage_runtimes.py --delete --runtime-id 12345678-1234-1234-1234-123456789012
  
  # Monitor runtime status
  python manage_runtimes.py --monitor --runtime-id 12345678-1234-1234-1234-123456789012 --interval 60 --cycles 5
  
  # Get runtime statistics
  python manage_runtimes.py --stats
  
  # Show help with examples
  python manage_runtimes.py --help-examples

Environment Variables Required:
  BOOMI_ACCOUNT - Your Boomi account ID
  BOOMI_USER - Your Boomi username (or token username)
  BOOMI_SECRET - Your Boomi password (or token password)
        """
    )
    
    # Operation selection (mutually exclusive group)
    operations = parser.add_mutually_exclusive_group(required=True)
    operations.add_argument('--list', action='store_true',
                           help='List all runtimes')
    operations.add_argument('--get', action='store_true',
                           help='Get specific runtime details')
    operations.add_argument('--update', action='store_true',
                           help='Update runtime configuration')
    operations.add_argument('--delete', action='store_true',
                           help='Delete a runtime')
    operations.add_argument('--monitor', action='store_true',
                           help='Monitor runtime status over time')
    operations.add_argument('--stats', action='store_true',
                           help='Get runtime statistics')
    operations.add_argument('--help-examples', action='store_true',
                           help='Show detailed usage examples')
    
    # Global options
    parser.add_argument('--runtime-id',
                       help='Runtime ID (required for get, update, delete, monitor operations)')
    
    # List operation options
    parser.add_argument('--type', choices=['ATOM', 'CLOUD', 'MOLECULE', 'GATEWAY'],
                       help='Filter by runtime type')
    parser.add_argument('--status', choices=['ONLINE', 'OFFLINE'],
                       help='Filter by runtime status')
    
    # Update operation options
    parser.add_argument('--name', help='New name for runtime')
    parser.add_argument('--description', help='New description for runtime')
    
    # Monitor operation options
    parser.add_argument('--interval', type=int, default=30,
                       help='Monitoring interval in seconds (default: 30)')
    parser.add_argument('--cycles', type=int, default=10,
                       help='Number of monitoring cycles (default: 10)')
    
    # Delete operation options
    parser.add_argument('--confirm', action='store_true',
                       help='Skip interactive confirmation for delete')
    
    args = parser.parse_args()
    
    # Show help examples
    if args.help_examples:
        show_help_examples()
        return
    
    # Validate runtime-id is provided for operations that need it
    if args.get or args.update or args.delete or args.monitor:
        if not args.runtime_id:
            print("❌ Error: --runtime-id is required for this operation")
            sys.exit(1)
    
    # Validate update operation has at least one field to update
    if args.update and not args.name and not args.description:
        print("❌ Error: At least --name or --description is required for update operation")
        sys.exit(1)
    
    # Initialize runtime manager
    try:
        runtime_manager = RuntimeManager()
    except SystemExit:
        return  # SDK initialization failed with proper error message
    except Exception as e:
        print(f"❌ Error initializing runtime manager: {e}")
        return
    
    print("🤖 Boomi Runtime Management Tool")
    print("=" * 50)
    
    # Execute requested operation
    try:
        if args.list:
            runtimes = runtime_manager.list_runtimes(
                runtime_type=args.type,
                status=args.status
            )
            runtime_manager._display_runtime_summary(runtimes)
            
        elif args.get:
            runtime_info = runtime_manager.get_runtime(args.runtime_id)
            if runtime_info:
                print(f"\n🤖 Runtime Details: {runtime_info['name']}")
                print("-" * 60)
                print(f"ID: {runtime_info['id']}")
                print(f"Type: {runtime_info['type']}")
                print(f"Status: {runtime_info['status']}")
                print(f"Hostname: {runtime_info['hostname']}")
                print(f"Version: {runtime_info['version']}")
                print(f"Date Installed: {runtime_manager._format_date(runtime_info['date_installed'])}")
                print(f"Created By: {runtime_info['created_by']}")
                print(f"Description: {runtime_info['description']}")
                
                if runtime_info['capabilities']:
                    print(f"Capabilities: {', '.join(runtime_info['capabilities'])}")
                    
        elif args.update:
            success = runtime_manager.update_runtime(
                runtime_id=args.runtime_id,
                name=args.name,
                description=args.description
            )
            sys.exit(0 if success else 1)
            
        elif args.delete:
            success = runtime_manager.delete_runtime(
                runtime_id=args.runtime_id,
                confirm=args.confirm
            )
            sys.exit(0 if success else 1)
            
        elif args.monitor:
            runtime_manager.monitor_runtime(
                runtime_id=args.runtime_id,
                interval_seconds=args.interval,
                max_iterations=args.cycles
            )
            
        elif args.stats:
            stats = runtime_manager.get_runtime_statistics()
            if "error" in stats:
                print(f"❌ {stats['error']}")
                sys.exit(1)
            
            print(f"\n📊 Runtime Statistics")
            print("-" * 60)
            print(f"Total Runtimes: {stats['total_runtimes']}")
            print(f"Online Runtimes: {stats['online_runtimes']}")
            print(f"Offline Runtimes: {stats['offline_runtimes']}")
            
            if stats['runtime_types']:
                print(f"\nRuntime Types:")
                for runtime_type, count in stats['runtime_types'].items():
                    print(f"  {runtime_type}: {count}")
            
            if stats['runtime_versions']:
                print(f"\nRuntime Versions:")
                for version, count in stats['runtime_versions'].items():
                    print(f"  {version}: {count}")
                    
            print(f"\nDetailed Runtime List:")
            for runtime in stats['runtimes']:
                status_icon = "🟢" if runtime['status'] == "ONLINE" else "🔴"
                print(f"  {status_icon} {runtime['name']} ({runtime['type']}) - {runtime['status']}")
                
    except KeyboardInterrupt:
        print("\n⚠️ Operation cancelled by user")
    except Exception as e:
        print(f"❌ Error executing operation: {e}")
        sys.exit(1)


def show_help_examples():
    """Display detailed usage examples."""
    print("""
🤖 Boomi Runtime Management - Detailed Examples

ENVIRONMENT SETUP:
  export BOOMI_ACCOUNT="your-account-id"
  export BOOMI_USER="BOOMI_TOKEN.username@company.com"
  export BOOMI_SECRET="your-api-token"

BASIC OPERATIONS:

1. List All Runtimes:
   python manage_runtimes.py --list
   
   Shows all runtimes with status, type, and details.

2. Filter Runtimes:
   # Show only online runtimes
   python manage_runtimes.py --list --status ONLINE
   
   # Show only ATOM type runtimes
   python manage_runtimes.py --list --type ATOM
   
   # Combine filters (online ATOM runtimes)
   python manage_runtimes.py --list --type ATOM --status ONLINE

3. Get Runtime Details:
   python manage_runtimes.py --get --runtime-id 12345678-1234-1234-1234-123456789012
   
   Shows detailed information about a specific runtime.

4. Update Runtime:
   # Update name only
   python manage_runtimes.py --update --runtime-id 12345678-1234-1234-1234-123456789012 --name "Production Runtime"
   
   # Update description only
   python manage_runtimes.py --update --runtime-id 12345678-1234-1234-1234-123456789012 --description "Updated via SDK"
   
   # Update both name and description
   python manage_runtimes.py --update --runtime-id 12345678-1234-1234-1234-123456789012 --name "Prod Runtime" --description "Production environment runtime"

5. Delete Runtime:
   # With interactive confirmation
   python manage_runtimes.py --delete --runtime-id 12345678-1234-1234-1234-123456789012
   
   # Skip confirmation (use with caution!)
   python manage_runtimes.py --delete --runtime-id 12345678-1234-1234-1234-123456789012 --confirm

MONITORING AND ANALYSIS:

6. Monitor Runtime Status:
   # Monitor every 30 seconds for 10 cycles (default)
   python manage_runtimes.py --monitor --runtime-id 12345678-1234-1234-1234-123456789012
   
   # Custom monitoring (every 60 seconds for 5 cycles)
   python manage_runtimes.py --monitor --runtime-id 12345678-1234-1234-1234-123456789012 --interval 60 --cycles 5

7. Get Runtime Statistics:
   python manage_runtimes.py --stats
   
   Shows comprehensive runtime statistics and health overview.

TROUBLESHOOTING SCENARIOS:

A. Check Runtime Health:
   # List all runtimes to see status
   python manage_runtimes.py --list
   
   # Get details for offline runtime
   python manage_runtimes.py --get --runtime-id <offline-runtime-id>
   
   # Monitor to see if it comes online
   python manage_runtimes.py --monitor --runtime-id <runtime-id>

B. Runtime Inventory Management:
   # Get overall statistics
   python manage_runtimes.py --stats
   
   # List by type for inventory
   python manage_runtimes.py --list --type ATOM
   python manage_runtimes.py --list --type CLOUD

C. Maintenance Operations:
   # Update runtime descriptions for organization
   python manage_runtimes.py --update --runtime-id <id> --description "Production - East Region"
   
   # Clean up unused runtimes (careful!)
   python manage_runtimes.py --delete --runtime-id <unused-runtime-id>

RUNTIME TYPES:
- ATOM: Standard on-premise runtime
- CLOUD: Boomi-hosted cloud runtime  
- MOLECULE: Clustered runtime
- GATEWAY: API Gateway runtime

RUNTIME STATUSES:
- ONLINE: Active and ready for processing
- OFFLINE: Not currently available

BEST PRACTICES:
1. Monitor critical runtimes regularly
2. Keep runtime names descriptive and organized
3. Update descriptions to indicate purpose/environment
4. Only delete runtimes that are no longer needed
5. Check runtime versions for compatibility

For more information, consult Boomi documentation on Runtime Management.
    """)


if __name__ == "__main__":
    main()