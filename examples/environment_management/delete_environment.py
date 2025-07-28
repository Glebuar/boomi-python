#!/usr/bin/env python3
"""
Boomi SDK Example: Delete Environment
=====================================

This example demonstrates how to delete an environment using the Boomi SDK.
WARNING: Deletion is permanent and cannot be undone!

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- Account must have appropriate permissions to delete environments
- Environment must not have attached runtimes or deployed components

Usage:
    cd examples/environment_management
    PYTHONPATH=../../src python3 delete_environment.py [environment_id]

Features:
- Safely deletes environments with confirmation prompts
- Shows environment details before deletion
- Creates test environment if no ID provided
- Verifies deletion was successful
- Handles common error scenarios (attached runtimes, permission denied)
"""

import os
import sys
import datetime

# Add the src directory to the path to import the SDK
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

from boomi import Boomi
from boomi.models import Environment as EnvironmentModel
from boomi.models import EnvironmentClassification

def get_environment_details(sdk, environment_id):
    """Helper function to get environment details."""
    try:
        environment = sdk.environment.get_environment(id_=environment_id)
        
        if hasattr(environment, '_kwargs') and 'Environment' in environment._kwargs:
            return environment._kwargs['Environment']
        return None
    except Exception as e:
        if hasattr(e, 'status') and e.status == 404:
            return None  # Environment doesn't exist
        raise e

def delete_environment_safely(sdk, environment_id, environment_name):
    """Delete the environment with proper confirmation and error handling."""
    
    print(f"⚠️  DELETION WARNING")
    print("=" * 60)
    print(f"   Environment ID: {environment_id}")
    print(f"   Environment Name: {environment_name}")
    print()
    print("   🚨 IMPORTANT NOTES:")
    print("   • Deletion is PERMANENT and cannot be undone")
    print("   • Environment must not have attached runtimes")
    print("   • Environment must not have deployed components")
    print("=" * 60)
    
    # Double confirmation for safety
    confirm1 = input("\nType 'DELETE' to confirm deletion: ").strip()
    if confirm1 != 'DELETE':
        print("❌ Deletion cancelled - confirmation text did not match")
        return False
    
    confirm2 = input(f"Type the environment name '{environment_name}' to proceed: ").strip()
    if confirm2 != environment_name:
        print("❌ Deletion cancelled - environment name did not match")
        return False
    
    print(f"\n🗑️  Deleting environment: {environment_name}")
    print(f"   ID: {environment_id}")
    
    try:
        # Perform the deletion
        sdk.environment.delete_environment(id_=environment_id)
        
        print("✅ Environment deletion request sent successfully!")
        
        # Verify the environment was actually deleted by trying to retrieve it
        print("🔍 Verifying deletion...")
        
        try:
            verification = get_environment_details(sdk, environment_id)
            if verification is None:
                print("✅ Environment deletion verified - environment no longer exists")
                return True
            else:
                print("⚠️  Warning: Environment may still exist after deletion request")
                return False
        except Exception as verify_error:
            if hasattr(verify_error, 'status') and verify_error.status == 404:
                print("✅ Environment deletion verified - environment no longer exists")
                return True
            else:
                print(f"⚠️  Could not verify deletion: {str(verify_error)}")
                return True  # Assume successful if we can't verify
        
    except Exception as e:
        print(f"❌ Error deleting environment: {str(e)}")
        
        if hasattr(e, 'status'):
            if e.status == 403:
                print("\n   Permission denied (403):")
                print("   • Check if your account has permission to delete environments")
                print("   • Verify you have the correct role assignments")
            elif e.status == 409:
                print("\n   Conflict (409) - Environment cannot be deleted:")
                print("   • Environment may have attached runtimes")
                print("   • Environment may have deployed components/processes")
                print("   • Remove all attachments and deployments first")
            elif e.status == 404:
                print("\n   Environment not found (404):")
                print("   • Environment may have already been deleted")
                print("   • Verify the environment ID is correct")
            elif e.status == 400:
                print("\n   Bad request (400):")
                print("   • Check that the environment ID format is valid")
        
        return False

def create_test_environment(sdk):
    """Create a test environment for deletion demonstration."""
    
    print("🏗️  Creating a test environment for the deletion demonstration...")
    
    try:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        environment_name = f"SDK_Delete_Test_{timestamp}"
        
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
            print(f"   Classification: {env_data.get('@classification', 'N/A')}")
            return env_id, env_name
        else:
            print("❌ Could not extract environment details from response")
            return None, None
            
    except Exception as e:
        print(f"❌ Error creating test environment: {str(e)}")
        return None, None

def main():
    """Main function to demonstrate environment deletion."""
    
    print("🚀 Boomi SDK - Delete Environment Example")
    print("=" * 50)
    
    # Check for required environment variables
    required_vars = ["BOOMI_ACCOUNT", "BOOMI_USER", "BOOMI_SECRET"]
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars:
        print("❌ Missing required environment variables:")
        for var in missing_vars:
            print(f"   - {var}")
        print("\nPlease set these variables in your environment")
        sys.exit(1)
    
    # Initialize the Boomi SDK
    sdk = Boomi(
        account_id=os.getenv("BOOMI_ACCOUNT"),
        username=os.getenv("BOOMI_USER"),
        password=os.getenv("BOOMI_SECRET"),
        timeout=30000,
    )
    
    print("✅ SDK initialized successfully!")
    print()
    
    try:
        environment_id = None
        environment_name = None
        created_test_env = False
        
        # Check if environment ID was provided as command line argument
        if len(sys.argv) > 1:
            environment_id = sys.argv[1]
            print(f"📍 Using provided environment ID: {environment_id}")
            
            # Get environment details to show what will be deleted
            current_details = get_environment_details(sdk, environment_id)
            if current_details:
                environment_name = current_details.get('@name', 'Unknown')
                print(f"📛 Environment name: {environment_name}")
                print(f"🏷️  Classification: {current_details.get('@classification', 'N/A')}")
            else:
                print("❌ Could not retrieve environment details - environment may not exist")
                return
        else:
            # Create a test environment to demonstrate with
            print("🔧 No environment ID provided - creating a test environment for demonstration")
            print()
            environment_id, environment_name = create_test_environment(sdk)
            if not environment_id:
                print("❌ Could not create test environment")
                return
            created_test_env = True
        
        print()
        
        # Show current environment details before deletion
        print("📋 Environment to be deleted:")
        print("-" * 50)
        current_details = get_environment_details(sdk, environment_id)
        if current_details:
            print(f"  🆔 ID: {current_details.get('@id', 'N/A')}")
            print(f"  📛 Name: {current_details.get('@name', 'N/A')}")
            print(f"  🏷️  Classification: {current_details.get('@classification', 'N/A')}")
        else:
            print("  ❌ Could not retrieve current environment details")
        print("-" * 50)
        print()
        
        # Perform the deletion with safety checks
        success = delete_environment_safely(sdk, environment_id, environment_name)
        
        if success:
            print(f"\n🎉 Environment '{environment_name}' has been successfully deleted!")
        else:
            print(f"\n💔 Failed to delete environment '{environment_name}'")
            if created_test_env:
                print("⚠️  Test environment was not cleaned up - you may need to delete it manually")
                print(f"   Environment ID: {environment_id}")
        
    except KeyboardInterrupt:
        print("\n❌ Operation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Example failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()