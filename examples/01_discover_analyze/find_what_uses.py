#!/usr/bin/env python3
"""
Find What Uses Component

This example demonstrates how to find what other components use a specific component.

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET

Usage:
    python find_what_uses_single.py COMPONENT_ID

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
    if len(sys.argv) != 2:
        print("Usage: python find_what_uses_single.py COMPONENT_ID")
        sys.exit(1)
    
    component_id = sys.argv[1]
    
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
            property=ComponentReferenceSimpleExpressionProperty.TO_COMPONENT_ID,
            argument=[component_id]
        )
        
        query_filter = ComponentReferenceQueryConfigQueryFilter(expression=simple_expression)
        query_config = ComponentReferenceQueryConfig(query_filter=query_filter)
        
        # Query component references
        result = sdk.component_reference.query_component_reference(request_body=query_config)
        
        # Process results
        references = []
        if hasattr(result, 'result') and result.result:
            references = result.result if isinstance(result.result, list) else [result.result]
        
        if references:
            print(f"✅ Found {len(references)} component(s) that use this component:")
            for i, ref in enumerate(references, 1):
                from_comp_id = getattr(ref, 'from_component_id', 'N/A')
                to_comp_id = getattr(ref, 'to_component_id', 'N/A')
                
                print(f"{i:2}. Component {from_comp_id} uses {to_comp_id}")
        else:
            print("❌ No components found that use this component")
            
    except Exception as e:
        print(f"❌ Error finding component references: {str(e)}")

if __name__ == "__main__":
    main()