#!/usr/bin/env python3
"""
Connector Document Management Tool

This example demonstrates how to manage connector documents including:
- Uploading documents to connectors
- Downloading documents from connectors
- Managing document metadata
- Batch document operations
- Document synchronization
"""

import os
import sys
import json
import argparse
import base64
import hashlib
from typing import Dict, List, Optional, Any, Tuple
from datetime import datetime, timedelta
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from boomi import Boomi
from boomi.models import (
    ConnectorDocument,
    ConnectorDocumentDownload,
    GenericConnectorRecordQueryConfig,
    GenericConnectorRecordSimpleExpression,
    GenericConnectorRecordSimpleExpressionOperator,
    GenericConnectorRecordSimpleExpressionProperty,
    ConnectorRecordContentBase64
)


class ConnectorDocumentManager:
    """Manages connector documents and content"""
    
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
    
    def upload_document(self, connector_id: str, file_path: str, 
                       document_name: Optional[str] = None,
                       content_type: str = "application/octet-stream") -> Optional[str]:
        """
        Upload a document to a connector
        
        Args:
            connector_id: Generic Connector Record ID
            file_path: Path to file to upload
            document_name: Optional document name (defaults to filename)
            content_type: MIME content type
            
        Returns:
            Document ID if successful
        """
        try:
            # Read file content
            file_path_obj = Path(file_path)
            if not file_path_obj.exists():
                print(f"❌ File not found: {file_path}")
                return None
            
            with open(file_path, 'rb') as f:
                content = f.read()
            
            # Encode content as base64
            encoded_content = base64.b64encode(content).decode('utf-8')
            
            # Use filename if document name not provided
            if not document_name:
                document_name = file_path_obj.name
            
            # Calculate content hash for verification
            content_hash = hashlib.sha256(content).hexdigest()
            
            if self.verbose:
                print(f"\n📤 Uploading document: {document_name}")
                print(f"   File: {file_path}")
                print(f"   Size: {len(content):,} bytes")
                print(f"   Hash: {content_hash[:16]}...")
                print(f"   Type: {content_type}")
            
            # Create connector document
            document = ConnectorDocument(
                connector_record_content_base64=ConnectorRecordContentBase64(
                    content=encoded_content
                )
            )
            
            # Upload document
            result = self.sdk.connector_document.create_connector_document(
                id_=connector_id,
                request_body=document
            )
            
            if result and hasattr(result, 'url'):
                print(f"✅ Document uploaded successfully")
                print(f"   Download URL: {result.url}")
                
                # Extract document ID from URL if present
                if '/download/' in result.url:
                    doc_id = result.url.split('/download/')[-1]
                    print(f"   Document ID: {doc_id}")
                    return doc_id
                
                return result.url
            else:
                print(f"❌ Upload failed - no URL returned")
                return None
                
        except Exception as e:
            print(f"❌ Error uploading document: {e}")
            if self.verbose:
                import traceback
                traceback.print_exc()
            return None
    
    def download_document(self, connector_id: str, output_path: Optional[str] = None) -> bool:
        """
        Download a document from a connector
        
        Args:
            connector_id: Generic Connector Record ID or download URL
            output_path: Optional output file path
            
        Returns:
            True if successful
        """
        try:
            if self.verbose:
                print(f"\n📥 Downloading document from connector: {connector_id}")
            
            # Get download info
            result = self.sdk.connector_document.get_connector_document(id_=connector_id)
            
            if not result or not hasattr(result, 'url'):
                print(f"❌ No download URL available")
                return False
            
            print(f"✅ Download URL obtained: {result.url}")
            
            if hasattr(result, 'message'):
                print(f"   Message: {result.message}")
            
            if hasattr(result, 'status_code'):
                print(f"   Status: {result.status_code}")
            
            # Note: Actual file download would require additional HTTP request
            # to the URL provided. This example shows how to get the download URL.
            
            if output_path:
                print(f"ℹ️ To download the file, use the URL above with appropriate authentication")
                print(f"   Suggested output: {output_path}")
            
            return True
            
        except Exception as e:
            print(f"❌ Error downloading document: {e}")
            if self.verbose:
                import traceback
                traceback.print_exc()
            return False
    
    def list_connector_records(self, connector_type: Optional[str] = None,
                              limit: int = 10) -> List[Dict[str, Any]]:
        """
        List generic connector records
        
        Args:
            connector_type: Optional filter by connector type
            limit: Maximum number of records
            
        Returns:
            List of connector records
        """
        try:
            if self.verbose:
                print(f"\n📋 Listing connector records...")
                if connector_type:
                    print(f"   Type filter: {connector_type}")
            
            # Build query
            if connector_type:
                query_expression = GenericConnectorRecordSimpleExpression(
                    operator=GenericConnectorRecordSimpleExpressionOperator.EQUALS,
                    property=GenericConnectorRecordSimpleExpressionProperty.CONNECTORTYPE,
                    argument=[connector_type]
                )
                query_config = GenericConnectorRecordQueryConfig(
                    query_filter={'expression': query_expression}
                )
            else:
                query_config = GenericConnectorRecordQueryConfig()
            
            # Query records
            result = self.sdk.generic_connector_record.query_generic_connector_record(
                request_body=query_config
            )
            
            records = []
            if result and hasattr(result, 'result') and result.result:
                for record in result.result[:limit]:
                    record_info = {
                        'id': getattr(record, 'id_', 'N/A'),
                        'name': getattr(record, 'name', 'N/A'),
                        'type': getattr(record, 'connector_type', 'N/A'),
                        'created': getattr(record, 'created_date', 'N/A'),
                        'modified': getattr(record, 'modified_date', 'N/A')
                    }
                    records.append(record_info)
            
            print(f"✅ Found {len(records)} connector record(s)")
            
            return records
            
        except Exception as e:
            print(f"❌ Error listing connector records: {e}")
            if self.verbose:
                import traceback
                traceback.print_exc()
            return []
    
    def sync_documents(self, source_dir: str, connector_id: str,
                      extensions: Optional[List[str]] = None) -> Dict[str, Any]:
        """
        Sync documents from a directory to a connector
        
        Args:
            source_dir: Source directory path
            connector_id: Target connector ID
            extensions: Optional file extensions to sync
            
        Returns:
            Sync results
        """
        try:
            source_path = Path(source_dir)
            if not source_path.exists() or not source_path.is_dir():
                print(f"❌ Invalid source directory: {source_dir}")
                return {'success': False, 'error': 'Invalid directory'}
            
            print(f"\n🔄 Syncing documents from {source_dir}")
            print(f"   Target connector: {connector_id}")
            
            # Find files to sync
            if extensions:
                patterns = [f"*.{ext}" for ext in extensions]
                files = []
                for pattern in patterns:
                    files.extend(source_path.glob(pattern))
            else:
                files = [f for f in source_path.iterdir() if f.is_file()]
            
            print(f"   Found {len(files)} file(s) to sync")
            
            results = {
                'total': len(files),
                'uploaded': 0,
                'failed': 0,
                'skipped': 0,
                'files': []
            }
            
            # Upload each file
            for file_path in files:
                file_info = {
                    'name': file_path.name,
                    'size': file_path.stat().st_size,
                    'status': 'pending'
                }
                
                # Skip large files
                if file_info['size'] > 10 * 1024 * 1024:  # 10MB limit
                    print(f"⏭️ Skipping {file_path.name} (too large: {file_info['size']:,} bytes)")
                    file_info['status'] = 'skipped'
                    results['skipped'] += 1
                else:
                    doc_id = self.upload_document(
                        connector_id=connector_id,
                        file_path=str(file_path),
                        content_type=self._get_content_type(file_path.suffix)
                    )
                    
                    if doc_id:
                        file_info['status'] = 'uploaded'
                        file_info['document_id'] = doc_id
                        results['uploaded'] += 1
                    else:
                        file_info['status'] = 'failed'
                        results['failed'] += 1
                
                results['files'].append(file_info)
            
            # Summary
            print(f"\n📊 Sync Summary:")
            print(f"   Total files: {results['total']}")
            print(f"   Uploaded: {results['uploaded']}")
            print(f"   Failed: {results['failed']}")
            print(f"   Skipped: {results['skipped']}")
            
            return results
            
        except Exception as e:
            print(f"❌ Error syncing documents: {e}")
            if self.verbose:
                import traceback
                traceback.print_exc()
            return {'success': False, 'error': str(e)}
    
    def batch_upload(self, file_list: List[str], connector_id: str) -> Dict[str, Any]:
        """
        Batch upload multiple documents
        
        Args:
            file_list: List of file paths
            connector_id: Target connector ID
            
        Returns:
            Upload results
        """
        print(f"\n📦 Batch uploading {len(file_list)} file(s)")
        
        results = {
            'total': len(file_list),
            'successful': 0,
            'failed': 0,
            'documents': []
        }
        
        for file_path in file_list:
            doc_id = self.upload_document(
                connector_id=connector_id,
                file_path=file_path
            )
            
            if doc_id:
                results['successful'] += 1
                results['documents'].append({
                    'file': file_path,
                    'document_id': doc_id,
                    'status': 'success'
                })
            else:
                results['failed'] += 1
                results['documents'].append({
                    'file': file_path,
                    'status': 'failed'
                })
        
        print(f"\n✅ Batch upload complete")
        print(f"   Successful: {results['successful']}/{results['total']}")
        print(f"   Failed: {results['failed']}/{results['total']}")
        
        return results
    
    def _get_content_type(self, extension: str) -> str:
        """Get MIME type for file extension"""
        mime_types = {
            '.json': 'application/json',
            '.xml': 'application/xml',
            '.txt': 'text/plain',
            '.csv': 'text/csv',
            '.pdf': 'application/pdf',
            '.zip': 'application/zip',
            '.gz': 'application/gzip',
            '.jpg': 'image/jpeg',
            '.jpeg': 'image/jpeg',
            '.png': 'image/png',
            '.html': 'text/html',
            '.js': 'application/javascript',
            '.css': 'text/css'
        }
        return mime_types.get(extension.lower(), 'application/octet-stream')


