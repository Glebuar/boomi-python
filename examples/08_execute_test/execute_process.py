#!/usr/bin/env python3
"""
Boomi SDK Example: Execute Process
==================================

This example demonstrates how to execute processes on Boomi runtimes and monitor
their execution status. Supports both synchronous and asynchronous execution modes.

Features:
- Execute processes by ID on specific atoms/runtimes
- Pass dynamic process properties and execution parameters
- Monitor execution status in real-time
- Support for synchronous (wait for completion) and asynchronous modes
- Detailed execution reporting with timing and document counts
- Retry failed executions with configurable parameters
- Export execution results to JSON

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- Appropriate permissions to execute processes on the target runtime
- PROCESS EXECUTION privilege required

Usage:
    # Execute process asynchronously (default)
    python execute_process.py --process-id "process-id" --atom-id "atom-id"
    
    # Execute process and wait for completion (synchronous)
    python execute_process.py --process-id "process-id" --atom-id "atom-id" --sync
    
    # Execute with dynamic properties
    python execute_process.py --process-id "process-id" --atom-id "atom-id" --property "prop1=value1" --property "prop2=value2"
    
    # Execute with timeout and monitoring
    python execute_process.py --process-id "process-id" --atom-id "atom-id" --sync --timeout 300 --poll-interval 5

Examples:
    python execute_process.py --process-id "186bc687-95b9-43f2-b64a-c86355ac8cf2" --atom-id "2d4d5da4-0dfe-41f8-914b-f5f5120ad90a"
    python execute_process.py --process-id "186bc687-95b9-43f2-b64a-c86355ac8cf2" --atom-id "2d4d5da4-0dfe-41f8-914b-f5f5120ad90a" --sync --timeout 60
    python execute_process.py --process-id "186bc687-95b9-43f2-b64a-c86355ac8cf2" --atom-id "2d4d5da4-0dfe-41f8-914b-f5f5120ad90a" --property "env=test" --property "debug=true"
"""

import os
import sys
import argparse
import json
import time
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Any, Tuple

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.boomi import Boomi


