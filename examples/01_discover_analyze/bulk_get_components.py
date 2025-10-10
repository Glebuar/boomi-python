#!/usr/bin/env python3
"""
Boomi SDK Example: Bulk Get Components
======================================

This example demonstrates how to retrieve multiple components in a single API call
using the bulk operation. This is more efficient than making individual calls
for each component.

Features:
- Retrieve up to 5 components in one API call (Boomi limit)
- Get full XML configuration for all components
- Handle mixed component types (process, connector, profile, etc.)
- Parse and display component metadata and configuration
- Extract configuration details from XML

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- COMPONENT ACCESS privilege required

Usage:
    python bulk_get_components.py COMPONENT_ID1 [COMPONENT_ID2] [...]
    
    Arguments:
    COMPONENT_IDs    One or more component IDs to retrieve (max 5)
    
Examples:
    python bulk_get_components.py 112b4efe-b173-4258-9492-613ead7d52ce
    python bulk_get_components.py 112b4efe-b173-4258-9492-613ead7d52ce 458d7f8d-2fd2-468d-a3d8-9a1e0f14ac6e
"""

import os
import sys
import xml.etree.ElementTree as ET
from typing import Optional, List, Dict

# Add parent directory to path for imports  
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# Load environment variables from .env file if available
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv is optional

from boomi import Boomi
from boomi.models import ComponentBulkRequest, ComponentBulkRequestType, BulkId


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


def format_date(date_str):
    """Format ISO date string to readable format"""
    if date_str and 'T' in date_str:
        return date_str.split('T')[0] + ' ' + date_str.split('T')[1].split('.')[0]
    return date_str or 'N/A'


def parse_component_xml(xml_string: str) -> Dict:
    """Parse component XML and extract metadata"""
    try:
        root = ET.fromstring(xml_string)
        
        # Extract attributes from the root element  
        component_data = {
            'name': root.get('name', 'N/A'),
            'component_id': root.get('componentId', 'N/A'),
            'type': root.get('type', 'N/A'),
            'version': root.get('version', 'N/A'),
            'created_date': root.get('createdDate', 'N/A'),
            'created_by': root.get('createdBy', 'N/A'),
            'modified_date': root.get('modifiedDate', 'N/A'),
            'modified_by': root.get('modifiedBy', 'N/A'),
            'folder_full_path': root.get('folderFullPath', 'N/A'),
            'folder_name': root.get('folderName', 'N/A'),
            'current_version': root.get('currentVersion', 'false').lower() == 'true',
            'deleted': root.get('deleted', 'false').lower() == 'true',
            'description': '',
            'has_config': False
        }
        
        # Look for description
        ns = {'ns0': 'http://api.platform.boomi.com/'}
        desc_elem = root.find('ns0:description', ns)
        if desc_elem is not None and desc_elem.text:
            component_data['description'] = desc_elem.text
            
        # Check if object/configuration exists
        object_elem = root.find('ns0:object', ns)
        component_data['has_config'] = object_elem is not None
        
        # Extract configuration details if available
        if component_data['has_config'] and object_elem is not None:
            config_info = []
            if component_data['type'] == 'process':
                # Extract process details
                process_elem = object_elem.find('process')
                if process_elem is not None:
                    shapes = process_elem.findall('.//shape')
                    config_info.append(f"{len(shapes)} shapes")
                    
            component_data['config_info'] = ', '.join(config_info) if config_info else 'Available'
        
        return component_data
        
    except ET.ParseError as e:
        return {
            'error': f'XML parse error: {e}',
            'raw_xml_length': len(xml_string)
        }


def print_component_info(component_data: Dict, index: int):
    """Print component information from parsed data"""
    print(f"\n{'='*60}")
    print(f"📋 Component #{index}")
    print(f"{'='*60}")
    
    if 'error' in component_data:
        print(f"  ❌ Error: {component_data['error']}")
        print(f"  Raw XML length: {component_data.get('raw_xml_length', 0)} chars")
        return
        
    print(f"  Name: {component_data['name']}")
    print(f"  Component ID: {component_data['component_id']}")
    print(f"  Type: {component_data['type']}")
    print(f"  Version: {component_data['version']}")
    
    # Status information
    status_parts = []
    if component_data['current_version']:
        status_parts.append("CURRENT")
    if component_data['deleted']:
        status_parts.append("DELETED")
    
    if status_parts:
        print(f"  Status: {' | '.join(status_parts)}")
    
    print(f"  Created: {format_date(component_data['created_date'])} by {component_data['created_by']}")
    print(f"  Modified: {format_date(component_data['modified_date'])} by {component_data['modified_by']}")
    
    # Folder information
    if component_data['folder_full_path'] != 'N/A':
        print(f"  Folder: {component_data['folder_full_path']}")
    
    # Description
    if component_data.get('description'):
        print(f"  Description: {component_data['description']}")
    
    # XML configuration check
    if component_data['has_config']:
        config_info = component_data.get('config_info', 'Available')
        print(f"  ✅ XML Configuration: {config_info}")
    else:
        print(f"  ❌ XML Configuration: Not available")


