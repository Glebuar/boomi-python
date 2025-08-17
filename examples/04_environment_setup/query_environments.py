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
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

from boomi import Boomi
from boomi.models import EnvironmentQueryConfig

def main():
    # Initialize SDK
    sdk = Boomi(
        account_id=os.getenv("BOOMI_ACCOUNT"),
        username=os.getenv("BOOMI_USER"),
        password=os.getenv("BOOMI_SECRET"),
        timeout=30000,
    )
    
    print("🔍 Querying available environments...")
    
    # Query all environments
    query_config = EnvironmentQueryConfig()
    query_response = sdk.environment.query_environment(query_config)
    
    # Process results
    environments = []
    if hasattr(query_response, 'result') and query_response.result:
        environments = query_response.result if isinstance(query_response.result, list) else [query_response.result]
    
    if environments:
        print(f"✅ Found {len(environments)} environment(s):")
        for i, env in enumerate(environments, 1):
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