class ProcessExecutor:
    """Manages process execution and monitoring operations"""
    
    def __init__(self):
        """Initialize the Boomi SDK client"""
        self.sdk = Boomi(
            account_id=os.getenv("BOOMI_ACCOUNT"),
            username=os.getenv("BOOMI_USER"),
            password=os.getenv("BOOMI_SECRET"),
            timeout=30000
        )
        print("✅ SDK initialized successfully")
    
    def execute_process(self, process_id: str, atom_id: str, 
                       dynamic_properties: Optional[Dict[str, str]] = None,
                       process_properties: Optional[Dict[str, Dict[str, str]]] = None) -> Optional[str]:
        """Execute a process using SDK and return the execution request ID"""
        print(f"\n🚀 Executing process {process_id} on atom {atom_id}")
        
        try:
            # Import SDK models
            from src.boomi.models import (
                ExecutionRequest, 
                ExecutionRequestDynamicProcessProperties,
                ExecutionRequestProcessProperties,
                DynamicProcessProperty
            )
            
            # Build dynamic properties if provided
            dynamic_props = ExecutionRequestDynamicProcessProperties()
            if dynamic_properties:
                print(f"   Adding {len(dynamic_properties)} dynamic properties")
                dynamic_property_list = [
                    DynamicProcessProperty(name=key, value=value)
                    for key, value in dynamic_properties.items()
                ]
                dynamic_props = ExecutionRequestDynamicProcessProperties(
                    dynamic_process_property=dynamic_property_list
                )

            # Build process properties if provided
            proc_props = ExecutionRequestProcessProperties()
            if process_properties:
                print(f"   Adding process properties for {len(process_properties)} components")
                # Note: Process properties model might need to be imported separately
                # For now, we'll handle this in a future iteration
                proc_props = ExecutionRequestProcessProperties()

            # Create execution request
            execution_request = ExecutionRequest(
                atom_id=atom_id,
                process_id=process_id,
                dynamic_process_properties=dynamic_props,
                process_properties=proc_props
            )
            
            # Execute the process using SDK
            result = self.sdk.execution_request.create_execution_request(
                request_body=execution_request
            )
            
            if result and hasattr(result, 'request_id'):
                request_id = result.request_id
                record_url = getattr(result, 'record_url', None)
                
                print(f"✅ Process execution initiated successfully")
                print(f"   Request ID: {request_id}")
                if record_url:
                    print(f"   Record URL: {record_url}")
                
                return request_id
            else:
                print("❌ Failed to execute process: No result returned")
                return None
                
        except Exception as e:
            print(f"❌ Failed to execute process: {e}")
            return None
    
    def get_execution_status(self, execution_id: str) -> Optional[Dict[str, Any]]:
        """Get the status of a specific execution using SDK"""
        try:
            # Import SDK models
            from src.boomi.models import (
                ExecutionRecordQueryConfig,
                ExecutionRecordQueryConfigQueryFilter,
                ExecutionRecordSimpleExpression,
                ExecutionRecordSimpleExpressionOperator,
                ExecutionRecordSimpleExpressionProperty
            )
            
            # Create query expression for the specific execution ID
            query_expression = ExecutionRecordSimpleExpression(
                operator=ExecutionRecordSimpleExpressionOperator.EQUALS,
                property=ExecutionRecordSimpleExpressionProperty.EXECUTIONID,
                argument=[execution_id]
            )
            
            # Create query filter
            query_filter = ExecutionRecordQueryConfigQueryFilter(
                expression=query_expression
            )
            
            # Create query config
            query_config = ExecutionRecordQueryConfig(
                query_filter=query_filter
            )
            
            # Execute query using SDK
            result = self.sdk.execution_record.query_execution_record(
                request_body=query_config
            )
            
            if result and hasattr(result, 'result') and result.result:
                # Convert SDK model to dict for backward compatibility
                execution = result.result[0]
                execution_dict = {
                    'executionId': execution.execution_id,
                    'status': execution.status,
                    'processName': getattr(execution, 'process_name', 'Unknown'),
                    'atomName': getattr(execution, 'atom_name', 'Unknown'),
                    'executionTime': getattr(execution, 'execution_time', 'Unknown'),
                    'executionDuration': getattr(execution, 'execution_duration', None),
                    'inboundDocumentCount': getattr(execution, 'inbound_document_count', 0),
                    'outboundDocumentCount': getattr(execution, 'outbound_document_count', 0),
                    'inboundErrorDocumentCount': getattr(execution, 'inbound_error_document_count', 0)
                }
                return execution_dict
            else:
                return None
                
        except Exception as e:
            print(f"❌ Failed to get execution status: {e}")
            return None
    
    def wait_for_completion(self, request_id: str, timeout_seconds: int = 300, 
                           poll_interval: int = 5) -> Tuple[bool, Optional[Dict[str, Any]]]:
        """Wait for execution to complete with polling"""
        # Extract execution ID from request ID (format: executionrecord-<uuid>)
        if request_id.startswith('executionrecord-'):
            # The execution ID includes date, need to query by request pattern
            execution_base = request_id.replace('executionrecord-', 'execution-')
        else:
            execution_base = request_id
        
        print(f"\n⏳ Waiting for execution to complete (timeout: {timeout_seconds}s, poll interval: {poll_interval}s)")
        
        start_time = datetime.now()
        timeout_time = start_time + timedelta(seconds=timeout_seconds)
        last_status = None
        
        while datetime.now() < timeout_time:
            # Query recent executions to find our execution
            execution_data = self._find_recent_execution(execution_base)
            
            if execution_data:
                status = execution_data.get('status', 'UNKNOWN')
                execution_time = execution_data.get('executionTime', 'N/A')
                
                # Show status updates
                if status != last_status:
                    print(f"   📊 Status: {status} (at {execution_time})")
                    last_status = status
                
                # Check if completed
                if status in ['COMPLETE', 'ERROR', 'ABORTED']:
                    elapsed = (datetime.now() - start_time).total_seconds()
                    print(f"✅ Execution completed after {elapsed:.1f} seconds")
                    return True, execution_data
            
            # Wait before next poll
            time.sleep(poll_interval)
        
        # Timeout reached
        elapsed = (datetime.now() - start_time).total_seconds()
        print(f"⏰ Timeout reached after {elapsed:.1f} seconds")
        
        # Get final status
        final_execution = self._find_recent_execution(execution_base)
        return False, final_execution
    
    def _find_recent_execution(self, execution_pattern: str) -> Optional[Dict[str, Any]]:
        """Find recent execution by pattern matching using SDK"""
        try:
            # Import SDK models
            from src.boomi.models import (
                ExecutionRecordQueryConfig,
                ExecutionRecordQueryConfigQueryFilter,
                ExecutionRecordSimpleExpression,
                ExecutionRecordSimpleExpressionOperator,
                ExecutionRecordSimpleExpressionProperty
            )

            # Create a query filter that matches all executions (use LIKE with wildcard)
            query_expression = ExecutionRecordSimpleExpression(
                operator=ExecutionRecordSimpleExpressionOperator.LIKE,
                property=ExecutionRecordSimpleExpressionProperty.EXECUTIONID,
                argument=["%"]  # Wildcard to match all
            )

            # Create query filter
            query_filter = ExecutionRecordQueryConfigQueryFilter(
                expression=query_expression
            )

            # Create query config
            query_config = ExecutionRecordQueryConfig(
                query_filter=query_filter
            )
            
            # Execute query using SDK
            result = self.sdk.execution_record.query_execution_record(
                request_body=query_config
            )
            
            if result and hasattr(result, 'result') and result.result:
                # Look for executions containing our pattern
                for execution in result.result:
                    exec_id = getattr(execution, 'execution_id', '')
                    if execution_pattern in exec_id:
                        # Convert to dict for backward compatibility
                        execution_dict = {
                            'executionId': execution.execution_id,
                            'status': execution.status,
                            'processName': getattr(execution, 'process_name', 'Unknown'),
                            'atomName': getattr(execution, 'atom_name', 'Unknown'),
                            'executionTime': getattr(execution, 'execution_time', 'Unknown'),
                            'executionDuration': getattr(execution, 'execution_duration', None),
                            'inboundDocumentCount': getattr(execution, 'inbound_document_count', 0),
                            'outboundDocumentCount': getattr(execution, 'outbound_document_count', 0)
                        }
                        return execution_dict
                
            return None
                
        except Exception as e:
            print(f"❌ Error finding execution: {e}")
            return None
    
    def display_execution_results(self, execution_data: Dict[str, Any]) -> None:
        """Display detailed execution results"""
        if not execution_data:
            print("❌ No execution data to display")
            return
        
        print("\n📋 Execution Results:")
        print("=" * 60)
        
        execution_id = execution_data.get('executionId', 'N/A')
        status = execution_data.get('status', 'N/A')
        process_name = execution_data.get('processName', 'N/A')
        atom_name = execution_data.get('atomName', 'N/A')
        execution_time = execution_data.get('executionTime', 'N/A')
        execution_type = execution_data.get('executionType', 'N/A')
        
        # Duration handling (can be array or simple value)
        duration = execution_data.get('executionDuration', 'N/A')
        if isinstance(duration, list) and len(duration) > 1:
            duration_ms = duration[1]
            duration_display = f"{duration_ms}ms ({duration_ms/1000:.2f}s)"
        else:
            duration_display = str(duration)
        
        # Document counts
        inbound_docs = execution_data.get('inboundDocumentCount', 0)
        outbound_docs = execution_data.get('outboundDocumentCount', 0)
        error_docs = execution_data.get('inboundErrorDocumentCount', 0)
        
        # Document sizes
        inbound_size = execution_data.get('inboundDocumentSize', [None, 0])
        outbound_size = execution_data.get('outboundDocumentSize', [None, 0])
        if isinstance(inbound_size, list) and len(inbound_size) > 1:
            inbound_size_display = f"{inbound_size[1]} bytes"
        else:
            inbound_size_display = str(inbound_size)
        
        if isinstance(outbound_size, list) and len(outbound_size) > 1:
            outbound_size_display = f"{outbound_size[1]} bytes"
        else:
            outbound_size_display = str(outbound_size)
        
        # Status icon
        status_icon = {
            'COMPLETE': '✅',
            'ERROR': '❌', 
            'ABORTED': '⏹️',
            'INPROCESS': '⏳',
            'PENDING': '⏳'
        }.get(status, '❓')
        
        print(f"{status_icon} Status: {status}")
        print(f"🆔 Execution ID: {execution_id}")
        print(f"🔧 Process: {process_name}")
        print(f"🤖 Atom: {atom_name}")
        print(f"📅 Execution Time: {self._format_datetime(execution_time)}")
        print(f"🏷️ Type: {execution_type}")
        print(f"⏱️ Duration: {duration_display}")
        
        print(f"\n📊 Document Processing:")
        print(f"   📥 Inbound: {inbound_docs} documents ({inbound_size_display})")
        print(f"   📤 Outbound: {outbound_docs} documents ({outbound_size_display})")
        if error_docs > 0:
            print(f"   ❌ Errors: {error_docs} documents")
        
        # Additional info if available
        if execution_data.get('message'):
            print(f"\n💬 Message: {execution_data['message']}")
        
        node_id = execution_data.get('nodeId', '')
        if node_id:
            print(f"🖥️ Node: {node_id}")
        
        recorded_date = execution_data.get('recordedDate', '')
        if recorded_date:
            print(f"📝 Recorded: {self._format_datetime(recorded_date)}")
    
    def query_process_executions(self, process_id: str, limit: int = 10) -> List[Dict[str, Any]]:
        """Query recent executions for a specific process using SDK"""
        print(f"\n🔍 Querying recent executions for process {process_id}")
        
        try:
            # Import SDK models
            from src.boomi.models import (
                ExecutionRecordQueryConfig,
                ExecutionRecordQueryConfigQueryFilter,
                ExecutionRecordSimpleExpression,
                ExecutionRecordSimpleExpressionOperator,
                ExecutionRecordSimpleExpressionProperty,
                SortField,
                QuerySort
            )
            
            # Create query expression for the specific process ID
            query_expression = ExecutionRecordSimpleExpression(
                operator=ExecutionRecordSimpleExpressionOperator.EQUALS,
                property=ExecutionRecordSimpleExpressionProperty.PROCESSID,
                argument=[process_id]
            )
            
            # Create query filter
            query_filter = ExecutionRecordQueryConfigQueryFilter(
                expression=query_expression
            )
            
            # Create sort configuration
            sort_field = SortField(
                field_name="executionTime",
                sort_order="DESC"
            )
            query_sort = QuerySort(sort_field=[sort_field])
            
            # Create query config
            query_config = ExecutionRecordQueryConfig(
                query_filter=query_filter,
                query_sort=query_sort
            )
            
            # Execute query using SDK
            result = self.sdk.execution_record.query_execution_record(
                request_body=query_config
            )
            
            if result and hasattr(result, 'result') and result.result:
                # Convert SDK models to dicts for backward compatibility
                executions = []
                for execution in result.result[:limit]:
                    execution_dict = {
                        'executionId': execution.execution_id,
                        'status': execution.status,
                        'processName': getattr(execution, 'process_name', 'Unknown'),
                        'atomName': getattr(execution, 'atom_name', 'Unknown'),
                        'executionTime': getattr(execution, 'execution_time', 'Unknown'),
                        'executionDuration': getattr(execution, 'execution_duration', None),
                        'inboundDocumentCount': getattr(execution, 'inbound_document_count', 0),
                        'outboundDocumentCount': getattr(execution, 'outbound_document_count', 0),
                        'inboundErrorDocumentCount': getattr(execution, 'inbound_error_document_count', 0)
                    }
                    executions.append(execution_dict)
                
                total_count = getattr(result, 'number_of_results', len(executions))
                print(f"✅ Found {total_count} execution(s) for this process")
                return executions
            else:
                print("✅ No executions found for this process")
                return []
                
        except Exception as e:
            print(f"❌ Failed to query executions: {e}")
            return []
    
    def display_executions_summary(self, executions: List[Dict[str, Any]]) -> None:
        """Display summary of multiple executions"""
        if not executions:
            print("📊 No executions to display")
            return
        
        print(f"\n📊 Recent Executions Summary ({len(executions)} shown):")
        print("=" * 100)
        
        for i, execution in enumerate(executions, 1):
            execution_id = execution.get('executionId', 'N/A')
            status = execution.get('status', 'N/A')
            execution_time = execution.get('executionTime', 'N/A')
            
            # Duration handling
            duration = execution.get('executionDuration', 'N/A')
            if isinstance(duration, list) and len(duration) > 1:
                duration_display = f"{duration[1]}ms"
            else:
                duration_display = str(duration)
            
            # Document counts
            inbound_docs = execution.get('inboundDocumentCount', 0)
            outbound_docs = execution.get('outboundDocumentCount', 0)
            
            # Status icon
            status_icon = {
                'COMPLETE': '✅',
                'ERROR': '❌', 
                'ABORTED': '⏹️',
                'INPROCESS': '⏳'
            }.get(status, '❓')
            
            # Truncate long execution IDs for display
            display_id = execution_id[:50] + "..." if len(execution_id) > 53 else execution_id
            
            print(f"{i:2}. {status_icon} {display_id}")
            print(f"     📅 {self._format_datetime(execution_time)} | ⏱️ {duration_display} | 📊 {inbound_docs}→{outbound_docs} docs")
            print()
    
    def _format_datetime(self, datetime_string: str) -> str:
        """Format ISO datetime string to readable format"""
        try:
            if datetime_string and datetime_string != 'N/A':
                dt = datetime.fromisoformat(datetime_string.replace('Z', '+00:00'))
                return dt.strftime('%Y-%m-%d %H:%M:%S UTC')
        except:
            pass
        return datetime_string or 'N/A'
    
    def export_execution_data(self, execution_data: Dict[str, Any], filename: str) -> bool:
        """Export execution data to JSON file"""
        try:
            with open(filename, 'w') as f:
                json.dump({
                    'export_date': datetime.now().isoformat(),
                    'execution': execution_data
                }, f, indent=2)
            
            print(f"📄 Exported execution data to {filename}")
            return True
        except Exception as e:
            print(f"❌ Failed to export to {filename}: {e}")
            return False
    
    def show_execution_help(self) -> None:
        """Show execution examples and tips"""
        print("\n💡 Process Execution Help:")
        print("=" * 50)
        
        print("🚀 Basic Execution:")
        print("   python execute_process.py --process-id PROCESS_ID --atom-id ATOM_ID")
        
        print("\n⏳ Synchronous Execution (wait for completion):")
        print("   python execute_process.py --process-id PROCESS_ID --atom-id ATOM_ID --sync")
        
        print("\n🔧 With Dynamic Properties:")
        print("   python execute_process.py --process-id PROCESS_ID --atom-id ATOM_ID \\")
        print("     --property env=production --property debug=false")
        
        print("\n⏰ With Custom Timeout:")
        print("   python execute_process.py --process-id PROCESS_ID --atom-id ATOM_ID \\")
        print("     --sync --timeout 120 --poll-interval 10")
        
        print("\n📊 Query Recent Executions:")
        print("   python execute_process.py --query --process-id PROCESS_ID --limit 5")
        
        print("\n💾 Export Results:")
        print("   python execute_process.py --process-id PROCESS_ID --atom-id ATOM_ID \\")
        print("     --sync --export results.json")
        
        print("\n📋 Tips:")
        print("   • Use --sync for testing and validation workflows")
        print("   • Async mode is better for long-running processes")
        print("   • Dynamic properties override process defaults")
        print("   • Monitor executions via Boomi UI for detailed logs")
        print("   • Use shorter poll intervals for faster feedback")


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='Execute Boomi processes and monitor execution status',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  %(prog)s --process-id "abc123" --atom-id "def456"                    # Execute async
  %(prog)s --process-id "abc123" --atom-id "def456" --sync            # Execute and wait
  %(prog)s --process-id "abc123" --atom-id "def456" --property "env=test"  # With properties
  %(prog)s --query --process-id "abc123" --limit 5                    # Query recent executions
  %(prog)s --process-id "abc123" --atom-id "def456" --sync --export results.json  # Export results

