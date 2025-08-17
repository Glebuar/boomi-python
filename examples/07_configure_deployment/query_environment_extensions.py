#!/usr/bin/env python3
"""
Boomi SDK Example: Query Environment Extensions
===============================================

This example demonstrates how to query for environment extensions using
the Boomi SDK. This allows you to search for extensions based on specific
criteria like environment ID and extension group ID.

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- Account must have appropriate permissions to query environment extensions

Usage:
    cd examples/environment_management
    PYTHONPATH=../../src python3 query_environment_extensions.py

Features:
- Queries environment extensions by environment ID
- Supports complex query filters with multiple criteria
- Shows extension configurations across multiple environments
- Demonstrates proper query structure for extension searches
"""

import os
import sys

# Add the src directory to the path to import the SDK
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

from boomi import Boomi

def query_extensions_by_environment(sdk, environment_id):
    """Query extensions for a specific environment."""
    
    print(f"🔍 Querying extensions for environment: {environment_id}")
    
    try:
        # Import the necessary query model classes
        from boomi.models import (
            EnvironmentExtensionsQueryConfig,
            EnvironmentExtensionsQueryConfigQueryFilter,
            EnvironmentExtensionsSimpleExpression,
            EnvironmentExtensionsSimpleExpressionOperator,
            EnvironmentExtensionsSimpleExpressionProperty
        )
        
        # Create query expression for specific environment
        simple_expression = EnvironmentExtensionsSimpleExpression(
            operator=EnvironmentExtensionsSimpleExpressionOperator.EQUALS,
            property=EnvironmentExtensionsSimpleExpressionProperty.ENVIRONMENT_ID,
            argument=[environment_id]
        )
        
        # Create query filter and config
        query_filter = EnvironmentExtensionsQueryConfigQueryFilter(expression=simple_expression)
        query_config = EnvironmentExtensionsQueryConfig(query_filter=query_filter)
        
        # Execute the query
        result = sdk.environment_extensions.query_environment_extensions(query_config)
        
        print("✅ Query executed successfully!")
        
        # Parse the response
        extensions_list = []
        if hasattr(result, '_kwargs'):
            print(f"   Response keys: {list(result._kwargs.keys())}")
            
            # Look for the query response data
            if 'EnvironmentExtensionsQueryResponse' in result._kwargs:
                query_data = result._kwargs['EnvironmentExtensionsQueryResponse']
                
                if 'EnvironmentExtensions' in query_data:
                    ext_data = query_data['EnvironmentExtensions']
                    if isinstance(ext_data, list):
                        extensions_list = ext_data
                    else:
                        extensions_list = [ext_data]
        
        return extensions_list
        
    except Exception as e:
        print(f"❌ Error querying extensions: {str(e)}")
        
        if hasattr(e, 'status'):
            if e.status == 403:
                print("\n   Permission denied (403)")
                print("   • Check if your account can query environment extensions")
            elif e.status == 400:
                print("\n   Bad request (400)")
                print("   • Check the query filter structure")
                print("   • Verify the environment ID format")
        
        return []

def query_extensions_by_extension_group(sdk, extension_group_id):
    """Query extensions for a specific extension group."""
    
    print(f"🔍 Querying extensions for extension group: {extension_group_id}")
    
    try:
        from boomi.models import (
            EnvironmentExtensionsQueryConfig,
            EnvironmentExtensionsQueryConfigQueryFilter,
            EnvironmentExtensionsSimpleExpression,
            EnvironmentExtensionsSimpleExpressionOperator,
            EnvironmentExtensionsSimpleExpressionProperty
        )
        
        # Create query expression for specific extension group
        simple_expression = EnvironmentExtensionsSimpleExpression(
            operator=EnvironmentExtensionsSimpleExpressionOperator.EQUALS,
            property=EnvironmentExtensionsSimpleExpressionProperty.EXTENSION_GROUP_ID,
            argument=[extension_group_id]
        )
        
        query_filter = EnvironmentExtensionsQueryConfigQueryFilter(expression=simple_expression)
        query_config = EnvironmentExtensionsQueryConfig(query_filter=query_filter)
        
        result = sdk.environment_extensions.query_environment_extensions(query_config)
        
        print("✅ Query executed successfully!")
        
        # Parse response (similar to above)
        extensions_list = []
        if hasattr(result, '_kwargs') and 'EnvironmentExtensionsQueryResponse' in result._kwargs:
            query_data = result._kwargs['EnvironmentExtensionsQueryResponse']
            if 'EnvironmentExtensions' in query_data:
                ext_data = query_data['EnvironmentExtensions']
                extensions_list = ext_data if isinstance(ext_data, list) else [ext_data]
        
        return extensions_list
        
    except Exception as e:
        print(f"❌ Error querying by extension group: {str(e)}")
        return []

