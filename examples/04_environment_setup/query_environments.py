#!/usr/bin/env python3
"""
Query Environments

This example demonstrates how to query available environments using the Boomi SDK.

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET

Usage:
    python query_environments.py

Endpoint:
- environment.query_environment
"""

import os
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

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

def main():
    # Initialize SDK
    sdk = Boomi(
        account_id=os.getenv("BOOMI_ACCOUNT"),
        username=os.getenv("BOOMI_USER"),
        password=os.getenv("BOOMI_SECRET"),
        timeout=30000,
    )
    
    print("🔍 Querying available environments...")
    
    all_environments = []
    
    # Query TEST environments
    try:
        simple_expression = EnvironmentSimpleExpression(
            operator=EnvironmentSimpleExpressionOperator.EQUALS,
            property=EnvironmentSimpleExpressionProperty.CLASSIFICATION,
            argument=["TEST"]
        )
        
        query_filter = EnvironmentQueryConfigQueryFilter(expression=simple_expression)
        query_config = EnvironmentQueryConfig(query_filter=query_filter)
        query_response = sdk.environment.query_environment(query_config)
        
        if hasattr(query_response, 'result') and query_response.result:
            test_envs = query_response.result if isinstance(query_response.result, list) else [query_response.result]
            all_environments.extend(test_envs)
            print(f"✅ Found {len(test_envs)} TEST environment(s)")
    except Exception as e:
        print(f"⚠️ Error querying TEST environments: {e}")
    
    # Query PROD environments
    try:
        simple_expression = EnvironmentSimpleExpression(
            operator=EnvironmentSimpleExpressionOperator.EQUALS,
            property=EnvironmentSimpleExpressionProperty.CLASSIFICATION,
            argument=["PROD"]
        )
        
        query_filter = EnvironmentQueryConfigQueryFilter(expression=simple_expression)
        query_config = EnvironmentQueryConfig(query_filter=query_filter)
        query_response = sdk.environment.query_environment(query_config)
        
        if hasattr(query_response, 'result') and query_response.result:
            prod_envs = query_response.result if isinstance(query_response.result, list) else [query_response.result]
            all_environments.extend(prod_envs)
            print(f"✅ Found {len(prod_envs)} PROD environment(s)")
    except Exception as e:
        print(f"⚠️ Error querying PROD environments: {e}")
    
    # Display results
    if all_environments:
        print(f"\n📋 Total environments found: {len(all_environments)}")
        for i, env in enumerate(all_environments, 1):
            env_id = getattr(env, 'id_', 'N/A')
            env_name = getattr(env, 'name', 'N/A')
            env_class = getattr(env, 'classification', 'N/A')
            
            print(f"{i:2}. {env_name}")
            print(f"    ID: {env_id}")
            print(f"    Classification: {env_class}")
    else:
        print("❌ No environments found")

if __name__ == "__main__":
    main()