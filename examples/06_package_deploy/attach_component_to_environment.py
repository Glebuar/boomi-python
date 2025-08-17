#!/usr/bin/env python3
"""
Create Component Environment Attachment

This example demonstrates how to attach a component to an environment.

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET

Usage:
    python create_component_environment_attachment.py COMPONENT_ID ENVIRONMENT_ID

Endpoint:
- component_environment_attachment.create_component_environment_attachment
"""

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

from boomi import Boomi
from boomi.models import ComponentEnvironmentAttachment

def main():
    if len(sys.argv) != 3:
        print("Usage: python create_component_environment_attachment.py COMPONENT_ID ENVIRONMENT_ID")
        sys.exit(1)
    
    component_id = sys.argv[1]
    environment_id = sys.argv[2]
    
    # Initialize SDK
    sdk = Boomi(
        account_id=os.getenv("BOOMI_ACCOUNT"),
        username=os.getenv("BOOMI_USER"),
        password=os.getenv("BOOMI_SECRET"),
        timeout=30000,
    )
    
    print(f"🔗 Creating component-environment attachment...")
    print(f"   Component ID: {component_id}")
    print(f"   Environment ID: {environment_id}")
    
    try:
        # Create the attachment
        attachment_request = ComponentEnvironmentAttachment(
            component_id=component_id,
            environment_id=environment_id
        )
        
        result = sdk.component_environment_attachment.create_component_environment_attachment(
            attachment_request
        )
        
        print("✅ Component attached to environment successfully!")
        print(f"   Attachment result: {result}")
        
    except Exception as e:
        print(f"❌ Error creating attachment: {str(e)}")
        if hasattr(e, 'status'):
            if e.status == 409:
                print("   Component may already be attached to this environment")

if __name__ == "__main__":
    main()