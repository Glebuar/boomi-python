#!/usr/bin/env python3
"""
Update Working Components

This example demonstrates how to update multiple components using the Boomi SDK.

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET

Usage:
    python update_working_components_single.py COMPONENT_ID1 COMPONENT_ID2 ...

Endpoint:
- component.update_component
"""

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

from boomi import Boomi

def main():
    if len(sys.argv) < 2:
        print("Usage: python update_working_components_single.py COMPONENT_ID1 [COMPONENT_ID2 ...]")
        sys.exit(1)
    
    component_ids = sys.argv[1:]
    
    # Initialize SDK
    sdk = Boomi(
        account_id=os.getenv("BOOMI_ACCOUNT"),
        username=os.getenv("BOOMI_USER"),
        password=os.getenv("BOOMI_SECRET"),
        timeout=30000,
    )
    
    print(f"🔄 Updating {len(component_ids)} component(s)...")
    
    for i, component_id in enumerate(component_ids, 1):
        print(f"\n{i}. Updating component: {component_id}")
        
        try:
            # Basic XML content for testing - in practice, provide actual XML
            xml_content = "<test>Updated component</test>"
            
            result = sdk.component.update_component(
                component_id=component_id, 
                request_body=xml_content
            )
            
            print(f"   ✅ Component {component_id} updated successfully")
            
        except Exception as e:
            print(f"   ❌ Error updating component {component_id}: {str(e)}")

if __name__ == "__main__":
    main()