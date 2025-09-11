#!/usr/bin/env python3
"""
Find What Uses Component

This example demonstrates how to find what other components use a specific component.

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET

Usage:
    python find_what_uses.py COMPONENT_ID

Endpoint:
- component_reference.query_component_reference
"""

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

from boomi import Boomi
from boomi.models import (
    ComponentReferenceQueryConfig,
    ComponentReferenceQueryConfigQueryFilter,
    ComponentReferenceSimpleExpression,
    ComponentReferenceSimpleExpressionOperator,
    ComponentReferenceSimpleExpressionProperty
)

def main():
    if len(sys.argv) > 1:
        component_id = sys.argv[1]
    else:
        component_id = "0864f99a-917f-457d-abc6-2762c0bb9b88"  # Test Date Data Map component
        print(f"ℹ️ No component_id provided, using default: {component_id}")
        print("💡 To use a different component, run: python find_what_uses.py YOUR_COMPONENT_ID")
        print("💡 IMPORTANT: Replace this component ID with your own component ID for production use")
    
    # Initialize SDK
    sdk = Boomi(
        account_id=os.getenv("BOOMI_ACCOUNT"),
        username=os.getenv("BOOMI_USER"),
        password=os.getenv("BOOMI_SECRET"),
        timeout=30000,
    )
    
    print(f"🔍 Finding what uses component: {component_id}")
    
    try:
        # Query for components that reference this component
        simple_expression = ComponentReferenceSimpleExpression(
            operator=ComponentReferenceSimpleExpressionOperator.EQUALS,
            property=ComponentReferenceSimpleExpressionProperty.COMPONENTID,
            argument=[component_id]
        )
        
        query_filter = ComponentReferenceQueryConfigQueryFilter(expression=simple_expression)
        query_config = ComponentReferenceQueryConfig(query_filter=query_filter)
        
        # Query component references
        result = sdk.component_reference.query_component_reference(request_body=query_config)
        
        # Process results
        component_references = []
        if hasattr(result, 'result') and result.result:
            component_references = result.result if isinstance(result.result, list) else [result.result]
        
        # Extract all references from the ComponentReference objects
        all_references = []
        for comp_ref in component_references:
            if hasattr(comp_ref, 'references') and comp_ref.references:
                all_references.extend(comp_ref.references)
        
        if all_references:
            print(f"✅ Found {len(all_references)} component(s) that use this component:")
            for i, ref in enumerate(all_references, 1):
                parent_comp_id = getattr(ref, 'parent_component_id', 'N/A')
                used_comp_id = getattr(ref, 'component_id', 'N/A')
                ref_type = getattr(ref, 'type_', 'N/A')
                
                print(f"{i:2}. Component {parent_comp_id} uses {used_comp_id} (type: {ref_type})")
        else:
            print("❌ No components found that use this component")
            
    except Exception as e:
        print(f"❌ Error finding component references: {str(e)}")

if __name__ == "__main__":
    main()