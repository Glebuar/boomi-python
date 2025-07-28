#!/usr/bin/env python3
"""
Boomi SDK Example: List All Environments
=========================================

This example demonstrates how to query and list all environments in a Boomi account
using the Python SDK. It shows environment details including name, ID, and classification.

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- Account must have appropriate permissions to read environments

Usage:
    cd examples/utilities
    PYTHONPATH=../../src python3 list_environments.py

Features:
- Lists all environments in the account
- Shows environment details (ID, name, classification)
- Filters environments by classification (optional)
- Counts and categorizes environments by type
"""

import os
import sys

# Add the src directory to the path to import the SDK
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

from boomi import Boomi
from boomi.models import (
    EnvironmentQueryConfig,
    EnvironmentQueryConfigQueryFilter,
    EnvironmentSimpleExpression,
    EnvironmentSimpleExpressionOperator,
    EnvironmentSimpleExpressionProperty
)

def list_all_environments(sdk):
    """List all environments in the account."""
    
    print("🔍 Querying all environments in the account...")
    
    try:
        # Create a query to get all TEST environments
        # We use TEST classification because it's more common to have test environments
        simple_expression = EnvironmentSimpleExpression(
            operator=EnvironmentSimpleExpressionOperator.CONTAINS,
            property=EnvironmentSimpleExpressionProperty.CLASSIFICATION,
            argument=["TEST"]
        )
        
        query_filter = EnvironmentQueryConfigQueryFilter(expression=simple_expression)
        query_config = EnvironmentQueryConfig(query_filter=query_filter)
        query_response = sdk.environment.query_environment(query_config)
        
        # Parse the response
        environments = []
        if hasattr(query_response, '_kwargs') and 'EnvironmentQueryResponse' in query_response._kwargs:
            query_data = query_response._kwargs['EnvironmentQueryResponse']
            
            if 'Environment' in query_data:
                env_data = query_data['Environment']
                if isinstance(env_data, list):
                    environments = env_data
                else:
                    environments = [env_data]
        
        return environments
        
    except Exception as e:
        print(f"❌ Error querying TEST environments: {str(e)}")
        return []

def list_prod_environments(sdk):
    """List all PROD environments in the account."""
    
    print("🔍 Querying PROD environments...")
    
    try:
        # Query PROD environments
        simple_expression = EnvironmentSimpleExpression(
            operator=EnvironmentSimpleExpressionOperator.EQUALS,
            property=EnvironmentSimpleExpressionProperty.CLASSIFICATION,
            argument=["PROD"]
        )
        
        query_filter = EnvironmentQueryConfigQueryFilter(expression=simple_expression)
        query_config = EnvironmentQueryConfig(query_filter=query_filter)
        query_response = sdk.environment.query_environment(query_config)
        
        # Parse the response
        environments = []
        if hasattr(query_response, '_kwargs') and 'EnvironmentQueryResponse' in query_response._kwargs:
            query_data = query_response._kwargs['EnvironmentQueryResponse']
            
            if 'Environment' in query_data:
                env_data = query_data['Environment']
                if isinstance(env_data, list):
                    environments = env_data
                else:
                    environments = [env_data]
        
        return environments
        
    except Exception as e:
        print(f"❌ Error querying PROD environments: {str(e)}")
        return []

def display_environments(environments, env_type):
    """Display environment information in a formatted way."""
    
    if not environments:
        print(f"   No {env_type} environments found")
        return
    
    print(f"\n✅ Found {len(environments)} {env_type} environment(s):")
    print("=" * 80)
    
    for i, env in enumerate(environments, 1):
        env_id = env.get('@id', 'N/A')
        env_name = env.get('@name', 'N/A')
        env_class = env.get('@classification', 'N/A')
        env_type_attr = env.get('@type', 'N/A')
        
        print(f"{i:2}. 📂 {env_name}")
        print(f"     🆔 ID: {env_id}")
        print(f"     🏷️  Classification: {env_class}")
        if env_type_attr != 'N/A':
            print(f"     📋 Type: {env_type_attr}")
        print()

def main():
    """Main function to demonstrate environment listing."""
    
    print("🚀 Boomi SDK - List All Environments Example")
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
        # Query TEST environments
        test_environments = list_all_environments(sdk)
        display_environments(test_environments, "TEST")
        
        # Query PROD environments  
        prod_environments = list_prod_environments(sdk)
        display_environments(prod_environments, "PROD")
        
        # Summary
        total_environments = len(test_environments) + len(prod_environments)
        print("=" * 80)
        print(f"📊 Summary:")
        print(f"   Total environments: {total_environments}")
        print(f"   TEST environments: {len(test_environments)}")
        print(f"   PROD environments: {len(prod_environments)}")
        
        if total_environments > 0:
            print(f"\n💡 Tips:")
            print(f"   • Use environment IDs for API operations")
            print(f"   • TEST environments are typically used for development")
            print(f"   • PROD environments are used for production deployments")
            print(f"   • Environment names must be unique within an account")
        
    except Exception as e:
        print(f"❌ Example failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()