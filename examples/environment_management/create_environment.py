#!/usr/bin/env python3
"""
Boomi SDK Example: Create Environment
=====================================

This example demonstrates how to create a new environment using the Boomi SDK.
Environments are used to organize and deploy components in Boomi.

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- Account must have appropriate permissions to create environments

Usage:
    cd examples/environment_management
    PYTHONPATH=../../src python3 create_environment.py

Features:
- Creates a TEST environment with unique name
- Shows how to set classification (TEST vs PROD)
- Displays created environment details
- Optional cleanup to delete the environment after creation
"""

import os
import sys
import datetime

# Add the src directory to the path to import the SDK
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

from boomi import Boomi
from boomi.models import Environment, EnvironmentClassification

def create_test_environment():
    """Create a test environment and display its details."""
    
    print("🚀 Boomi SDK - Create Environment Example")
    print("=" * 50)
    
    # Initialize the Boomi SDK
    sdk = Boomi(
        account_id=os.getenv("BOOMI_ACCOUNT"),
        username=os.getenv("BOOMI_USER"),
        password=os.getenv("BOOMI_SECRET"),
        timeout=30000,
    )
    
    print("✅ SDK initialized successfully!")
    
    # Generate a unique environment name using timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    environment_name = f"SDK_Test_Environment_{timestamp}"
    
    print(f"\n📝 Creating environment: {environment_name}")
    print("   Classification: TEST")
    
    try:
        # Create the environment request
        new_environment = Environment(
            name=environment_name,
            classification=EnvironmentClassification.TEST  # Can be TEST or PROD
        )
        
        # Make the API call to create the environment
        created_environment = sdk.environment.create_environment(new_environment)
        
        print("\n✅ Environment created successfully!")
        print("\n📋 Environment Details:")
        print(f"   ID: {created_environment.id_}")
        print(f"   Name: {created_environment.name}")
        print(f"   Classification: {created_environment.classification}")
        print(f"   Parent Account: {created_environment.parent_account}")
        
        # Ask user if they want to delete the environment
        print("\n" + "=" * 50)
        response = input("Would you like to delete this test environment? (y/n): ")
        
        if response.lower() == 'y':
            print(f"\n🗑️  Deleting environment {environment_name}...")
            sdk.environment.delete_environment(id_=created_environment.id_)
            print("✅ Environment deleted successfully!")
        else:
            print(f"\n💡 Environment '{environment_name}' has been kept.")
            print(f"   You can use it for testing and deployments.")
            print(f"   Remember to delete it when no longer needed.")
            
        return created_environment
        
    except Exception as e:
        print(f"\n❌ Error creating environment: {str(e)}")
        
        # Handle specific error cases
        if hasattr(e, 'status'):
            if e.status == 403:
                print("\n⚠️  Permission denied (403)")
                print("   Your account may not have permission to create environments.")
                print("   This could be due to:")
                print("   - Account role restrictions")
                print("   - License limitations (e.g., Basic vs Unlimited environment support)")
                print("   - Test Connection Licensing not enabled (for TEST environments)")
            elif e.status == 409:
                print("\n⚠️  Conflict (409)")
                print("   An environment with this name may already exist.")
            elif e.status == 400:
                print("\n⚠️  Bad Request (400)")
                print("   Check that the environment name is valid.")
        
        if hasattr(e, 'response') and hasattr(e.response, 'text'):
            print(f"\n   Response details: {e.response.text}")
        
        raise


def demonstrate_environment_classifications():
    """Show the different environment classifications available."""
    
    print("\n📚 Environment Classifications:")
    print("   - PROD: Production environment (default)")
    print("   - TEST: Test environment (requires Test Connection Licensing)")
    print("\nNote: Classification cannot be changed after creation.")


if __name__ == "__main__":
    # Check for required environment variables
    required_vars = ["BOOMI_ACCOUNT", "BOOMI_USER", "BOOMI_SECRET"]
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars:
        print("❌ Missing required environment variables:")
        for var in missing_vars:
            print(f"   - {var}")
        print("\nPlease set these variables in your environment or .env file")
        sys.exit(1)
    
    try:
        # Show classification options
        demonstrate_environment_classifications()
        
        # Create the environment
        created_env = create_test_environment()
        
    except Exception as e:
        print(f"\n❌ Example failed: {str(e)}")
        sys.exit(1)