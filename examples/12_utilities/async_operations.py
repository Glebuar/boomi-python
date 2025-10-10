#!/usr/bin/env python3
"""
Async Operations Management - Handle long-running asynchronous operations

This example demonstrates how to work with Boomi's asynchronous operations,
which are used for long-running tasks that might timeout in synchronous calls.
It shows how to initiate async operations, poll for completion, and retrieve results.

Features:
- Start async operations for various services
- Poll operation status with configurable intervals
- Retrieve and process async operation results
- Handle timeouts and errors gracefully
- Support for multiple async operation types

Supported Operations:
- AtomCounters - Get atom performance counters
- AtomDiskSpace - Get atom disk usage information
- ListQueues - List atom message queues
- AtomStatus - Get atom runtime status
- Many other async operations

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET

Usage:
    python async_operations.py [options]
    
Examples:
    # Get atom counters asynchronously
    python async_operations.py --operation atom_counters --atom-id ATOM_ID
    
    # Get disk space with custom polling
    python async_operations.py --operation atom_disk_space --atom-id ATOM_ID --poll-interval 3 --timeout 60
    
    # List queues asynchronously
    python async_operations.py --operation list_queues --atom-id ATOM_ID
    
    # Get atom status
    python async_operations.py --operation atom_status --atom-id ATOM_ID
"""

import os
import sys
import argparse
import time
from typing import Optional, Any, Dict
from datetime import datetime, timedelta

# Import Boomi SDK
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))
from boomi import Boomi
from boomi.models import *


