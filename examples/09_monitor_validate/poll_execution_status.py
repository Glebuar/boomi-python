#!/usr/bin/env python3
"""
Poll Execution Status - Monitor execution progress and wait for completion

This example demonstrates how to monitor execution progress and wait for completion
using the ExecutionRecord API endpoint.

Features:
- Poll execution status with configurable intervals
- Wait for completion with timeout
- Handle different execution states (running, complete, error)
- Return final execution result with comprehensive details
- Progress indicators and status updates
- Timeout and retry logic

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET

Usage:
    python poll_execution_status.py EXECUTION_ID [options]
    
Examples:
    # Basic polling with default timeout (5 minutes) and interval (5 seconds)
    python poll_execution_status.py execution-abc123-def456-2025.08.17
    
    # Custom timeout and polling interval
    python poll_execution_status.py execution-abc123-def456-2025.08.17 --timeout 600 --interval 10
    
    # JSON output for automation
    python poll_execution_status.py execution-abc123-def456-2025.08.17 --json
    
    # Verbose mode with detailed progress
    python poll_execution_status.py execution-abc123-def456-2025.08.17 --verbose

Required Endpoints:
- ExecutionRecord/query - Check execution status and get details
"""

import os
import sys
import argparse
import requests
from requests.auth import HTTPBasicAuth
import json
import time
from datetime import datetime, timedelta
from typing import Optional, Dict, Any, Tuple


