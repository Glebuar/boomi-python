#!/usr/bin/env python3
"""
Boomi SDK Example: Query Packaged Components
=============================================

This example demonstrates how to list and search packaged components in Boomi
using various filter criteria. It provides a comprehensive CLI interface for
package discovery and management.

Features:
- List all packaged components with pagination
- Search by component name or type
- Filter by author, creation date, or package version
- Show package details including deployment status
- Group results by component type or status
- Export results to JSON format

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- Appropriate permissions to query packaged components

Usage:
    # List all packaged components
    python query_packaged_components.py --list
    
    # Search by component type
    python query_packaged_components.py --type process
    
    # Filter by author
    python query_packaged_components.py --author "alex.gurtoviy@intapp.com"
    
    # Search by component ID
    python query_packaged_components.py --component-id "186bc687-95b9-43f2-b64a-c86355ac8cf2"
    
    # Show only active (non-deleted) packages
    python query_packaged_components.py --active-only
    
    # Export results to JSON
    python query_packaged_components.py --list --export results.json

Examples:
    python query_packaged_components.py --list
    python query_packaged_components.py --type process --active-only
    python query_packaged_components.py --author "john.doe@company.com"
    python query_packaged_components.py --component-id "123456789"
"""

import os
import sys
import argparse
import json
from datetime import datetime
from typing import List, Dict, Optional, Any
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
from boomi.models import PackagedComponentQueryConfig


