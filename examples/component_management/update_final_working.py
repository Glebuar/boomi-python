#!/usr/bin/env python3
"""
Boomi Component Update Examples - Final Working Solution
======================================================
Updates components by preserving their exact object structure.
"""

import os
import sys
sys.path.insert(0, '../../src')
from boomi import Boomi

def get_sdk():
    return Boomi(
        account_id=os.getenv("BOOMI_ACCOUNT"),
        username=os.getenv("BOOMI_USER"), 
        password=os.getenv("BOOMI_SECRET")
    )

def find_component_by_type(sdk, component_type):
    """Find first current version, non-deleted component of given type"""
    from boomi.models import (
        ComponentMetadataQueryConfig,
        ComponentMetadataQueryConfigQueryFilter,
        ComponentMetadataSimpleExpression,
        ComponentMetadataSimpleExpressionOperator,
        ComponentMetadataSimpleExpressionProperty
    )
    
    expression = ComponentMetadataSimpleExpression(
        operator=ComponentMetadataSimpleExpressionOperator.EQUALS,
        property=ComponentMetadataSimpleExpressionProperty.TYPE,
        argument=[component_type]
    )
    
    query_filter = ComponentMetadataQueryConfigQueryFilter(expression=expression)
    query_config = ComponentMetadataQueryConfig(query_filter=query_filter)
    
    components = sdk.component_metadata.query_component_metadata(request_body=query_config)
    if hasattr(components, 'result') and components.result:
        for comp in components.result:
            if comp.deleted == 'false' and comp.current_version == 'true':
                return comp.component_id, comp.name, comp.folder_id
    return None, None, None

def dict_to_xml(obj, indent=0):
    """Convert dictionary/object structure to XML string"""
    if obj is None:
        return ""
    
    xml_parts = []
    indent_str = "  " * indent
    
    if isinstance(obj, dict):
        for key, value in obj.items():
            if isinstance(value, dict):
                if value:  # Non-empty dict
                    xml_parts.append(f"{indent_str}<{key}>")
                    xml_parts.append(dict_to_xml(value, indent + 1))
                    xml_parts.append(f"{indent_str}</{key}>")
                else:  # Empty dict
                    xml_parts.append(f"{indent_str}<{key}/>")
            elif isinstance(value, list):
                for item in value:
                    xml_parts.append(f"{indent_str}<{key}>")
                    if isinstance(item, dict):
                        xml_parts.append(dict_to_xml(item, indent + 1))
                    else:
                        xml_parts.append(f"{indent_str}  {item}")
                    xml_parts.append(f"{indent_str}</{key}>")
            elif value is None:
                xml_parts.append(f"{indent_str}<{key}/>")
            else:
                # Escape XML special characters
                escaped_value = str(value).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
                xml_parts.append(f"{indent_str}<{key}>{escaped_value}</{key}>")
    
    return "\n".join(xml_parts)

def update_component_generic(component_type, display_name):
    """Generic component update that preserves exact structure"""
    sdk = get_sdk()
    component_id, original_name, folder_id = find_component_by_type(sdk, component_type)
    
    if not component_id:
        print(f"❌ No suitable {component_type} component found")
        return False
    
    try:
        # Get the existing component with its complete structure
        existing = sdk.component.get_component(component_id=component_id)
        
        # Start building the XML
        xml_parts = [
            f'<Component xmlns="http://api.platform.boomi.com/"',
            f'           componentId="{component_id}"',
            f'           name="Updated {original_name}"',
            f'           type="{component_type}"',
            f'           folderId="{folder_id}">',
            f'      <description>Updated {component_type} via Python SDK</description>'
        ]
        
        # Add the object structure if it exists
        if hasattr(existing, 'object') and existing.object:
            xml_parts.append('      <object>')
            
            # Convert the object structure to XML
            if hasattr(existing.object, '__dict__'):
                # If it's a model object, get its dictionary representation
                obj_dict = existing.object.__dict__
            elif isinstance(existing.object, dict):
                obj_dict = existing.object
            else:
                obj_dict = {'content': str(existing.object)}
            
            # Add the object content with proper indentation
            object_xml = dict_to_xml(obj_dict, 4)
            if object_xml:
                xml_parts.append("        " + object_xml.replace("\n", "\n        "))
            
            xml_parts.append('      </object>')
        
        xml_parts.append('    </Component>')
        
        xml = '\n'.join(xml_parts)
        
        # Try the update
        result = sdk.component.update_component(component_id=component_id, request_body=xml)
        
        print(f"✅ {display_name} updated: {getattr(result, 'name', 'Success')} (v{getattr(result, 'version', '?')})")
        print(f"📁 Folder preserved: {getattr(result, 'folder_name', 'Unknown')}")
        return True
        
    except Exception as e:
        print(f"❌ {display_name} update failed: {e}")
        return False

def main():
    """Test component updates with structure preservation"""
    print("🔄 Final Component Update Test - Structure Preservation")
    print("=" * 60)
    
    # Test key component types
    updates = [
        ("process", "Process"),
        ("script.processing", "Processing Script"),
        ("connector-action", "Connector Action"),
        ("crossref", "Cross Reference"),
        ("profile.json", "JSON Profile"),
    ]
    
    success_count = 0
    for comp_type, display_name in updates:
        print(f"\n🔄 Testing {display_name} update...")
        try:
            if update_component_generic(comp_type, display_name):
                success_count += 1
        except Exception as e:
            print(f"❌ {display_name} update error: {e}")
    
    print(f"\n📊 FINAL RESULTS: {success_count}/{len(updates)} successful updates")
    
    if success_count == len(updates):
        print("🎉 ALL COMPONENT TYPES CAN BE UPDATED!")
        print("🏆 Structure preservation approach works for all components!")
    elif success_count > 0:
        print(f"🎉 {success_count} component types working with structure preservation!")
        print("📈 Significant improvement over basic XML approach!")
    else:
        print("⚠️  Structure preservation needs further refinement")
    
    return success_count

if __name__ == "__main__":
    main()