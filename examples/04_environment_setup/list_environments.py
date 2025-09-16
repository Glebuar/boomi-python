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

# Load environment variables from .env file if available
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv is optional

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
        # Create a query to get ALL environments using IS_NOT_NULL on ID
        simple_expression = EnvironmentSimpleExpression(
            operator=EnvironmentSimpleExpressionOperator.ISNOTNULL,
            property=EnvironmentSimpleExpressionProperty.ID,
            argument=[]
        )

        query_filter = EnvironmentQueryConfigQueryFilter(expression=simple_expression)
        query_config = EnvironmentQueryConfig(query_filter=query_filter)
        query_response = sdk.environment.query_environment(query_config)

        # Parse the response - use modern SDK response format
        environments = []
        if hasattr(query_response, 'result') and query_response.result:
            # Direct access to result attribute (modern SDK format)
            result_data = query_response.result
            if isinstance(result_data, list):
                environments = result_data
            else:
                environments = [result_data]

        return environments

    except Exception as e:
        print(f"❌ Error querying environments: {str(e)}")
        return []


def display_environments(environments, env_type):
    """Display environment information in a formatted way."""
    
    if not environments:
        print(f"   No {env_type} environments found")
        return
    
    print(f"\n✅ Found {len(environments)} {env_type} environment(s):")
    print("=" * 80)
    
    for i, env in enumerate(environments, 1):
        # Handle Environment objects with proper attributes
        env_id = getattr(env, 'id_', 'N/A')
        env_name = getattr(env, 'name', 'N/A')
        env_class = getattr(env, 'classification', 'N/A')
        # Environment objects don't have type_ attribute, get from _kwargs if needed
        env_type_attr = env._kwargs.get('@type', 'Environment') if hasattr(env, '_kwargs') else 'Environment'
        
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
        # Query ALL environments
        all_environments = list_all_environments(sdk)

        # Categorize environments by classification
        test_environments = []
        prod_environments = []
        other_environments = []

        for env in all_environments:
            classification = getattr(env, 'classification', 'UNKNOWN')
            if classification == 'TEST':
                test_environments.append(env)
            elif classification == 'PROD':
                prod_environments.append(env)
            else:
                other_environments.append(env)

        # Display environments by type
        display_environments(test_environments, "TEST")
        display_environments(prod_environments, "PROD")
        if other_environments:
            display_environments(other_environments, "OTHER")
        
        # Summary
        total_environments = len(all_environments)
        print("=" * 80)
        print(f"📊 Summary:")
        print(f"   Total environments: {total_environments}")
        print(f"   TEST environments: {len(test_environments)}")
        print(f"   PROD environments: {len(prod_environments)}")
        if other_environments:
            print(f"   OTHER environments: {len(other_environments)}")
        
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