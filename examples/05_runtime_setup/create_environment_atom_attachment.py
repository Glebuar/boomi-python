#!/usr/bin/env python3
"""
Create Environment Atom Attachment

This example demonstrates how to create an attachment between a runtime (atom) and environment.

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET

Usage:
    python create_environment_atom_attachment.py ATOM_ID ENVIRONMENT_ID

Endpoint:
- environment_atom_attachment.create_environment_atom_attachment
"""

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

from boomi import Boomi
from boomi.models import EnvironmentAtomAttachment

def main():
    if len(sys.argv) != 3:
        print("Usage: python create_environment_atom_attachment.py ATOM_ID ENVIRONMENT_ID")
        sys.exit(1)
    
    atom_id = sys.argv[1]
    environment_id = sys.argv[2]
    
    # Initialize SDK
    sdk = Boomi(
        account_id=os.getenv("BOOMI_ACCOUNT"),
        username=os.getenv("BOOMI_USER"),
        password=os.getenv("BOOMI_SECRET"),
        timeout=30000,
    )
    
    print(f"🔗 Creating environment-atom attachment...")
    print(f"   Atom ID: {atom_id}")
    print(f"   Environment ID: {environment_id}")
    
    try:
        # Create the attachment request
        attachment_request = EnvironmentAtomAttachment(
            atom_id=atom_id,
            environment_id=environment_id
        )
        
        # Make the API call
        created_attachment = sdk.environment_atom_attachment.create_environment_atom_attachment(
            attachment_request
        )
        
        print("✅ Attachment created successfully!")
        
        # Parse the response
        if hasattr(created_attachment, '_kwargs') and 'EnvironmentAtomAttachment' in created_attachment._kwargs:
            attachment_data = created_attachment._kwargs['EnvironmentAtomAttachment']
            
            print(f"  🆔 Attachment ID: {attachment_data.get('@id', 'N/A')}")
            print(f"  🤖 Atom ID: {attachment_data.get('@atomId', 'N/A')}")
            print(f"  🌍 Environment ID: {attachment_data.get('@environmentId', 'N/A')}")
        else:
            print("⚠️  Unexpected response format")
            
    except Exception as e:
        print(f"❌ Error creating attachment: {str(e)}")

if __name__ == "__main__":
    main()