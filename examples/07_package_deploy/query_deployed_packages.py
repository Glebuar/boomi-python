#!/usr/bin/env python3
"""
Boomi SDK Example: Query Deployed Packages
==========================================

This example demonstrates how to list and search deployed packages in Boomi
environments. It provides comprehensive deployment tracking and monitoring.

Features:
- List all deployed packages across environments
- Filter by environment, component type, or deployment status
- Track deployment history and dates
- Show active vs inactive deployments
- Group results by environment or component type
- Export deployment data to JSON

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- Appropriate permissions to query deployed packages

Usage:
    # List all deployed packages
    python query_deployed_packages.py --list
    
    # Filter by environment ID
    python query_deployed_packages.py --environment "74851c30-98b2-4a6f-838b-61eee5627b13"
    
    # Show only active deployments
    python query_deployed_packages.py --active-only
    
    # Filter by component type
    python query_deployed_packages.py --type process
    
    # Group by environment
    python query_deployed_packages.py --group-by environment
    
    # Export to JSON
    python query_deployed_packages.py --list --export deployments.json

Examples:
    python query_deployed_packages.py --list
    python query_deployed_packages.py --active-only --type process
    python query_deployed_packages.py --environment "env-id-123" --list
    python query_deployed_packages.py --group-by environment --summary
"""

import os
import sys
import argparse
import json
from datetime import datetime
from typing import List, Dict, Optional, Any
from collections import defaultdict
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
from boomi.models import DeployedPackageQueryConfig