def query_extensions_with_complex_filter(sdk, environment_id, extension_group_id):
    """Demonstrate complex query with multiple criteria."""
    
    print(f"🔍 Querying with complex filter...")
    print(f"   Environment ID: {environment_id}")
    print(f"   Extension Group ID: {extension_group_id}")
    
    try:
        from boomi.models import (
            EnvironmentExtensionsQueryConfig,
            EnvironmentExtensionsQueryConfigQueryFilter,
            EnvironmentExtensionsGroupingExpression,
            EnvironmentExtensionsGroupingExpressionOperator,
            EnvironmentExtensionsSimpleExpression,
            EnvironmentExtensionsSimpleExpressionOperator,
            EnvironmentExtensionsSimpleExpressionProperty
        )
        
        # Create first expression for environment ID
        env_expression = EnvironmentExtensionsSimpleExpression(
            operator=EnvironmentExtensionsSimpleExpressionOperator.EQUALS,
            property=EnvironmentExtensionsSimpleExpressionProperty.ENVIRONMENT_ID,
            argument=[environment_id]
        )
        
        # Create second expression for extension group ID
        group_expression = EnvironmentExtensionsSimpleExpression(
            operator=EnvironmentExtensionsSimpleExpressionOperator.EQUALS,
            property=EnvironmentExtensionsSimpleExpressionProperty.EXTENSION_GROUP_ID,
            argument=[extension_group_id]
        )
        
        # Combine with AND grouping expression
        grouping_expression = EnvironmentExtensionsGroupingExpression(
            operator=EnvironmentExtensionsGroupingExpressionOperator.AND,
            nested_expression=[env_expression, group_expression]
        )
        
        query_filter = EnvironmentExtensionsQueryConfigQueryFilter(expression=grouping_expression)
        query_config = EnvironmentExtensionsQueryConfig(query_filter=query_filter)
        
        result = sdk.environment_extensions.query_environment_extensions(query_config)
        
        print("✅ Complex query executed successfully!")
        
        # Parse response
        extensions_list = []
        if hasattr(result, '_kwargs') and 'EnvironmentExtensionsQueryResponse' in result._kwargs:
            query_data = result._kwargs['EnvironmentExtensionsQueryResponse']
            if 'EnvironmentExtensions' in query_data:
                ext_data = query_data['EnvironmentExtensions']
                extensions_list = ext_data if isinstance(ext_data, list) else [ext_data]
        
        return extensions_list
        
    except Exception as e:
        print(f"❌ Error with complex query: {str(e)}")
        return []

def display_extensions_summary(extensions_list):
    """Display summary of queried extensions."""
    
    if not extensions_list:
        print("   No extensions found matching the query criteria")
        print("\n💡 This could mean:")
        print("   • No extensions are configured for the specified criteria")
        print("   • The environment or extension group ID doesn't exist")
        print("   • There are permission issues accessing the extensions")
        return
    
    print(f"\n✅ Found {len(extensions_list)} extension configuration(s):")
    print("=" * 80)
    
    for i, ext in enumerate(extensions_list, 1):
        env_id = ext.get('@environmentId', 'N/A')
        ext_group_id = ext.get('@extensionGroupId', 'N/A')
        ext_id = ext.get('@id', 'N/A')
        
        print(f"\n{i}. Extension Configuration:")
        print(f"   ID: {ext_id}")
        print(f"   Environment ID: {env_id}")
        print(f"   Extension Group ID: {ext_group_id}")
        
        # Count different types of extensions
        extension_types = []
        if 'connections' in ext:
            conn_data = ext['connections']
            if 'connection' in conn_data:
                connections = conn_data['connection']
                count = len(connections) if isinstance(connections, list) else 1
                extension_types.append(f"Connections: {count}")
        
        if 'properties' in ext:
            prop_data = ext['properties']
            if 'property' in prop_data:
                properties = prop_data['property']
                count = len(properties) if isinstance(properties, list) else 1
                extension_types.append(f"Properties: {count}")
        
        if 'crossReferences' in ext:
            xref_data = ext['crossReferences']
            if 'crossReference' in xref_data:
                cross_refs = xref_data['crossReference']
                count = len(cross_refs) if isinstance(cross_refs, list) else 1
                extension_types.append(f"Cross References: {count}")
        
        if 'tradingPartners' in ext:
            tp_data = ext['tradingPartners']
            if 'tradingPartner' in tp_data:
                partners = tp_data['tradingPartner']
                count = len(partners) if isinstance(partners, list) else 1
                extension_types.append(f"Trading Partners: {count}")
        
        if extension_types:
            print(f"   Extension Types: {', '.join(extension_types)}")
        else:
            print("   Extension Types: None configured")

