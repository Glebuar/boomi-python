#!/usr/bin/env python3
"""
Boomi SDK Example: Bulk Get Components

NOTE: As of August 2025, the SDK's bulk_component method has a bug where it cannot
properly parse the XML response from the API. The API returns XML for bulk operations,
but the SDK expects a parsed dictionary. This example includes a workaround using
direct API calls until the SDK is fixed.

This example demonstrates how to retrieve multiple components in a single API call
using the bulk operation. This is more efficient than making individual calls
for each component.

Features:
- Retrieve up to 5 components in one API call (Boomi limit)
- Get full XML configuration for all components
- Handle mixed component types (process, connector, profile, etc.)
- Show component metadata and configuration

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- Or create a .env file with these variables

Usage:
    python bulk_get_components.py COMPONENT_ID1 COMPONENT_ID2 [...]
    
    Arguments:
    COMPONENT_IDs    One or more component IDs to retrieve (max 5)
    
    Examples:
    python bulk_get_components.py 112b4efe-b173-4258-9492-613ead7d52ce 458d7f8d-2fd2-468d-a3d8-9a1e0f14ac6e
    python bulk_get_components.py id1 id2 id3 id4 id5
"""

import os
import sys
sys.path.insert(0, '../../src')
from boomi import Boomi
from boomi.models import ComponentBulkRequest, ComponentBulkRequestType, BulkId

# Load environment variables
try:
    from dotenv import load_dotenv
    load_dotenv('../../.env')
except ImportError:
    pass

def format_date(date_str):
    """Format ISO date string to readable format"""
    if date_str and 'T' in date_str:
        return date_str.split('T')[0] + ' ' + date_str.split('T')[1].split('.')[0]
    return date_str or 'N/A'

def print_component_info(component, index):
    """Print component information"""
    print(f"\n{'='*60}")
    print(f"📋 Component #{index}")
    print(f"{'='*60}")
    print(f"  Name: {getattr(component, 'name', 'N/A')}")
    print(f"  Component ID: {getattr(component, 'component_id', 'N/A')}")
    print(f"  Type: {getattr(component, 'type_', 'N/A')}")
    print(f"  Version: {getattr(component, 'version', 'N/A')}")
    
    # Status information
    current_version = getattr(component, 'current_version', 'false')
    deleted = getattr(component, 'deleted', 'false')
    status_parts = []
    
    if str(current_version).lower() == 'true':
        status_parts.append("CURRENT")
    if str(deleted).lower() == 'true':
        status_parts.append("DELETED")
    
    if status_parts:
        print(f"  Status: {' | '.join(status_parts)}")
    
    print(f"  Created: {format_date(getattr(component, 'created_date', 'N/A'))} by {getattr(component, 'created_by', 'N/A')}")
    print(f"  Modified: {format_date(getattr(component, 'modified_date', 'N/A'))} by {getattr(component, 'modified_by', 'N/A')}")
    
    # Folder information
    folder_path = getattr(component, 'folder_full_path', None) or getattr(component, 'folder_name', None)
    if folder_path:
        print(f"  Folder: {folder_path}")
    
    # XML configuration check
    obj = getattr(component, 'object', None)
    if obj:
        print(f"  ✅ XML Configuration: Available")
        if isinstance(obj, dict):
            print(f"     Configuration keys: {', '.join(list(obj.keys())[:5])}")
    else:
        print(f"  ❌ XML Configuration: Not available")

