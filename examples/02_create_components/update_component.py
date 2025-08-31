#!/usr/bin/env python3
"""
Update Component

This example demonstrates how to update a component using the Boomi SDK.

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET

Usage:
    python update_component.py COMPONENT_ID

Endpoint:
- component.get_component
- component.update_component
"""

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

from boomi import Boomi
import xml.etree.ElementTree as ET
import time

def main():
    if len(sys.argv) != 2:
        print("Usage: python update_component.py COMPONENT_ID")
        sys.exit(1)
    
    component_id = sys.argv[1]
    
    # Initialize SDK
    sdk = Boomi(
        account_id=os.getenv("BOOMI_ACCOUNT"),
        username=os.getenv("BOOMI_USER"),
        password=os.getenv("BOOMI_SECRET"),
        timeout=30000,
    )
    
    print(f"🔄 Updating component: {component_id}")
    
    try:
        # First, get the component to retrieve its current XML structure
        print("📥 Retrieving component to get proper XML structure...")
        component = sdk.component.get_component(component_id=component_id)
        
        if not component:
            print("❌ Component not found")
            return
        
        print(f"   Found: {getattr(component, 'name', 'Unknown')}")
        
        # The component object contains the XML structure
        # For this example, we'll just update the description in the XML
        
        # Get the XML content from the component
        xml_content = None
        if hasattr(component, 'object_') and component.object_:
            xml_content = component.object_
        elif hasattr(component, 'xml') and component.xml:
            xml_content = component.xml
        else:
            # Try to get raw response
            print("❌ Component doesn't have accessible XML structure")
            return
        
        # Parse and modify the XML
        try:
            root = ET.fromstring(xml_content)
            
            # Update the description attribute
            current_desc = root.get('description', '')
            new_desc = f"Updated via SDK at {int(time.time())}"
            root.set('description', new_desc)
            
            # Convert back to XML string
            modified_xml = ET.tostring(root, encoding='unicode')
            
            print(f"   Previous description: {current_desc or '(none)'}")
            print(f"   New description: {new_desc}")
            
        except ET.ParseError as e:
            print(f"❌ Failed to parse component XML: {e}")
            return
        
        print("📤 Updating component with modified XML...")
        
        # Update the component with the modified XML
        result = sdk.component.update_component(
            component_id=component_id, 
            request_body=modified_xml
        )
        
        print("✅ Component updated successfully!")
        print(f"   Component ID: {component_id}")
        
    except Exception as e:
        print(f"❌ Error updating component: {str(e)}")

if __name__ == "__main__":
    main()