class AsyncOperationManager:
    """Manage Boomi async operations"""
    
    # Map operation names to SDK methods
    ASYNC_OPERATIONS = {
        'atom_counters': {
            'name': 'Atom Counters',
            'description': 'Get performance counters for an atom',
            'requires_atom': True
        },
        'persisted_process_properties': {
            'name': 'Persisted Process Properties',
            'description': 'Get persisted process properties for an atom',
            'requires_atom': True
        },
        'atom_disk_space': {
            'name': 'Atom Disk Space',
            'description': 'Get disk space usage for an atom',
            'requires_atom': True
        },
        'list_queues': {
            'name': 'List Queues',
            'description': 'List message queues on an atom',
            'requires_atom': True
        },
        'listener_status': {
            'name': 'Listener Status',
            'description': 'Get listener status for an atom',
            'requires_atom': True
        },
        'atom_security_policies': {
            'name': 'Atom Security Policies',
            'description': 'Get security policies for an atom',
            'requires_atom': True
        }
    }
    
    def __init__(self):
        """Initialize SDK and validate environment"""
        self.account_id = os.getenv('BOOMI_ACCOUNT')
        self.username = os.getenv('BOOMI_USER')
        self.password = os.getenv('BOOMI_SECRET')
        
        if not all([self.account_id, self.username, self.password]):
            print("❌ Missing required environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET")
            sys.exit(1)
        
        # Initialize SDK
        self.sdk = Boomi(
            account_id=self.account_id,
            username=self.username,
            password=self.password,
            timeout=30000
        )
        
        print("✅ SDK initialized successfully")
    
    def start_async_operation(self, operation: str, atom_id: Optional[str] = None, 
                            queue_name: Optional[str] = None) -> Optional[str]:
        """Start an async operation and return the token"""
        print(f"\n🚀 Starting async operation: {self.ASYNC_OPERATIONS[operation]['name']}")
        
        try:
            token = None
            
            if operation == 'atom_counters':
                result = self.sdk.atom.async_get_atom_counters(id_=atom_id)
                if hasattr(result, 'async_token'):
                    token = result.async_token.token

            elif operation == 'persisted_process_properties':
                result = self.sdk.atom.async_get_persisted_process_properties(id_=atom_id)
                if hasattr(result, 'async_token'):
                    token = result.async_token.token

            elif operation == 'atom_disk_space':
                result = self.sdk.atom_disk_space.async_get_atom_disk_space(id_=atom_id)
                if hasattr(result, 'async_token'):
                    token = result.async_token.token
                    
            elif operation == 'list_queues':
                result = self.sdk.list_queues.async_get_list_queues(id_=atom_id)
                if hasattr(result, 'async_token'):
                    token = result.async_token.token
                    
            elif operation == 'listener_status':
                result = self.sdk.listener_status.async_get_listener_status(id_=atom_id)
                if hasattr(result, 'async_token'):
                    token = result.async_token.token

            elif operation == 'atom_security_policies':
                result = self.sdk.atom_security_policies.async_get_atom_security_policies(id_=atom_id)
                if hasattr(result, 'async_token'):
                    token = result.async_token.token
            
            else:
                print(f"❌ Unknown operation: {operation}")
                return None
            
            if token:
                print(f"✅ Async operation started successfully")
                print(f"   🎫 Token: {token}")
                return token
            else:
                print("❌ Failed to get async token")
                return None
                
        except Exception as e:
            print(f"❌ Failed to start async operation: {e}")
            return None
    
    def poll_async_result(self, operation: str, token: str, poll_interval: int = 2,
                         max_attempts: int = 30) -> Optional[Any]:
        """Poll for async operation result"""
        print(f"\n⏳ Polling for async result (token: {token[:20]}...)")
        
        for attempt in range(max_attempts):
            if attempt > 0:
                print(f"   ⏳ Waiting {poll_interval} seconds... (attempt {attempt+1}/{max_attempts})")
                time.sleep(poll_interval)
            
            try:
                result = None
                
                if operation == 'atom_counters':
                    result = self.sdk.atom.async_token_atom_counters(token=token)

                elif operation == 'persisted_process_properties':
                    result = self.sdk.atom.async_token_persisted_process_properties(token=token)

                elif operation == 'atom_disk_space':
                    result = self.sdk.atom_disk_space.async_token_atom_disk_space(token=token)
                    
                elif operation == 'list_queues':
                    result = self.sdk.list_queues.async_token_list_queues(token=token)
                    
                elif operation == 'listener_status':
                    result = self.sdk.listener_status.async_token_listener_status(token=token)

                elif operation == 'atom_security_policies':
                    result = self.sdk.atom_security_policies.async_token_atom_security_policies(token=token)
                
                if result:
                    # Check if we have actual results or still processing
                    if hasattr(result, 'status') and result.status == 'PROCESSING':
                        print(f"   ⏳ Still processing...")
                        continue
                    else:
                        print("✅ Async operation completed successfully")
                        return result
                        
            except Exception as e:
                # Some operations return 202 while still processing
                if '202' in str(e) or 'still processing' in str(e).lower():
                    print(f"   ⏳ Still processing...")
                    continue
                else:
                    print(f"❌ Error polling result: {e}")
                    return None
        
        print("❌ Async operation timed out")
        return None
    
    def process_result(self, operation: str, result: Any) -> Dict[str, Any]:
        """Process and display async operation result"""
        print(f"\n📊 Processing {self.ASYNC_OPERATIONS[operation]['name']} results")
        
        processed = {}
        
        try:
            if operation == 'atom_counters':
                # AtomCounters returns counter groups
                print("\n📊 Atom Counters:")
                if hasattr(result, 'result') and result.result:
                    counters_data = result.result[0] if isinstance(result.result, list) else result.result
                    if hasattr(counters_data, 'counter_group') and counters_data.counter_group:
                        for group in counters_data.counter_group:
                            group_name = getattr(group, 'name', 'Unknown')
                            print(f"   📈 {group_name}")
                            processed[group_name] = {}

            elif operation == 'persisted_process_properties':
                # PersistedProcessProperties returns property data
                print("\n⚙️ Persisted Process Properties:")
                if hasattr(result, 'result') and result.result:
                    props_data = result.result[0] if isinstance(result.result, list) else result.result
                    print(f"   Properties loaded from atom")
                    processed['properties'] = True

            elif operation == 'atom_disk_space':
                if hasattr(result, 'disk_partition') and result.disk_partition:
                    print("\n💾 Atom Disk Space Usage:")
                    for partition in result.disk_partition:
                        name = getattr(partition, 'name', 'Unknown')
                        total = getattr(partition, 'total_space', 0)
                        used = getattr(partition, 'used_space', 0)
                        free = getattr(partition, 'free_space', 0)
                        
                        if total > 0:
                            usage_pct = (used / total) * 100
                            print(f"   📁 {name}:")
                            print(f"      Total: {total:,} bytes")
                            print(f"      Used:  {used:,} bytes ({usage_pct:.1f}%)")
                            print(f"      Free:  {free:,} bytes")
                            
                            processed[name] = {
                                'total': total,
                                'used': used,
                                'free': free,
                                'usage_pct': usage_pct
                            }
                            
            elif operation == 'list_queues':
                if hasattr(result, 'result') and result.result:
                    print("\n📬 Message Queues:")
                    for queue_result in result.result:
                        if hasattr(queue_result, 'queue_record') and queue_result.queue_record:
                            for queue in queue_result.queue_record:
                                name = getattr(queue, 'queue_name', 'Unknown')
                                q_type = getattr(queue, 'queue_type', 'Unknown')
                                messages = getattr(queue, 'messages_count', 0)
                                
                                print(f"   📮 {name} ({q_type})")
                                print(f"      Messages: {messages}")
                                
                                processed[name] = {
                                    'type': q_type,
                                    'messages': messages
                                }
                                
            elif operation == 'listener_status':
                if hasattr(result, 'result') and result.result:
                    print("\n🎧 Listener Status:")
                    listener_list = result.result if isinstance(result.result, list) else [result.result]
                    for listener in listener_list:
                        name = getattr(listener, 'listener_name', 'Unknown')
                        status = getattr(listener, 'status', 'Unknown')
                        print(f"   📡 {name}: {status}")
                        processed[name] = status

            elif operation == 'atom_security_policies':
                if hasattr(result, 'result') and result.result:
                    print("\n🔒 Security Policies:")
                    policy_list = result.result if isinstance(result.result, list) else [result.result]
                    for policy in policy_list:
                        policy_type = getattr(policy, 'type', 'Unknown')
                        enabled = getattr(policy, 'enabled', False)
                        print(f"   🛡️ {policy_type}: {'Enabled' if enabled else 'Disabled'}")
                        processed[policy_type] = enabled
            
        except Exception as e:
            print(f"❌ Error processing result: {e}")
        
        return processed
    
    def run_async_workflow(self, operation: str, atom_id: Optional[str] = None,
                          queue_name: Optional[str] = None, poll_interval: int = 2,
                          timeout: int = 60) -> bool:
        """Run complete async workflow: start, poll, process"""
        print(f"\n🔄 Running async workflow for: {self.ASYNC_OPERATIONS[operation]['name']}")
        print(f"   ⏱️ Timeout: {timeout} seconds")
        print(f"   🔄 Poll interval: {poll_interval} seconds")
        
        # Validate requirements
        op_info = self.ASYNC_OPERATIONS[operation]
        if op_info.get('requires_atom') and not atom_id:
            print("❌ Atom ID required for this operation")
            return False
            
        if op_info.get('requires_queue') and not queue_name:
            print("❌ Queue name required for this operation")
            return False
        
        # Start async operation
        token = self.start_async_operation(operation, atom_id, queue_name)
        if not token:
            print("❌ Failed to start async operation")
            return False
        
        # Poll for result
        max_attempts = timeout // poll_interval
        result = self.poll_async_result(operation, token, poll_interval, max_attempts)
        if not result:
            print("❌ Failed to get async result")
            return False
        
        # Process and display result
        processed = self.process_result(operation, result)
        
        print(f"\n✅ Async operation completed successfully")
        print(f"   📊 Processed {len(processed)} result item(s)")
        
        return True
    
    def show_operations(self):
        """Display available async operations"""
        print("\n📋 Available Async Operations:")
        print("=" * 60)
        
        for key, info in self.ASYNC_OPERATIONS.items():
            print(f"\n   🔹 {key}")
            print(f"      Name: {info['name']}")
            print(f"      Description: {info['description']}")
            
            requirements = []
            if info.get('requires_atom'):
                requirements.append('atom-id')
            if info.get('requires_queue'):
                requirements.append('queue-name')
            if requirements:
                print(f"      Required: {', '.join(requirements)}")
        
        print("\n💡 Use --operation parameter to specify operation")
        print("   Example: --operation atom_counters --atom-id ATOM_ID")


