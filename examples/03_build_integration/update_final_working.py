#!/usr/bin/env python3
"""
Update Component (Simple)

This example demonstrates how to update a component using the Boomi SDK.

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET

Usage:
    python update_component_simple.py COMPONENT_ID XML_CONTENT

Endpoint:
- component.update_component
"""

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

from boomi import Boomi

def main():
    if len(sys.argv) != 3:
        print("Usage: python update_component_simple.py COMPONENT_ID XML_CONTENT")
        sys.exit(1)
    
    component_id = sys.argv[1]
    xml_content = sys.argv[2]
    
    # Initialize SDK
    sdk = Boomi(
        account_id=os.getenv("BOOMI_ACCOUNT"),
        username=os.getenv("BOOMI_USER"),
        password=os.getenv("BOOMI_SECRET"),
        timeout=30000,
    )
    
    print(f"🔄 Updating component: {component_id}")
    
    try:
        # Update the component
        result = sdk.component.update_component(
            component_id=component_id, 
            request_body=xml_content
        )
        
        print("✅ Component updated successfully!")
        print(f"   Result: {result}")
        
    except Exception as e:
        print(f"❌ Error updating component: {str(e)}")

if __name__ == "__main__":
    main()