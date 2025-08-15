#!/usr/bin/env python3
"""
Boomi SDK Example: List All Components

This example demonstrates how to query and display all components 
from the Boomi Platform API using the Python SDK. It shows components
in all folders including root folder.

Features:
- Lists all components in the account (all types)
- Shows component metadata (name, ID, version, folder, type, dates, etc.)
- Filters to show only current active versions by default
- Organizes results by folder structure and component type
- Provides detailed component information

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- Or create a .env file with these variables

Usage:
    python list_all_components.py [--all] [--type TYPE]
    
    Options:
    --all           Show all versions including deleted and non-current versions
    --type TYPE     Filter by component type (process, connector, profile, etc.)
"""

import os
import sys
sys.path.insert(0, '../../src')
from boomi import Boomi
from boomi.models import (
    ComponentMetadataQueryConfig, 
    ComponentMetadataQueryConfigQueryFilter,
    ComponentMetadataSimpleExpression,
    ComponentMetadataSimpleExpressionOperator,
    ComponentMetadataSimpleExpressionProperty
)

# Load environment variables from .env file if dotenv is available
try:
    from dotenv import load_dotenv
    # Load from the root directory
    load_dotenv('../../.env')
except ImportError:
    pass  # dotenv is optional

def format_date(date_str):
    """Format ISO date string to readable format"""
    if date_str and 'T' in date_str:
        return date_str.split('T')[0]  # Just return YYYY-MM-DD part
    return date_str or 'N/A'

def print_component_details(component, index):
    """Print detailed information for a single component"""
    print(f"   {index:2d}. {getattr(component, 'name', 'N/A')}")
    print(f"       Component ID: {getattr(component, 'component_id', 'N/A')}")
    print(f"       Type: {getattr(component, 'type_', 'N/A')}")
    print(f"       Version: {getattr(component, 'version', 'N/A')}")
    
    # Show version status
    current_version = getattr(component, 'current_version', 'false')
    deleted = getattr(component, 'deleted', 'false')
    status_indicators = []
    
    if str(current_version).lower() == 'true':
        status_indicators.append("CURRENT")
    if str(deleted).lower() == 'true':
        status_indicators.append("DELETED")
        
    if status_indicators:
        print(f"       Status: {' | '.join(status_indicators)}")
    
    print(f"       Created: {format_date(getattr(component, 'created_date', 'N/A'))} by {getattr(component, 'created_by', 'N/A')}")
    print(f"       Modified: {format_date(getattr(component, 'modified_date', 'N/A'))} by {getattr(component, 'modified_by', 'N/A')}")
    
    # Show folder path
    folder_path = getattr(component, 'folder_full_path', None) or getattr(component, 'folder_name', None)
    if folder_path:
        print(f"       Folder: {folder_path}")
    
    # Show branch info if available
    branch_name = getattr(component, 'branch_name', None)
    if branch_name and branch_name != 'main':
        print(f"       Branch: {branch_name}")
    
    print()

