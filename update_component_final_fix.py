#!/usr/bin/env python3
"""
Final fixed version with correct XML generation that matches Boomi's exact format
"""

import os
import sys
sys.path.insert(0, 'src')
from boomi import Boomi

def dict_to_xml_boomi_format(obj, indent=0):
    """
    Convert dictionary to XML matching Boomi's exact format.
    
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
                    child_xml = dict_to_xml_boomi_format(children, indent + 1)
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
                        item_xml = dict_to_xml_boomi_format({key: item}, indent)
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

def update_component_with_fix(component_id, new_name=None):
    """Update a component with the final fixed XML generation"""
    
    # Get credentials
    account_id = os.getenv("BOOMI_ACCOUNT", "psrisksand-U7OGUC")
    username = os.getenv("BOOMI_USER", "BOOMI_TOKEN.hlib.bochkarov@intapp.com")
    password = os.getenv("BOOMI_SECRET", "08bc1505-c54d-407e-9c25-9a7472b1e898")
    
    print(f"🎯 Component ID: {component_id}")
    
    # Initialize SDK
    sdk = Boomi(
        account_id=account_id,
        username=username,
        password=password,
        timeout=30000
    )
    
    try:
        # Get the existing component
        existing = sdk.component.get_component(component_id=component_id)
        
        if not existing:
            print("❌ Component not found")
            return False
        
        print(f"✅ Retrieved: {existing.name}")
        print(f"   Type: {existing.type_}")
        print(f"   Version: {existing.version}")
        
        # Set the new name
        updated_name = new_name or f"SDK Fix Validated - {existing.name}"
        
        # Build the XML header exactly as Boomi expects
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
\t<bns:description>Component update issue #3 - XML generation fix validated</bns:description>'''
        
        # Add the object with proper formatting
        if hasattr(existing, 'object') and existing.object:
            xml += '\n\t<bns:object>'
            
            # Get the object dict
            obj_dict = existing.object if isinstance(existing.object, dict) else {}
            
            # Generate XML with correct format
            object_xml = dict_to_xml_boomi_format(obj_dict, 0)
            
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
        
        xml += '\n\t<bns:processOverrides/>\n</bns:Component>'
        
        # Save for inspection
        debug_file = f"final_fix_{component_id[:8]}.xml"
        with open(debug_file, "w") as f:
            f.write(xml)
        print(f"📝 XML saved to: {debug_file}")
        
        print(f"🔄 Updating...")
        
        # Perform the update
        result = sdk.component.update_component(component_id=component_id, request_body=xml)
        
        print(f"✅ SUCCESS! Updated to version {result.version}")
        print(f"   Name: {result.name}")
        print(f"   Folder: {result.folder_name}")
        
        return True
        
    except Exception as e:
        print(f"❌ Failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Test the final fix with both simple and complex components"""
    print("🚀 FINAL FIX - Issue #3 XML Generation Resolution")
    print("=" * 60)
    
    results = []
    
    # Test 1: Complex component (52 shapes)
    print("\n1️⃣ COMPLEX Component (52 shapes):")
    print("-" * 40)
    complex_id = "f7f52a40-21fa-4850-a415-c88d69c8f5a2"
    complex_success = update_component_with_fix(complex_id)
    results.append(("Complex (52 shapes)", complex_success))
    
    print("\n" + "=" * 60)
    
    # Test 2: Simple component (2 shapes)  
    print("\n2️⃣ SIMPLE Component (2 shapes):")
    print("-" * 40)
    simple_id = "112b4efe-b173-4258-9492-613ead7d52ce"
    simple_success = update_component_with_fix(simple_id)
    results.append(("Simple (2 shapes)", simple_success))
    
    # Final results
    print("\n" + "=" * 60)
    print("📊 ISSUE #3 RESOLUTION RESULTS:")
    print("-" * 40)
    
    for name, success in results:
        status = "✅ WORKING" if success else "❌ FAILED"
        print(f"   {name}: {status}")
    
    all_success = all(r[1] for r in results)
    
    if all_success:
        print("\n🎉 ISSUE #3 RESOLVED!")
        print("✅ Root cause: dict_to_xml incorrectly handled XML attributes")
        print("✅ Solution: Proper XML generation with self-closing tags for attribute-only elements")
        print("✅ Validation: Both simple and complex components update successfully")
    else:
        print("\n⚠️  Issue still under investigation...")

if __name__ == "__main__":
    main()