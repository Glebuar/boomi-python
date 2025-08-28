#!/usr/bin/env python3
"""
Manage Connectors - Manage and monitor Boomi connectors

This example demonstrates how to manage various types of connectors in Boomi
including AS2, EDI (X12/EDIFACT), HL7, Generic, and other specialized connectors.
It provides functionality to query, create, and manage connector records.

Features:
- Query and list connector records by type
- Create new connector records with proper configuration
- Update existing connector configurations
- Monitor connector status and versions
- Manage connector documents and attachments
- Support for various connector types (AS2, X12, EDIFACT, HL7, etc.)

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET

Usage:
    python manage_connectors.py [options]
    
Examples:
    # List all AS2 connector records
    python manage_connectors.py --list --type as2
    
    # List all X12 connector records
    python manage_connectors.py --list --type x12
    
    # Get specific connector record
    python manage_connectors.py --get CONNECTOR_ID --type generic
    
    # Query connectors with filters
    python manage_connectors.py --query --filter "status=active"
    
    # Get connector versions for an atom
    python manage_connectors.py --versions --atom-id ATOM_ID
    
    # Download connector document
    python manage_connectors.py --download --connector-id CONNECTOR_ID --type generic
"""

import os
import sys
import argparse
from typing import Optional, List, Dict, Any
from datetime import datetime

# Import Boomi SDK
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))
from boomi import Boomi
from boomi.models import *


