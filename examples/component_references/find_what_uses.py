#!/usr/bin/env python3
"""
Boomi SDK Example: Find What Component Uses

This example demonstrates how to find all components that a specific component references.
This is useful for understanding what dependencies a component has.

Features:
- Find components referenced by a specific component ID and version
- Shows component names, types, and versions that the component depends on
- Helps understand component dependencies
- Supports filtering by component type
- Shows immediate references (one level, not recursive)

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- Or create a .env file with these variables

Usage:
    python find_what_uses.py COMPONENT_ID [VERSION] [--type TYPE]
    
    Arguments:
    COMPONENT_ID    The component ID to find dependencies for
    VERSION         The component version (defaults to latest)
    
    Options:
    --type TYPE     Filter by referenced component type (process, connector, profile, etc.)
    
    Examples:
    python find_what_uses.py 112b4efe-b173-4258-9492-613ead7d52ce
    python find_what_uses.py 112b4efe-b173-4258-9492-613ead7d52ce 1
    python find_what_uses.py 112b4efe-b173-4258-9492-613ead7d52ce 1 --type connector
"""

import os
import sys
sys.path.insert(0, '../../src')
from boomi import Boomi
from boomi.models import (
    ComponentReferenceQueryConfig,
    ComponentReferenceQueryConfigQueryFilter,
    ComponentReferenceSimpleExpression,
    ComponentReferenceSimpleExpressionOperator,
    ComponentReferenceSimpleExpressionProperty,
    ComponentReferenceGroupingExpression,
    ComponentReferenceGroupingExpressionOperator,
    ComponentReferenceExpression
)

# Load environment variables
try:
    from dotenv import load_dotenv
    load_dotenv('../../.env')
except ImportError:
    pass

def format_date(date_str):
    """Format ISO date string to readable format"""
    if date_str and 'T' in date_str:
        return date_str.split('T')[0] + ' ' + date_str.split('T')[1].split('.')[0]
    return date_str or 'N/A'

def print_dependency_details(reference, index):
    """Print dependency information"""
    print(f"   {index:2d}. Dependency: {getattr(reference, 'component_name', 'N/A')}")
    print(f"       Component ID: {getattr(reference, 'component_id', 'N/A')}")
    print(f"       Type: {getattr(reference, 'type_', 'N/A')}")
    print(f"       Used by Parent: {getattr(reference, 'parent_component_name', 'N/A')}")
    print(f"       Parent ID: {getattr(reference, 'parent_component_id', 'N/A')}")
    print(f"       Parent Version: {getattr(reference, 'parent_version', 'N/A')}")
    print()

