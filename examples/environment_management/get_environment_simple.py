#!/usr/bin/env python3
"""
Boomi SDK Example: Get Environment Details (Simple)
===================================================

This example demonstrates how to retrieve environment details using a known environment ID.

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- Account must have appropriate permissions to read environments

Usage:
    cd examples/environment_management
    PYTHONPATH=../../src python3 get_environment_simple.py [environment_id]

Features:
- Retrieves environment details by ID
- Shows complete environment information
- Creates a test environment if no ID provided
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
    """Get detailed information for a specific environment."""
    
    print(f"🔍 Retrieving environment details for ID: {environment_id}")
    
    try:
        # Get the specific environment by ID
        environment = sdk.environment.get_environment(id_=environment_id)
        
        print("\n✅ Environment details retrieved successfully!")
        print("=" * 60)
        
        # Parse the environment data (handle the nested response structure)
        if hasattr(environment, '_kwargs') and 'Environment' in environment._kwargs:
            env_data = environment._kwargs['Environment']
            
            print(f"Environment Information:")
            print(f"  🆔 ID: {env_data.get('@id', 'N/A')}")
            print(f"  📛 Name: {env_data.get('@name', 'N/A')}")
            print(f"  🏷️  Classification: {env_data.get('@classification', 'N/A')}")
            
            # Show additional fields if present
            if '@parentAccount' in env_data:
                print(f"  🏢 Parent Account: {env_data.get('@parentAccount')}")
            if '@parentEnvironment' in env_data:
                print(f"  🌍 Parent Environment: {env_data.get('@parentEnvironment')}")
        else:
            print("⚠️  Unexpected response format")
            if hasattr(environment, '_kwargs'):
                print(f"   Raw response: {environment._kwargs}")
        
        print("=" * 60)
        return environment
        
    except Exception as e:
        print(f"❌ Error getting environment details: {str(e)}")
        if hasattr(e, 'status'):
            if e.status == 403:
                print("   Permission denied - check if your account can read this environment")
            elif e.status == 404:
                print("   Environment not found - it may have been deleted")
        return None


def create_test_environment(sdk):
    """Create a test environment and return its ID."""
    
    print("🏗️  Creating a test environment first...")
    
    try:
        # Generate a unique environment name
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        environment_name = f"SDK_Get_Test_{timestamp}"
        
        # Create the environment
        new_environment = EnvironmentModel(
            name=environment_name,
            classification=EnvironmentClassification.TEST
        )
        
        created_environment = sdk.environment.create_environment(new_environment)
        
        # Extract the ID from the response
        if hasattr(created_environment, '_kwargs') and 'Environment' in created_environment._kwargs:
            env_data = created_environment._kwargs['Environment']
            env_id = env_data.get('@id')
            env_name = env_data.get('@name')
            
            print(f"✅ Created test environment: {env_name}")
            print(f"   ID: {env_id}")
            return env_id
        else:
            print("❌ Could not extract environment ID from response")
            return None
            
    except Exception as e:
        print(f"❌ Error creating test environment: {str(e)}")
        return None


def main():
    """Main function to demonstrate environment retrieval."""
    
    print("🚀 Boomi SDK - Get Environment Details Example")
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
        # Check if environment ID was provided as command line argument
        environment_id = None
        if len(sys.argv) > 1:
            environment_id = sys.argv[1]
            print(f"📍 Using provided environment ID: {environment_id}")
        else:
            # Create a test environment to demonstrate with
            environment_id = create_test_environment(sdk)
            
        if not environment_id:
            print("❌ No environment ID available")
            return
        
        print()
        
        # Get environment details
        environment = get_environment_details(sdk, environment_id)
        
        # If we created a test environment, offer to clean it up
        if len(sys.argv) <= 1 and environment:  # We created it ourselves
            print("\n" + "=" * 50)
            response = input("Would you like to delete the test environment? (y/n): ")
            
            if response.lower() == 'y':
                print(f"\n🗑️  Deleting test environment...")
                sdk.environment.delete_environment(id_=environment_id)
                print("✅ Test environment deleted successfully!")
            else:
                print(f"💡 Test environment kept with ID: {environment_id}")
        
    except Exception as e:
        print(f"❌ Example failed: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()