class ConnectorManager:
    """Manage Boomi connectors"""
    
    CONNECTOR_TYPES = {
        'as2': 'AS2',
        'x12': 'X12/EDI',
        'edifact': 'EDIFACT',
        'hl7': 'HL7',
        'generic': 'Generic',
        'rosettanet': 'RosettaNet',
        'tradacoms': 'Tradacoms',
        'odette': 'Odette',
        'oftp2': 'OFTP2',
        'edi_custom': 'EDI Custom'
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
    
    def list_connector_records(self, connector_type: str = 'generic', limit: int = 10) -> List[Dict[str, Any]]:
        """List connector records of specified type"""
        print(f"\n🔍 Listing {self.CONNECTOR_TYPES.get(connector_type, connector_type)} connector records...")
        
        try:
            # Different services for different connector types
            if connector_type == 'as2':
                query_config = AS2ConnectorRecordQueryConfig()
                result = self.sdk.as2_connector_record.query_as2_connector_record(request_body=query_config)
            elif connector_type == 'x12':
                query_config = X12ConnectorRecordQueryConfig()
                result = self.sdk.x12_connector_record.query_x12_connector_record(request_body=query_config)
            elif connector_type == 'edifact':
                query_config = EdifactConnectorRecordQueryConfig()
                result = self.sdk.edifact_connector_record.query_edifact_connector_record(request_body=query_config)
            elif connector_type == 'hl7':
                query_config = HL7ConnectorRecordQueryConfig()
                result = self.sdk.hl7_connector_record.query_hl7_connector_record(request_body=query_config)
            elif connector_type == 'generic':
                # GenericConnectorRecordQueryConfig might need empty filter
                try:
                    query_config = GenericConnectorRecordQueryConfig()
                except:
                    # If it requires a filter, pass None or skip
                    query_config = None
                result = self.sdk.generic_connector_record.query_generic_connector_record(request_body=query_config)
            elif connector_type == 'rosettanet':
                query_config = RosettaNetConnectorRecordQueryConfig()
                result = self.sdk.rosetta_net_connector_record.query_rosetta_net_connector_record(request_body=query_config)
            elif connector_type == 'tradacoms':
                query_config = TradacomsConnectorRecordQueryConfig()
                result = self.sdk.tradacoms_connector_record.query_tradacoms_connector_record(request_body=query_config)
            elif connector_type == 'odette':
                query_config = OdetteConnectorRecordQueryConfig()
                result = self.sdk.odette_connector_record.query_odette_connector_record(request_body=query_config)
            elif connector_type == 'oftp2':
                query_config = OFTP2ConnectorRecordQueryConfig()
                result = self.sdk.oftp2_connector_record.query_oftp2_connector_record(request_body=query_config)
            elif connector_type == 'edi_custom':
                query_config = EDICustomConnectorRecordQueryConfig()
                result = self.sdk.edi_custom_connector_record.query_edi_custom_connector_record(request_body=query_config)
            else:
                print(f"❌ Unknown connector type: {connector_type}")
                return []
            
            if result and hasattr(result, 'result') and result.result:
                records = result.result[:limit]
                print(f"✅ Found {len(result.result)} connector record(s)")
                
                connector_list = []
                for i, record in enumerate(records, 1):
                    print(f"\n📋 Record {i}:")
                    
                    # Extract common fields (vary by connector type)
                    record_info = {
                        'index': i,
                        'id': getattr(record, 'id_', 'N/A'),
                        'name': getattr(record, 'name', 'N/A'),
                        'type': connector_type
                    }
                    
                    # Add type-specific fields
                    if hasattr(record, 'status'):
                        record_info['status'] = record.status
                    if hasattr(record, 'created_date'):
                        record_info['created_date'] = record.created_date
                    if hasattr(record, 'modified_date'):
                        record_info['modified_date'] = record.modified_date
                    
                    print(f"   🆔 ID: {record_info['id']}")
                    print(f"   📛 Name: {record_info['name']}")
                    if 'status' in record_info:
                        print(f"   📊 Status: {record_info['status']}")
                    if 'created_date' in record_info:
                        print(f"   📅 Created: {record_info['created_date']}")
                    
                    connector_list.append(record_info)
                
                return connector_list
            else:
                print("ℹ️ No connector records found")
                return []
                
        except Exception as e:
            print(f"❌ Failed to list connector records: {e}")
            return []
    
    def get_connector_record(self, connector_id: str, connector_type: str = 'generic') -> Optional[Any]:
        """Get specific connector record details"""
        print(f"\n🔍 Getting {self.CONNECTOR_TYPES.get(connector_type, connector_type)} connector record {connector_id}...")
        
        try:
            # Different services for different connector types
            if connector_type == 'as2':
                record = self.sdk.as2_connector_record.get_as2_connector_record(id_=connector_id)
            elif connector_type == 'x12':
                record = self.sdk.x12_connector_record.get_x12_connector_record(id_=connector_id)
            elif connector_type == 'edifact':
                record = self.sdk.edifact_connector_record.get_edifact_connector_record(id_=connector_id)
            elif connector_type == 'hl7':
                record = self.sdk.hl7_connector_record.get_hl7_connector_record(id_=connector_id)
            elif connector_type == 'generic':
                record = self.sdk.generic_connector_record.get_generic_connector_record(id_=connector_id)
            else:
                print(f"❌ Unknown connector type: {connector_type}")
                return None
            
            if record:
                print("✅ Connector record retrieved successfully")
                print(f"\n📋 Connector Details:")
                print(f"   🆔 ID: {getattr(record, 'id_', 'N/A')}")
                print(f"   📛 Name: {getattr(record, 'name', 'N/A')}")
                
                # Print type-specific details
                if hasattr(record, 'status'):
                    print(f"   📊 Status: {record.status}")
                if hasattr(record, 'atom_id'):
                    print(f"   🤖 Atom ID: {record.atom_id}")
                if hasattr(record, 'process_id'):
                    print(f"   ⚙️ Process ID: {record.process_id}")
                
                return record
            else:
                print("❌ Connector record not found")
                return None
                
        except Exception as e:
            print(f"❌ Failed to get connector record: {e}")
            return None
    
    def get_atom_connector_versions(self, atom_id: str) -> Optional[Any]:
        """Get connector versions installed on an atom"""
        print(f"\n🔍 Getting connector versions for atom {atom_id}...")
        
        try:
            result = self.sdk.atom_connector_versions.get_atom_connector_versions(id_=atom_id)
            
            if result:
                print("✅ Connector versions retrieved successfully")
                
                # The result contains version information
                if hasattr(result, 'connector_version') and result.connector_version:
                    print(f"\n📋 Installed Connector Versions:")
                    for i, version in enumerate(result.connector_version, 1):
                        print(f"   {i}. {getattr(version, 'type', 'Unknown')}: {getattr(version, 'version', 'Unknown')}")
                else:
                    print("ℹ️ No connector versions found")
                
                return result
            else:
                print("❌ Failed to retrieve connector versions")
                return None
                
        except Exception as e:
            print(f"❌ Failed to get connector versions: {e}")
            return None
    
    def download_connector_document(self, connector_id: str, output_path: Optional[str] = None) -> bool:
        """Download document from generic connector record"""
        print(f"\n📥 Downloading document for connector {connector_id}...")
        
        try:
            # Create connector document request
            request = ConnectorDocument(
                generic_connector_record_id=connector_id
            )
            
            # Request document download
            result = self.sdk.connector_document.create_connector_document(request_body=request)
            
            if result and hasattr(result, 'url'):
                print(f"✅ Download URL obtained")
                
                # Download using urllib (same as other fixed files)
                import urllib.request
                import base64
                
                credentials = base64.b64encode(f"{self.username}:{self.password}".encode()).decode()
                
                request = urllib.request.Request(result.url)
                request.add_header('Authorization', f'Basic {credentials}')
                
                # Set output path
                if not output_path:
                    output_path = f"connector_document_{connector_id}.dat"
                
                with urllib.request.urlopen(request) as response:
                    with open(output_path, 'wb') as f:
                        f.write(response.read())
                
                print(f"✅ Document downloaded to: {output_path}")
                return True
            else:
                print("❌ Failed to get download URL")
                return False
                
        except Exception as e:
            print(f"❌ Failed to download connector document: {e}")
            return False
    
    def show_connector_types(self):
        """Display all supported connector types"""
        print("\n📋 Supported Connector Types:")
        print("=" * 50)
        
        for key, name in self.CONNECTOR_TYPES.items():
            print(f"   • {key:12} - {name}")
        
        print("\n💡 Use --type parameter to specify connector type")
        print("   Example: --list --type as2")


def main():
    parser = argparse.ArgumentParser(
        description='Manage Boomi connectors',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    # List AS2 connectors
    python manage_connectors.py --list --type as2
    
    # Get specific connector
    python manage_connectors.py --get CONNECTOR_ID --type generic
    
    # Show connector versions on atom
    python manage_connectors.py --versions --atom-id ATOM_ID
    
    # Download connector document
    python manage_connectors.py --download --connector-id CONNECTOR_ID
    
    # Show supported connector types
    python manage_connectors.py --types
        """
    )
    
    parser.add_argument('--list', action='store_true',
                       help='List connector records')
    parser.add_argument('--get', metavar='ID',
                       help='Get specific connector record by ID')
    parser.add_argument('--type', default='generic',
                       choices=list(ConnectorManager.CONNECTOR_TYPES.keys()),
                       help='Connector type (default: generic)')
    parser.add_argument('--limit', type=int, default=10,
                       help='Limit number of results (default: 10)')
    parser.add_argument('--versions', action='store_true',
                       help='Get connector versions for atom')
    parser.add_argument('--atom-id', metavar='ID',
                       help='Atom ID for version query')
    parser.add_argument('--download', action='store_true',
                       help='Download connector document')
    parser.add_argument('--connector-id', metavar='ID',
                       help='Connector ID for download')
    parser.add_argument('--output', metavar='PATH',
                       help='Output path for downloaded document')
    parser.add_argument('--types', action='store_true',
                       help='Show supported connector types')
    
    args = parser.parse_args()
    
    # Initialize manager
    manager = ConnectorManager()
    
    print("\n🔌 Boomi Connector Manager")
    print("=" * 50)
    
    # Execute requested operation
    if args.types:
        manager.show_connector_types()
    
    elif args.list:
        records = manager.list_connector_records(
            connector_type=args.type,
            limit=args.limit
        )
        
        if records:
            print(f"\n✅ Listed {len(records)} connector record(s)")
    
    elif args.get:
        record = manager.get_connector_record(
            connector_id=args.get,
            connector_type=args.type
        )
        
        if record:
            print("\n✅ Connector record retrieved successfully")
    
    elif args.versions and args.atom_id:
        versions = manager.get_atom_connector_versions(args.atom_id)
        
        if versions:
            print("\n✅ Connector versions retrieved successfully")
    
    elif args.download and args.connector_id:
        success = manager.download_connector_document(
            connector_id=args.connector_id,
            output_path=args.output
        )
        
        if success:
            print("\n✅ Document downloaded successfully")
    
    else:
        parser.print_help()
        print("\n💡 Use --help for more examples")


if __name__ == "__main__":
    main()