#!/usr/bin/env python3
"""
Connector Document Management Tool

This example demonstrates how to work with Boomi connector documents:
- Query connector records from a specific execution
- Request download URLs for connector documents

Note: The Boomi API does not support uploading documents via the SDK.
Connector documents are created through processes or connector operations.
This tool focuses on querying and downloading existing documents.

GenericConnectorRecord queries REQUIRE an execution ID - you cannot list
all connector records across all executions. You must specify which execution's
connector records you want to query.
"""

import os
import sys
import argparse
from typing import List, Dict, Any, Optional
from datetime import datetime, timedelta

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from boomi import Boomi
from boomi.models import (
    ConnectorDocument,
    GenericConnectorRecordQueryConfig,
    GenericConnectorRecordQueryConfigQueryFilter,
    GenericConnectorRecordSimpleExpression,
    GenericConnectorRecordSimpleExpressionOperator,
    GenericConnectorRecordSimpleExpressionProperty,
    ExecutionRecordQueryConfig,
    ExecutionRecordQueryConfigQueryFilter,
    ExecutionRecordSimpleExpression,
    ExecutionRecordSimpleExpressionOperator,
    ExecutionRecordSimpleExpressionProperty
)


class ConnectorDocumentManager:
    """Manages connector document queries and downloads"""

    def __init__(self, verbose: bool = False):
        """Initialize the manager"""
        self.verbose = verbose

        # Initialize SDK
        self.sdk = Boomi(
            account_id=os.environ.get('BOOMI_ACCOUNT'),
            username=os.environ.get('BOOMI_USER'),
            password=os.environ.get('BOOMI_SECRET'),
            timeout=30000
        )

        if self.verbose:
            print("✅ Connector Document Manager initialized")

    def get_recent_executions(self, days: int = 7, limit: int = 10) -> List[Dict[str, Any]]:
        """
        Get recent executions to help find execution IDs

        Args:
            days: Number of days to look back
            limit: Maximum number of executions

        Returns:
            List of execution records
        """
        try:
            if self.verbose:
                print(f"\n📋 Finding executions from last {days} days...")

            # Query recent executions
            end_time = datetime.now()
            start_time = end_time - timedelta(days=days)

            query_expression = ExecutionRecordSimpleExpression(
                operator=ExecutionRecordSimpleExpressionOperator.GREATERTHAN,
                property=ExecutionRecordSimpleExpressionProperty.EXECUTIONTIME,
                argument=[start_time.strftime('%Y-%m-%dT%H:%M:%SZ')]
            )

            query_filter = ExecutionRecordQueryConfigQueryFilter(expression=query_expression)
            query_config = ExecutionRecordQueryConfig(query_filter=query_filter)

            result = self.sdk.execution_record.query_execution_record(
                request_body=query_config
            )

            executions = []
            if result and hasattr(result, 'result') and result.result:
                for execution in result.result[:limit]:
                    exec_info = {
                        'id': getattr(execution, 'execution_id', 'N/A'),
                        'process': getattr(execution, 'process_name', 'N/A'),
                        'status': getattr(execution, 'status', 'N/A'),
                        'time': getattr(execution, 'execution_time', 'N/A'),
                        'atom': getattr(execution, 'atom_id', 'N/A')
                    }
                    executions.append(exec_info)

            print(f"✅ Found {len(executions)} execution(s)")
            return executions

        except Exception as e:
            print(f"❌ Error finding executions: {e}")
            if hasattr(e, 'error_detail'):
                print(f"   Detail: {e.error_detail}")
            return []

    def list_connector_records(self, execution_id: str, limit: int = 10) -> List[Dict[str, Any]]:
        """
        List connector records for a specific execution

        Args:
            execution_id: The execution ID to query
            limit: Maximum number of records

        Returns:
            List of connector records
        """
        try:
            if self.verbose:
                print(f"\n📋 Listing connector records for execution: {execution_id}")

            # Build query for execution ID
            query_expression = GenericConnectorRecordSimpleExpression(
                operator=GenericConnectorRecordSimpleExpressionOperator.EQUALS,
                property=GenericConnectorRecordSimpleExpressionProperty.EXECUTIONID,
                argument=[execution_id]
            )

            query_filter = GenericConnectorRecordQueryConfigQueryFilter(
                expression=query_expression
            )
            query_config = GenericConnectorRecordQueryConfig(
                query_filter=query_filter
            )

            result = self.sdk.generic_connector_record.query_generic_connector_record(
                request_body=query_config
            )

            records = []
            if result and hasattr(result, 'result') and result.result:
                for record in result.result[:limit]:
                    record_info = {
                        'id': getattr(record, 'id_', 'N/A'),
                        'connection': getattr(record, 'connection_name', 'N/A'),
                        'operation': getattr(record, 'operation_name', 'N/A'),
                        'status': getattr(record, 'status', 'N/A'),
                        'type': getattr(record, 'connector_type', 'N/A'),
                        'date': getattr(record, 'date_processed', 'N/A'),
                        'size': getattr(record, 'size', 0)
                    }
                    records.append(record_info)

            print(f"✅ Found {len(records)} connector record(s)")

            return records

        except Exception as e:
            print(f"❌ Error listing connector records: {e}")
            if hasattr(e, 'error_detail'):
                print(f"   Detail: {e.error_detail}")
            return []

    def request_download_url(self, connector_record_id: str) -> Optional[str]:
        """
        Request a download URL for a connector document

        Args:
            connector_record_id: Generic Connector Record ID

        Returns:
            Download URL if successful
        """
        try:
            if self.verbose:
                print(f"\n📥 Requesting download URL for: {connector_record_id}")

            # Create connector document request
            document = ConnectorDocument(
                generic_connector_record_id=connector_record_id
            )

            # Request download URL
            result = self.sdk.connector_document.create_connector_document(
                request_body=document
            )

            if result and hasattr(result, 'url'):
                print(f"✅ Download URL obtained")
                print(f"   URL: {result.url}")

                if hasattr(result, 'message'):
                    print(f"   Message: {result.message}")

                return result.url
            else:
                print(f"❌ Failed to get download URL")
                return None

        except Exception as e:
            print(f"❌ Error requesting download: {e}")
            if hasattr(e, 'error_detail'):
                print(f"   Detail: {e.error_detail}")
            return None


