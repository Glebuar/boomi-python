#!/usr/bin/env python3
"""
Queue Management Example for Boomi Python SDK

This example demonstrates how to manage queues and messages in Boomi runtime environments:
- List all queues for a runtime
- Clear messages from queues
- Move messages between queues
- Monitor queue status and message counts

The example uses async queue operations as per Boomi API requirements for queue listing.

Usage:
    python manage_queues.py --list --atom-id <atom-id>
    python manage_queues.py --clear --atom-id <atom-id> --queue-name <name>
    python manage_queues.py --move --atom-id <atom-id> --source-queue <name> --dest-queue <name>
    python manage_queues.py --monitor --atom-id <atom-id>
"""

import argparse
import json
import os
import sys
import time
from datetime import datetime
from typing import Dict, List, Optional, Any

# Add src to Python path for SDK imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "src"))

from boomi import Boomi
from boomi.models import (
    ClearQueueRequest,
    MoveQueueRequest,
    QueueAttributes,
    AsyncOperationTokenResult,
    ListQueuesAsyncResponse
)


class QueueManager:
    """Manages Boomi runtime queues and messages."""
    
    def __init__(self):
        """Initialize the Queue Manager with SDK."""
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
    
    def list_queues_async(self, atom_id: str, timeout_seconds: int = 60) -> List[Dict]:
        """
        List all queues for a runtime using async operations.
        
        Args:
            atom_id: The runtime/atom ID
            timeout_seconds: Maximum time to wait for async operation
            
        Returns:
            List of queue information dictionaries
        """
        print(f"📋 Listing queues for runtime: {atom_id}")
        
        try:
            # Step 1: Initiate async list queues operation
            print("   Initiating async queue list operation...")
            token_result = self.sdk.list_queues.async_get_list_queues(id_=atom_id)
            
            if not hasattr(token_result, 'async_token') or not hasattr(token_result.async_token, 'token'):
                print("❌ Failed to get async operation token")
                return []
                
            token = token_result.async_token.token
            print(f"   Got async token: {token}")
            
            # Step 2: Poll for results
            print("   Polling for results...")
            start_time = time.time()
            
            while time.time() - start_time < timeout_seconds:
                try:
                    response = self.sdk.list_queues.async_token_list_queues(token=token)
                    
                    if hasattr(response, 'result') and response.result:
                        print(f"✅ Retrieved {len(response.result)} queue records")
                        return self._parse_queue_response(response.result)
                        
                    print("   Still processing... waiting 2 seconds")
                    time.sleep(2)
                    
                except Exception as poll_error:
                    if "still processing" in str(poll_error).lower():
                        time.sleep(2)
                        continue
                    else:
                        raise poll_error
            
            print(f"⚠️ Timeout after {timeout_seconds} seconds")
            return []
            
        except Exception as e:
            print(f"❌ Error listing queues: {e}")
            return []
    
    def _parse_queue_response(self, queue_results: List) -> List[Dict]:
        """Parse the async queue response into a usable format."""
        queues = []

        for result in queue_results:
            if hasattr(result, 'queue_record') and result.queue_record:
                for queue_record in result.queue_record:
                    queue_info = {
                        'name': getattr(queue_record, 'queue_name', 'Unknown'),
                        'type': getattr(queue_record, 'queue_type', 'Unknown'),
                        'message_count': getattr(queue_record, 'messages_count', 0),
                        'dead_letter_count': getattr(queue_record, 'dead_letters_count', 0),
                        'subscribers': []
                    }
                    
                    # Add subscriber information for topics
                    if hasattr(queue_record, 'topic_subscribers') and queue_record.topic_subscribers:
                        for subscriber in queue_record.topic_subscribers:
                            queue_info['subscribers'].append({
                                'name': getattr(subscriber, 'subscriber_name', 'Unknown'),
                                'message_count': getattr(subscriber, 'messages_count', 0)
                            })
                    
                    queues.append(queue_info)
        
        return queues
    
    def clear_queue(self, atom_id: str, queue_name: str, clear_dlq: bool = False, 
                   subscriber_name: Optional[str] = None) -> bool:
        """
        Clear messages from a queue.
        
        Args:
            atom_id: The runtime/atom ID
            queue_name: Name of the queue to clear
            clear_dlq: Whether to clear dead letter queue (True) or regular queue (False)
            subscriber_name: Subscriber name (for topic queues only)
            
        Returns:
            True if successful, False otherwise
        """
        print(f"🗑️ Clearing {'DLQ' if clear_dlq else 'regular'} messages from queue: {queue_name}")
        
        try:
            # Create clear queue request
            clear_request = ClearQueueRequest(
                atom_id=atom_id,
                queue_name=queue_name,
                dlq=clear_dlq
            )
            
            # Add subscriber name if provided
            if subscriber_name:
                clear_request.subscriber_name = subscriber_name
                print(f"   Targeting subscriber: {subscriber_name}")
            
            # Execute clear operation
            result = self.sdk.clear_queue.execute_clear_queue(
                id_=atom_id,
                request_body=clear_request
            )
            
            print("✅ Clear queue operation submitted successfully")
            print("   Note: Check queue message count to verify completion")
            return True
            
        except Exception as e:
            print(f"❌ Error clearing queue: {e}")
            return False
    
    def move_queue_messages(self, atom_id: str, source_queue: str, dest_queue: str, 
                          source_dlq: bool = False, dest_dlq: bool = False,
                          source_subscriber: Optional[str] = None,
                          dest_subscriber: Optional[str] = None) -> bool:
        """
        Move messages from one queue to another.
        
        Args:
            atom_id: The runtime/atom ID
            source_queue: Source queue name
            dest_queue: Destination queue name
            source_dlq: Whether source is dead letter queue
            dest_dlq: Whether destination is dead letter queue
            source_subscriber: Source subscriber name (for topics)
            dest_subscriber: Destination subscriber name (for topics)
            
        Returns:
            True if successful, False otherwise
        """
        print(f"📦 Moving messages from '{source_queue}' to '{dest_queue}'")
        
        try:
            # Create source queue attributes
            source_attrs = QueueAttributes(
                dlq=source_dlq,
                queue_name=source_queue
            )
            if source_subscriber:
                source_attrs.subscriber_name = source_subscriber
                print(f"   Source subscriber: {source_subscriber}")
            
            # Create destination queue attributes  
            dest_attrs = QueueAttributes(
                dlq=dest_dlq,
                queue_name=dest_queue
            )
            if dest_subscriber:
                dest_attrs.subscriber_name = dest_subscriber
                print(f"   Destination subscriber: {dest_subscriber}")
            
            # Create move request
            move_request = MoveQueueRequest(
                atom_id=atom_id,
                source_queue=source_attrs,
                destination_queue=dest_attrs
            )
            
            # Execute move operation
            result = self.sdk.move_queue_request.create_move_queue_request(
                request_body=move_request
            )
            
            print("✅ Move queue operation submitted successfully")
            print("   Note: Monitor queue counts to track move progress")
            return True
            
        except Exception as e:
            print(f"❌ Error moving queue messages: {e}")
            return False
    
    def monitor_queues(self, atom_id: str, interval_seconds: int = 10, 
                      max_iterations: int = 6) -> None:
        """
        Monitor queue status and message counts over time.
        
        Args:
            atom_id: The runtime/atom ID
            interval_seconds: Time between checks
            max_iterations: Maximum number of monitoring cycles
        """
        print(f"👁️ Monitoring queues for runtime: {atom_id}")
        print(f"   Checking every {interval_seconds} seconds for {max_iterations} cycles")
        
        for i in range(max_iterations):
            print(f"\n--- Monitoring Cycle {i+1}/{max_iterations} ---")
            print(f"Time: {datetime.now().strftime('%H:%M:%S')}")
            
            queues = self.list_queues_async(atom_id, timeout_seconds=30)
            
            if queues:
                self._display_queue_summary(queues, show_details=False)
            else:
                print("   No queues found or error occurred")
            
            if i < max_iterations - 1:  # Don't sleep after last iteration
                print(f"   Waiting {interval_seconds} seconds...")
                time.sleep(interval_seconds)
        
        print("\n📊 Monitoring complete")
    
    def _display_queue_summary(self, queues: List[Dict], show_details: bool = True) -> None:
        """Display a formatted summary of queue information."""
        if not queues:
            print("   No queues found")
            return
        
        print(f"\n📋 Found {len(queues)} queue(s):")
        print("-" * 80)
        
        total_messages = 0
        total_dlq_messages = 0
        
        for queue in queues:
            name = queue['name']
            qtype = queue['type']
            msg_count = self._safe_int(queue['message_count'])
            dlq_count = self._safe_int(queue['dead_letter_count'])
            
            total_messages += msg_count
            total_dlq_messages += dlq_count
            
            status_icon = "🟢" if msg_count == 0 and dlq_count == 0 else "🟡" if dlq_count == 0 else "🔴"
            
            print(f"{status_icon} {name} ({qtype})")
            print(f"    Messages: {msg_count:,}, DLQ: {dlq_count:,}")
            
            # Show subscribers for topics
            if show_details and queue['subscribers']:
                print(f"    Subscribers:")
                for subscriber in queue['subscribers']:
                    sub_name = subscriber['name']
                    sub_count = self._safe_int(subscriber['message_count'])
                    print(f"      - {sub_name}: {sub_count:,} messages")
            
            if show_details:
                print()
        
        print("-" * 80)
        print(f"📊 Total: {total_messages:,} messages, {total_dlq_messages:,} DLQ messages")
        
        # Queue health assessment
        if total_dlq_messages > 0:
            print("⚠️ Warning: Dead letter messages detected - investigate failed processing")
        elif total_messages == 0:
            print("✅ All queues are empty - system processing normally")
        else:
            print(f"ℹ️ {total_messages:,} messages pending processing")
    
    def _safe_int(self, value: Any) -> int:
        """Safely convert value to integer, handling None and string values."""
        if value is None:
            return 0
        if isinstance(value, int):
            return value
        try:
            return int(str(value))
        except (ValueError, TypeError):
            return 0
    
    def get_queue_statistics(self, atom_id: str) -> Dict[str, Any]:
        """
        Get comprehensive queue statistics for a runtime.
        
        Args:
            atom_id: The runtime/atom ID
            
        Returns:
            Dictionary with queue statistics
        """
        queues = self.list_queues_async(atom_id)
        
        if not queues:
            return {"error": "No queues found or error occurred"}
        
        stats = {
            "total_queues": len(queues),
            "queue_types": {},
            "total_messages": 0,
            "total_dlq_messages": 0,
            "empty_queues": 0,
            "queues_with_dlq": 0,
            "topic_subscribers": 0,
            "queues": []
        }
        
        for queue in queues:
            qtype = queue['type']
            msg_count = self._safe_int(queue['message_count'])
            dlq_count = self._safe_int(queue['dead_letter_count'])
            
            # Update type counts
            stats["queue_types"][qtype] = stats["queue_types"].get(qtype, 0) + 1
            
            # Update totals
            stats["total_messages"] += msg_count
            stats["total_dlq_messages"] += dlq_count
            
            # Update counts
            if msg_count == 0 and dlq_count == 0:
                stats["empty_queues"] += 1
            if dlq_count > 0:
                stats["queues_with_dlq"] += 1
            
            # Count subscribers
            stats["topic_subscribers"] += len(queue['subscribers'])
            
            stats["queues"].append({
                "name": queue['name'],
                "type": qtype,
                "messages": msg_count,
                "dlq_messages": dlq_count,
                "subscribers": len(queue['subscribers'])
            })
        
        return stats


