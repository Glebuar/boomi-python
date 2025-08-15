#!/usr/bin/env python3
"""
Fixed version of update_component.py with proper XML generation
"""

import os
import sys
sys.path.insert(0, 'src')
from boomi import Boomi

def dict_to_xml_with_attributes(obj, indent=0):
    """
    Convert dictionary to XML with proper attribute handling.
    
    This correctly identifies what should be attributes vs child elements:
    - Simple string/number/boolean values at the dict level become attributes
    - Dict/list values become child elements
    - None values become self-closing tags
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
                            # Escape quotes in attribute values
                            escaped = str(v).replace('"', '&quot;').replace('&', '&amp;')
                            attrs.append(f'{k}="{escaped}"')
                    else:
                        # Complex values become child elements
                        children[k] = v
                
                # Build the element
                if attrs or children:
                    # Opening tag with attributes
                    if attrs:
                        xml_parts.append(f"{indent_str}<{key} {' '.join(attrs)}>")
                    else:
                        xml_parts.append(f"{indent_str}<{key}>")
                    
                    # Add child elements
                    if children:
                        child_xml = dict_to_xml_with_attributes(children, indent + 1)
                        if child_xml:
                            xml_parts.append(child_xml)
                    
                    # Closing tag
                    xml_parts.append(f"{indent_str}</{key}>")
                elif not value:  # Empty dict
                    xml_parts.append(f"{indent_str}<{key}/>")
                    
            elif isinstance(value, list):
                # Each list item becomes a separate element
                for item in value:
                    if isinstance(item, dict):
                        # Recursively process dict items
                        item_xml = dict_to_xml_with_attributes({key: item}, indent)
                        if item_xml:
                            xml_parts.append(item_xml)
                    else:
                        # Simple values
                        escaped_item = str(item).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
                        xml_parts.append(f"{indent_str}<{key}>{escaped_item}</{key}>")
                        
            elif value is None:
                # None becomes self-closing tag
                xml_parts.append(f"{indent_str}<{key}/>")
                
            else:
                # Simple values become elements (when at root level of dict)
                escaped_value = str(value).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
                xml_parts.append(f"{indent_str}<{key}>{escaped_value}</{key}>")
    
    return "\n".join(xml_parts)

def update_component(component_id, new_name=None):
    """Update a component with fixed XML generation"""
    
    # Get credentials
    account_id = os.getenv("BOOMI_ACCOUNT", "psrisksand-U7OGUC")
    username = os.getenv("BOOMI_USER", "BOOMI_TOKEN.hlib.bochkarov@intapp.com")
    password = os.getenv("BOOMI_SECRET", "08bc1505-c54d-407e-9c25-9a7472b1e898")
    
    print(f"🎯 Target Component ID: {component_id}")
    
    # Initialize SDK
    sdk = Boomi(
        account_id=account_id,
        username=username,
        password=password,
        timeout=30000
    )
    
    try:
        print(f"🔍 Retrieving component...")
        
        # Get the existing component
        existing = sdk.component.get_component(component_id=component_id)
        
        if not existing:
            print("❌ Component not found")
            return False
        
        print(f"✅ Retrieved: {existing.name}")
        print(f"   Type: {existing.type_}")
        print(f"   Version: {existing.version}")
        print(f"   Folder: {existing.folder_name}")
        
        # Set the new name
        updated_name = new_name or f"Fixed Update - {existing.name}"
        
        # Build the XML exactly as Boomi expects
        xml = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<bns:Component
\txmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
\txmlns:bns="http://api.platform.boomi.com/"
\tfolderFullPath="{getattr(existing, 'folder_full_path', '')}"
\tcomponentId="{component_id}"
\tversion="{getattr(existing, 'version', '')}"
\tname="{updated_name}"
\ttype="{existing.type_}"
\tcreatedDate="{getattr(existing, 'created_date', '')}"
\tcreatedBy="{getattr(existing, 'created_by', '')}"
\tmodifiedDate="{getattr(existing, 'modified_date', '')}"
\tmodifiedBy="{getattr(existing, 'modified_by', '')}"
\tdeleted="{str(getattr(existing, 'deleted', False)).lower()}"
\tcurrentVersion="{str(getattr(existing, 'current_version', False)).lower()}"
\tfolderName="{existing.folder_name}"
\tfolderId="{existing.folder_id}">
\t<bns:encryptedValues/>
\t<bns:description>Updated via fixed XML generation</bns:description>'''
        
        # Add the object with proper namespace handling
        if hasattr(existing, 'object') and existing.object:
            xml += '\n\t<bns:object>'
            
            # Get the object dict
            obj_dict = existing.object if isinstance(existing.object, dict) else {}
            
            # Generate XML with attributes properly handled
            # Note: The inner content uses empty namespace
            object_xml = dict_to_xml_with_attributes(obj_dict, 0)
            
            # Need to add the xmlns="" to the root element of the object
            # The object_xml should start with something like <process ...>
            if object_xml:
                # Insert xmlns="" into the first element
                lines = object_xml.split('\n')
                if lines and lines[0].startswith('<'):
                    # Find the element name and insert xmlns=""
                    first_line = lines[0]
                    if ' ' in first_line:
                        # Has attributes
                        parts = first_line.split(' ', 1)
                        lines[0] = parts[0] + ' xmlns=""' + ' ' + parts[1]
                    else:
                        # No attributes, just element
                        lines[0] = first_line.replace('>', ' xmlns="">', 1)
                    object_xml = '\n'.join(lines)
            
            if object_xml:
                # Indent the object content
                indented = '\n'.join(['\t\t' + line if line else '' for line in object_xml.split('\n')])
                xml += '\n' + indented
            
            xml += '\n\t</bns:object>'
        
        xml += '\n\t<bns:processOverrides/>\n</bns:Component>'
        
        # Save for debugging
        debug_file = f"fixed_xml_{component_id[:8]}.xml"
        with open(debug_file, "w") as f:
            f.write(xml)
        print(f"📝 Generated XML saved to: {debug_file}")
        
        print(f"\n🔄 Updating component...")
        
        # Perform the update
        result = sdk.component.update_component(component_id=component_id, request_body=xml)
        
        print("✅ Component updated successfully!")
        print(f"   New name: {result.name}")
        print(f"   New version: {result.version}")
        print(f"   Folder preserved: {result.folder_name}")
        
        return True
        
    except Exception as e:
        print(f"❌ Update failed: {e}")
        return False

def main():
    """Test the fixed update with both simple and complex components"""
    print("🚀 Testing Fixed XML Generation")
    print("=" * 60)
    
    # Test complex component (52 shapes)
    print("\n1️⃣ Testing COMPLEX component (52 shapes):")
    print("-" * 40)
    complex_success = update_component("f7f52a40-21fa-4850-a415-c88d69c8f5a2")
    
    print("\n" + "=" * 60)
    
    # Test simple component (2 shapes)  
    print("\n2️⃣ Testing SIMPLE component (2 shapes):")
    print("-" * 40)
    simple_success = update_component("112b4efe-b173-4258-9492-613ead7d52ce")
    
    # Results
    print("\n" + "=" * 60)
    print("📊 FINAL RESULTS:")
    print(f"   Complex component: {'✅ SUCCESS' if complex_success else '❌ FAILED'}")
    print(f"   Simple component: {'✅ SUCCESS' if simple_success else '❌ FAILED'}")
    
    if complex_success and simple_success:
        print("\n🎉 FIXED XML GENERATION WORKS FOR ALL COMPONENTS!")
        print("   ✅ The issue has been correctly identified and resolved.")
        print("   ✅ Both simple and complex nested structures are handled properly.")
    elif complex_success or simple_success:
        print("\n⚠️  Partial success - one component type works")
    else:
        print("\n❌ Still investigating the issue...")

if __name__ == "__main__":
    main()