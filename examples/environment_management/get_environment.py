#!/usr/bin/env python3
"""
Boomi SDK Example: Get Environment Details
==========================================

This example demonstrates how to retrieve environment details using the Boomi SDK.
It first lists available environments, then retrieves detailed information for a specific environment.

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- Account must have appropriate permissions to read environments

Usage:
    cd examples/environment_management
    PYTHONPATH=../../src python3 get_environment.py

Features:
- Lists all available environments in the account
- Allows user to select an environment to view details
- Shows complete environment information (ID, name, classification)
- Demonstrates both query and get operations
"""

import os
import sys

# Add the src directory to the path to import the SDK
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

from boomi import Boomi
from boomi.models import EnvironmentQueryConfig

def list_environments(sdk):
    """List all environments in the account and return them."""
    
    print("📋 Retrieving all environments in the account...")
    
    try:
        # Query all environments (no filters = get all)
        query_config = EnvironmentQueryConfig()
        query_response = sdk.environment.query_environment(query_config)
        
        # Parse the response to get the list of environments
        environments = []
        if hasattr(query_response, '_kwargs') and 'EnvironmentQueryResponse' in query_response._kwargs:
            query_data = query_response._kwargs['EnvironmentQueryResponse']
            
            # Handle single environment vs multiple environments
            if 'Environment' in query_data:
                env_data = query_data['Environment']
                if isinstance(env_data, list):
                    environments = env_data
                else:
                    environments = [env_data]
        
        if not environments:
            print("❌ No environments found or unable to parse response")
            if hasattr(query_response, '_kwargs'):
                print(f"   Raw response: {query_response._kwargs}")
            return []
        
        print(f"\n✅ Found {len(environments)} environment(s):")
        print("-" * 80)
        
        for i, env in enumerate(environments, 1):
            env_id = env.get('@id', 'N/A')
            env_name = env.get('@name', 'N/A')
            env_class = env.get('@classification', 'N/A')
            
            print(f"{i:2}. {env_name}")
            print(f"    ID: {env_id}")
            print(f"    Classification: {env_class}")
            print()
        
        return environments
        
    except Exception as e:
        print(f"❌ Error querying environments: {str(e)}")
        if hasattr(e, 'status'):
            if e.status == 403:
                print("   Permission denied - check if your account can read environments")
        return []


def get_environment_details(sdk, environment_id, environment_name):
    """Get detailed information for a specific environment."""
    
    print(f"🔍 Retrieving details for environment: {environment_name}")
    print(f"   ID: {environment_id}")
    
    try:
        # Get the specific environment by ID
        environment = sdk.environment.get_environment(id_=environment_id)
        
        print("\n✅ Environment details retrieved successfully!")
        print("=" * 60)
        
        # Parse the environment data
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


def main():
    """Main function to demonstrate environment retrieval."""
    
    print("🚀 Boomi SDK - Get Environment Details Example")
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
        # Step 1: List all environments
        environments = list_environments(sdk)
        
        if not environments:
            print("❌ No environments available to query")
            return
        
        # Step 2: Let user select an environment or auto-select first one
        if len(environments) == 1:
            selected_env = environments[0]
            print(f"📍 Auto-selecting the only environment: {selected_env.get('@name', 'Unknown')}")
        else:
            print("Please select an environment to view details:")
            try:
                choice = input(f"Enter number (1-{len(environments)}): ").strip()
                index = int(choice) - 1
                
                if 0 <= index < len(environments):
                    selected_env = environments[index]
                else:
                    print("❌ Invalid selection")
                    return
            except (ValueError, KeyboardInterrupt):
                print("\n❌ Invalid input or cancelled")
                return
        
        # Step 3: Get detailed information for the selected environment
        print()
        env_id = selected_env.get('@id')
        env_name = selected_env.get('@name', 'Unknown')
        
        if env_id:
            get_environment_details(sdk, env_id, env_name)
        else:
            print("❌ Cannot retrieve details - environment ID not found")
        
    except Exception as e:
        print(f"❌ Example failed: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()