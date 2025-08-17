#!/usr/bin/env python3
"""
Update Components (Batch)

This example demonstrates how to update multiple components in batch using the Boomi SDK.

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET

Usage:
    python update_components_single.py COMPONENT_ID1 COMPONENT_ID2 ...

Endpoint:
- component.update_component
"""

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

from boomi import Boomi

def main():
    if len(sys.argv) < 2:
        print("Usage: python update_components_single.py COMPONENT_ID1 [COMPONENT_ID2 ...]")
        sys.exit(1)
    
    component_ids = sys.argv[1:]
    
    # Initialize SDK
    sdk = Boomi(
        account_id=os.getenv("BOOMI_ACCOUNT"),
        username=os.getenv("BOOMI_USER"),
        password=os.getenv("BOOMI_SECRET"),
        timeout=30000,
    )
    
    print(f"🔄 Batch updating {len(component_ids)} component(s)...")
    
    success_count = 0
    
    for i, component_id in enumerate(component_ids, 1):
        print(f"\n{i}/{len(component_ids)}. Updating component: {component_id}")
        
        try:
            # Basic XML content for testing - in practice, provide actual XML
            xml_content = f"<test>Batch updated component {i}</test>"
            
            result = sdk.component.update_component(
                component_id=component_id, 
                request_body=xml_content
            )
            
            print(f"   ✅ Success")
            success_count += 1
            
        except Exception as e:
            print(f"   ❌ Error: {str(e)}")
    
    print(f"\n📊 Batch update complete: {success_count}/{len(component_ids)} successful")

if __name__ == "__main__":
    main()