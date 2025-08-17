#!/usr/bin/env python3
"""
Update Component XML

This example demonstrates how to update a component using XML/etree methods.

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET

Usage:
    python update_component_xml_single.py COMPONENT_ID --name "New Name"

Endpoint:
- component.update_component_etree
"""

import os
import sys
import xml.etree.ElementTree as ET
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

from boomi import Boomi

def main():
    if len(sys.argv) < 2:
        print("Usage: python update_component_xml_single.py COMPONENT_ID [--name 'New Name']")
        sys.exit(1)
    
    component_id = sys.argv[1]
    new_name = None
    
    # Parse simple name argument
    if len(sys.argv) >= 4 and sys.argv[2] == "--name":
        new_name = sys.argv[3]
    
    # Initialize SDK
    sdk = Boomi(
        account_id=os.getenv("BOOMI_ACCOUNT"),
        username=os.getenv("BOOMI_USER"),
        password=os.getenv("BOOMI_SECRET"),
        timeout=30000,
    )
    
    print(f"🔄 Updating component XML: {component_id}")
    
    try:
        # Create a simple XML element tree for update
        root = ET.Element("Component")
        root.set("id", component_id)
        
        if new_name:
            root.set("name", new_name)
            print(f"   Setting name to: {new_name}")
        
        # Update the component using etree
        response = sdk.component.update_component_etree(component_id, root)
        
        print("✅ Component XML updated successfully!")
        print(f"   Response: {response}")
        
    except Exception as e:
        print(f"❌ Error updating component XML: {str(e)}")

if __name__ == "__main__":
    main()