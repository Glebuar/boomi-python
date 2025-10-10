#!/usr/bin/env python3
"""
Compare Component Versions

This example demonstrates how to compare different versions of a component.

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET

Usage:
    python compare_component_versions_single.py COMPONENT_ID VERSION1 VERSION2

Endpoint:
- component_diff_request.create_component_diff_request
"""

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

from boomi import Boomi
from boomi.models import ComponentDiffRequest

def main():
    if len(sys.argv) != 4:
        print("Usage: python compare_component_versions_single.py COMPONENT_ID VERSION1 VERSION2")
        sys.exit(1)
    
    component_id = sys.argv[1]
    version1 = sys.argv[2]
    version2 = sys.argv[3]
    
    # Initialize SDK
    sdk = Boomi(
        account_id=os.getenv("BOOMI_ACCOUNT"),
        username=os.getenv("BOOMI_USER"),
        password=os.getenv("BOOMI_SECRET"),
        timeout=30000,
    )
    
    print(f"🔍 Comparing component versions:")
    print(f"   Component ID: {component_id}")
    print(f"   Version 1: {version1}")
    print(f"   Version 2: {version2}")
    
    try:
        # Create component diff request
        # Note: version parameters should be integers
        diff_request = ComponentDiffRequest(
            component_id=component_id,
            source_version=int(version1),
            target_version=int(version2)
        )
        
        # Create the diff request
        result = sdk.component_diff_request.create_component_diff_request(
            diff_request
        )
        
        print("✅ Component version comparison completed!")
        print(f"   Diff result: {result}")
        
    except Exception as e:
        print(f"❌ Error comparing component versions: {str(e)}")

if __name__ == "__main__":
    main()