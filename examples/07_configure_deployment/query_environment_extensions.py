#!/usr/bin/env python3
"""
Query Environment Extensions

This example demonstrates how to query environment extensions using the Boomi SDK.

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET

Usage:
    python query_environment_extensions_single.py [ENVIRONMENT_ID]

Endpoint:
- environment_extensions.query_environment_extensions
"""

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

from boomi import Boomi
from boomi.models import (
    EnvironmentExtensionsQueryConfig,
    EnvironmentExtensionsQueryConfigQueryFilter,
    EnvironmentExtensionsSimpleExpression,
    EnvironmentExtensionsSimpleExpressionOperator,
    EnvironmentExtensionsSimpleExpressionProperty
)

def main():
    environment_id = sys.argv[1] if len(sys.argv) > 1 else None
    
    # Initialize SDK
    sdk = Boomi(
        account_id=os.getenv("BOOMI_ACCOUNT"),
        username=os.getenv("BOOMI_USER"),
        password=os.getenv("BOOMI_SECRET"),
        timeout=30000,
    )
    
    print("🔍 Querying environment extensions...")
    
    try:
        if environment_id:
            # Query extensions for specific environment
            simple_expression = EnvironmentExtensionsSimpleExpression(
                operator=EnvironmentExtensionsSimpleExpressionOperator.EQUALS,
                property=EnvironmentExtensionsSimpleExpressionProperty.ENVIRONMENT_ID,
                argument=[environment_id]
            )
            query_filter = EnvironmentExtensionsQueryConfigQueryFilter(expression=simple_expression)
            query_config = EnvironmentExtensionsQueryConfig(query_filter=query_filter)
            print(f"   Filtering by environment ID: {environment_id}")
        else:
            # Query all environment extensions
            query_config = EnvironmentExtensionsQueryConfig()
        
        # Query environment extensions
        result = sdk.environment_extensions.query_environment_extensions(query_config)
        
        # Process results
        extensions = []
        if hasattr(result, 'result') and result.result:
            extensions = result.result if isinstance(result.result, list) else [result.result]
        
        if extensions:
            print(f"✅ Found {len(extensions)} environment extension(s):")
            for i, ext in enumerate(extensions, 1):
                ext_id = getattr(ext, 'id_', 'N/A')
                ext_env_id = getattr(ext, 'environment_id', 'N/A')
                ext_type = getattr(ext, 'extension_type', 'N/A')
                
                print(f"{i:2}. Extension ID: {ext_id}")
                print(f"    Environment ID: {ext_env_id}")
                print(f"    Type: {ext_type}")
        else:
            print("❌ No environment extensions found")
            
    except Exception as e:
        print(f"❌ Error querying environment extensions: {str(e)}")

if __name__ == "__main__":
    main()