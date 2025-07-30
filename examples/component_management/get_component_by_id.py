#!/usr/bin/env python3
"""
Boomi SDK Example: Get Component by ID

This example demonstrates how to retrieve a specific component by its ID
using the Boomi Python SDK. It shows how to get the full component XML
configuration including all shapes, connections, and properties.

Features:
- Retrieves component by ID
- Shows component metadata (name, type, version, dates)
- Displays full XML configuration
- Handles different component types (process, connector, profile, etc.)
- Supports version-specific retrieval

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- Or create a .env file with these variables

Usage:
    python get_component_by_id.py COMPONENT_ID [VERSION]
    
    Arguments:
    COMPONENT_ID    The component ID to retrieve
    VERSION         Optional: specific version to retrieve (defaults to latest)
    
    Examples:
    python get_component_by_id.py 112b4efe-b173-4258-9492-613ead7d52ce
    python get_component_by_id.py 112b4efe-b173-4258-9492-613ead7d52ce 1
"""

import os
import sys
sys.path.insert(0, '../../src')
from boomi import Boomi

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

def print_component_metadata(component):
    """Print component metadata information"""
    print("📋 Component Metadata:")
    print("=" * 50)
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
    
    # Branch information
    branch_name = getattr(component, 'branch_name', None)
    if branch_name and branch_name != 'main':
        print(f"  Branch: {branch_name}")
    
    # Description
    description = getattr(component, 'description', None)
    if description:
        print(f"  Description: {description}")

def print_component_xml(component):
    """Print component XML configuration"""
    print("\n🔧 Component Configuration:")
    print("=" * 50)
    
    # Check for XML object
    obj = getattr(component, 'object', None)
    if obj:
        print("📄 Component has XML configuration object")
        
        # Try to show some basic structure info
        if hasattr(obj, '__dict__'):
            obj_dict = obj.__dict__ if hasattr(obj, '__dict__') else {}
            print(f"📊 Configuration contains {len(obj_dict)} top-level elements")
            
            # Show top-level keys
            if obj_dict:
                print("🔑 Top-level configuration elements:")
                for key in sorted(obj_dict.keys()):
                    if not key.startswith('_'):
                        value = obj_dict[key]
                        value_type = type(value).__name__
                        print(f"    • {key}: {value_type}")
        else:
            print(f"📄 Configuration object type: {type(obj).__name__}")
    else:
        print("❌ No XML configuration object found")
    
    # Check for encrypted values
    encrypted_values = getattr(component, 'encrypted_values', None)
    if encrypted_values:
        print(f"\n🔒 Component has encrypted values configured")
    
    # Check for process overrides
    process_overrides = getattr(component, 'process_overrides', None)
    if process_overrides:
        print(f"\n⚙️ Component has process overrides configured")

def get_component_by_id(component_id, version=None):
    """Retrieve and display component by ID"""
    
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
    print(f"🎯 Target Component ID: {component_id}")
    if version:
        print(f"📌 Specific Version: {version}")
    else:
        print(f"📌 Version: Latest")
    
    # Initialize the Boomi SDK
    sdk = Boomi(
        account_id=account_id,
        username=username, 
        password=password,
        timeout=30000
    )
    
    print(f"\n🔍 Retrieving component...")
    
    try:
        # Construct component identifier
        if version:
            component_identifier = f"{component_id}~{version}"
        else:
            component_identifier = component_id
        
        # Get the component
        result = sdk.component.get_component(component_id=component_identifier)
        
        print("✅ Component retrieved successfully!")
        print(f"📊 Response type: {type(result).__name__}")
        
        # Handle response - check if it's wrapped in _kwargs
        component = None
        if hasattr(result, '_kwargs') and result._kwargs:
            if 'Component' in result._kwargs:
                component = result._kwargs['Component']
            else:
                # Try to find the component in the response
                for key, value in result._kwargs.items():
                    if hasattr(value, 'component_id') or hasattr(value, 'name'):
                        component = value
                        break
        else:
            component = result
        
        if component:
            print_component_metadata(component)
            print_component_xml(component)
            
            print(f"\n🎉 SUCCESS!")
            print(f"📍 Component '{getattr(component, 'name', 'N/A')}' retrieved successfully")
            print(f"🔧 Component contains full XML configuration for deployment/analysis")
            
            return True
        else:
            print("❌ No component data found in response")
            print("Response structure:")
            if hasattr(result, '__dict__'):
                for key, value in result.__dict__.items():
                    if not key.startswith('_'):
                        print(f"  {key}: {type(value).__name__}")
            return False
            
    except Exception as e:
        error_msg = str(e)
        print(f"❌ Component retrieval failed: {error_msg}")
        
        # Provide helpful troubleshooting hints
        if "404" in error_msg or "not found" in error_msg.lower():
            print("🔍 Component not found - check the component ID")
            print("💡 Use list_all_components.py to find valid component IDs")
        elif "403" in error_msg:
            print("🔍 Permission issue - check your API credentials and account permissions")
        elif "400" in error_msg:
            print("🔍 Bad request - check component ID format")
            if version:
                print("💡 Version format should be a number (e.g., 1, 2, 3)")
        elif "401" in error_msg:
            print("🔍 Authentication failed - verify your credentials")
        else:
            print("🔍 Check network connectivity and API endpoint availability")
            
        return False

def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print("❌ Error: Component ID is required")
        print("\nUsage:")
        print(f"  {sys.argv[0]} COMPONENT_ID [VERSION]")
        print("\nExamples:")
        print(f"  {sys.argv[0]} 112b4efe-b173-4258-9492-613ead7d52ce")
        print(f"  {sys.argv[0]} 112b4efe-b173-4258-9492-613ead7d52ce 1")
        print("\n💡 Use list_all_components.py to find component IDs")
        return
    
    component_id = sys.argv[1]
    version = sys.argv[2] if len(sys.argv) > 2 else None
    
    print("🚀 Boomi SDK Example: Get Component by ID")
    print("=" * 45)
    print()
    
    success = get_component_by_id(component_id, version)
    
    print(f"\n{'='*45}")
    if success:
        print("🌟 Component retrieval completed successfully!")
    else:
        print("💥 Component retrieval encountered issues")

if __name__ == "__main__":
    main()