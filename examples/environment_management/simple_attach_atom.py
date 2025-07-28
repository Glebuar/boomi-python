#!/usr/bin/env python3
"""
Boomi SDK Example: Simple Atom-Environment Attachment
=====================================================

This example demonstrates attaching an atom to an environment using known IDs.
This is a simplified version that bypasses complex querying issues.

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- Provide atom ID and environment ID as arguments or it will create a test environment

Usage:
    cd examples/environment_management
    PYTHONPATH=../../src python3 simple_attach_atom.py [atom_id] [environment_id]

Example:
    PYTHONPATH=../../src python3 simple_attach_atom.py afeeb4ea-3bb9-4640-b41e-f6aba08d3c41 74851c30-98b2-4a6f-838b-61eee5627b13
"""

import os
import sys
import datetime

# Add the src directory to the path to import the SDK
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

from boomi import Boomi
from boomi.models import (
    Environment as EnvironmentModel,
    EnvironmentClassification,
    EnvironmentAtomAttachment
)

def create_test_environment(sdk):
    """Create a test environment for demonstration."""
    
    print("🏗️  Creating a test environment...")
    
    try:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        environment_name = f"SDK_Attach_Test_{timestamp}"
        
        new_environment = EnvironmentModel(
            name=environment_name,
            classification=EnvironmentClassification.TEST
        )
        
        created_environment = sdk.environment.create_environment(new_environment)
        
        if hasattr(created_environment, '_kwargs') and 'Environment' in created_environment._kwargs:
            env_data = created_environment._kwargs['Environment']
            env_id = env_data.get('@id')
            env_name = env_data.get('@name')
            
            print(f"✅ Created test environment: {env_name}")
            print(f"   ID: {env_id}")
            return env_id, env_name
        else:
            print("❌ Could not extract environment details from response")
            return None, None
            
    except Exception as e:
        print(f"❌ Error creating test environment: {str(e)}")
        return None, None

def create_attachment(sdk, atom_id, environment_id):
    """Create the atom-environment attachment."""
    
    print(f"🔗 Creating attachment...")
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
        
        print("\n✅ Attachment created successfully!")
        
        # Parse the response - try multiple possible response structures
        attachment_data = None
        
        if hasattr(created_attachment, '_kwargs'):
            print(f"   Response structure: {list(created_attachment._kwargs.keys())}")
            
            # Try different possible response keys
            for key in ['EnvironmentAtomAttachment', 'Environment', 'response']:
                if key in created_attachment._kwargs:
                    attachment_data = created_attachment._kwargs[key]
                    break
        
        if attachment_data:
            print("\n📋 Attachment Details:")
            print("=" * 50)
            
            # Handle different response formats
            if isinstance(attachment_data, dict):
                att_id = attachment_data.get('@id', attachment_data.get('id', 'N/A'))
                att_atom_id = attachment_data.get('@atomId', attachment_data.get('atomId', 'N/A'))
                att_env_id = attachment_data.get('@environmentId', attachment_data.get('environmentId', 'N/A'))
                
                print(f"  🆔 Attachment ID: {att_id}")
                print(f"  🤖 Atom ID: {att_atom_id}")
                print(f"  🌍 Environment ID: {att_env_id}")
            else:
                print(f"  Raw data: {attachment_data}")
            
            print("=" * 50)
            return created_attachment
        else:
            print("⚠️  Attachment created but response format unexpected")
            print(f"   Raw response: {created_attachment._kwargs if hasattr(created_attachment, '_kwargs') else 'No _kwargs'}")
            return created_attachment
        
    except Exception as e:
        print(f"❌ Error creating attachment: {str(e)}")
        
        if hasattr(e, 'status'):
            if e.status == 403:
                print("\n   Permission denied (403)")
                print("   • Check if your account can manage environment attachments")
            elif e.status == 409:
                print("\n   Conflict (409)")
                print("   • The atom may already be attached to this environment")
                print("   • Check existing attachments first")
            elif e.status == 404:
                print("\n   Not found (404)")
                print("   • Verify the atom ID and environment ID are correct")
            elif e.status == 400:
                print("\n   Bad request (400)")
                print("   • Check the request format and IDs")
        
        return None

def main():
    """Main function."""
    
    print("🚀 Boomi SDK - Simple Atom-Environment Attachment")
    print("=" * 60)
    
    # Check for required environment variables
    required_vars = ["BOOMI_ACCOUNT", "BOOMI_USER", "BOOMI_SECRET"]
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars:
        print("❌ Missing required environment variables:")
        for var in missing_vars:
            print(f"   - {var}")
        sys.exit(1)
    
    # Initialize the SDK
    sdk = Boomi(
        account_id=os.getenv("BOOMI_ACCOUNT"),
        username=os.getenv("BOOMI_USER"),
        password=os.getenv("BOOMI_SECRET"),
        timeout=30000,
    )
    
    print("✅ SDK initialized successfully!")
    print()
    
    try:
        # Parse arguments
        if len(sys.argv) >= 3:
            atom_id = sys.argv[1]
            environment_id = sys.argv[2]
            print(f"📍 Using provided Atom ID: {atom_id}")
            print(f"📍 Using provided Environment ID: {environment_id}")
            created_test_env = False
        else:
            print("💡 Usage: python3 simple_attach_atom.py <atom_id> <environment_id>")
            print("   No IDs provided - will create a test environment")
            print("   You need to provide an atom ID that exists in your account")
            
            # Create test environment but still need atom ID
            environment_id, env_name = create_test_environment(sdk)
            if not environment_id:
                print("❌ Could not create test environment")
                return
            created_test_env = True
            
            # Ask for atom ID
            print(f"\n💡 Known atom IDs from earlier investigation:")
            print(f"   • afeeb4ea-3bb9-4640-b41e-f6aba08d3c41 (PROD-On-Prem - ONLINE)")
            print(f"   • dd5a0c41-3911-46a0-9ff0-3f5c2a69c8b8 (On-Prem-Local-VM - OFFLINE)")
            
            atom_id = input("\nEnter atom ID to attach: ").strip()
            if not atom_id:
                print("❌ No atom ID provided")
                return
        
        print()
        
        # Create the attachment
        attachment = create_attachment(sdk, atom_id, environment_id)
        
        if attachment:
            print(f"\n🎉 Successfully attached atom to environment!")
        
        # Clean up if we created test environment
        if 'created_test_env' in locals() and created_test_env:
            print("\n" + "=" * 60)
            response = input("Delete test environment? (y/n): ")
            if response.lower() == 'y':
                sdk.environment.delete_environment(id_=environment_id)
                print("✅ Test environment deleted")
        
    except Exception as e:
        print(f"❌ Example failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()