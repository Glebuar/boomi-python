#!/usr/bin/env python3
"""
Query Execution Records

This example demonstrates how to query execution records using the Boomi SDK.

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET

Usage:
    python query_execution_records.py

Endpoint:
- execution_record.query_execution_record
"""

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

from boomi import Boomi
from boomi.models import (
    ExecutionRecordQueryConfig,
    ExecutionRecordQueryConfigQueryFilter,
    ExecutionRecordSimpleExpression,
    ExecutionRecordSimpleExpressionOperator,
    ExecutionRecordSimpleExpressionProperty
)

def main():
    # Initialize SDK
    sdk = Boomi(
        account_id=os.getenv("BOOMI_ACCOUNT"),
        username=os.getenv("BOOMI_USER"),
        password=os.getenv("BOOMI_SECRET"),
        timeout=30000,
    )
    
    print("🔍 Querying execution records...")
    
    try:
        # Create query to get recent execution records
        simple_expression = ExecutionRecordSimpleExpression(
            operator=ExecutionRecordSimpleExpressionOperator.GREATER_THAN,
            property=ExecutionRecordSimpleExpressionProperty.EXECUTION_TIME,
            argument=["2024-01-01T00:00:00Z"]  # Records since 2024
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
            for i, record in enumerate(records, 1):
                # Handle both dict and object formats
                if hasattr(record, '__dict__'):
                    exec_id = getattr(record, 'execution_id', 'N/A')
                    exec_time = getattr(record, 'execution_time', 'N/A')
                    status = getattr(record, 'status', 'N/A')
                else:
                    exec_id = record.get('executionId', 'N/A')
                    exec_time = record.get('executionTime', 'N/A')
                    status = record.get('status', 'N/A')
                
                print(f"{i:2}. Execution ID: {exec_id}")
                print(f"    Time: {exec_time}")
                print(f"    Status: {status}")
        else:
            print("❌ No execution records found")
            
    except Exception as e:
        print(f"❌ Error querying execution records: {str(e)}")

if __name__ == "__main__":
    main()