class DeployedPackageQuerier:
    """Manages deployed package query operations"""
    
    def __init__(self):
        """Initialize the Boomi SDK client"""
        self.sdk = Boomi(
            account_id=os.getenv("BOOMI_ACCOUNT"),
            username=os.getenv("BOOMI_USER"),
            password=os.getenv("BOOMI_SECRET"),
            timeout=30000
        )
        print("✅ SDK initialized successfully")
    
    def _model_to_dict(self, model_obj) -> Dict[str, Any]:
        """Convert a model object to a dictionary for easier processing"""
        if hasattr(model_obj, '__dict__'):
            # Helper function to convert string booleans to actual booleans (SDK bug workaround)
            def str_to_bool(value):
                if isinstance(value, bool):
                    return value
                if isinstance(value, str):
                    return value.lower() in ('true', '1', 'yes', 'on')
                return bool(value)

            # Convert the model object to dict using its attributes
            result = {}
            for key, value in vars(model_obj).items():
                if not key.startswith('_') and value is not None:
                    # Handle enum values
                    if hasattr(value, 'value'):
                        result[key] = value.value
                    # Convert boolean string fields
                    elif key in ['active'] and isinstance(value, str):
                        result[key] = str_to_bool(value)
                    else:
                        result[key] = value
            return result
        else:
            # Fallback if it's already a dict or other type
            return model_obj if isinstance(model_obj, dict) else {}
    
    def query_all_deployed_packages(self) -> List[Dict[str, Any]]:
        """Query all deployed packages using SDK"""
        print("\n🔍 Querying all deployed packages...")
        
        try:
            # Create query config to get all deployed packages
            from boomi.models import (
                DeployedPackageQueryConfigQueryFilter,
                DeployedPackageSimpleExpression,
                DeployedPackageSimpleExpressionOperator,
                DeployedPackageSimpleExpressionProperty
            )

            # Use ISNOTNULL to get all packages with package IDs
            expression = DeployedPackageSimpleExpression(
                operator=DeployedPackageSimpleExpressionOperator.ISNOTNULL,
                property=DeployedPackageSimpleExpressionProperty.PACKAGEID,
                argument=[]
            )

            query_filter = DeployedPackageQueryConfigQueryFilter(expression=expression)
            query_config = DeployedPackageQueryConfig(query_filter=query_filter)
            
            # Query using SDK
            result = self.sdk.deployed_package.query_deployed_package(
                request_body=query_config
            )
            
            if hasattr(result, 'result') and result.result:
                packages = result.result
                total_count = result.number_of_results if hasattr(result, 'number_of_results') else len(packages)
                
                print(f"✅ Found {total_count} deployed package(s)")
                # Convert model objects to dicts for processing
                return [self._model_to_dict(pkg) for pkg in packages]
            else:
                print("✅ No deployed packages found")
                return []
                
        except Exception as e:
            print(f"❌ Failed to query deployed packages: {e}")
            return []
    
    def filter_packages(self, packages: List[Dict[str, Any]], 
                       environment_id: Optional[str] = None,
                       component_type: Optional[str] = None,
                       active_only: bool = False,
                       deployed_by: Optional[str] = None) -> List[Dict[str, Any]]:
        """Filter packages based on criteria"""
        
        filtered = packages
        
        if environment_id:
            print(f"🔍 Filtering by environment ID: {environment_id}")
            filtered = [p for p in filtered if p.get('environment_id', '') == environment_id]

        if component_type:
            print(f"🔍 Filtering by component type: {component_type}")
            filtered = [p for p in filtered if p.get('component_type', '').lower() == component_type.lower()]

        if active_only:
            print(f"🔍 Filtering to active deployments only")
            filtered = [p for p in filtered if p.get('active', False)]

        if deployed_by:
            print(f"🔍 Filtering by deployed by: {deployed_by}")
            filtered = [p for p in filtered if deployed_by.lower() in p.get('deployed_by', '').lower()]
        
        print(f"📊 Filter results: {len(filtered)} package(s) match criteria")
        return filtered
    
    def display_packages_summary(self, packages: List[Dict[str, Any]]) -> None:
        """Display summary statistics of deployed packages"""
        if not packages:
            print("📊 No packages to display")
            return
        
        print("\n📊 Deployment Summary:")
        print("=" * 60)
        
        # Count by various categories
        env_counts = {}
        type_counts = {}
        status_counts = {'active': 0, 'inactive': 0}
        deployer_counts = {}
        branch_counts = {}
        
        for pkg in packages:
            # Environment counts
            env_id = pkg.get('environment_id', 'Unknown')
            env_counts[env_id] = env_counts.get(env_id, 0) + 1

            # Type counts
            comp_type = pkg.get('component_type', 'Unknown')
            type_counts[comp_type] = type_counts.get(comp_type, 0) + 1

            # Status counts
            if pkg.get('active', False):
                status_counts['active'] += 1
            else:
                status_counts['inactive'] += 1

            # Deployer counts
            deployer = pkg.get('deployed_by', 'Unknown')
            deployer_counts[deployer] = deployer_counts.get(deployer, 0) + 1

            # Branch counts
            branch = pkg.get('branch_name', 'Unknown')
            branch_counts[branch] = branch_counts.get(branch, 0) + 1
        
        print(f"📦 Total Deployments: {len(packages)}")
        print(f"✅ Active: {status_counts['active']}")
        print(f"⏸️ Inactive: {status_counts['inactive']}")
        
        print(f"\n🏗️ Component Types:")
        for comp_type, count in sorted(type_counts.items()):
            print(f"   • {comp_type}: {count}")
        
        print(f"\n🌍 Top Environments:")
        sorted_envs = sorted(env_counts.items(), key=lambda x: x[1], reverse=True)
        for env_id, count in sorted_envs[:5]:
            # Truncate long environment IDs for display
            display_env = env_id[:20] + "..." if len(env_id) > 23 else env_id
            print(f"   • {display_env}: {count}")
        
        print(f"\n👥 Top Deployers:")
        sorted_deployers = sorted(deployer_counts.items(), key=lambda x: x[1], reverse=True)
        for deployer, count in sorted_deployers[:5]:
            print(f"   • {deployer}: {count}")
        
        print(f"\n🌿 Branches:")
        for branch, count in sorted(branch_counts.items()):
            print(f"   • {branch}: {count}")
    
    def display_packages_detailed(self, packages: List[Dict[str, Any]], limit: int = 20) -> None:
        """Display detailed package information"""
        if not packages:
            print("📋 No packages to display")
            return
        
        print(f"\n📋 Detailed Deployment List (showing {min(limit, len(packages))} of {len(packages)}):")
        print("=" * 120)
        
        for i, pkg in enumerate(packages[:limit], 1):
            deployment_id = pkg.get('deployment_id', 'N/A')
            package_id = pkg.get('package_id', 'N/A')
            package_version = pkg.get('package_version', 'N/A')
            component_id = pkg.get('component_id', 'N/A')
            component_type = pkg.get('component_type', 'N/A')
            environment_id = pkg.get('environment_id', 'N/A')
            deployed_date = pkg.get('deployed_date', 'N/A')
            deployed_by = pkg.get('deployed_by', 'N/A')
            active = pkg.get('active', False)
            version = pkg.get('version', 'N/A')
            notes = pkg.get('notes', '')
            branch_name = pkg.get('branch_name', 'N/A')
            
            # Status indicators
            status_icon = "✅" if active else "⏸️"
            
            print(f"{i:2}. 🚀 Deployment: {package_version} (v{version})")
            print(f"     🆔 Deployment ID: {deployment_id}")
            print(f"     📦 Package ID: {package_id}")
            print(f"     🔧 Component ID: {component_id}")
            print(f"     🏗️ Type: {component_type}")
            print(f"     🌍 Environment: {environment_id}")
            print(f"     {status_icon} Status: {'ACTIVE' if active else 'INACTIVE'}")
            print(f"     📅 Deployed: {self._format_date(deployed_date)}")
            print(f"     👤 Deployed By: {deployed_by}")
            print(f"     🌿 Branch: {branch_name}")
            
            if notes:
                # Truncate long notes
                display_notes = notes[:80] + "..." if len(notes) > 80 else notes
                print(f"     📝 Notes: {display_notes}")
            
            print()
        
        if len(packages) > limit:
            print(f"... and {len(packages) - limit} more deployments")
            print(f"💡 Use --limit {len(packages)} to see all results")
    
    def display_packages_grouped(self, packages: List[Dict[str, Any]], group_by: str) -> None:
        """Display packages grouped by specified field"""
        if not packages:
            print("📋 No packages to display")
            return
        
        print(f"\n📋 Deployments Grouped by {group_by.title()}:")
        print("=" * 80)
        
        # Group packages
        groups = defaultdict(list)
        for pkg in packages:
            if group_by == 'environment':
                key = pkg.get('environment_id', 'Unknown')
            elif group_by == 'component':
                key = pkg.get('component_id', 'Unknown')
            elif group_by == 'type':
                key = pkg.get('component_type', 'Unknown')
            elif group_by == 'deployer':
                key = pkg.get('deployed_by', 'Unknown')
            else:
                key = 'All'

            groups[key].append(pkg)
        
        # Display groups
        for group_key, group_packages in sorted(groups.items()):
            active_count = sum(1 for p in group_packages if p.get('active', False))
            inactive_count = len(group_packages) - active_count
            
            # Truncate long keys for display
            display_key = group_key[:50] + "..." if len(group_key) > 53 else group_key
            
            print(f"\n🔸 {display_key}")
            print(f"   📊 Total: {len(group_packages)} | ✅ Active: {active_count} | ⏸️ Inactive: {inactive_count}")
            
            # Show latest deployments for this group
            sorted_packages = sorted(group_packages,
                                   key=lambda x: x.get('deployed_date', ''),
                                   reverse=True)

            for i, pkg in enumerate(sorted_packages[:3], 1):
                package_version = pkg.get('package_version', 'N/A')
                deployed_date = pkg.get('deployed_date', 'N/A')
                status = "ACTIVE" if pkg.get('active', False) else "INACTIVE"
                print(f"     {i}. {package_version} - {status} ({self._format_date(deployed_date)})")
            
            if len(group_packages) > 3:
                print(f"     ... and {len(group_packages) - 3} more")
    
    def _format_date(self, date_string: str) -> str:
        """Format ISO date string to readable format"""
        try:
            if date_string and date_string != 'N/A':
                dt = datetime.fromisoformat(date_string.replace('Z', '+00:00'))
                return dt.strftime('%Y-%m-%d %H:%M UTC')
        except:
            pass
        return date_string or 'N/A'
    
    def export_to_json(self, packages: List[Dict[str, Any]], filename: str) -> bool:
        """Export packages to JSON file"""
        try:
            with open(filename, 'w') as f:
                json.dump({
                    'query_date': datetime.now().isoformat(),
                    'total_deployments': len(packages),
                    'deployments': packages
                }, f, indent=2)
            
            print(f"📄 Exported {len(packages)} deployments to {filename}")
            return True
        except Exception as e:
            print(f"❌ Failed to export to {filename}: {e}")
            return False
    
    def show_available_filters(self) -> None:
        """Show available filter options with examples"""
        print("\n🔍 Available Filter Options:")
        print("=" * 50)
        
        print("🌍 Environment Filtering:")
        print("   --environment ENV_ID    # Filter by specific environment")
        
        print("\n🏗️ Component Types:")
        print("   • process - Business processes")
        print("   • connector - Data connectors") 
        print("   • webservice - Web services")
        print("   • flowservice - Flow services")
        
        print("\n📊 Status Filtering:")
        print("   --active-only          # Show only active deployments")
        print("   --deployed-by USER     # Filter by deployer")
        
        print("\n📋 Grouping Options:")
        print("   --group-by environment # Group by environment")
        print("   --group-by component   # Group by component")
        print("   --group-by type        # Group by component type")
        print("   --group-by deployer    # Group by deployer")
        
        print("\n📊 Display Options:")
        print("   --limit 50             # Show more results")
        print("   --summary              # Show summary only")
        print("   --export results.json  # Export to JSON")


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='Query and analyze Boomi deployed packages',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  %(prog)s --list                                   # List all deployments
  %(prog)s --active-only                           # Show only active deployments
  %(prog)s --environment "74851c30-98b2-4a6f"     # Filter by environment
  %(prog)s --type process                          # Show only process deployments
  %(prog)s --group-by environment                  # Group by environment
  %(prog)s --deployed-by "alex.gurtoviy"           # Filter by deployer
  %(prog)s --list --export deployments.json       # Export to JSON