def main():
    parser = argparse.ArgumentParser(
        description='Manage Boomi async operations',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    # Get atom counters
    python async_operations.py --operation atom_counters --atom-id ATOM_ID
    
    # Get disk space with custom polling
    python async_operations.py --operation atom_disk_space --atom-id ATOM_ID --poll-interval 3
    
    # List queues
    python async_operations.py --operation list_queues --atom-id ATOM_ID
    
    # Get atom status
    python async_operations.py --operation atom_status --atom-id ATOM_ID
    
    # Show available operations
    python async_operations.py --list-operations
        """
    )
    
    parser.add_argument('--operation',
                       choices=list(AsyncOperationManager.ASYNC_OPERATIONS.keys()),
                       help='Async operation to execute')
    parser.add_argument('--atom-id', metavar='ID',
                       help='Atom ID for operations that require it')
    parser.add_argument('--queue-name', metavar='NAME',
                       help='Queue name for queue operations')
    parser.add_argument('--poll-interval', type=int, default=2,
                       help='Polling interval in seconds (default: 2)')
    parser.add_argument('--timeout', type=int, default=60,
                       help='Operation timeout in seconds (default: 60)')
    parser.add_argument('--list-operations', action='store_true',
                       help='Show available async operations')
    
    args = parser.parse_args()
    
    # Initialize manager
    manager = AsyncOperationManager()
    
    print("\n⚡ Boomi Async Operations Manager")
    print("=" * 60)
    
    # Execute requested operation
    if args.list_operations:
        manager.show_operations()
    
    elif args.operation:
        success = manager.run_async_workflow(
            operation=args.operation,
            atom_id=args.atom_id,
            queue_name=args.queue_name,
            poll_interval=args.poll_interval,
            timeout=args.timeout
        )
        
        if not success:
            sys.exit(1)
    
    else:
        parser.print_help()
        print("\n💡 Use --help for more examples")


if __name__ == "__main__":
    main()