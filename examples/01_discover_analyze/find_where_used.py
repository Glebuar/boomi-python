#!/usr/bin/env python3
"""
Boomi SDK Example: Find Where Component is Used

This example demonstrates how to find all components that reference a specific component.
This is useful for understanding dependencies and impact analysis before making changes.

Features:
- Find components that reference a specific component ID
- Shows component names, types, and versions that depend on the target component
- Helps with impact analysis before making changes
- Supports filtering by component type
- Shows immediate references (one level, not recursive)

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- Or create a .env file with these variables

Usage:
    python find_where_used.py COMPONENT_ID [--type TYPE]
    
    Arguments:
    COMPONENT_ID    The component ID to find references for
    
    Options:
    --type TYPE     Filter by component type (process, connector, profile, etc.)
    
    Examples:
    python find_where_used.py 112b4efe-b173-4258-9492-613ead7d52ce
    python find_where_used.py 112b4efe-b173-4258-9492-613ead7d52ce --type process
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
    ComponentReferenceGroupingExpressionOperator
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

def print_reference_details(reference, index):
    """Print reference information"""
    print(f"   {index:2d}. Parent Component: {getattr(reference, 'parent_component_name', 'N/A')}")
    print(f"       Parent ID: {getattr(reference, 'parent_component_id', 'N/A')}")
    print(f"       Parent Type: {getattr(reference, 'parent_type', 'N/A')}")
    print(f"       Parent Version: {getattr(reference, 'parent_version', 'N/A')}")
    print(f"       Referenced Component: {getattr(reference, 'component_name', 'N/A')}")
    print(f"       Referenced ID: {getattr(reference, 'component_id', 'N/A')}")
    print(f"       Referenced Type: {getattr(reference, 'type_', 'N/A')}")
    print()

def find_where_used(component_id, component_type=None):
    """Find components that reference the specified component"""
    
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
    print(f"🎯 Target Component ID: {component_id}")
    if component_type:
        print(f"🎭 Filter by Type: {component_type}")
    
    # Initialize the Boomi SDK
    sdk = Boomi(
        account_id=account_id,
        username=username, 
        password=password,
        timeout=30000
    )
    
    print(f"\n🔍 Finding components that reference this component...")
    
    try:
        # Create query to find components that reference the target component
        if component_type:
            # Create expressions for componentId and type
            component_expr = ComponentReferenceSimpleExpression(
                operator=ComponentReferenceSimpleExpressionOperator.EQUALS,
                property=ComponentReferenceSimpleExpressionProperty.COMPONENTID,
                argument=[component_id]
            )
            
            type_expr = ComponentReferenceSimpleExpression(
                operator=ComponentReferenceSimpleExpressionOperator.EQUALS,
                property=ComponentReferenceSimpleExpressionProperty.TYPE,
                argument=[component_type]
            )
            
            # Combine with AND
            grouping_expr = ComponentReferenceGroupingExpression(
                operator=ComponentReferenceGroupingExpressionOperator.AND,
                nested_expression=[component_expr, type_expr]
            )
            
            query_filter = ComponentReferenceQueryConfigQueryFilter(expression=grouping_expr)
        else:
            # Simple query for componentId only
            expression = ComponentReferenceSimpleExpression(
                operator=ComponentReferenceSimpleExpressionOperator.EQUALS,
                property=ComponentReferenceSimpleExpressionProperty.COMPONENTID,
                argument=[component_id]
            )
            query_filter = ComponentReferenceQueryConfigQueryFilter(expression=expression)
        
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
            print(f"✅ Found {len(references)} component reference(s)")
            
            print(f"\n📋 Components that reference '{component_id}':")
            print("=" * 80)
            
            # Display each reference
            for i, reference in enumerate(references, 1):
                print_reference_details(reference, i)
            
            # Summary
            print(f"📊 Summary:")
            print("=" * 80)
            print(f"  • Total references found: {len(references)}")
            
            # Count by parent type
            parent_types = {}
            for ref in references:
                parent_type = getattr(ref, 'parent_type', 'Unknown')
                parent_types[parent_type] = parent_types.get(parent_type, 0) + 1
            
            if parent_types:
                print(f"  • Parent component types:")
                for ptype, count in sorted(parent_types.items()):
                    print(f"     • {ptype}: {count}")
            
            print(f"\n💡 Impact Analysis:")
            print(f"  • {len(references)} component(s) depend on the target component")
            print(f"  • Changes to the target component may affect these dependencies")
            print(f"  • Consider testing all dependent components after modifications")
            
            return True
        else:
            print("📝 No references found")
            print("This could mean:")
            print("  • No components reference the target component")
            print("  • The component ID doesn't exist")
            print("  • The component is not used by any other components")
            print("  • Insufficient permissions to view references")
            return True
            
    except Exception as e:
        error_msg = str(e)
        print(f"❌ Query failed: {error_msg}")
        
        # Provide helpful troubleshooting hints
        if "404" in error_msg or "not found" in error_msg.lower():
            print("🔍 Component not found - check the component ID")
        elif "403" in error_msg:
            print("🔍 Permission issue - check your API credentials and account permissions")
        elif "400" in error_msg:
            print("🔍 Bad request - check component ID format")
        elif "401" in error_msg:
            print("🔍 Authentication failed - verify your credentials")
        else:
            print("🔍 Check network connectivity and API endpoint availability")
            
        return False

def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        component_id = "112b4efe-b173-4258-9492-613ead7d52ce"  # XML Example Test component
        print(f"ℹ️ No component_id provided, using default: {component_id}")
        print("💡 To use a different component, run: python find_where_used.py YOUR_COMPONENT_ID")
    else:
        component_id = sys.argv[1]
    component_type = None
    
    # Parse --type argument
    if '--type' in sys.argv:
        try:
            type_index = sys.argv.index('--type')
            if type_index + 1 < len(sys.argv):
                component_type = sys.argv[type_index + 1]
        except (ValueError, IndexError):
            print("❌ Error: --type requires a component type argument")
            return
    
    print("🚀 Boomi SDK Example: Find Where Component is Used")
    print("=" * 55)
    print()
    
    success = find_where_used(component_id, component_type)
    
    print(f"\n{'='*55}")
    if success:
        print("🌟 Where-used analysis completed successfully!")
    else:
        print("💥 Where-used analysis encountered issues")

if __name__ == "__main__":
    main()