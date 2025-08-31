#!/usr/bin/env python3
"""
Update Component (Fixed Version)

This example demonstrates how to update a component using the Boomi SDK.
Uses direct API call to get XML since SDK model doesn't expose it.

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET

Usage:
    python update_component_fixed.py COMPONENT_ID

Endpoint:
- component.get_component (for metadata)
- Direct API call for XML retrieval  
- component.update_component
"""

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

from boomi import Boomi
import xml.etree.ElementTree as ET
import time
import requests
import base64

def main():
    if len(sys.argv) != 2:
        print("Usage: python update_component_fixed.py COMPONENT_ID")
        sys.exit(1)
    
    component_id = sys.argv[1]
    account_id = os.getenv("BOOMI_ACCOUNT")
    username = os.getenv("BOOMI_USER")
    password = os.getenv("BOOMI_SECRET")
    
    # Initialize SDK
    sdk = Boomi(
        account_id=account_id,
        username=username,
        password=password,
        timeout=30000,
    )
    
    print(f"🔄 Updating component: {component_id}")
    
    try:
        # First, get component metadata via SDK
        print("📥 Retrieving component metadata...")
        component = sdk.component.get_component(component_id=component_id)
        
        if not component:
            print("❌ Component not found")
            return
        
        print(f"   Found: {getattr(component, 'name', 'Unknown')}")
        print(f"   Type: {getattr(component, 'type_', 'Unknown')}")
        
        # Get the actual XML via direct API call (SDK doesn't expose raw XML)
        print("📥 Retrieving component XML...")
        url = f"https://api.boomi.com/api/rest/v1/{account_id}/Component/{component_id}"
        auth = base64.b64encode(f"{username}:{password}".encode()).decode()
        headers = {
            "Authorization": f"Basic {auth}",
            "Accept": "application/xml",
            "Content-Type": "application/xml"
        }
        
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"❌ Failed to get component XML: {response.status_code}")
            return
        
        xml_content = response.text
        
        # Parse and modify the XML
        try:
            root = ET.fromstring(xml_content)
            
            # Update the description attribute
            current_desc = root.get('description', '')
            new_desc = f"Updated via SDK example at {int(time.time())}"
            root.set('description', new_desc)
            
            # Convert back to XML string
            modified_xml = ET.tostring(root, encoding='unicode')
            
            print(f"   Previous description: {current_desc or '(none)'}")
            print(f"   New description: {new_desc}")
            
        except ET.ParseError as e:
            print(f"❌ Failed to parse component XML: {e}")
            return
        
        print("📤 Updating component with modified XML...")
        
        # Update the component with the modified XML via SDK
        result = sdk.component.update_component(
            component_id=component_id, 
            request_body=modified_xml
        )
        
        print("✅ Component updated successfully!")
        print(f"   Component ID: {component_id}")
        
        # Verify the update
        print("🔍 Verifying update...")
        updated_component = sdk.component.get_component(component_id=component_id)
        if updated_component:
            print(f"   Name: {getattr(updated_component, 'name', 'Unknown')}")
            print(f"   Modified by: {getattr(updated_component, 'modified_by', 'Unknown')}")
        
    except Exception as e:
        print(f"❌ Error updating component: {str(e)}")

if __name__ == "__main__":
    main()