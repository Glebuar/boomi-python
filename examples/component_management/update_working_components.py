#!/usr/bin/env python3
"""
Boomi Component Update Examples - Working Validation
===================================================
Validated update examples for component types that exist in the account.
"""

import os
from dotenv import load_dotenv
import sys
sys.path.insert(0, '../src')
from boomi import Boomi

load_dotenv()

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
        # Find first current version, non-deleted component
        for comp in components.result:
            if comp.deleted == 'false' and comp.current_version == 'true':
                return comp.component_id, comp.name
    return None, None

# Process Component Update
def update_process():
    """Update a process component with enhanced functionality"""
    sdk = get_sdk()
    component_id, original_name = find_component_by_type(sdk, "process")
    if not component_id:
        print("❌ No suitable process component found")
        return False
    
    xml = f'''<Component xmlns="http://api.platform.boomi.com/"
           componentId="{component_id}"
           name="Updated {original_name}"
           type="process">
      <description>Updated process with enhanced logging via Python SDK</description>
      <object>
        <process xmlns="" allowSimultaneous="false" enableUserLog="true">
          <shapes>
            <shape image="start" name="start" shapetype="start" userlabel="Updated Start" x="100" y="100">
              <configuration><noaction/></configuration>
              <dragpoints><dragpoint name="start.drag" toShape="message" x="250" y="126"/></dragpoints>
            </shape>
            <shape image="message_icon" name="message" shapetype="message" userlabel="SDK Update Message" x="300" y="100">
              <configuration>
                <message combined="false">
                  <msgTxt>Component updated via Boomi Python SDK!</msgTxt>
                  <msgParameters/>
                </message>
              </configuration>
              <dragpoints><dragpoint name="message.drag" toShape="stop" x="450" y="126"/></dragpoints>
            </shape>
            <shape image="stop_icon" name="stop" shapetype="stop" userlabel="Updated Stop" x="500" y="100">
              <configuration><stop continue="true"/></configuration>
              <dragpoints/>
            </shape>
          </shapes>
        </process>
      </object>
    </Component>'''
    
    try:
        result = sdk.component.update_component(component_id=component_id, request_body=xml)
        print(f"✅ Process updated: {getattr(result, 'name', 'Success')} (v{getattr(result, 'version', '?')})")
        return True
    except Exception as e:
        print(f"❌ Process update failed: {e}")
        return False

# Map Transform Component Update  
def update_map():
    """Update a map transform component"""
    sdk = get_sdk()
    component_id, original_name = find_component_by_type(sdk, "transform.map")
    if not component_id:
        print("❌ No suitable map component found")
        return False
    
    # Note: Map components require complex XML structure - this is a simplified example
    xml = f'''<Component xmlns="http://api.platform.boomi.com/"
           componentId="{component_id}"
           name="Updated {original_name}"
           type="transform.map">
      <description>Updated data mapping transformation via Python SDK</description>
    </Component>'''
    
    try:
        result = sdk.component.update_component(component_id=component_id, request_body=xml)
        print(f"✅ Map updated: {getattr(result, 'name', 'Success')} (v{getattr(result, 'version', '?')})")
        return True
    except Exception as e:
        print(f"❌ Map update failed: {e}")
        return False

# Database Profile Update
def update_db_profile():
    """Update a database profile component"""
    sdk = get_sdk()
    component_id, original_name = find_component_by_type(sdk, "profile.db")
    if not component_id:
        print("❌ No suitable database profile found")
        return False
    
    xml = f'''<Component xmlns="http://api.platform.boomi.com/"
           componentId="{component_id}"
           name="Updated {original_name}"
           type="profile.db">
      <description>Updated database profile via Python SDK</description>
    </Component>'''
    
    try:
        result = sdk.component.update_component(component_id=component_id, request_body=xml)
        print(f"✅ DB Profile updated: {getattr(result, 'name', 'Success')} (v{getattr(result, 'version', '?')})")
        return True
    except Exception as e:
        print(f"❌ DB Profile update failed: {e}")
        return False

# XML Profile Update
def update_xml_profile():
    """Update an XML profile component"""
    sdk = get_sdk()
    component_id, original_name = find_component_by_type(sdk, "profile.xml")
    if not component_id:
        print("❌ No suitable XML profile found")
        return False
    
    xml = f'''<Component xmlns="http://api.platform.boomi.com/"
           componentId="{component_id}"
           name="Updated {original_name}"
           type="profile.xml">
      <description>Updated XML profile via Python SDK</description>
    </Component>'''
    
    try:
        result = sdk.component.update_component(component_id=component_id, request_body=xml)
        print(f"✅ XML Profile updated: {getattr(result, 'name', 'Success')} (v{getattr(result, 'version', '?')})")
        return True
    except Exception as e:
        print(f"❌ XML Profile update failed: {e}")
        return False

# JSON Profile Update
def update_json_profile():
    """Update a JSON profile component"""
    sdk = get_sdk()
    component_id, original_name = find_component_by_type(sdk, "profile.json")
    if not component_id:
        print("❌ No suitable JSON profile found")
        return False
    
    xml = f'''<Component xmlns="http://api.platform.boomi.com/"
           componentId="{component_id}"
           name="Updated {original_name}"
           type="profile.json">
      <description>Updated JSON profile via Python SDK</description>
    </Component>'''
    
    try:
        result = sdk.component.update_component(component_id=component_id, request_body=xml)
        print(f"✅ JSON Profile updated: {getattr(result, 'name', 'Success')} (v{getattr(result, 'version', '?')})")
        return True
    except Exception as e:
        print(f"❌ JSON Profile update failed: {e}")
        return False

def main():
    """Run validated component update examples"""
    print("🔄 Boomi Component Update Examples - Validated")
    print("=" * 50)
    
    # Test components that exist in the account
    updates = [
        ("Process", update_process),
        ("Map Transform", update_map), 
        ("Database Profile", update_db_profile),
        ("XML Profile", update_xml_profile),
        ("JSON Profile", update_json_profile),
    ]
    
    success_count = 0
    for name, func in updates:
        print(f"\n🔄 Testing {name} update...")
        try:
            if func():
                success_count += 1
        except Exception as e:
            print(f"❌ {name} update error: {e}")
    
    print(f"\n📊 Results: {success_count}/{len(updates)} successful updates")
    
    if success_count > 0:
        print("🎉 Component update functionality validated!")
        print("The SDK can successfully update Boomi components.")
    else:
        print("⚠️  No updates succeeded - check credentials and component availability.")

if __name__ == "__main__":
    main()