def bulk_get_components(component_ids):
    """Retrieve multiple components in bulk"""
    
    # Check for required environment variables
    account_id = os.getenv("BOOMI_ACCOUNT")
    username = os.getenv("BOOMI_USER") 
    password = os.getenv("BOOMI_SECRET")
    
    if not all([account_id, username, password]):
        print("❌ Error: Missing required environment variables")
        print("   Please set: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET")
        return False
    
    print(f"🏢 Account: {account_id}")
    print(f"👤 User: {username}")
    print(f"🎯 Component IDs to retrieve: {len(component_ids)}")
    
    if len(component_ids) > 5:
        print(f"⚠️ Warning: Maximum 5 components allowed per bulk request. Only first 5 will be retrieved.")
        component_ids = component_ids[:5]
    
    # Initialize the Boomi SDK
    sdk = Boomi(
        account_id=account_id,
        username=username, 
        password=password,
        timeout=30000
    )
    
    print(f"\n🔍 Retrieving {len(component_ids)} components in bulk...")
    
    try:
        # Create bulk request with proper structure
        bulk_ids = [BulkId(id_=comp_id) for comp_id in component_ids]
        bulk_request = ComponentBulkRequest(
            request=bulk_ids,
            type_=ComponentBulkRequestType.GET
        )
        
        # Execute bulk get
        result = sdk.component.bulk_component(request_body=bulk_request)
        
        print("✅ Bulk retrieval successful!")
        print(f"📊 Response type: {type(result).__name__}")
        
        # Handle response - the fixed SDK returns list of XML strings
        components = []
        if isinstance(result, list):
            # Fixed SDK returns list of XML strings
            import xml.etree.ElementTree as ET
            
            for xml_string in result:
                try:
                    # Parse each component XML string
                    component_elem = ET.fromstring(xml_string)
                    
                    # Create a mock component object with parsed attributes
                    class MockComponent:
                        def __init__(self, elem):
                            # Extract component attributes from XML
                            self.name = elem.get('name', 'N/A')
                            self.component_id = elem.get('componentId', 'N/A')
                            self.type_ = elem.get('type', 'N/A')
                            self.version = elem.get('version', 'N/A')
                            self.created_date = elem.get('createdDate', 'N/A')
                            self.created_by = elem.get('createdBy', 'N/A')
                            self.modified_date = elem.get('modifiedDate', 'N/A')
                            self.modified_by = elem.get('modifiedBy', 'N/A')
                            self.folder_full_path = elem.get('folderFullPath', 'N/A')
                            self.folder_name = elem.get('folderName', 'N/A')
                            self.current_version = elem.get('currentVersion', 'false') == 'true'
                            self.deleted = elem.get('deleted', 'false') == 'true'
                            
                            # Check if object exists
                            ns = {'bns': 'http://api.platform.boomi.com/'}
                            object_elem = elem.find('bns:object', ns)
                            self.object = object_elem is not None
                    
                    components.append(MockComponent(component_elem))
                    
                except ET.ParseError as e:
                    print(f"⚠️ Failed to parse component XML: {e}")
                    components.append(xml_string)  # Add raw string as fallback
        else:
            # Fallback to original parsing logic
            if hasattr(result, '_kwargs') and result._kwargs:
                if 'Component' in result._kwargs:
                    components = [result._kwargs['Component']]
                elif 'Components' in result._kwargs:
                    components = result._kwargs['Components']
            elif hasattr(result, 'result'):
                components = result.result if isinstance(result.result, list) else [result.result]
            elif hasattr(result, 'component_id'):
                components = [result]
        
        if components:
            print(f"✅ Retrieved {len(components)} component(s)")
            
            # Display each component
            for i, component in enumerate(components, 1):
                print_component_info(component, i)
            
            # Summary
            print(f"\n{'='*60}")
            print(f"📊 Summary")
            print(f"{'='*60}")
            print(f"  • Total components retrieved: {len(components)}")
            print(f"  • Component types: {', '.join(set(getattr(c, 'type_', 'Unknown') for c in components))}")
            print(f"  • All have XML configuration: {'Yes' if all(getattr(c, 'object', None) for c in components) else 'No'}")
            
            return True
        else:
            print("❌ No components found in response")
            print("Response structure:")
            if hasattr(result, '__dict__'):
                for key, value in result.__dict__.items():
                    if not key.startswith('_'):
                        print(f"  {key}: {type(value).__name__}")
            return False
            
    except Exception as e:
        error_msg = str(e)
        print(f"❌ Bulk retrieval failed: {error_msg}")
        
        # Provide helpful troubleshooting hints
        if "404" in error_msg or "not found" in error_msg.lower():
            print("🔍 One or more components not found - check the component IDs")
            print("💡 Use list_all_components.py to find valid component IDs")
        elif "403" in error_msg:
            print("🔍 Permission issue - check your API credentials and account permissions")
        elif "400" in error_msg:
            print("🔍 Bad request - check component ID format")
            print("💡 Component IDs should be valid UUIDs")
        elif "401" in error_msg:
            print("🔍 Authentication failed - verify your credentials")
        else:
            print("🔍 Check network connectivity and API endpoint availability")
            
        return False

def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print("❌ Error: At least one component ID is required")
        print("\nUsage:")
        print(f"  {sys.argv[0]} COMPONENT_ID1 [COMPONENT_ID2 ...]")
        print("\nExamples:")
        print(f"  {sys.argv[0]} 112b4efe-b173-4258-9492-613ead7d52ce")
        print(f"  {sys.argv[0]} 112b4efe-b173-4258-9492-613ead7d52ce 458d7f8d-2fd2-468d-a3d8-9a1e0f14ac6e")
        print("\n💡 Use list_all_components.py to find component IDs")
        print("⚠️ Maximum 5 components per bulk request (Boomi limit)")
        return
    
    component_ids = sys.argv[1:]
    
    print("🚀 Boomi SDK Example: Bulk Get Components")
    print("=" * 45)
    print()
    
    success = bulk_get_components(component_ids)
    
    print(f"\n{'='*45}")
    if success:
        print("🌟 Bulk retrieval completed successfully!")
    else:
        print("💥 Bulk retrieval encountered issues")

if __name__ == "__main__":
    main()