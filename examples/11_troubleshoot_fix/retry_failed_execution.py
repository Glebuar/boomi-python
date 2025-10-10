#!/usr/bin/env python3
"""
Boomi SDK Example: Retry Failed Execution
==========================================

This example demonstrates how to retry a failed execution with intelligent 
retry strategies and failure analysis.

Features:
- Retry execution with same or modified parameters
- Handle transient vs permanent failures
- Implement retry strategies (immediate, delayed, exponential backoff)
- Track retry attempts and success rates
- Analyze failure patterns for retry decision making
- Support for custom execution properties

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- EXECUTE privilege required
- Valid execution ID from a failed execution

Usage:
    # Retry failed execution with default settings
    python retry_failed_execution.py EXECUTION_ID
    
    # Retry with custom parameters
    python retry_failed_execution.py EXECUTION_ID --max-retries 5 --strategy exponential
    
    # Retry with custom execution properties
    python retry_failed_execution.py EXECUTION_ID --property "debugMode=true" --property "maxRetries=1"
    
    # Check failure analysis only (no retry)
    python retry_failed_execution.py EXECUTION_ID --analyze-only

Examples:
    python retry_failed_execution.py execution-12345-2024.01.01
    python retry_failed_execution.py execution-12345-2024.01.01 --max-retries 3 --strategy linear --delay 10
    python retry_failed_execution.py execution-12345-2024.01.01 --analyze-only --verbose
"""

import os
import sys
import argparse
import time
import json
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Any, Tuple
from enum import Enum

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# Load environment variables from .env file if available
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv is optional

from boomi import Boomi
from boomi.models import (
    ExecutionRecord,
    ExecutionRecordQueryConfig,
    ExecutionRecordQueryConfigQueryFilter,
    ExecutionRecordSimpleExpression,
    ExecutionRecordSimpleExpressionOperator,
    ExecutionRecordSimpleExpressionProperty,
    ExecutionRequest,
    ExecutionRequestDynamicProcessProperties,
    DynamicProcessProperty
)


def validate_environment() -> tuple[str, str, str]:
    """Validate required environment variables and return credentials"""
    account_id = os.getenv("BOOMI_ACCOUNT")
    username = os.getenv("BOOMI_USER") 
    password = os.getenv("BOOMI_SECRET")
    
    if not all([account_id, username, password]):
        print("❌ Error: Missing required environment variables")
        print("   Please set: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET")
        print("   You can also create a .env file with these variables")
        sys.exit(1)
    
    return account_id, username, password


class RetryStrategy(Enum):
    """Retry strategy options"""
    IMMEDIATE = "immediate"
    LINEAR = "linear"
    EXPONENTIAL = "exponential"


class FailureType(Enum):
    """Types of execution failures"""
    TRANSIENT = "transient"
    PERMANENT = "permanent"
    UNKNOWN = "unknown"