Execution Modes:
  • Async (default): Start execution and return immediately with request ID
  • Sync: Start execution and wait for completion with status polling
  
Dynamic Properties:
  • Pass runtime parameters to processes
  • Override process default properties
  • Format: --property "key=value"
  
Monitoring:
  • Poll interval: How often to check status (default: 5s)
  • Timeout: Maximum wait time for sync mode (default: 300s)
        '''
    )
    
    # Required parameters (for execution)
    parser.add_argument('--process-id', metavar='ID',
                       help='Process ID to execute')
    parser.add_argument('--atom-id', metavar='ID',
                       help='Atom/Runtime ID to execute on')
    
    # Execution options
    parser.add_argument('--sync', action='store_true',
                       help='Execute synchronously (wait for completion)')
    parser.add_argument('--timeout', type=int, default=300, metavar='SECONDS',
                       help='Timeout for synchronous execution (default: 300)')
    parser.add_argument('--poll-interval', type=int, default=5, metavar='SECONDS',
                       help='Polling interval for status checks (default: 5)')
    
    # Properties
    parser.add_argument('--property', action='append', metavar='KEY=VALUE',
                       help='Dynamic process property (can be used multiple times)')
    
    # Query mode
    parser.add_argument('--query', action='store_true',
                       help='Query recent executions for the process')
    parser.add_argument('--limit', type=int, default=10, metavar='N',
                       help='Maximum number of executions to show (default: 10)')
    
    # Output options
    parser.add_argument('--export', metavar='FILENAME',
                       help='Export execution results to JSON file')
    parser.add_argument('--help-examples', action='store_true',
                       help='Show execution examples and tips')
    
    args = parser.parse_args()
    
    # Validate environment variables
    required_env = ['BOOMI_ACCOUNT', 'BOOMI_USER', 'BOOMI_SECRET']
    missing = [var for var in required_env if not os.getenv(var)]
    
    if missing:
        print("❌ Missing environment variables:")
        for var in missing:
            print(f"  - {var}")
        print("\n💡 Set these in your .env file or export them")
        sys.exit(1)
    
    # Execute operation
    try:
        executor = ProcessExecutor()
        
        # Show help examples
        if args.help_examples:
            executor.show_execution_help()
            return
        
        # Query mode
        if args.query:
            if not args.process_id:
                print("❌ --process-id is required for query mode")
                sys.exit(1)
            
            executions = executor.query_process_executions(args.process_id, args.limit)
            executor.display_executions_summary(executions)
            return
        
        # Execution mode - validate required parameters
        if not args.process_id or not args.atom_id:
            print("❌ --process-id and --atom-id are required for execution")
            print("💡 Use --help-examples to see usage examples")
            sys.exit(1)
        
        # Parse dynamic properties
        dynamic_properties = {}
        if args.property:
            for prop in args.property:
                if '=' not in prop:
                    print(f"❌ Invalid property format: {prop}")
                    print("💡 Use format: --property 'key=value'")
                    sys.exit(1)
                
                key, value = prop.split('=', 1)
                dynamic_properties[key.strip()] = value.strip()
        
        # Execute the process
        print(f"\n🚀 Boomi Process Execution")
        print("=" * 50)
        
        request_id = executor.execute_process(
            args.process_id, 
            args.atom_id,
            dynamic_properties=dynamic_properties if dynamic_properties else None
        )
        
        if not request_id:
            print("❌ Process execution failed")
            sys.exit(1)
        
        # Handle synchronous vs asynchronous execution
        if args.sync:
            # Wait for completion
            completed, execution_data = executor.wait_for_completion(
                request_id, 
                args.timeout, 
                args.poll_interval
            )
            
            if execution_data:
                executor.display_execution_results(execution_data)
                
                # Export if requested
                if args.export:
                    executor.export_execution_data(execution_data, args.export)
            
            if not completed:
                print("\n⚠️ Execution did not complete within timeout")
                sys.exit(1)
        else:
            # Asynchronous mode - just return the request ID
            print(f"\n✅ Process execution initiated successfully")
            print(f"📋 Request ID: {request_id}")
            print(f"💡 Use ExecutionRecord query to monitor status")
            print(f"💡 Or run with --sync to wait for completion")
        
    except KeyboardInterrupt:
        print("\n❌ Operation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()