def main():
    """Main execution function"""
    if len(sys.argv) < 2 or '--help' in sys.argv or '-h' in sys.argv:
        print("Boomi SDK Example: Bulk Get Components")
        print("=" * 40)
        print("This example demonstrates bulk component retrieval.")
        print()
        print("Usage: python bulk_get_components.py COMPONENT_ID1 [COMPONENT_ID2] [...]")
        print()
        print("Arguments:")
        print("  COMPONENT_IDs    One or more component IDs to retrieve (max 5)")
        print()
        print("Examples:")
        print("  python bulk_get_components.py 112b4efe-b173-4258-9492-613ead7d52ce")
        print("  python bulk_get_components.py 112b4efe-b173-4258-9492-613ead7d52ce 458d7f8d-2fd2-468d-a3d8-9a1e0f14ac6e")
        print()
        print("Environment Variables:")
        print("  BOOMI_ACCOUNT    Your Boomi account ID")
        print("  BOOMI_USER       Your Boomi username")
        print("  BOOMI_SECRET     Your Boomi API token/password")
        sys.exit(0)
        
    component_ids = sys.argv[1:]
    
    print("🚀 Boomi SDK Example: Bulk Get Components")
    print("=" * 50)
    
    # Validate environment variables
    account_id, username, password = validate_environment()
    
    print(f"🏢 Account: {account_id}")
    print(f"👤 User: {username}")
    print(f"🎯 Component IDs to retrieve: {len(component_ids)}")
    
    if len(component_ids) > 5:
        print(f"⚠️ Warning: Maximum 5 components allowed per bulk request. Only first 5 will be retrieved.")
        component_ids = component_ids[:5]
    
    # Initialize SDK
    try:
        sdk = Boomi(
            account_id=account_id,
            username=username,
            password=password,
            timeout=30000
        )
        print("✅ SDK initialized successfully")
    except Exception as e:
        print(f"❌ Failed to initialize SDK: {e}")
        sys.exit(1)
    
    try:
        # Bulk retrieve components
        print(f"\n🔍 Retrieving {len(component_ids)} components in bulk...")
        
        # Create bulk request
        bulk_ids = [BulkId(id_=comp_id) for comp_id in component_ids]
        bulk_request = ComponentBulkRequest(
            request=bulk_ids,
            type_=ComponentBulkRequestType.GET
        )
        
        # Execute bulk get - SDK returns list of XML strings
        result = sdk.component.bulk_component(request_body=bulk_request)
        
        print("✅ Bulk retrieval successful!")
        print(f"📊 Response type: {type(result).__name__}")
        
        # Process XML responses
        if isinstance(result, list) and result:
            print(f"\n{'='*80}")
            print(f"📋 BULK COMPONENT RETRIEVAL RESULTS ({len(result)} components)")
            print(f"{'='*80}")
            
            component_types = []
            for i, xml_string in enumerate(result, 1):
                component_data = parse_component_xml(xml_string)
                print_component_info(component_data, i)
                
                if 'type' in component_data and component_data['type'] != 'N/A':
                    component_types.append(component_data['type'])
            
            # Summary
            print(f"\n{'='*60}")
            print(f"📊 BULK RETRIEVAL SUMMARY")
            print(f"{'='*60}")
            print(f"  • Total components retrieved: {len(result)}")
            print(f"  • Component types: {', '.join(set(component_types)) if component_types else 'Unknown'}")
            print(f"  • Average XML length: {sum(len(xml) for xml in result) // len(result)} characters")
            
            print(f"\n✅ Successfully retrieved {len(result)} component(s) in bulk!")
        else:
            print(f"\n❌ No components retrieved. Check component IDs and permissions.")
            print(f"   Result type: {type(result)}")
            print(f"   Result: {result}")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ Error during bulk component retrieval: {e}")
        
        # Provide helpful troubleshooting hints
        error_msg = str(e)
        if "404" in error_msg or "not found" in error_msg.lower():
            print("🔍 One or more components not found - check the component IDs")
        elif "403" in error_msg:
            print("🔍 Permission issue - check your API credentials and account permissions")
        elif "400" in error_msg:
            print("🔍 Bad request - check component ID format (should be valid UUIDs)")
        elif "401" in error_msg:
            print("🔍 Authentication failed - verify your credentials")
        else:
            print("🔍 Check network connectivity and API endpoint availability")
            
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()