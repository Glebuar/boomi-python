#!/usr/bin/env python3
"""
Query Component Environment Attachments

This example demonstrates how to query component-environment attachments.

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET

Usage:
    python query_component_attachments_single.py [--component COMPONENT_ID]

Endpoint:
- component_environment_attachment.query_component_environment_attachment
"""

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

from boomi import Boomi
from boomi.models import (
    ComponentEnvironmentAttachmentQueryConfig,
    ComponentEnvironmentAttachmentQueryConfigQueryFilter,
    ComponentEnvironmentAttachmentSimpleExpression,
    ComponentEnvironmentAttachmentSimpleExpressionOperator,
    ComponentEnvironmentAttachmentSimpleExpressionProperty
)

def main():
    component_id = None
    
    # Parse arguments
    if len(sys.argv) >= 3 and sys.argv[1] == "--component":
        component_id = sys.argv[2]
    
    # Initialize SDK
    sdk = Boomi(
        account_id=os.getenv("BOOMI_ACCOUNT"),
        username=os.getenv("BOOMI_USER"),
        password=os.getenv("BOOMI_SECRET"),
        timeout=30000,
    )
    
    print("🔍 Querying component-environment attachments...")
    
    try:
        if component_id:
            # Query attachments for specific component
            simple_expression = ComponentEnvironmentAttachmentSimpleExpression(
                operator=ComponentEnvironmentAttachmentSimpleExpressionOperator.EQUALS,
                property=ComponentEnvironmentAttachmentSimpleExpressionProperty.COMPONENT_ID,
                argument=[component_id]
            )
            query_filter = ComponentEnvironmentAttachmentQueryConfigQueryFilter(expression=simple_expression)
            query_config = ComponentEnvironmentAttachmentQueryConfig(query_filter=query_filter)
            print(f"   Filtering by component ID: {component_id}")
        else:
            # Query all attachments
            query_config = ComponentEnvironmentAttachmentQueryConfig()
        
        # Query component environment attachments
        result = sdk.component_environment_attachment.query_component_environment_attachment(
            query_config
        )
        
        # Process results
        attachments = []
        if hasattr(result, 'result') and result.result:
            attachments = result.result if isinstance(result.result, list) else [result.result]
        
        if attachments:
            print(f"✅ Found {len(attachments)} component-environment attachment(s):")
            for i, attachment in enumerate(attachments, 1):
                att_id = getattr(attachment, 'id_', 'N/A')
                comp_id = getattr(attachment, 'component_id', 'N/A')
                env_id = getattr(attachment, 'environment_id', 'N/A')
                
                print(f"{i:2}. Attachment ID: {att_id}")
                print(f"    Component ID: {comp_id}")
                print(f"    Environment ID: {env_id}")
        else:
            print("❌ No component-environment attachments found")
            
    except Exception as e:
        print(f"❌ Error querying attachments: {str(e)}")

if __name__ == "__main__":
    main()