class ExecutionRetrier:
    """Manages intelligent retry of failed executions"""
    
    def __init__(self, verbose: bool = False):
        """Initialize the Boomi SDK client"""
        account_id, username, password = validate_environment()
        
        self.sdk = Boomi(
            account_id=account_id,
            username=username,
            password=password,
            timeout=30000
        )
        self.verbose = verbose
        print("✅ SDK initialized successfully")
    
    def get_execution_details(self, execution_id: str) -> Optional[Dict]:
        """Get details of the failed execution"""
        try:
            if self.verbose:
                print(f"\n🔍 Retrieving execution details for {execution_id}...")
            
            # Query for the specific execution
            query_expression = ExecutionRecordSimpleExpression(
                operator=ExecutionRecordSimpleExpressionOperator.EQUALS,
                property=ExecutionRecordSimpleExpressionProperty.EXECUTIONID,
                argument=[execution_id]
            )
            
            query_filter = ExecutionRecordQueryConfigQueryFilter(expression=query_expression)
            query_config = ExecutionRecordQueryConfig(query_filter=query_filter)
            
            result = self.sdk.execution_record.query_execution_record(request_body=query_config)
            
            if hasattr(result, 'result') and result.result:
                exec_record = result.result[0]
                
                execution_details = {
                    'execution_id': getattr(exec_record, 'execution_id', execution_id),
                    'process_id': getattr(exec_record, 'process_id', 'N/A'),
                    'process_name': getattr(exec_record, 'process_name', 'N/A'),
                    'atom_id': getattr(exec_record, 'atom_id', 'N/A'),
                    'atom_name': getattr(exec_record, 'atom_name', 'N/A'),
                    'status': getattr(exec_record, 'status', 'N/A'),
                    'execution_time': getattr(exec_record, 'execution_time', 'N/A'),
                    'execution_duration': getattr(exec_record, 'execution_duration', 0),
                    'error_type': getattr(exec_record, 'error_type', 'N/A'),
                    'error': getattr(exec_record, 'error', 'N/A'),
                    'inbound_document_count': getattr(exec_record, 'inbound_document_count', 0),
                    'outbound_document_count': getattr(exec_record, 'outbound_document_count', 0)
                }
                
                print(f"✅ Found execution record")
                if self.verbose:
                    print(f"   📄 Process: {execution_details['process_name']}")
                    print(f"   🔧 Atom: {execution_details['atom_name']}")
                    print(f"   📅 Time: {execution_details['execution_time']}")
                    print(f"   📊 Status: {execution_details['status']}")
                    print(f"   ⏱️ Duration: {execution_details['execution_duration']}ms")
                
                return execution_details
            else:
                print(f"❌ Execution record {execution_id} not found")
                return None
                
        except Exception as e:
            print(f"❌ Error retrieving execution details: {e}")
            return None
    
    def analyze_failure(self, execution_details: Dict) -> Tuple[FailureType, str]:
        """Analyze the failure to determine if it's worth retrying"""
        if not execution_details:
            return FailureType.UNKNOWN, "No execution details available"
        
        error_message = str(execution_details.get('error', '')).lower()
        error_type = str(execution_details.get('error_type', '')).lower()
        status = str(execution_details.get('status', '')).upper()
        
        print(f"\n🔬 Analyzing failure type...")
        
        # Transient error patterns (worth retrying)
        transient_patterns = [
            'timeout', 'connection', 'network', 'temporary', 'throttle',
            'rate limit', 'service unavailable', '503', '502', '504',
            'retry', 'temporary failure', 'connection reset'
        ]
        
        # Permanent error patterns (not worth retrying)
        permanent_patterns = [
            'authentication', 'unauthorized', '401', '403', 'permission',
            'invalid', 'malformed', 'syntax error', 'not found', '404',
            'bad request', '400', 'validation', 'schema', 'format'
        ]
        
        # Check for transient patterns
        for pattern in transient_patterns:
            if pattern in error_message or pattern in error_type:
                reason = f"Detected transient error pattern: '{pattern}'"
                print(f"   ✅ {reason}")
                return FailureType.TRANSIENT, reason
        
        # Check for permanent patterns
        for pattern in permanent_patterns:
            if pattern in error_message or pattern in error_type:
                reason = f"Detected permanent error pattern: '{pattern}'"
                print(f"   ❌ {reason}")
                return FailureType.PERMANENT, reason
        
        # If no clear pattern, default based on status
        if status in ['ERROR', 'ABORTED']:
            reason = f"General failure (status: {status}) - may be worth retrying"
            print(f"   ⚠️ {reason}")
            return FailureType.UNKNOWN, reason
        
        return FailureType.UNKNOWN, "Unable to categorize failure type"
    
    def calculate_delay(self, attempt: int, strategy: RetryStrategy, base_delay: int) -> int:
        """Calculate delay before next retry attempt"""
        if strategy == RetryStrategy.IMMEDIATE:
            return 0
        elif strategy == RetryStrategy.LINEAR:
            return base_delay * attempt
        elif strategy == RetryStrategy.EXPONENTIAL:
            return min(base_delay * (2 ** (attempt - 1)), 300)  # Cap at 5 minutes
        return base_delay
    
    def retry_execution(self, execution_details: Dict, 
                       max_retries: int = 3,
                       strategy: RetryStrategy = RetryStrategy.LINEAR,
                       base_delay: int = 10,
                       custom_properties: List[str] = None) -> bool:
        """Retry the failed execution with specified strategy"""
        
        process_id = execution_details.get('process_id')
        atom_id = execution_details.get('atom_id')
        
        if not process_id or not atom_id:
            print("❌ Cannot retry - missing process ID or atom ID")
            return False
        
        print(f"\n🚀 Starting retry sequence...")
        print(f"   📄 Process: {execution_details.get('process_name', 'N/A')}")
        print(f"   🔧 Atom: {execution_details.get('atom_name', 'N/A')}")
        print(f"   📊 Max Retries: {max_retries}")
        print(f"   ⚡ Strategy: {strategy.value}")
        print(f"   ⏱️ Base Delay: {base_delay}s")
        
        for attempt in range(1, max_retries + 1):
            try:
                print(f"\n🔄 Retry Attempt {attempt}/{max_retries}")
                
                # Calculate delay for this attempt
                if attempt > 1:
                    delay = self.calculate_delay(attempt - 1, strategy, base_delay)
                    if delay > 0:
                        print(f"   ⏳ Waiting {delay}s before retry...")
                        time.sleep(delay)
                
                # Prepare dynamic process properties
                dynamic_properties_dict = {}
                
                # Add custom properties from user
                if custom_properties:
                    for prop_str in custom_properties:
                        if '=' in prop_str:
                            key, value = prop_str.split('=', 1)
                            dynamic_properties_dict[key.strip()] = value.strip()
                
                # Add retry tracking properties
                dynamic_properties_dict["retryAttempt"] = str(attempt)
                dynamic_properties_dict["originalExecutionId"] = execution_details['execution_id']
                dynamic_properties_dict["retryTimestamp"] = datetime.now().isoformat()
                
                # Create dynamic properties object
                dynamic_props = None
                if dynamic_properties_dict:
                    dynamic_property_list = [
                        DynamicProcessProperty(name=key, value=value)
                        for key, value in dynamic_properties_dict.items()
                    ]
                    dynamic_props = ExecutionRequestDynamicProcessProperties(
                        dynamic_process_property=dynamic_property_list
                    )
                
                # Create execution request
                execution_request = ExecutionRequest(
                    process_id=process_id,
                    atom_id=atom_id,
                    dynamic_process_properties=dynamic_props
                )
                
                # Execute the retry
                print(f"   🎯 Submitting retry request...")
                result = self.sdk.execution_request.create_execution_request(request_body=execution_request)
                
                if result:
                    request_id = getattr(result, 'request_id', 'N/A')
                    print(f"   ✅ Retry submitted successfully!")
                    print(f"   📋 Request ID: {request_id}")
                    
                    # Wait a moment and check initial status
                    print(f"   ⏱️ Checking initial status...")
                    time.sleep(3)
                    
                    # Try to get the new execution ID from request ID
                    new_execution_id = request_id.replace('executionrecord-', 'execution-') if 'executionrecord-' in request_id else request_id
                    
                    # Check if it started successfully
                    retry_details = self.get_execution_details(new_execution_id)
                    if retry_details:
                        status = retry_details.get('status', 'UNKNOWN')
                        print(f"   📊 Retry Status: {status}")
                        
                        if status in ['COMPLETE', 'INPROCESS']:
                            print(f"\n✅ Retry attempt {attempt} appears successful!")
                            if status == 'COMPLETE':
                                print(f"   🎉 Execution completed successfully")
                                return True
                            else:
                                print(f"   🔄 Execution is running - monitor for completion")
                                return True
                        elif status == 'ERROR':
                            print(f"   ❌ Retry attempt {attempt} failed")
                            if attempt == max_retries:
                                print(f"   💔 All retry attempts exhausted")
                                return False
                            else:
                                print(f"   🔄 Will try again...")
                                continue
                    else:
                        print(f"   ⚠️ Could not verify retry status")
                        
                else:
                    print(f"   ❌ Failed to submit retry request")
                    if attempt == max_retries:
                        return False
                    
            except Exception as e:
                print(f"   ❌ Retry attempt {attempt} failed: {e}")
                if attempt == max_retries:
                    print(f"   💔 All retry attempts exhausted")
                    return False
        
        return False
    
    def analyze_only(self, execution_id: str) -> bool:
        """Analyze failure without retrying"""
        print(f"\n🔬 Failure Analysis Mode")
        print("=" * 60)
        
        execution_details = self.get_execution_details(execution_id)
        if not execution_details:
            return False
        
        # Display detailed execution info
        print(f"\n📋 EXECUTION DETAILS:")
        print(f"   🆔 Execution ID: {execution_details['execution_id']}")
        print(f"   📄 Process: {execution_details['process_name']} ({execution_details['process_id']})")
        print(f"   🔧 Atom: {execution_details['atom_name']} ({execution_details['atom_id']})")
        print(f"   📅 Execution Time: {execution_details['execution_time']}")
        print(f"   ⏱️ Duration: {execution_details['execution_duration']}ms")
        print(f"   📊 Status: {execution_details['status']}")
        print(f"   📨 Documents In: {execution_details['inbound_document_count']}")
        print(f"   📤 Documents Out: {execution_details['outbound_document_count']}")
        
        # Show error details
        if execution_details['error'] != 'N/A':
            print(f"\n❌ ERROR DETAILS:")
            print(f"   🏷️ Error Type: {execution_details['error_type']}")
            print(f"   📝 Error Message: {execution_details['error']}")
        
        # Analyze failure type
        failure_type, reason = self.analyze_failure(execution_details)
        
        print(f"\n🎯 RETRY RECOMMENDATION:")
        if failure_type == FailureType.TRANSIENT:
            print(f"   ✅ RECOMMENDED: This appears to be a transient failure")
            print(f"   💡 Suggestion: Retry with linear or exponential backoff")
            print(f"   🔄 Command: python {sys.argv[0]} {execution_id} --strategy exponential --max-retries 3")
        elif failure_type == FailureType.PERMANENT:
            print(f"   ❌ NOT RECOMMENDED: This appears to be a permanent failure")
            print(f"   💡 Suggestion: Fix the underlying issue before retrying")
            print(f"   🛠️ Recommended: Review error details and fix configuration/data")
        else:
            print(f"   ⚠️ UNCERTAIN: Failure type unclear - manual review recommended")
            print(f"   💡 Suggestion: Review error details and retry with caution")
            print(f"   🔄 Command: python {sys.argv[0]} {execution_id} --max-retries 1")
        
        print(f"\n   📋 Analysis Reason: {reason}")
        
        return True


