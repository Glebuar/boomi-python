#!/usr/bin/env python3
"""
Boomi SDK Example: Detach Atom from Environment
===============================================

This example demonstrates how to detach an atom from an environment using 
the attachment ID.

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- Account must have appropriate permissions to manage attachments
- Need the attachment ID (returned from create_attachment or query operations)

Usage:
    cd examples/environment_management
    PYTHONPATH=../../src python3 detach_atom_from_environment.py [attachment_id]

Features:
- Detaches atom from environment using attachment ID
- Shows confirmation of successful detachment
- Verifies detachment by checking if environment can be deleted
"""

import os
import sys

# Add the src directory to the path to import the SDK
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

from boomi import Boomi

def detach_atom_from_environment(sdk, attachment_id):
    """Detach the atom using the attachment ID."""
    
    print(f"🔓 Detaching atom from environment...")
    print(f"   Attachment ID: {attachment_id}")
    
    try:
        # Make the detachment API call
        result = sdk.environment_atom_attachment.delete_environment_atom_attachment(id_=attachment_id)
        
        print("\n✅ Detachment request sent successfully!")
        
        # The response should be a boolean true or similar
        if hasattr(result, '_kwargs'):
            print(f"   Response: {result._kwargs}")
        else:
            print(f"   Result: {result}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error detaching atom: {str(e)}")
        
        if hasattr(e, 'status'):
            if e.status == 403:
                print("\n   Permission denied (403)")
                print("   • Check if your account can manage environment attachments")
            elif e.status == 404:
                print("\n   Not found (404)")
                print("   • The attachment ID may not exist")
                print("   • The attachment may have already been removed")
            elif e.status == 400:
                print("\n   Bad request (400)")
                print("   • Check the attachment ID format")
        
        return False

def verify_detachment(sdk, environment_id):
    """Verify detachment by trying to delete the environment."""
    
    print(f"\n🔍 Verifying detachment by testing environment deletion...")
    print(f"   Environment ID: {environment_id}")
    
    try:
        # Try to delete the environment - this should work if atom is detached
        sdk.environment.delete_environment(id_=environment_id)
        print("✅ Environment deleted successfully - detachment verified!")
        return True
        
    except Exception as e:
        if hasattr(e, 'status'):
            if "contains containers attached" in str(e) or "attached" in str(e).lower():
                print("⚠️  Environment still has attachments - detachment may not have worked")
                return False
            elif e.status == 404:
                print("✅ Environment not found - it may have been deleted already")
                return True
        
        print(f"❌ Could not verify detachment: {str(e)}")
        return False

def main():
    """Main function to demonstrate atom detachment."""
    
    print("🚀 Boomi SDK - Detach Atom from Environment")
    print("=" * 55)
    
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
        # Get attachment ID from arguments or use the known one from earlier test
        if len(sys.argv) > 1:
            attachment_id = sys.argv[1]
            print(f"📍 Using provided attachment ID: {attachment_id}")
        else:
            print("💡 Usage: python3 detach_atom_from_environment.py <attachment_id>")
            print("\n   Example from earlier test:")
            example_id = "RU5WX0NPTlRfQVRUQUNIYWZlZWI0ZWEtM2JiOS00NjQwLWI0MWUtZjZhYmEwOGQzYzQxOjA0ZGZhNDQ3LWJmMzktNDVhZi04ZDYzLTllODQzZTJiYjI4NQ"
            print(f"   {example_id}")
            
            response = input("\nWould you like to use this example attachment ID? (y/n): ")
            if response.lower() == 'y':
                attachment_id = example_id
                print(f"📍 Using example attachment ID")
            else:
                attachment_id = input("Enter attachment ID: ").strip()
                if not attachment_id:
                    print("❌ No attachment ID provided")
                    return
        
        print()
        
        # Perform the detachment
        success = detach_atom_from_environment(sdk, attachment_id)
        
        if success:
            print(f"\n🎉 Atom successfully detached from environment!")
            
            # If we know the environment ID, try to verify by deleting it
            # The example attachment ID contains the environment ID: 04dfa447-bf39-45af-8d63-9e843e2bb285
            known_env_id = "04dfa447-bf39-45af-8d63-9e843e2bb285"
            
            print(f"\n💡 Would you like to verify detachment by deleting the test environment?")
            print(f"   Environment ID: {known_env_id}")
            verify_response = input("Verify by deleting environment? (y/n): ")
            
            if verify_response.lower() == 'y':
                verify_detachment(sdk, known_env_id)
        
    except KeyboardInterrupt:
        print("\n❌ Operation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Example failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()