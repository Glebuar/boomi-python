#!/usr/bin/env python3
"""
Boomi SDK Example: Query Execution Records
==========================================

This example demonstrates how to query execution records using the Boomi SDK.

Features:
- Query recent execution records
- Filter by execution time
- Display execution status and details
- Handle both object and dictionary response formats

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- RUNTIME MANAGEMENT privilege recommended for complete data access

Usage:
    python execution_records.py

Examples:
    python execution_records.py
"""

import os
import sys
import argparse
from typing import Optional
from datetime import datetime, timedelta

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# Load environment variables from .env file if available
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv is optional

from src.boomi import Boomi
from src.boomi.models import (
    ExecutionRecordQueryConfig,
    ExecutionRecordQueryConfigQueryFilter,
    ExecutionRecordSimpleExpression,
    ExecutionRecordSimpleExpressionOperator,
    ExecutionRecordSimpleExpressionProperty
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


def main():
    """Main execution function"""
    # Parse command-line arguments
    parser = argparse.ArgumentParser(
        description='Query Boomi execution records',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  %(prog)s                              # Query all recent executions
  %(prog)s --status ERROR               # Query only failed executions
  %(prog)s --status COMPLETE            # Query only successful executions
  %(prog)s --days 7                     # Query executions from last 7 days
  %(prog)s --process-id "abc123"        # Query executions for specific process
  %(prog)s --atom-id "def456"           # Query executions on specific atom
  %(prog)s --limit 20                   # Show up to 20 records
        '''
    )

    parser.add_argument('--status', choices=['COMPLETE', 'ERROR', 'ABORTED', 'INPROCESS'],
                       help='Filter by execution status')
    parser.add_argument('--days', type=int, default=1,
                       help='Number of days to look back (default: 1)')
    parser.add_argument('--process-id', metavar='ID',
                       help='Filter by specific process ID')
    parser.add_argument('--atom-id', metavar='ID',
                       help='Filter by specific atom/runtime ID')
    parser.add_argument('--limit', type=int, default=10, metavar='N',
                       help='Maximum number of records to display (default: 10)')

    args = parser.parse_args()

    print("🚀 Boomi SDK Example: Query Execution Records")
    print("=" * 50)

    # Validate environment variables
    account_id, username, password = validate_environment()
    
    # Initialize SDK
    try:
        sdk = Boomi(
            account_id=account_id,
            username=username,
            password=password,
            timeout=30000
        )
        print("✅ SDK initialized successfully")
        print(f"🏢 Account: {account_id}")
        print(f"👤 User: {username}")
    except Exception as e:
        print(f"❌ Failed to initialize SDK: {e}")
        sys.exit(1)
    
    try:
        # Query recent execution records
        filter_desc = []
        if args.status:
            filter_desc.append(f"status={args.status}")
        if args.process_id:
            filter_desc.append(f"process={args.process_id}")
        if args.atom_id:
            filter_desc.append(f"atom={args.atom_id}")
        filter_desc.append(f"last {args.days} day(s)")

        print(f"\n🔍 Querying execution records ({', '.join(filter_desc)})...")

        # Build query based on arguments
        if args.status:
            simple_expression = ExecutionRecordSimpleExpression(
                operator=ExecutionRecordSimpleExpressionOperator.EQUALS,
                property=ExecutionRecordSimpleExpressionProperty.STATUS,
                argument=[args.status]
            )
        elif args.process_id:
            simple_expression = ExecutionRecordSimpleExpression(
                operator=ExecutionRecordSimpleExpressionOperator.EQUALS,
                property=ExecutionRecordSimpleExpressionProperty.PROCESSID,
                argument=[args.process_id]
            )
        elif args.atom_id:
            simple_expression = ExecutionRecordSimpleExpression(
                operator=ExecutionRecordSimpleExpressionOperator.EQUALS,
                property=ExecutionRecordSimpleExpressionProperty.ATOMID,
                argument=[args.atom_id]
            )
        else:
            # Default: Get executions from the specified time period
            start_date = datetime.now() - timedelta(days=args.days)
            simple_expression = ExecutionRecordSimpleExpression(
                operator=ExecutionRecordSimpleExpressionOperator.GREATERTHAN,
                property=ExecutionRecordSimpleExpressionProperty.EXECUTIONTIME,
                argument=[start_date.strftime("%Y-%m-%dT00:00:00Z")]
            )
        
        query_filter = ExecutionRecordQueryConfigQueryFilter(expression=simple_expression)
        query_config = ExecutionRecordQueryConfig(query_filter=query_filter)
        
        # Query execution records
        result = sdk.execution_record.query_execution_record(request_body=query_config)
        
        # Process results
        records = []
        if hasattr(result, 'result') and result.result:
            records = result.result if isinstance(result.result, list) else [result.result]
        
        if records:
            print(f"✅ Found {len(records)} execution record(s):")
            print("-" * 60)
            
            for i, record in enumerate(records[:10], 1):  # Limit to first 10
                # Handle both dict and object formats
                if hasattr(record, '__dict__'):
                    exec_id = getattr(record, 'execution_id', 'N/A')
                    exec_time = getattr(record, 'execution_time', 'N/A')
                    status = getattr(record, 'status', 'N/A')
                    process_name = getattr(record, 'process_name', 'N/A')
                    atom_name = getattr(record, 'atom_name', 'N/A')
                else:
                    exec_id = record.get('executionId', 'N/A')
                    exec_time = record.get('executionTime', 'N/A')
                    status = record.get('status', 'N/A')
                    process_name = record.get('processName', 'N/A')
                    atom_name = record.get('atomName', 'N/A')
                
                # Format execution time
                if exec_time != 'N/A' and 'T' in str(exec_time):
                    exec_time = str(exec_time).replace('T', ' ').split('.')[0]
                
                print(f"{i:2}. Execution ID: {exec_id}")
                print(f"    Process: {process_name}")
                print(f"    Runtime: {atom_name}")
                print(f"    Time: {exec_time}")
                print(f"    Status: {status}")
                print()
                
            if len(records) > 10:
                print(f"... and {len(records) - 10} more records")
        else:
            print("❌ No execution records found")
            print("   This might indicate no recent executions or insufficient permissions")
            
        print("✅ Query execution records completed successfully!")
            
    except Exception as e:
        print(f"❌ Error during query execution records: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()