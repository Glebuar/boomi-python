#!/usr/bin/env python3
"""
Update Component

This example demonstrates how to update a component using the Boomi SDK.

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET

Usage:
    python update_component_clean.py COMPONENT_ID

Endpoint:
- component.update_component
"""

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

from boomi import Boomi

def main():
    if len(sys.argv) != 2:
        print("Usage: python update_component_clean.py COMPONENT_ID")
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
        # Simple XML for testing - in practice, provide actual component XML
        xml_content = "<test>Updated component content</test>"
        
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