Filter Options:
  • Environment: Filter by specific environment ID
  • Component types: process, connector, webservice, flowservice
  • Active status: Show only currently active deployments
  • Deployer: Filter by who deployed the package

Grouping Options:
  • environment: Group deployments by environment
  • component: Group by component ID
  • type: Group by component type
  • deployer: Group by who deployed
        '''
    )
    
    # Action flags
    parser.add_argument('--list', action='store_true',
                       help='List all deployed packages')
    parser.add_argument('--summary', action='store_true',
                       help='Show summary statistics only')
    parser.add_argument('--filters-help', action='store_true',
                       help='Show available filter options')
    
    # Filter options
    parser.add_argument('--environment', metavar='ENV_ID',
                       help='Filter by environment ID')
    parser.add_argument('--type', metavar='TYPE',
                       help='Filter by component type (process, connector, etc.)')
    parser.add_argument('--active-only', action='store_true',
                       help='Show only active deployments')
    parser.add_argument('--deployed-by', metavar='USER',
                       help='Filter by deployer (partial match)')
    
    # Display options
    parser.add_argument('--group-by', metavar='FIELD',
                       choices=['environment', 'component', 'type', 'deployer'],
                       help='Group results by field (environment, component, type, deployer)')
    parser.add_argument('--limit', type=int, default=20, metavar='N',
                       help='Maximum number of packages to display (default: 20)')
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
        querier = DeployedPackageQuerier()
        
        # Show filter help
        if args.filters_help:
            querier.show_available_filters()
            return
        
        # Default to list if no specific action
        if not any([args.list, args.summary, args.group_by, args.environment, 
                   args.type, args.active_only, args.deployed_by]):
            args.list = True
        
        # Query packages
        print(f"\n🚀 Boomi Deployed Packages Query")
        print("=" * 50)
        
        packages = querier.query_all_deployed_packages()
        
        if not packages:
            print("❌ No deployed packages found")
            return
        
        # Apply filters
        filtered_packages = querier.filter_packages(
            packages,
            environment_id=args.environment,
            component_type=args.type,
            active_only=args.active_only,
            deployed_by=args.deployed_by
        )
        
        # Display results
        if args.summary or (not args.list and not args.group_by and filtered_packages):
            querier.display_packages_summary(filtered_packages)
        
        if args.group_by and filtered_packages:
            querier.display_packages_grouped(filtered_packages, args.group_by)
        elif args.list and filtered_packages:
            querier.display_packages_detailed(filtered_packages, args.limit)
        
        # Export if requested
        if args.export and filtered_packages:
            querier.export_to_json(filtered_packages, args.export)
        
        # Final summary
        if filtered_packages:
            print(f"\n✅ Query completed successfully")
            print(f"📊 Total found: {len(packages)} deployments")
            print(f"🎯 After filters: {len(filtered_packages)} deployments")
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