def get_available_environments(sdk):
    """Get list of available environments for user selection."""
    
    try:
        from boomi.models import (
            EnvironmentQueryConfig,
            EnvironmentQueryConfigQueryFilter,
            EnvironmentSimpleExpression,
            EnvironmentSimpleExpressionOperator,
            EnvironmentSimpleExpressionProperty
        )
        
        # Query for TEST environments
        simple_expression = EnvironmentSimpleExpression(
            operator=EnvironmentSimpleExpressionOperator.CONTAINS,
            property=EnvironmentSimpleExpressionProperty.CLASSIFICATION,
            argument=["TEST"]
        )
        
        query_filter = EnvironmentQueryConfigQueryFilter(expression=simple_expression)
        query_config = EnvironmentQueryConfig(query_filter=query_filter)
        
        result = sdk.environment.query_environment(query_config)
        
        environments = []
        if hasattr(result, '_kwargs') and 'EnvironmentQueryResponse' in result._kwargs:
            query_data = result._kwargs['EnvironmentQueryResponse']
            if 'Environment' in query_data:
                env_data = query_data['Environment']
                environments = env_data if isinstance(env_data, list) else [env_data]
        
        return environments[:3]  # Return first 3 for demo
        
    except Exception as e:
        print(f"   Could not retrieve environments: {str(e)}")
        return []

def main():
    """Main function to demonstrate environment extensions querying."""
    
    print("🚀 Boomi SDK - Query Environment Extensions")
    print("=" * 58)
    
    # Check for required environment variables
    required_vars = ["BOOMI_ACCOUNT", "BOOMI_USER", "BOOMI_SECRET"]
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars:
        print("❌ Missing required environment variables:")
        for var in missing_vars:
            print(f"   - {var}")
        sys.exit(1)
    
    # Initialize the SDK
    sdk = Boomi(
        account_id=os.getenv("BOOMI_ACCOUNT"),
        username=os.getenv("BOOMI_USER"),
        password=os.getenv("BOOMI_SECRET"),
        timeout=30000,
    )
    
    print("✅ SDK initialized successfully!")
    print()
    
    try:
        # Get some available environments to demonstrate queries
        print("🔍 Getting available environments for demo...")
        environments = get_available_environments(sdk)
        
        if environments:
            print(f"   Found {len(environments)} environments for demonstration")
            
            # Demonstrate query for first environment
            first_env = environments[0]
            env_id = first_env.get('@id')
            env_name = first_env.get('@name', 'Unknown')
            
            print(f"\n📋 Querying extensions for environment: {env_name}")
            print(f"   Environment ID: {env_id}")
            
            # Query extensions for this environment
            extensions = query_extensions_by_environment(sdk, env_id)
            display_extensions_summary(extensions)
            
        else:
            print("   No environments found for demonstration")
            print("\n💡 To test extension queries manually:")
            print("   1. Use list_environments.py to find available environment IDs")
            print("   2. Run this script with a known environment ID")
        
        print("\n📚 Query Examples Demonstrated:")
        print("=" * 60)
        print("✅ Query by Environment ID - Find all extensions for a specific environment")
        print("✅ Query by Extension Group ID - Find extensions for a specific group")
        print("✅ Complex Query with AND operator - Combine multiple criteria")
        
        print("\n💡 Use Cases for Extension Queries:")
        print("   • Find all environments using specific connection configurations")
        print("   • Audit extension configurations across multiple environments")
        print("   • Identify environments with specific property overrides")
        print("   • Search for environments with particular trading partner setups")
        print("   • Validate extension consistency across environment groups")
        
        print("\n🔧 Query Filter Options:")
        print("   • environmentId - Filter by specific environment")
        print("   • extensionGroupId - Filter by extension group")
        print("   • Use AND/OR operators to combine multiple criteria")
        print("   • Supports CONTAINS, EQUALS, and other comparison operators")
        
    except KeyboardInterrupt:
        print("\n❌ Operation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Example failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()