def main():
    """Main function"""
    parser = argparse.ArgumentParser(
        description='Manage Boomi connector documents',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # List connector records
  %(prog)s --list
  
  # Upload a document
  %(prog)s --upload /path/to/file.json --connector CONNECTOR_ID
  
  # Download a document
  %(prog)s --download CONNECTOR_ID --output /path/to/output.json
  
  # Sync directory to connector
  %(prog)s --sync /path/to/docs --connector CONNECTOR_ID --extensions json,xml
  
  # Batch upload files
  %(prog)s --batch file1.json file2.xml file3.csv --connector CONNECTOR_ID
  
  # List connector records of specific type
  %(prog)s --list --type "Database"
  
  # Show help with examples
  %(prog)s --help-examples
"""
    )
    
    # Operations
    parser.add_argument('--list', action='store_true',
                       help='List connector records')
    parser.add_argument('--upload', metavar='FILE',
                       help='Upload a document')
    parser.add_argument('--download', metavar='ID',
                       help='Download a document')
    parser.add_argument('--sync', metavar='DIR',
                       help='Sync directory to connector')
    parser.add_argument('--batch', nargs='+', metavar='FILE',
                       help='Batch upload files')
    
    # Options
    parser.add_argument('--connector', metavar='ID',
                       help='Connector ID')
    parser.add_argument('--output', metavar='PATH',
                       help='Output file path for download')
    parser.add_argument('--extensions', metavar='EXT',
                       help='File extensions for sync (comma-separated)')
    parser.add_argument('--type', metavar='TYPE',
                       help='Filter by connector type')
    parser.add_argument('--name', metavar='NAME',
                       help='Document name for upload')
    parser.add_argument('--limit', type=int, default=10,
                       help='Limit results (default: 10)')
    
    # Common options
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='Enable verbose output')
    parser.add_argument('--help-examples', action='store_true',
                       help='Show detailed examples')
    
    args = parser.parse_args()
    
    # Show examples if requested
    if args.help_examples:
        print("""
Connector Document Management Examples:

1. List all connector records:
   python manage_connector_documents.py --list

2. List database connectors:
   python manage_connector_documents.py --list --type "Database"

3. Upload a JSON file:
   python manage_connector_documents.py --upload config.json \\
       --connector abc123-def456 --name "Configuration"

4. Download a document:
   python manage_connector_documents.py --download abc123-def456 \\
       --output downloaded.json

5. Sync JSON and XML files from directory:
   python manage_connector_documents.py --sync /data/configs \\
       --connector abc123-def456 --extensions json,xml

6. Batch upload multiple files:
   python manage_connector_documents.py --batch file1.json file2.xml file3.csv \\
       --connector abc123-def456

7. Upload with custom document name:
   python manage_connector_documents.py --upload data.csv \\
       --connector abc123-def456 --name "Sales Data Q1"

8. List with increased limit:
   python manage_connector_documents.py --list --limit 50

Environment Variables Required:
  BOOMI_ACCOUNT - Boomi account ID
  BOOMI_USER - Boomi username
  BOOMI_SECRET - Boomi password/token

Note: Connector IDs are Generic Connector Record IDs from the Boomi platform.
      Use --list to find available connectors first.
""")
        return
    
    # Check for at least one operation
    if not any([args.list, args.upload, args.download, args.sync, args.batch]):
        parser.print_help()
        return
    
    # Initialize manager
    manager = ConnectorDocumentManager(verbose=args.verbose)
    
    # Execute operations
    if args.list:
        # List connector records
        records = manager.list_connector_records(
            connector_type=args.type,
            limit=args.limit
        )
        
        if records:
            print("\n📋 Connector Records:")
            for i, record in enumerate(records, 1):
                print(f"\n{i}. {record['name']}")
                print(f"   ID: {record['id']}")
                print(f"   Type: {record['type']}")
                print(f"   Created: {record['created']}")
                print(f"   Modified: {record['modified']}")
    
    elif args.upload:
        # Upload document
        if not args.connector:
            print("❌ Error: --connector is required for upload")
            return
        
        doc_id = manager.upload_document(
            connector_id=args.connector,
            file_path=args.upload,
            document_name=args.name
        )
        
        if doc_id:
            print(f"\n✅ Document uploaded: {doc_id}")
    
    elif args.download:
        # Download document
        success = manager.download_document(
            connector_id=args.download,
            output_path=args.output
        )
        
        if success:
            print("\n✅ Download information retrieved")
    
    elif args.sync:
        # Sync directory
        if not args.connector:
            print("❌ Error: --connector is required for sync")
            return
        
        extensions = None
        if args.extensions:
            extensions = [ext.strip() for ext in args.extensions.split(',')]
        
        results = manager.sync_documents(
            source_dir=args.sync,
            connector_id=args.connector,
            extensions=extensions
        )
        
        if results.get('total', 0) > 0:
            print(f"\n✅ Sync completed: {results['uploaded']}/{results['total']} uploaded")
    
    elif args.batch:
        # Batch upload
        if not args.connector:
            print("❌ Error: --connector is required for batch upload")
            return
        
        results = manager.batch_upload(
            file_list=args.batch,
            connector_id=args.connector
        )
        
        print(f"\n✅ Batch complete: {results['successful']}/{results['total']} successful")


if __name__ == '__main__':
    main()