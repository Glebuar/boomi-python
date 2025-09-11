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
    python find_where_used.py 0864f99a-917f-457d-abc6-2762c0bb9b88
    python find_where_used.py 0864f99a-917f-457d-abc6-2762c0bb9b88 --type process
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
    print(f"   {index:2d}. Parent Component ID: {getattr(reference, 'parent_component_id', 'N/A')}")
    print(f"       Parent Version: {getattr(reference, 'parent_version', 'N/A')}")
    print(f"       Referenced Component ID: {getattr(reference, 'component_id', 'N/A')}")
    print(f"       Reference Type: {getattr(reference, 'type_', 'N/A')}")
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
        
        # Handle response - extract ComponentReference objects first
        component_references = []
        if hasattr(result, 'result') and result.result:
            component_references = result.result if isinstance(result.result, list) else [result.result]
        
        # Extract all references from the ComponentReference objects
        references = []
        for comp_ref in component_references:
            if hasattr(comp_ref, 'references') and comp_ref.references:
                references.extend(comp_ref.references)
        
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
            
            # Count by reference type
            reference_types = {}
            for ref in references:
                ref_type = getattr(ref, 'type_', 'Unknown')
                reference_types[ref_type] = reference_types.get(ref_type, 0) + 1
            
            if reference_types:
                print(f"  • Reference types:")
                for ref_type, count in sorted(reference_types.items()):
                    print(f"     • {ref_type}: {count}")
            
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
        component_id = "0864f99a-917f-457d-abc6-2762c0bb9b88"  # Test Date Data Map component
        print(f"ℹ️ No component_id provided, using default: {component_id}")
        print("💡 To use a different component, run: python find_where_used.py YOUR_COMPONENT_ID")
        print("💡 IMPORTANT: Replace this component ID with your own component ID for production use")
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