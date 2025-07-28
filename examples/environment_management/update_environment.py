#!/usr/bin/env python3
"""
Boomi SDK Example: Update Environment Name
==========================================

This example demonstrates how to update an environment's name using the Boomi SDK.
Note: Only the environment name can be modified - classification and ID are immutable.

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- Account must have appropriate permissions to modify environments

Usage:
    cd examples/environment_management
    PYTHONPATH=../../src python3 update_environment.py [environment_id] [new_name]

Features:
- Updates environment name (only field that can be modified)
- Shows before and after environment details
- Creates test environment if no ID provided
- Validates that the update was successful
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
    except Exception:
        return None

def update_environment_name(sdk, environment_id, current_name, new_name):
    """Update the environment name and return the updated environment."""
    
    print(f"🔄 Updating environment name...")
    print(f"   Environment ID: {environment_id}")
    print(f"   Current name: {current_name}")
    print(f"   New name: {new_name}")
    
    try:
        # Get current environment details first
        current_env = get_environment_details(sdk, environment_id)
        if not current_env:
            print("❌ Could not retrieve current environment details")
            return None
        
        # Create the update request with new name
        # Note: We need to include the ID and classification from current environment
        update_request = EnvironmentModel(
            id_=environment_id,
            name=new_name,
            classification=EnvironmentClassification(current_env.get('@classification', 'PROD'))
        )
        
        # Perform the update
        updated_environment = sdk.environment.update_environment(
            id_=environment_id,
            request_body=update_request
        )
        
        print("\n✅ Environment updated successfully!")
        
        # Parse and display the updated environment details
        if hasattr(updated_environment, '_kwargs') and 'Environment' in updated_environment._kwargs:
            env_data = updated_environment._kwargs['Environment']
            
            print("\n📋 Updated Environment Details:")
            print("=" * 50)
            print(f"  🆔 ID: {env_data.get('@id', 'N/A')}")
            print(f"  📛 Name: {env_data.get('@name', 'N/A')}")
            print(f"  🏷️  Classification: {env_data.get('@classification', 'N/A')}")
            print("=" * 50)
            
            # Verify the name was actually changed
            if env_data.get('@name') == new_name:
                print("✅ Name update verified!")
            else:
                print("⚠️  Warning: Name may not have been updated as expected")
            
            return updated_environment
        else:
            print("⚠️  Unexpected response format")
            if hasattr(updated_environment, '_kwargs'):
                print(f"   Raw response: {updated_environment._kwargs}")
            return updated_environment
        
    except Exception as e:
        print(f"❌ Error updating environment: {str(e)}")
        if hasattr(e, 'status'):
            if e.status == 403:
                print("   Permission denied - check if your account can modify environments")
            elif e.status == 404:
                print("   Environment not found - it may have been deleted")
            elif e.status == 400:
                print("   Bad request - check if the new name is valid")
        return None

def create_test_environment(sdk):
    """Create a test environment for demonstration."""
    
    print("🏗️  Creating a test environment for the update demonstration...")
    
    try:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        environment_name = f"SDK_Update_Test_Original_{timestamp}"
        
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
            print("❌ Could not extract environment ID from response")
            return None, None
            
    except Exception as e:
        print(f"❌ Error creating test environment: {str(e)}")
        return None, None

def main():
    """Main function to demonstrate environment name update."""
    
    print("🚀 Boomi SDK - Update Environment Name Example")
    print("=" * 55)
    
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
        original_name = None
        new_name = None
        created_test_env = False
        
        # Parse command line arguments
        if len(sys.argv) >= 3:
            environment_id = sys.argv[1]
            new_name = sys.argv[2]
            print(f"📍 Using provided environment ID: {environment_id}")
            print(f"📝 New name: {new_name}")
            
            # Get current details
            current_details = get_environment_details(sdk, environment_id)
            if current_details:
                original_name = current_details.get('@name', 'Unknown')
            else:
                print("❌ Could not retrieve environment details")
                return
                
        elif len(sys.argv) == 2:
            environment_id = sys.argv[1]
            # Get current details to show current name
            current_details = get_environment_details(sdk, environment_id)
            if current_details:
                original_name = current_details.get('@name', 'Unknown')
                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                new_name = f"Updated_{original_name}_{timestamp}"
                print(f"📍 Using provided environment ID: {environment_id}")
                print(f"📝 Auto-generated new name: {new_name}")
            else:
                print("❌ Could not retrieve environment details")
                return
        else:
            # Create a test environment to demonstrate with
            environment_id, original_name = create_test_environment(sdk)
            if not environment_id:
                print("❌ Could not create test environment")
                return
            created_test_env = True
            
            # Generate a new name
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            new_name = f"SDK_Update_Test_UPDATED_{timestamp}"
        
        print()
        
        # Show current environment details
        print("📋 Current Environment Details:")
        print("-" * 40)
        current_details = get_environment_details(sdk, environment_id)
        if current_details:
            print(f"  🆔 ID: {current_details.get('@id', 'N/A')}")
            print(f"  📛 Name: {current_details.get('@name', 'N/A')}")
            print(f"  🏷️  Classification: {current_details.get('@classification', 'N/A')}")
        print("-" * 40)
        print()
        
        # Perform the update
        updated_environment = update_environment_name(sdk, environment_id, original_name, new_name)
        
        # If we created a test environment, offer to clean it up
        if created_test_env and updated_environment:
            print("\n" + "=" * 55)
            response = input("Would you like to delete the test environment? (y/n): ")
            
            if response.lower() == 'y':
                print(f"\n🗑️  Deleting test environment...")
                sdk.environment.delete_environment(id_=environment_id)
                print("✅ Test environment deleted successfully!")
            else:
                print(f"💡 Test environment kept with ID: {environment_id}")
                print(f"   Updated name: {new_name}")
        
    except Exception as e:
        print(f"❌ Example failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()