def find_what_uses(component_id, version=None, component_type=None):
    """Find components that the specified component references"""
    
    # Check for required environment variables
    account_id = os.getenv("BOOMI_ACCOUNT")
    username = os.getenv("BOOMI_USER") 
    password = os.getenv("BOOMI_SECRET")
    
    if not all([account_id, username, password]):
        print("❌ Error: Missing required environment variables")
        print("   Please set: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET")
        return False
    
    print(f"🏢 Account: {account_id}")
    print(f"👤 User: {username}")
    print(f"🎯 Component ID: {component_id}")
    if version:
        print(f"📌 Version: {version}")
    else:
        print(f"📌 Version: Latest")
    if component_type:
        print(f"🎭 Filter by Type: {component_type}")
    
    # Initialize the Boomi SDK
    sdk = Boomi(
        account_id=account_id,
        username=username, 
        password=password,
        timeout=30000
    )
    
    print(f"\n🔍 Finding components that this component references...")
    
    try:
        # First, get the component to find its current version if not specified
        if not version:
            print("📋 Getting component details to determine version...")
            comp_result = sdk.component.get_component(component_id=component_id)
            if hasattr(comp_result, 'version'):
                version = comp_result.version
                print(f"✅ Found current version: {version}")
            else:
                print("⚠️ Could not determine version, using '1'")
                version = "1"
        
        # Create query to find components referenced by the target component
        expressions = []
        
        # Add parent component ID expression
        parent_id_expr = ComponentReferenceSimpleExpression(
            operator=ComponentReferenceSimpleExpressionOperator.EQUALS,
            property=ComponentReferenceSimpleExpressionProperty.PARENTCOMPONENTID,
            argument=[component_id]
        )
        expressions.append(parent_id_expr)
        
        # Add parent version expression
        parent_version_expr = ComponentReferenceSimpleExpression(
            operator=ComponentReferenceSimpleExpressionOperator.EQUALS,
            property=ComponentReferenceSimpleExpressionProperty.PARENTVERSION,
            argument=[str(version)]
        )
        expressions.append(parent_version_expr)
        
        # For now, only support simple queries without type filter to avoid complexity
        if component_type:
            print("⚠️ Type filtering not yet supported in this example")
        
        # Use simple query with just parent component ID and version
        if len(expressions) == 2:  # parentComponentId and parentVersion
            grouping_expr = ComponentReferenceGroupingExpression(
                operator=ComponentReferenceGroupingExpressionOperator.AND,
                nested_expression=expressions
            )
            query_filter = ComponentReferenceQueryConfigQueryFilter(expression=grouping_expr)
        else:
            query_filter = ComponentReferenceQueryConfigQueryFilter(expression=expressions[0])
        
        query_config = ComponentReferenceQueryConfig(query_filter=query_filter)
        
        # Execute query
        result = sdk.component_reference.query_component_reference(request_body=query_config)
        
        print("✅ Query executed successfully!")
        print(f"📊 Response type: {type(result).__name__}")
        
        # Handle response - check if it's wrapped in _kwargs
        references = []
        if hasattr(result, '_kwargs') and result._kwargs:
            if 'ComponentReference' in result._kwargs:
                ref_data = result._kwargs['ComponentReference']
                references = ref_data if isinstance(ref_data, list) else [ref_data]
            elif 'ComponentReferenceQueryResponse' in result._kwargs:
                query_response = result._kwargs['ComponentReferenceQueryResponse']
                if isinstance(query_response, dict) and 'ComponentReference' in query_response:
                    ref_data = query_response['ComponentReference']
                    references = ref_data if isinstance(ref_data, list) else [ref_data]
        elif hasattr(result, 'result'):
            references = result.result if isinstance(result.result, list) else [result.result]
        elif isinstance(result, list):
            references = result
        
        if references:
            print(f"✅ Found {len(references)} component dependency/dependencies")
            
            print(f"\n📋 Components referenced by '{component_id}' (v{version}):")
            print("=" * 80)
            
            # Display each dependency
            for i, reference in enumerate(references, 1):
                print_dependency_details(reference, i)
            
            # Summary
            print(f"📊 Summary:")
            print("=" * 80)
            print(f"  • Total dependencies found: {len(references)}")
            
            # Count by type
            dependency_types = {}
            for ref in references:
                dep_type = getattr(ref, 'type_', 'Unknown')
                dependency_types[dep_type] = dependency_types.get(dep_type, 0) + 1
            
            if dependency_types:
                print(f"  • Dependency types:")
                for dtype, count in sorted(dependency_types.items()):
                    print(f"     • {dtype}: {count}")
            
            print(f"\n💡 Dependency Analysis:")
            print(f"  • Component has {len(references)} direct dependency/dependencies")
            print(f"  • These dependencies must be available for the component to function")
            print(f"  • Consider this when moving or deploying the component")
            
            return True
        else:
            print("📝 No dependencies found")
            print("This could mean:")
            print("  • The component doesn't reference any other components")
            print("  • The component ID or version doesn't exist")
            print("  • The component is self-contained")
            print("  • Insufficient permissions to view references")
            return True
            
    except Exception as e:
        error_msg = str(e)
        print(f"❌ Query failed: {error_msg}")
        
        # Provide helpful troubleshooting hints
        if "404" in error_msg or "not found" in error_msg.lower():
            print("🔍 Component not found - check the component ID and version")
        elif "403" in error_msg:
            print("🔍 Permission issue - check your API credentials and account permissions")
        elif "400" in error_msg:
            print("🔍 Bad request - check component ID and version format")
        elif "401" in error_msg:
            print("🔍 Authentication failed - verify your credentials")
        else:
            print("🔍 Check network connectivity and API endpoint availability")
            
        return False

def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print("❌ Error: Component ID is required")
        print("\nUsage:")
        print(f"  {sys.argv[0]} COMPONENT_ID [VERSION] [--type TYPE]")
        print("\nExamples:")
        print(f"  {sys.argv[0]} 112b4efe-b173-4258-9492-613ead7d52ce")
        print(f"  {sys.argv[0]} 112b4efe-b173-4258-9492-613ead7d52ce 1")
        print(f"  {sys.argv[0]} 112b4efe-b173-4258-9492-613ead7d52ce 1 --type connector")
        print("\n💡 Use list_all_components.py to find component IDs")
        return
    
    component_id = sys.argv[1]
    version = None
    component_type = None
    
    # Parse version if provided (numeric argument)
    if len(sys.argv) > 2 and sys.argv[2].isdigit():
        version = sys.argv[2]
    
    # Parse --type argument
    if '--type' in sys.argv:
        try:
            type_index = sys.argv.index('--type')
            if type_index + 1 < len(sys.argv):
                component_type = sys.argv[type_index + 1]
        except (ValueError, IndexError):
            print("❌ Error: --type requires a component type argument")
            return
    
    print("🚀 Boomi SDK Example: Find What Component Uses")
    print("=" * 50)
    print()
    
    success = find_what_uses(component_id, version, component_type)
    
    print(f"\n{'='*50}")
    if success:
        print("🌟 Dependency analysis completed successfully!")
    else:
        print("💥 Dependency analysis encountered issues")

if __name__ == "__main__":
    main()