class PackagedComponentQuerier:
    """Manages packaged component query operations"""
    
    def __init__(self):
        """Initialize the Boomi SDK client"""
        self.sdk = Boomi(
            account_id=os.getenv("BOOMI_ACCOUNT"),
            username=os.getenv("BOOMI_USER"),
            password=os.getenv("BOOMI_SECRET"),
            timeout=30000
        )
        print("✅ SDK initialized successfully")
    
    def _model_to_dict(self, obj) -> Dict[str, Any]:
        """Convert model object to dictionary"""
        if obj is None:
            return {}

        # Helper function to convert string booleans to actual booleans (SDK bug workaround)
        def str_to_bool(value):
            if isinstance(value, bool):
                return value
            if isinstance(value, str):
                return value.lower() in ('true', '1', 'yes', 'on')
            return bool(value)

        # Get all non-private, non-method attributes
        result = {}
        for attr_name in dir(obj):
            if not attr_name.startswith('_') and not callable(getattr(obj, attr_name, None)):
                try:
                    value = getattr(obj, attr_name)
                    # Convert boolean string fields
                    if attr_name in ['deleted', 'shareable', 'fully_publicly_consumable'] and isinstance(value, str):
                        result[attr_name] = str_to_bool(value)
                    else:
                        result[attr_name] = value
                except:
                    pass
        return result
    
    def query_all_packaged_components(self) -> List[Dict[str, Any]]:
        """Query all packaged components using SDK"""
        print("\n🔍 Querying all packaged components...")
        
        try:
            # Create query config to get all packaged components
            from boomi.models import (
                PackagedComponentQueryConfigQueryFilter,
                PackagedComponentSimpleExpression,
                PackagedComponentSimpleExpressionOperator
            )

            # Use ISNOTNULL to get all packages with component IDs
            expression = PackagedComponentSimpleExpression(
                operator=PackagedComponentSimpleExpressionOperator.ISNOTNULL,
                property="componentId",
                argument=[]
            )

            query_filter = PackagedComponentQueryConfigQueryFilter(expression=expression)
            query_config = PackagedComponentQueryConfig(query_filter=query_filter)
            
            # Query using SDK
            result = self.sdk.packaged_component.query_packaged_component(
                request_body=query_config
            )
            
            if hasattr(result, 'result') and result.result:
                components = result.result
                total_count = result.number_of_results if hasattr(result, 'number_of_results') else len(components)
                
                print(f"✅ Found {total_count} packaged component(s)")
                # Convert model objects to dicts for backward compatibility
                return [self._model_to_dict(comp) for comp in components]
            else:
                print("✅ No packaged components found")
                return []
                
        except Exception as e:
            print(f"❌ Failed to query packaged components: {e}")
            return []
    
    def filter_components(self, components: List[Dict[str, Any]], 
                         component_type: Optional[str] = None,
                         author: Optional[str] = None,
                         component_id: Optional[str] = None,
                         active_only: bool = False) -> List[Dict[str, Any]]:
        """Filter components based on criteria"""
        
        filtered = components
        
        if component_type:
            print(f"🔍 Filtering by component type: {component_type}")
            filtered = [c for c in filtered if c.get('component_type', '').lower() == component_type.lower()]

        if author:
            print(f"🔍 Filtering by author: {author}")
            filtered = [c for c in filtered if author.lower() in c.get('created_by', '').lower()]

        if component_id:
            print(f"🔍 Filtering by component ID: {component_id}")
            filtered = [c for c in filtered if c.get('component_id', '') == component_id]
        
        if active_only:
            print(f"🔍 Filtering to active (non-deleted) components only")
            filtered = [c for c in filtered if not c.get('deleted', False)]
        
        print(f"📊 Filter results: {len(filtered)} component(s) match criteria")
        return filtered
    
    def display_components_summary(self, components: List[Dict[str, Any]]) -> None:
        """Display summary statistics of components"""
        if not components:
            print("📊 No components to display")
            return
        
        print("\n📊 Component Summary:")
        print("=" * 60)
        
        # Count by type
        type_counts = {}
        status_counts = {'active': 0, 'deleted': 0}
        author_counts = {}
        branch_counts = {}
        
        for comp in components:
            # Type counts
            comp_type = comp.get('component_type', 'Unknown')
            type_counts[comp_type] = type_counts.get(comp_type, 0) + 1

            # Status counts
            if comp.get('deleted', False):
                status_counts['deleted'] += 1
            else:
                status_counts['active'] += 1

            # Author counts
            author = comp.get('created_by', 'Unknown')
            author_counts[author] = author_counts.get(author, 0) + 1

            # Branch counts
            branch = comp.get('branch_name', 'Unknown')
            branch_counts[branch] = branch_counts.get(branch, 0) + 1
        
        print(f"📦 Total Components: {len(components)}")
        print(f"✅ Active: {status_counts['active']}")
        print(f"🗑️ Deleted: {status_counts['deleted']}")
        
        print(f"\n🏗️ Component Types:")
        for comp_type, count in sorted(type_counts.items()):
            print(f"   • {comp_type}: {count}")
        
        print(f"\n👥 Top Authors:")
        sorted_authors = sorted(author_counts.items(), key=lambda x: x[1], reverse=True)
        for author, count in sorted_authors[:5]:
            print(f"   • {author}: {count}")
        
        print(f"\n🌿 Branches:")
        for branch, count in sorted(branch_counts.items()):
            print(f"   • {branch}: {count}")
    
    def display_components_detailed(self, components: List[Dict[str, Any]], limit: int = 20) -> None:
        """Display detailed component information"""
        if not components:
            print("📋 No components to display")
            return
        
        print(f"\n📋 Detailed Component List (showing {min(limit, len(components))} of {len(components)}):")
        print("=" * 100)
        
        for i, comp in enumerate(components[:limit], 1):
            package_id = comp.get('package_id', 'N/A')
            package_version = comp.get('package_version', 'N/A')
            component_id = comp.get('component_id', 'N/A')
            component_type = comp.get('component_type', 'N/A')
            created_date = comp.get('created_date', 'N/A')
            created_by = comp.get('created_by', 'N/A')
            deleted = comp.get('deleted', False)
            shareable = comp.get('shareable', False)
            branch_name = comp.get('branch_name', 'N/A')
            notes = comp.get('notes', '')
            
            # Status indicators
            status_icon = "🗑️" if deleted else "✅"
            share_icon = "🌐" if shareable else "🔒"
            
            print(f"{i:2}. 📦 Package: {package_version}")
            print(f"     🆔 Package ID: {package_id}")
            print(f"     🔧 Component ID: {component_id}")
            print(f"     🏗️ Type: {component_type}")
            print(f"     {status_icon} Status: {'DELETED' if deleted else 'ACTIVE'}")
            print(f"     {share_icon} Shareable: {'Yes' if shareable else 'No'}")
            print(f"     📅 Created: {self._format_date(created_date)}")
            print(f"     👤 Author: {created_by}")
            print(f"     🌿 Branch: {branch_name}")
            
            if notes:
                # Truncate long notes
                display_notes = notes[:100] + "..." if len(notes) > 100 else notes
                print(f"     📝 Notes: {display_notes}")
            
            print()
        
        if len(components) > limit:
            print(f"... and {len(components) - limit} more components")
            print(f"💡 Use --limit {len(components)} to see all results")
    
    def _format_date(self, date_string: str) -> str:
        """Format ISO date string to readable format"""
        try:
            if date_string and date_string != 'N/A':
                dt = datetime.fromisoformat(date_string.replace('Z', '+00:00'))
                return dt.strftime('%Y-%m-%d %H:%M UTC')
        except:
            pass
        return date_string or 'N/A'
    
    def export_to_json(self, components: List[Dict[str, Any]], filename: str) -> bool:
        """Export components to JSON file"""
        try:
            with open(filename, 'w') as f:
                json.dump({
                    'query_date': datetime.now().isoformat(),
                    'total_components': len(components),
                    'components': components
                }, f, indent=2)
            
            print(f"📄 Exported {len(components)} components to {filename}")
            return True
        except Exception as e:
            print(f"❌ Failed to export to {filename}: {e}")
            return False
    
    def show_available_filters(self) -> None:
        """Show available filter options with examples"""
        print("\n🔍 Available Filter Options:")
        print("=" * 50)
        
        print("🏗️ Component Types:")
        print("   • process - Business processes")
        print("   • connector - Data connectors") 
        print("   • webservice - Web services")
        print("   • flowservice - Flow services")
        print("   • certificate - Certificates")
        print("   • customlibrary - Custom libraries")
        
        print("\n🔍 Search Examples:")
        print("   --type process")
        print("   --author 'john.doe@company.com'")
        print("   --component-id '123456789'")
        print("   --active-only")
        
        print("\n📊 Display Options:")
        print("   --limit 50          # Show more results")
        print("   --summary           # Show summary only")
        print("   --export results.json  # Export to JSON")


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='Query and search Boomi packaged components',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  %(prog)s --list                                   # List all components
  %(prog)s --type process                           # Show only process components
  %(prog)s --author "alex.gurtoviy@intapp.com"      # Filter by author
  %(prog)s --component-id "186bc687-95b9-43f2"     # Find specific component
  %(prog)s --active-only                           # Show only active components
  %(prog)s --list --export components.json         # Export to JSON
  %(prog)s --summary                               # Show summary stats only

