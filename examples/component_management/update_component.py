#!/usr/bin/env python3
"""
Boomi SDK Example: Update Component

This example demonstrates how to update a Boomi component while preserving
its folder location and internal structure. The update preserves the existing
XML configuration and only modifies the component metadata.

Features:
- Updates component name and description
- Preserves folder location after update
- Maintains component's internal XML structure
- Supports all component types (process, connector, profile, etc.)
- Handles component version management

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- Or create a .env file with these variables

Usage:
    python update_component.py COMPONENT_ID [OPTIONS]
    
    Arguments:
    COMPONENT_ID    The component ID to update
    
    Options:
    --name=NAME     New name for the component
    --desc=DESC     New description for the component
    
    Examples:
    python update_component.py 112b4efe-b173-4258-9492-613ead7d52ce
    python update_component.py 112b4efe-b173-4258-9492-613ead7d52ce --name="Updated Process"
    python update_component.py 112b4efe-b173-4258-9492-613ead7d52ce --name="New Name" --desc="Updated description"
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

def dict_to_xml(obj, indent=0):
    """Convert dictionary/object structure to XML string with proper attribute handling"""
    if obj is None:
        return ""
    
    xml_parts = []
    indent_str = "\t" * indent
    
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key.startswith('_'):  # Skip private attributes
                continue
                
            if isinstance(value, dict):
                if value:
                    # Check if this dict has attributes (string/number values) vs child elements
                    attrs = []
                    children = []
                    
                    for k, v in value.items():
                        if isinstance(v, (str, int, float, bool)) and v is not None:
                            attrs.append(f'{k}="{v}"')
                        else:
                            children.append((k, v))
                    
                    # Build the element
                    if attrs and not children:
                        # All attributes, no children - self-closing tag
                        xml_parts.append(f"{indent_str}<{key} {' '.join(attrs)}/>")
                    elif attrs and children:
                        # Has both attributes and children
                        xml_parts.append(f"{indent_str}<{key} {' '.join(attrs)}>")
                        for child_key, child_value in children:
                            xml_parts.append(dict_to_xml({child_key: child_value}, indent + 1))
                        xml_parts.append(f"{indent_str}</{key}>")
                    elif children:
                        # Only children, no attributes
                        xml_parts.append(f"{indent_str}<{key}>")
                        xml_parts.append(dict_to_xml(value, indent + 1))
                        xml_parts.append(f"{indent_str}</{key}>")
                    else:
                        # Empty dict
                        xml_parts.append(f"{indent_str}<{key}/>")
                else:
                    # Empty dict
                    xml_parts.append(f"{indent_str}<{key}/>")
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        xml_parts.append(dict_to_xml({key: item}, indent))
                    else:
                        escaped_item = str(item).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
                        xml_parts.append(f"{indent_str}<{key}>{escaped_item}</{key}>")
            elif value is None:
                xml_parts.append(f"{indent_str}<{key}/>")
            else:
                # Escape XML special characters
                escaped_value = str(value).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
                xml_parts.append(f"{indent_str}<{key}>{escaped_value}</{key}>")
    
    return "\n".join(xml_parts)

def update_component(component_id, new_name=None, new_description=None):
    """Update a component while preserving its structure and folder"""
    
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
    
    # Initialize the Boomi SDK
    sdk = Boomi(
        account_id=account_id,
        username=username, 
        password=password,
        timeout=30000
    )
    
    try:
        print(f"\n🔍 Retrieving existing component...")
        
        # Get the existing component with its complete structure
        existing = sdk.component.get_component(component_id=component_id)
        
        if not existing:
            print("❌ Component not found")
            return False
        
        print("✅ Component retrieved successfully!")
        
        # Extract component details
        original_name = getattr(existing, 'name', 'Unknown')
        component_type = getattr(existing, 'type_', 'unknown')
        folder_id = getattr(existing, 'folder_id', None)
        folder_name = getattr(existing, 'folder_name', 'Unknown')
        
        # Set defaults if not provided
        updated_name = new_name or f"Updated {original_name}"
        updated_description = new_description or f"Updated {component_type} component via Python SDK"
        
        print(f"📋 Original: {original_name}")
        print(f"📝 New name: {updated_name}")
        print(f"📁 Folder: {folder_name} (ID: {folder_id})")
        
        # Build the update XML in the exact format that works (based on OpenAPI spec)
        xml = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<bns:Component
\txmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
\txmlns:bns="http://api.platform.boomi.com/" folderFullPath="{getattr(existing, 'folder_full_path', '')}" componentId="{component_id}" version="{getattr(existing, 'version', '')}" name="{updated_name}" type="{component_type}" createdDate="{getattr(existing, 'created_date', '')}" createdBy="{getattr(existing, 'created_by', '')}" modifiedDate="{getattr(existing, 'modified_date', '')}" modifiedBy="{getattr(existing, 'modified_by', '')}" deleted="{str(getattr(existing, 'deleted', False)).lower()}" currentVersion="{str(getattr(existing, 'current_version', False)).lower()}" folderName="{folder_name}" folderId="{folder_id}">
\t<bns:encryptedValues/>'''
        
        # Add description if provided
        if updated_description:
            xml += f'\n\t<bns:description>{updated_description}</bns:description>'
        
        # Preserve the existing object structure if it exists
        if hasattr(existing, 'object') and existing.object:
            xml += '\n\t<bns:object>'
            
            # Convert the object structure to XML
            obj_dict = existing.object if isinstance(existing.object, dict) else {}
            
            # Add the object content with proper indentation
            object_xml = dict_to_xml(obj_dict, 2)
            if object_xml:
                xml += '\n' + object_xml
            
            xml += '\n\t</bns:object>'
        
        # Close the component tag
        xml += '\n\t<bns:processOverrides/>\n</bns:Component>'
        
        print(f"\n🔄 Updating component...")
        
        # Perform the update
        result = sdk.component.update_component(component_id=component_id, request_body=xml)
        
        print("✅ Component updated successfully!")
        
        # Show update results
        updated_name_result = getattr(result, 'name', 'N/A')
        updated_version = getattr(result, 'version', 'N/A')
        updated_folder = getattr(result, 'folder_name', 'N/A')
        modified_date = getattr(result, 'modified_date', 'N/A')
        modified_by = getattr(result, 'modified_by', 'N/A')
        
        print(f"\n📊 Update Results:")
        print("=" * 50)
        print(f"  Updated Name: {updated_name_result}")
        print(f"  New Version: {updated_version}")
        print(f"  Folder: {updated_folder}")
        print(f"  Modified: {format_date(modified_date)} by {modified_by}")
        
        print(f"\n🎉 SUCCESS!")
        print(f"📍 Component '{updated_name_result}' updated to version {updated_version}")
        print(f"📁 Folder location preserved: {updated_folder}")
        
        return True
        
    except Exception as e:
        error_msg = str(e)
        print(f"❌ Component update failed: {error_msg}")
        
        # Provide helpful troubleshooting hints
        if "404" in error_msg or "not found" in error_msg.lower():
            print("🔍 Component not found - check the component ID")
        elif "403" in error_msg:
            print("🔍 Permission issue - check your API credentials and permissions")
        elif "400" in error_msg:
            print("🔍 Bad request - check component ID format or XML structure")
        elif "401" in error_msg:
            print("🔍 Authentication failed - verify your credentials")
        else:
            print("🔍 Check network connectivity and API endpoint availability")
            
        return False

def parse_arguments():
    """Parse command line arguments"""
    if len(sys.argv) < 2:
        return None, None, None
    
    component_id = sys.argv[1]
    new_name = None
    new_description = None
    
    # Parse optional arguments
    for arg in sys.argv[2:]:
        if arg.startswith('--name='):
            new_name = arg.split('=', 1)[1]
        elif arg.startswith('--desc='):
            new_description = arg.split('=', 1)[1]
    
    return component_id, new_name, new_description

def main():
    """Main entry point"""
    component_id, new_name, new_description = parse_arguments()
    
    if not component_id:
        print("❌ Error: Component ID is required")
        print("\nUsage:")
        print(f"  {sys.argv[0]} COMPONENT_ID [OPTIONS]")
        print("\nOptions:")
        print("  --name=NAME     New name for the component")
        print("  --desc=DESC     New description for the component")
        print("\nExamples:")
        print(f"  {sys.argv[0]} 112b4efe-b173-4258-9492-613ead7d52ce")
        print(f"  {sys.argv[0]} 112b4efe-b173-4258-9492-613ead7d52ce --name=\"Updated Process\"")
        print(f"  {sys.argv[0]} 112b4efe-b173-4258-9492-613ead7d52ce --name=\"New Name\" --desc=\"Updated description\"")
        print("\n💡 Use get_component.py to view component details")
        return
    
    print("🚀 Boomi SDK Example: Update Component")
    print("=" * 45)
    print()
    
    success = update_component(component_id, new_name, new_description)
    
    print(f"\n{'='*45}")
    if success:
        print("🌟 Component update completed successfully!")
    else:
        print("💥 Component update encountered issues")

if __name__ == "__main__":
    main()