class ExecutionStatusPoller:
    """Poll execution status and wait for completion"""
    
    def __init__(self):
        self.account_id = os.getenv('BOOMI_ACCOUNT')
        self.username = os.getenv('BOOMI_USER')
        self.password = os.getenv('BOOMI_SECRET')
        
        if not all([self.account_id, self.username, self.password]):
            raise ValueError("Environment variables BOOMI_ACCOUNT, BOOMI_USER, and BOOMI_SECRET must be set")
        
        self.base_url = f"https://api.boomi.com/api/rest/v1/{self.account_id}"
        self.auth = HTTPBasicAuth(self.username, self.password)
        self.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

    def get_execution_status(self, execution_id: str) -> Optional[Dict[str, Any]]:
        """Get current execution status and details"""
        url = f"{self.base_url}/ExecutionRecord/query"
        
        query_payload = {
            "QueryFilter": {
                "expression": {
                    "argument": [execution_id],
                    "operator": "EQUALS",
                    "property": "executionId"
                }
            }
        }
        
        try:
            response = requests.post(url, json=query_payload, auth=self.auth, headers=self.headers, timeout=30)
            
            if response.status_code == 200:
                result = response.json()
                executions = result.get('result', [])
                
                if executions:
                    return executions[0]  # Return first (should be only) matching execution
                else:
                    return None
            else:
                print(f"❌ Error querying execution status: {response.status_code}")
                print(f"Response: {response.text}")
                return None
                
        except requests.exceptions.RequestException as e:
            print(f"❌ Request failed: {str(e)}")
            return None

    def is_execution_complete(self, status: str) -> Tuple[bool, bool]:
        """
        Check if execution is complete and successful
        
        Returns:
            Tuple[bool, bool]: (is_complete, is_successful)
        """
        status_upper = status.upper()
        
        if status_upper in ['COMPLETE']:
            return True, True
        elif status_upper in ['ERROR', 'ABORTED', 'FAILED']:
            return True, False
        elif status_upper in ['INPROCESS', 'STARTED', 'PENDING', 'RUNNING']:
            return False, False
        else:
            # Unknown status, treat as incomplete
            return False, False

    def format_duration(self, duration_ms: Any) -> str:
        """Format execution duration for display"""
        if isinstance(duration_ms, list):
            # Handle ['Long', milliseconds] format
            if len(duration_ms) >= 2:
                ms = duration_ms[1]
            else:
                return "Unknown"
        elif isinstance(duration_ms, (int, float)):
            ms = duration_ms
        else:
            return str(duration_ms)
        
        try:
            ms = int(ms)
            if ms < 1000:
                return f"{ms}ms"
            elif ms < 60000:
                return f"{ms/1000:.1f}s"
            else:
                minutes = ms // 60000
                seconds = (ms % 60000) / 1000
                return f"{minutes}m {seconds:.1f}s"
        except (ValueError, TypeError):
            return str(duration_ms)

    def display_execution_details(self, execution: Dict[str, Any], verbose: bool = False) -> None:
        """Display execution details in a formatted way"""
        status = execution.get('status', 'Unknown')
        process_name = execution.get('processName', 'Unknown Process')
        execution_time = execution.get('executionTime', 'Unknown')
        duration = execution.get('executionDuration', 'Unknown')
        atom_name = execution.get('atomName', 'Unknown')
        
        # Status indicator
        status_upper = status.upper()
        if status_upper == 'COMPLETE':
            status_indicator = "✅"
        elif status_upper in ['ERROR', 'ABORTED', 'FAILED']:
            status_indicator = "❌"
        elif status_upper in ['INPROCESS', 'STARTED', 'PENDING', 'RUNNING']:
            status_indicator = "🟡"
        else:
            status_indicator = "❓"
        
        print(f"{status_indicator} Status: {status}")
        print(f"📋 Process: {process_name}")
        print(f"🚀 Atom: {atom_name}")
        print(f"⏰ Execution Time: {execution_time}")
        print(f"⏱️ Duration: {self.format_duration(duration)}")
        
        # Document counts
        in_docs = execution.get('inboundDocumentCount', 0)
        out_docs = execution.get('outboundDocumentCount', 0)
        print(f"📊 Documents: {in_docs} in / {out_docs} out")
        
        # Error details if present
        error = execution.get('error')
        if error:
            print(f"💥 Error: {error}")
        
        if verbose:
            print(f"🆔 Execution ID: {execution.get('executionId', 'Unknown')}")
            print(f"🆔 Process ID: {execution.get('processId', 'Unknown')}")
            print(f"🆔 Atom ID: {execution.get('atomId', 'Unknown')}")
            
            # Additional metrics if available
            for key, label in [
                ('executionHost', '🖥️ Host'),
                ('executionRank', '📈 Rank'),
                ('executionType', '🔧 Type'),
                ('executionSubType', '🔍 Sub-Type')
            ]:
                value = execution.get(key)
                if value:
                    print(f"{label}: {value}")

    def poll_execution(
        self, 
        execution_id: str, 
        timeout_seconds: int = 300, 
        poll_interval: int = 5,
        verbose: bool = False
    ) -> Tuple[bool, Optional[Dict[str, Any]]]:
        """
        Poll execution status until completion or timeout
        
        Args:
            execution_id: The execution ID to monitor
            timeout_seconds: Maximum time to wait (default: 5 minutes)
            poll_interval: Seconds between polls (default: 5 seconds)
            verbose: Show detailed progress information
            
        Returns:
            Tuple[bool, Optional[Dict]]: (success, final_execution_data)
        """
        print(f"🔍 Starting to poll execution: {execution_id}")
        print(f"⏱️ Timeout: {timeout_seconds}s, Poll Interval: {poll_interval}s")
        print()
        
        start_time = datetime.now()
        timeout_time = start_time + timedelta(seconds=timeout_seconds)
        poll_count = 0
        
        while datetime.now() < timeout_time:
            poll_count += 1
            
            if verbose or poll_count == 1:
                print(f"📡 Poll #{poll_count} - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            
            # Get current execution status
            execution = self.get_execution_status(execution_id)
            
            if not execution:
                print(f"❌ Could not retrieve execution status (poll #{poll_count})")
                if poll_count == 1:
                    # If we can't get status on first try, execution might not exist
                    return False, None
                else:
                    # On subsequent tries, continue polling
                    time.sleep(poll_interval)
                    continue
            
            status = execution.get('status', 'Unknown')
            is_complete, is_successful = self.is_execution_complete(status)
            
            if verbose or poll_count == 1:
                self.display_execution_details(execution, verbose)
                print()
            elif not is_complete:
                # Show brief progress indicator
                elapsed = int((datetime.now() - start_time).total_seconds())
                print(f"🟡 Still {status} after {elapsed}s... (poll #{poll_count})")
            
            if is_complete:
                print(f"🎯 Execution completed after {poll_count} poll(s)")
                if verbose:
                    print("Final execution details:")
                    self.display_execution_details(execution, verbose)
                return is_successful, execution
            
            # Wait before next poll
            time.sleep(poll_interval)
        
        # Timeout reached
        print(f"⏰ Timeout reached after {timeout_seconds}s ({poll_count} polls)")
        
        # Get final status
        final_execution = self.get_execution_status(execution_id)
        if final_execution:
            print("Final execution status:")
            self.display_execution_details(final_execution, verbose)
            return False, final_execution
        
        return False, None

    def run_examples(self) -> None:
        """Show example usage and test with known execution IDs"""
        print("🔍 ExecutionStatusPoller - Examples and Testing")
        print("=" * 50)
        
        # Try to find a recent execution to use as an example
        url = f"{self.base_url}/ExecutionRecord/query"
        
        query_payload = {
            "QuerySort": {
                "sortField": [{
                    "fieldName": "executionTime",
                    "sortOrder": "DESC"
                }]
            }
        }
        
        try:
            response = requests.post(url, json=query_payload, auth=self.auth, headers=self.headers, timeout=30)
            
            if response.status_code == 200:
                result = response.json()
                executions = result.get('result', [])
                
                if executions:
                    print(f"Found {len(executions)} recent execution(s)")
                    print("\nRecent executions available for polling:")
                    
                    for i, execution in enumerate(executions[:5]):
                        execution_id = execution.get('executionId', 'Unknown')
                        process_name = execution.get('processName', 'Unknown')
                        status = execution.get('status', 'Unknown')
                        execution_time = execution.get('executionTime', 'Unknown')
                        
                        print(f"  {i+1}. {execution_id}")
                        print(f"     Process: {process_name}")
                        print(f"     Status: {status}")
                        print(f"     Time: {execution_time}")
                        print()
                    
                    # Test with the most recent execution
                    latest_execution_id = executions[0].get('executionId')
                    if latest_execution_id:
                        print(f"Testing status polling with: {latest_execution_id}")
                        success, final_data = self.poll_execution(latest_execution_id, timeout_seconds=30, verbose=True)
                        
                        if success:
                            print("✅ Polling test successful - execution completed")
                        else:
                            print("⚠️ Polling test completed - execution may still be running or failed")
                else:
                    print("No recent executions found to test with")
            else:
                print(f"❌ Error querying recent executions: {response.status_code}")
                
        except Exception as e:
            print(f"❌ Error during examples: {str(e)}")


def main():
    parser = argparse.ArgumentParser(
        description="Poll execution status and wait for completion",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    # Basic polling
    python poll_execution_status.py execution-abc123-def456-2025.08.17
    
    # Custom timeout and interval
    python poll_execution_status.py execution-abc123-def456-2025.08.17 --timeout 600 --interval 10
    
    # JSON output for automation
    python poll_execution_status.py execution-abc123-def456-2025.08.17 --json
    
    # Show examples and test
    python poll_execution_status.py --examples
        """
    )
    
    parser.add_argument('execution_id', nargs='?', help='Execution ID to monitor')
    parser.add_argument('--timeout', type=int, default=300, help='Timeout in seconds (default: 300)')
    parser.add_argument('--interval', type=int, default=5, help='Poll interval in seconds (default: 5)')
    parser.add_argument('--json', action='store_true', help='Output JSON format')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    parser.add_argument('--examples', action='store_true', help='Show examples and test with recent executions')
    
    args = parser.parse_args()
    
    try:
        poller = ExecutionStatusPoller()
        
        if args.examples:
            poller.run_examples()
            return
        
        if not args.execution_id:
            parser.print_help()
            print("\n❌ Error: execution_id is required (use --examples to see available executions)")
            sys.exit(1)
        
        # Poll the specified execution
        success, final_data = poller.poll_execution(
            args.execution_id,
            timeout_seconds=args.timeout,
            poll_interval=args.interval,
            verbose=args.verbose
        )
        
        if args.json:
            # JSON output for automation
            result = {
                "execution_id": args.execution_id,
                "success": success,
                "completed": final_data is not None,
                "final_data": final_data
            }
            print(json.dumps(result, indent=2))
        else:
            # Human-readable summary
            print("\n" + "="*50)
            print("📊 POLLING SUMMARY")
            print("="*50)
            
            if final_data:
                status = final_data.get('status', 'Unknown')
                if success:
                    print("✅ Result: SUCCESSFUL - Execution completed successfully")
                else:
                    print(f"❌ Result: FAILED - Execution ended with status: {status}")
                
                # Show key metrics
                process_name = final_data.get('processName', 'Unknown')
                duration = poller.format_duration(final_data.get('executionDuration', 'Unknown'))
                
                print(f"📋 Process: {process_name}")
                print(f"⏱️ Duration: {duration}")
                print(f"🆔 Execution ID: {args.execution_id}")
            else:
                print("❌ Result: NO DATA - Could not retrieve final execution status")
        
        sys.exit(0 if success else 1)
        
    except KeyboardInterrupt:
        print("\n⛔ Polling interrupted by user")
        sys.exit(130)
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()