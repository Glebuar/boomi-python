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
    """Convert dictionary to XML matching Boomi's exact format.
    
    Key rules:
    1. Elements with only attributes and no children are self-closing
    2. Simple values at dict level become attributes  
    3. Complex values (dict/list) become child elements
    4. None/null values become self-closing empty elements
    """
    if obj is None:
        return ""
    
    xml_parts = []
    indent_str = "\t" * indent
    
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key.startswith('_'):  # Skip private attributes
                continue
                
            if isinstance(value, dict):
                # Separate attributes from child elements
                attrs = []
                children = {}
                
                for k, v in value.items():
                    if k.startswith('_'):
                        continue
                    # Simple values become attributes
                    if isinstance(v, (str, int, float, bool)) and v is not None:
                        if isinstance(v, bool):
                            attrs.append(f'{k}="{str(v).lower()}"')
                        else:
                            # Escape quotes and ampersands in attribute values
                            escaped = str(v).replace('&', '&amp;').replace('"', '&quot;')
                            attrs.append(f'{k}="{escaped}"')
                    else:
                        # Complex values become child elements
                        children[k] = v
                
                # Build the element
                if not children and attrs:
                    # Only attributes, no children - self-closing tag
                    xml_parts.append(f"{indent_str}<{key} {' '.join(attrs)}/>")
                elif children:
                    # Has children (with or without attributes)
                    if attrs:
                        xml_parts.append(f"{indent_str}<{key} {' '.join(attrs)}>")
                    else:
                        xml_parts.append(f"{indent_str}<{key}>")
                    
                    # Add child elements
                    child_xml = dict_to_xml(children, indent + 1)
                    if child_xml:
                        xml_parts.append(child_xml)
                    
                    # Closing tag
                    xml_parts.append(f"{indent_str}</{key}>")
                elif not value:
                    # Empty dict, no attributes
                    xml_parts.append(f"{indent_str}<{key}/>")
                else:
                    # Has no attrs and no children but is not empty (edge case)
                    xml_parts.append(f"{indent_str}<{key}/>")
                    
            elif isinstance(value, list):
                # Each list item becomes a separate element
                for item in value:
                    if isinstance(item, dict):
                        # Recursively process dict items in list
                        item_xml = dict_to_xml({key: item}, indent)
                        if item_xml:
                            xml_parts.append(item_xml)
                    else:
                        # Simple values in list
                        escaped_item = str(item).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
                        xml_parts.append(f"{indent_str}<{key}>{escaped_item}</{key}>")
                        
            elif value is None:
                # None becomes self-closing tag
                xml_parts.append(f"{indent_str}<{key}/>")
                
            else:
                # Simple values at root level become elements
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
        # Include branch attributes if they exist
        branch_attrs = ""
        if hasattr(existing, 'branch_name') and existing.branch_name:
            branch_attrs += f' branchName="{existing.branch_name}"'
        if hasattr(existing, 'branch_id') and existing.branch_id:
            branch_attrs += f' branchId="{existing.branch_id}"'
            
        xml = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<bns:Component
\txmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
\txmlns:bns="http://api.platform.boomi.com/" folderFullPath="{getattr(existing, 'folder_full_path', '')}" componentId="{component_id}" version="{getattr(existing, 'version', '')}" name="{updated_name}" type="{component_type}" createdDate="{getattr(existing, 'created_date', '')}" createdBy="{getattr(existing, 'created_by', '')}" modifiedDate="{getattr(existing, 'modified_date', '')}" modifiedBy="{getattr(existing, 'modified_by', '')}" deleted="{str(getattr(existing, 'deleted', False)).lower()}" currentVersion="{str(getattr(existing, 'current_version', False)).lower()}" folderName="{folder_name}" folderId="{folder_id}"{branch_attrs}>
\t<bns:encryptedValues/>'''
        
        # Add description if provided
        if updated_description:
            xml += f'\n\t<bns:description>{updated_description}</bns:description>'
        
        # Preserve the existing object structure if it exists
        if hasattr(existing, 'object') and existing.object:
            xml += '\n\t<bns:object>'
            
            # Get the object dict
            obj_dict = existing.object if isinstance(existing.object, dict) else {}
            
            # Generate XML with correct format
            object_xml = dict_to_xml(obj_dict, 0)
            
            # Add xmlns="" to the root element of the object content
            if object_xml:
                lines = object_xml.split('\n')
                if lines and lines[0].startswith('<'):
                    first_line = lines[0]
                    # Insert xmlns="" after the element name
                    if ' ' in first_line and not '>' in first_line.split(' ', 1)[0]:
                        # Has attributes - insert after element name
                        parts = first_line.split(' ', 1)
                        lines[0] = parts[0] + ' xmlns=""' + ' ' + parts[1]
                    elif first_line.endswith('/>'):
                        # Self-closing with no attributes
                        lines[0] = first_line.replace('/>', ' xmlns=""/>', 1)
                    else:
                        # Opening tag with no attributes
                        lines[0] = first_line.replace('>', ' xmlns="">', 1)
                    object_xml = '\n'.join(lines)
            
            # Indent the object content properly
            if object_xml:
                indented_lines = []
                for line in object_xml.split('\n'):
                    if line.strip():  # Skip empty lines
                        indented_lines.append('\t\t' + line)
                xml += '\n' + '\n'.join(indented_lines)
            
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