Filter Options:
  • Component types: process, connector, webservice, flowservice, certificate
  • Search by author email or username
  • Filter by component ID (exact match)
  • Show only active (non-deleted) components
        '''
    )
    
    # Action flags
    parser.add_argument('--list', action='store_true',
                       help='List all packaged components')
    parser.add_argument('--summary', action='store_true',
                       help='Show summary statistics only')
    parser.add_argument('--filters-help', action='store_true',
                       help='Show available filter options')
    
    # Filter options
    parser.add_argument('--type', metavar='TYPE',
                       help='Filter by component type (process, connector, etc.)')
    parser.add_argument('--author', metavar='AUTHOR',
                       help='Filter by author (partial match)')
    parser.add_argument('--component-id', metavar='COMPONENT_ID',
                       help='Filter by component ID (exact match)')
    parser.add_argument('--active-only', action='store_true',
                       help='Show only active (non-deleted) components')
    
    # Display options
    parser.add_argument('--limit', type=int, default=20, metavar='N',
                       help='Maximum number of components to display (default: 20)')
    parser.add_argument('--export', metavar='FILENAME',
                       help='Export results to JSON file')
    
    args = parser.parse_args()
    
    # Validate environment variables
    required_env = ['BOOMI_ACCOUNT', 'BOOMI_USER', 'BOOMI_SECRET']
    missing = [var for var in required_env if not os.getenv(var)]
    
    if missing:
        print("❌ Missing environment variables:")
        for var in missing:
            print(f"  - {var}")
        print("\n💡 Set these in your .env file or export them")
        sys.exit(1)
    
    # Execute operation
    try:
        querier = PackagedComponentQuerier()
        
        # Show filter help
        if args.filters_help:
            querier.show_available_filters()
            return
        
        # Default to list if no specific action
        if not args.list and not args.summary and not any([args.type, args.author, args.component_id, args.active_only]):
            args.list = True
        
        # Query components
        print(f"\n🚀 Boomi Packaged Components Query")
        print("=" * 50)
        
        components = querier.query_all_packaged_components()
        
        if not components:
            print("❌ No packaged components found")
            return
        
        # Apply filters
        filtered_components = querier.filter_components(
            components,
            component_type=args.type,
            author=args.author,
            component_id=args.component_id,
            active_only=args.active_only
        )
        
        # Display results
        if args.summary or (not args.list and filtered_components):
            querier.display_components_summary(filtered_components)
        
        if args.list and filtered_components:
            querier.display_components_detailed(filtered_components, args.limit)
        
        # Export if requested
        if args.export and filtered_components:
            querier.export_to_json(filtered_components, args.export)
        
        # Final summary
        if filtered_components:
            print(f"\n✅ Query completed successfully")
            print(f"📊 Total found: {len(components)} components")
            print(f"🎯 After filters: {len(filtered_components)} components")
            if args.export:
                print(f"📄 Exported to: {args.export}")
        
    except KeyboardInterrupt:
        print("\n❌ Operation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()