def main():
    """Main CLI interface for queue management operations."""
    parser = argparse.ArgumentParser(
        description="Manage Boomi runtime queues and messages",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # List all queues for a runtime
  python manage_queues.py --list --atom-id 12345678-1234-1234-1234-123456789012
  
  # Clear regular messages from a queue
  python manage_queues.py --clear --atom-id 12345678-1234-1234-1234-123456789012 --queue-name "MyQueue"
  
  # Clear dead letter messages from a queue
  python manage_queues.py --clear --atom-id 12345678-1234-1234-1234-123456789012 --queue-name "MyQueue" --dlq
  
  # Move messages between queues
  python manage_queues.py --move --atom-id 12345678-1234-1234-1234-123456789012 --source-queue "Queue1" --dest-queue "Queue2"
  
  # Monitor queues over time
  python manage_queues.py --monitor --atom-id 12345678-1234-1234-1234-123456789012 --interval 30 --cycles 10
  
  # Get detailed queue statistics
  python manage_queues.py --stats --atom-id 12345678-1234-1234-1234-123456789012
  
  # Show help with examples
  python manage_queues.py --help-examples

Environment Variables Required:
  BOOMI_ACCOUNT - Your Boomi account ID
  BOOMI_USER - Your Boomi username (or token username)
  BOOMI_SECRET - Your Boomi password (or token password)
        """
    )
    
    # Operation selection (mutually exclusive group)
    operations = parser.add_mutually_exclusive_group(required=True)
    operations.add_argument('--list', action='store_true',
                           help='List all queues for the runtime')
    operations.add_argument('--clear', action='store_true', 
                           help='Clear messages from a queue')
    operations.add_argument('--move', action='store_true',
                           help='Move messages between queues')
    operations.add_argument('--monitor', action='store_true',
                           help='Monitor queue status over time')
    operations.add_argument('--stats', action='store_true',
                           help='Get detailed queue statistics')
    operations.add_argument('--help-examples', action='store_true',
                           help='Show detailed usage examples')
    
    # Global options
    parser.add_argument('--atom-id', 
                       help='Runtime/Atom ID (required for all operations except help-examples)')
    
    # Clear operation options
    parser.add_argument('--queue-name', help='Queue name (required for clear operations)')
    parser.add_argument('--dlq', action='store_true', 
                       help='Target dead letter queue instead of regular queue')
    parser.add_argument('--subscriber', help='Subscriber name (for topic queues)')
    
    # Move operation options
    parser.add_argument('--source-queue', help='Source queue name (required for move operations)')
    parser.add_argument('--dest-queue', help='Destination queue name (required for move operations)')
    parser.add_argument('--source-dlq', action='store_true',
                       help='Source is dead letter queue')
    parser.add_argument('--dest-dlq', action='store_true', 
                       help='Destination is dead letter queue')
    parser.add_argument('--source-subscriber', help='Source subscriber name (for topics)')
    parser.add_argument('--dest-subscriber', help='Destination subscriber name (for topics)')
    
    # Monitor operation options
    parser.add_argument('--interval', type=int, default=10,
                       help='Monitoring interval in seconds (default: 10)')
    parser.add_argument('--cycles', type=int, default=6,
                       help='Number of monitoring cycles (default: 6)')
    
    args = parser.parse_args()
    
    # Show help examples
    if args.help_examples:
        show_help_examples()
        return
    
    # Validate atom-id is provided for all operations except help-examples
    if not args.atom_id:
        print("❌ Error: --atom-id is required for all operations")
        sys.exit(1)
    
    # Validate operation-specific arguments
    if args.clear and not args.queue_name:
        print("❌ Error: --queue-name is required for clear operations")
        sys.exit(1)
    
    if args.move and (not args.source_queue or not args.dest_queue):
        print("❌ Error: --source-queue and --dest-queue are required for move operations")
        sys.exit(1)
    
    # Initialize queue manager
    try:
        queue_manager = QueueManager()
    except SystemExit:
        return  # SDK initialization failed with proper error message
    except Exception as e:
        print(f"❌ Error initializing queue manager: {e}")
        return
    
    print("🔧 Boomi Queue Management Tool")
    print("=" * 50)
    
    # Execute requested operation
    try:
        if args.list:
            queues = queue_manager.list_queues_async(args.atom_id)
            queue_manager._display_queue_summary(queues)
            
        elif args.clear:
            success = queue_manager.clear_queue(
                atom_id=args.atom_id,
                queue_name=args.queue_name,
                clear_dlq=args.dlq,
                subscriber_name=args.subscriber
            )
            sys.exit(0 if success else 1)
            
        elif args.move:
            success = queue_manager.move_queue_messages(
                atom_id=args.atom_id,
                source_queue=args.source_queue,
                dest_queue=args.dest_queue,
                source_dlq=args.source_dlq,
                dest_dlq=args.dest_dlq,
                source_subscriber=args.source_subscriber,
                dest_subscriber=args.dest_subscriber
            )
            sys.exit(0 if success else 1)
            
        elif args.monitor:
            queue_manager.monitor_queues(
                atom_id=args.atom_id,
                interval_seconds=args.interval,
                max_iterations=args.cycles
            )
            
        elif args.stats:
            stats = queue_manager.get_queue_statistics(args.atom_id)
            if "error" in stats:
                print(f"❌ {stats['error']}")
                sys.exit(1)
            
            print(f"\n📊 Queue Statistics for Runtime: {args.atom_id}")
            print("-" * 60)
            print(f"Total Queues: {stats['total_queues']}")
            print(f"Empty Queues: {stats['empty_queues']}")
            print(f"Queues with DLQ Messages: {stats['queues_with_dlq']}")
            print(f"Total Messages: {stats['total_messages']:,}")
            print(f"Total DLQ Messages: {stats['total_dlq_messages']:,}")
            print(f"Topic Subscribers: {stats['topic_subscribers']}")
            
            if stats['queue_types']:
                print(f"\nQueue Types:")
                for qtype, count in stats['queue_types'].items():
                    print(f"  {qtype}: {count}")
                    
            print(f"\nDetailed Queue List:")
            for queue in stats['queues']:
                dlq_info = f", DLQ: {queue['dlq_messages']}" if queue['dlq_messages'] > 0 else ""
                sub_info = f", Subscribers: {queue['subscribers']}" if queue['subscribers'] > 0 else ""
                print(f"  {queue['name']} ({queue['type']}): {queue['messages']} messages{dlq_info}{sub_info}")
                
    except KeyboardInterrupt:
        print("\n⚠️ Operation cancelled by user")
    except Exception as e:
        print(f"❌ Error executing operation: {e}")
        sys.exit(1)


def show_help_examples():
    """Display detailed usage examples."""
    print("""
🔧 Boomi Queue Management - Detailed Examples

ENVIRONMENT SETUP:
  export BOOMI_ACCOUNT="your-account-id"
  export BOOMI_USER="BOOMI_TOKEN.username@company.com"
  export BOOMI_SECRET="your-api-token"

BASIC OPERATIONS:

1. List All Queues:
   python manage_queues.py --list --atom-id 12345678-1234-1234-1234-123456789012
   
   Shows all queues with message counts and types.

2. Clear Queue Messages:
   # Clear regular messages
   python manage_queues.py --clear --atom-id 12345678-1234-1234-1234-123456789012 --queue-name "ProcessQueue"
   
   # Clear dead letter messages
   python manage_queues.py --clear --atom-id 12345678-1234-1234-1234-123456789012 --queue-name "ProcessQueue" --dlq
   
   # Clear topic subscriber messages
   python manage_queues.py --clear --atom-id 12345678-1234-1234-1234-123456789012 --queue-name "MyTopic" --subscriber "subscriber1"

3. Move Messages Between Queues:
   # Basic queue to queue move
   python manage_queues.py --move --atom-id 12345678-1234-1234-1234-123456789012 --source-queue "FailedQueue" --dest-queue "RetryQueue"
   
   # Move DLQ messages to regular queue
   python manage_queues.py --move --atom-id 12345678-1234-1234-1234-123456789012 --source-queue "ProcessQueue" --dest-queue "ProcessQueue" --source-dlq --dest-queue "ProcessQueue"

MONITORING AND ANALYSIS:

4. Monitor Queues Over Time:
   # Monitor every 30 seconds for 10 cycles
   python manage_queues.py --monitor --atom-id 12345678-1234-1234-1234-123456789012 --interval 30 --cycles 10

5. Get Detailed Statistics:
   python manage_queues.py --stats --atom-id 12345678-1234-1234-1234-123456789012

TROUBLESHOOTING SCENARIOS:

A. Clear Stuck Messages:
   # List queues to identify issues
   python manage_queues.py --list --atom-id <atom-id>
   
   # Clear problematic queue
   python manage_queues.py --clear --atom-id <atom-id> --queue-name "StuckQueue"

B. Recover Failed Messages:
   # Move DLQ messages back to processing queue
   python manage_queues.py --move --atom-id <atom-id> --source-queue "ProcessQueue" --dest-queue "ProcessQueue" --source-dlq

C. Queue Monitoring During Deployment:
   # Monitor during high-load periods
   python manage_queues.py --monitor --atom-id <atom-id> --interval 15 --cycles 20

QUEUE TYPES AND USAGE:
- Point-to-Point: Direct queue to queue messaging
- Publish/Subscribe: Topic-based messaging with subscribers
- Dead Letter Queue (DLQ): Failed message storage

BEST PRACTICES:
1. Always list queues before performing operations
2. Use monitoring during high-traffic periods
3. Clear DLQ messages only after investigating failures
4. Move messages during low-traffic windows when possible
5. Monitor queue depths to prevent memory issues

For more information, consult Boomi documentation on Queue Management.
    """)


if __name__ == "__main__":
    main()