def main():
    """Main execution function"""
    parser = argparse.ArgumentParser(
        description="Retry failed Boomi execution with intelligent strategies",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python retry_failed_execution.py execution-12345-2024.01.01
  python retry_failed_execution.py execution-12345-2024.01.01 --max-retries 5 --strategy exponential
  python retry_failed_execution.py execution-12345-2024.01.01 --property "debugMode=true" --property "retryCount=1"
  python retry_failed_execution.py execution-12345-2024.01.01 --analyze-only --verbose

Retry Strategies:
  immediate    - No delay between retries
  linear       - Delay increases linearly (delay * attempt)
  exponential  - Delay doubles each attempt (capped at 5 minutes)
        """
    )
    
    parser.add_argument("execution_id", help="Failed execution ID to retry")
    parser.add_argument("--max-retries", type=int, default=3,
                       help="Maximum number of retry attempts (default: 3)")
    parser.add_argument("--strategy", choices=["immediate", "linear", "exponential"], 
                       default="linear", help="Retry strategy (default: linear)")
    parser.add_argument("--delay", type=int, default=10,
                       help="Base delay in seconds between retries (default: 10)")
    parser.add_argument("--property", action="append", dest="properties",
                       help="Custom execution property (format: key=value)")
    parser.add_argument("--analyze-only", action="store_true",
                       help="Analyze failure without retrying")
    parser.add_argument("--verbose", action="store_true",
                       help="Enable verbose output")
    
    args = parser.parse_args()
    
    print("🚀 Boomi SDK Example: Retry Failed Execution")
    print("=" * 60)
    
    try:
        retrier = ExecutionRetrier(verbose=args.verbose)
        
        # Convert strategy string to enum
        strategy_map = {
            'immediate': RetryStrategy.IMMEDIATE,
            'linear': RetryStrategy.LINEAR,
            'exponential': RetryStrategy.EXPONENTIAL
        }
        retry_strategy = strategy_map[args.strategy]
        
        if args.analyze_only:
            # Just analyze the failure
            success = retrier.analyze_only(args.execution_id)
        else:
            # Get execution details first
            execution_details = retrier.get_execution_details(args.execution_id)
            if not execution_details:
                print("\n❌ Cannot proceed - execution not found")
                sys.exit(1)
            
            # Check if it's actually failed
            status = execution_details.get('status', '').upper()
            if status not in ['ERROR', 'ABORTED']:
                print(f"\n⚠️ Warning: Execution status is '{status}', not ERROR or ABORTED")
                print(f"   This may not be a failed execution requiring retry")
                
                user_input = input("\n   Continue with retry anyway? [y/N]: ").strip().lower()
                if user_input not in ['y', 'yes']:
                    print("   Operation cancelled")
                    sys.exit(0)
            
            # Analyze failure first
            failure_type, reason = retrier.analyze_failure(execution_details)
            
            if failure_type == FailureType.PERMANENT:
                print(f"\n⚠️ Warning: This appears to be a permanent failure")
                print(f"   Reason: {reason}")
                print(f"   Retrying may not be successful")
                
                user_input = input("\n   Continue with retry anyway? [y/N]: ").strip().lower()
                if user_input not in ['y', 'yes']:
                    print("   Retry cancelled - consider fixing the underlying issue first")
                    sys.exit(0)
            
            # Proceed with retry
            success = retrier.retry_execution(
                execution_details=execution_details,
                max_retries=args.max_retries,
                strategy=retry_strategy,
                base_delay=args.delay,
                custom_properties=args.properties
            )
        
        if success:
            print(f"\n✅ Operation completed successfully!")
        else:
            print(f"\n❌ Operation failed")
            sys.exit(1)
            
    except KeyboardInterrupt:
        print(f"\n\n⚠️ Operation interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error during retry operation: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()