def query_all_components(show_all=False, component_type=None):
    """Query and display all components from Boomi"""
    
    # Check for required environment variables
    account_id = os.getenv("BOOMI_ACCOUNT")
    username = os.getenv("BOOMI_USER") 
    password = os.getenv("BOOMI_SECRET")
    
    if not all([account_id, username, password]):
        print("❌ Error: Missing required environment variables")
        print("   Please set: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET")
        return
    
    print(f"🏢 Account: {account_id}")
    print(f"👤 User: {username}")
    mode_desc = "all versions" if show_all else "current active versions only"
    type_filter = f" (type: {component_type})" if component_type else ""
    print(f"📋 Mode: {mode_desc}{type_filter}")
    
    # Initialize the Boomi SDK
    sdk = Boomi(
        account_id=account_id,
        username=username, 
        password=password,
        timeout=30000
    )
    
    print("\n🔍 Querying components...")
    
    try:
        # Create query config
        if component_type:
            # Query for specific component type
            expression = ComponentMetadataSimpleExpression(
                operator=ComponentMetadataSimpleExpressionOperator.EQUALS,
                property=ComponentMetadataSimpleExpressionProperty.TYPE,
                argument=[component_type]
            )
            query_filter = ComponentMetadataQueryConfigQueryFilter(expression=expression)
            query_config = ComponentMetadataQueryConfig(query_filter=query_filter)
        else:
            # Query for all components - use a filter that matches all components
            expression = ComponentMetadataSimpleExpression(
                operator=ComponentMetadataSimpleExpressionOperator.LIKE,
                property=ComponentMetadataSimpleExpressionProperty.NAME,
                argument=["%"]  # Wildcard that matches all names
            )
            query_filter = ComponentMetadataQueryConfigQueryFilter(expression=expression)
            query_config = ComponentMetadataQueryConfig(query_filter=query_filter)
        
        result = sdk.component_metadata.query_component_metadata(request_body=query_config)
        
        # Check results
        if hasattr(result, 'result') and result.result:
            all_components = result.result
            print(f"✅ Found {len(all_components)} total component version(s)")
            
            # Filter components based on mode
            if show_all:
                components = all_components
                print(f"📊 Showing all {len(components)} component versions")
            else:
                # Filter to current versions and non-deleted only  
                components = [c for c in all_components 
                             if str(getattr(c, 'current_version', 'false')).lower() == 'true'
                             and str(getattr(c, 'deleted', 'true')).lower() == 'false']
                print(f"📊 Showing {len(components)} current active component versions")
                
                if len(components) != len(all_components):
                    hidden_count = len(all_components) - len(components)
                    print(f"💡 {hidden_count} historical/deleted versions hidden (use --all to show)")
            
            if not components:
                print("📝 No components match the current filter criteria")
                return
            
            print("\n📂 Components by Folder and Type:")
            print("=" * 80)
            
            # Sort by folder, type, and name for better organization
            sorted_components = sorted(components, key=lambda x: (
                getattr(x, 'folder_full_path', '') or getattr(x, 'folder_name', '') or 'Root',
                getattr(x, 'type', ''),
                getattr(x, 'name', ''),
                int(getattr(x, 'version', '0'))
            ))
            
            # Group and display by folder and type
            current_folder = None
            current_type = None
            component_index = 1
            
            for component in sorted_components:
                folder = (getattr(component, 'folder_full_path', None) or 
                         getattr(component, 'folder_name', None) or 'Root')
                comp_type = getattr(component, 'type_', 'Unknown')
                
                # Print folder header when it changes
                if folder != current_folder:
                    if current_folder is not None:
                        print()
                    print(f"📁 Folder: {folder}")
                    print("   " + "-" * 70)
                    current_folder = folder
                    current_type = None  # Reset type when folder changes
                
                # Print type header when it changes within folder
                if comp_type != current_type:
                    if current_type is not None:
                        print()
                    print(f"   📋 Type: {comp_type}")
                    current_type = comp_type
                
                print_component_details(component, component_index)
                component_index += 1
            
            # Display summary statistics
            print("📊 Summary Statistics:")
            print("=" * 80)
            
            # Count by folder and type
            folder_counts = {}
            type_counts = {}
            unique_components = set()
            deleted_count = 0
            current_count = 0
            
            for component in components:
                folder = (getattr(component, 'folder_full_path', None) or 
                         getattr(component, 'folder_name', None) or 'Root')
                comp_type = getattr(component, 'type_', 'Unknown')
                
                folder_counts[folder] = folder_counts.get(folder, 0) + 1
                type_counts[comp_type] = type_counts.get(comp_type, 0) + 1
                unique_components.add(getattr(component, 'component_id', ''))
                
                if str(getattr(component, 'deleted', 'false')).lower() == 'true':
                    deleted_count += 1
                if str(getattr(component, 'current_version', 'false')).lower() == 'true':
                    current_count += 1
            
            print(f"  • Total component versions shown: {len(components)}")
            print(f"  • Unique components: {len(unique_components)}")
            if show_all:
                print(f"  • Current versions: {current_count}")
                print(f"  • Deleted versions: {deleted_count}")
            print(f"  • Folders with components: {len(folder_counts)}")
            print(f"  • Component types: {len(type_counts)}")
            
            print(f"\n  📁 Components per folder:")
            for folder, count in sorted(folder_counts.items()):
                print(f"     • {folder}: {count}")
            
            print(f"\n  📋 Components per type:")
            for comp_type, count in sorted(type_counts.items()):
                print(f"     • {comp_type}: {count}")
        
        else:
            print("❌ No components found")
            print("This could mean:")
            print("  • No components exist in the account")
            print("  • Insufficient permissions to view components") 
                
    except Exception as e:
        print(f"❌ Error querying components: {e}")
        print("Please check:")
        print("  • Environment variables are set correctly")
        print("  • Account has permission to query components")
        print("  • Network connectivity to Boomi API")

def main():
    """Main entry point"""
    show_all = '--all' in sys.argv
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
    
    print("🚀 Boomi SDK Example: List All Components")
    print("=" * 50)
    
    if show_all:
        print("🔍 Mode: Showing ALL component versions (including deleted)")
    else:
        print("🔍 Mode: Showing CURRENT ACTIVE components only")
        print("💡 Use --all flag to show all versions including deleted")
    
    if component_type:
        print(f"🎯 Filter: Only showing components of type '{component_type}'")
    else:
        print("🎯 Filter: Showing all component types")
        print("💡 Use --type TYPE to filter by specific component type")
    
    print()
    query_all_components(show_all, component_type)

if __name__ == "__main__":
    main()