def main():
    """Main function"""
    parser = argparse.ArgumentParser(
        description='Manage Boomi connector documents',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Find recent executions
  %(prog)s --find-executions

  # List connector records for an execution
  %(prog)s --list-records EXECUTION_ID

  # List with more results
  %(prog)s --list-records EXECUTION_ID --limit 50

  # Request download URL for a connector record
  %(prog)s --download CONNECTOR_RECORD_ID

  # Verbose output
  %(prog)s --list-records EXECUTION_ID --verbose

Environment Variables Required:
  BOOMI_ACCOUNT - Boomi account ID
  BOOMI_USER - Boomi username
  BOOMI_SECRET - Boomi password/token

Note: Connector documents cannot be uploaded via the API.
      They are created through processes or connector operations.
      This tool helps query and download existing documents.

      GenericConnectorRecord queries require an execution ID.
      Use --find-executions to find execution IDs first.
"""
    )

    # Operations
    parser.add_argument('--find-executions', action='store_true',
                       help='Find recent executions')
    parser.add_argument('--list-records', metavar='EXECUTION_ID',
                       help='List connector records for execution')
    parser.add_argument('--download', metavar='RECORD_ID',
                       help='Request download URL for connector record')

    # Options
    parser.add_argument('--days', type=int, default=7,
                       help='Days to look back for executions (default: 7)')
    parser.add_argument('--limit', type=int, default=10,
                       help='Limit results (default: 10)')
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='Enable verbose output')

    args = parser.parse_args()

    # Check for at least one operation
    if not any([args.find_executions, args.list_records, args.download]):
        parser.print_help()
        return

    # Initialize manager
    manager = ConnectorDocumentManager(verbose=args.verbose)

    # Execute operations
    if args.find_executions:
        executions = manager.get_recent_executions(days=args.days, limit=args.limit)

        if executions:
            print("\n📋 Recent Executions:")
            for i, execution in enumerate(executions, 1):
                print(f"\n{i}. {execution['process']}")
                print(f"   ID: {execution['id']}")
                print(f"   Status: {execution['status']}")
                print(f"   Time: {execution['time']}")
                print(f"   Atom: {execution['atom']}")

    elif args.list_records:
        records = manager.list_connector_records(
            execution_id=args.list_records,
            limit=args.limit
        )

        if records:
            print("\n📋 Connector Records:")
            for i, record in enumerate(records, 1):
                print(f"\n{i}. {record['connection']} / {record['operation']}")
                print(f"   ID: {record['id']}")
                print(f"   Type: {record['type']}")
                print(f"   Status: {record['status']}")
                print(f"   Date: {record['date']}")
                print(f"   Size: {record['size']} KB")

    elif args.download:
        url = manager.request_download_url(connector_record_id=args.download)

        if url:
            print(f"\n✅ Use the URL above to download the document")
            print(f"   Note: Authentication required for download")


if __name__ == '__main__':
    main()
