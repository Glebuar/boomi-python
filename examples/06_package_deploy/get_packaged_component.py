#!/usr/bin/env python3
"""
Boomi SDK Example: Get Packaged Component
==========================================

This example demonstrates how to retrieve and inspect packaged component details,
including metadata, contents, version history, and manifest information.

Features:
- Get package metadata and component details
- List all components included in package
- Show package version information and history
- Display deployment status across environments  
- Export package details to JSON
- Download package manifest (when available)

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- Valid package ID
- Appropriate permissions to view packaged components

Usage:
    # Get basic package information
    python get_packaged_component.py PACKAGE_ID
    
    # Get detailed package information with verbose output
    python get_packaged_component.py PACKAGE_ID --detailed --verbose
    
    # Export package details to JSON
    python get_packaged_component.py PACKAGE_ID --export package_details.json
    
    # Show deployment status across environments
    python get_packaged_component.py PACKAGE_ID --show-deployments

Examples:
    python get_packaged_component.py 91682a5d-5554-4754-9330-553563d58f75
    python get_packaged_component.py 91682a5d-5554-4754-9330-553563d58f75 --detailed --show-deployments
    python get_packaged_component.py 91682a5d-5554-4754-9330-553563d58f75 --export my_package.json
"""

import os
import sys
import argparse
import json
from datetime import datetime
from typing import List, Dict, Optional, Any

# Add parent directory to path for imports
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

# Load environment variables from .env file if available
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv is optional

from boomi import Boomi
from boomi.models import (
    PackagedComponent,
    PackagedComponentQueryConfig,
    PackagedComponentQueryConfigQueryFilter,
    PackagedComponentSimpleExpression,
    PackagedComponentSimpleExpressionOperator,
    DeployedPackageQueryConfig,
    DeployedPackageQueryConfigQueryFilter,
    DeployedPackageSimpleExpression,
    DeployedPackageSimpleExpressionOperator,
    DeployedPackageSimpleExpressionProperty
)


def validate_environment() -> tuple[str, str, str]:
    """Validate required environment variables and return credentials"""
    account_id = os.getenv("BOOMI_ACCOUNT")
    username = os.getenv("BOOMI_USER") 
    password = os.getenv("BOOMI_SECRET")
    
    if not all([account_id, username, password]):
        print("❌ Error: Missing required environment variables")
        print("   Please set: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET")
        print("   You can also create a .env file with these variables")
        sys.exit(1)
    
    return account_id, username, password


class PackageInspector:
    """Manages package inspection and analysis operations"""
    
    def __init__(self, verbose: bool = False):
        """Initialize the Boomi SDK client"""
        account_id, username, password = validate_environment()
        
        self.sdk = Boomi(
            account_id=account_id,
            username=username,
            password=password,
            timeout=30000
        )
        self.verbose = verbose
        print("✅ SDK initialized successfully")
    
    def get_package_details(self, package_id: str) -> Optional[Dict]:
        """Get detailed information about a packaged component"""
        try:
            if self.verbose:
                print(f"\n🔍 Retrieving package details for {package_id}...")
            
            # Get the packaged component
            package = self.sdk.packaged_component.get_packaged_component(id_=package_id)
            
            if package:
                # Extract package information
                # Helper function to convert string booleans to actual booleans (SDK bug workaround)
                def str_to_bool(value):
                    if isinstance(value, bool):
                        return value
                    if isinstance(value, str):
                        return value.lower() in ('true', '1', 'yes', 'on')
                    return bool(value)

                package_info = {
                    'package_id': getattr(package, 'package_id', package_id),
                    'component_id': getattr(package, 'component_id', 'N/A'),
                    'component_type': getattr(package, 'component_type', 'N/A'),
                    'package_version': getattr(package, 'package_version', 'N/A'),
                    'component_version': getattr(package, 'component_version', 'N/A'),
                    'created_date': getattr(package, 'created_date', 'N/A'),
                    'created_by': getattr(package, 'created_by', 'N/A'),
                    'deleted': str_to_bool(getattr(package, 'deleted', False)),
                    'shareable': str_to_bool(getattr(package, 'shareable', False)),
                    'fully_publicly_consumable': str_to_bool(getattr(package, 'fully_publicly_consumable', False)),
                    'branch_name': getattr(package, 'branch_name', 'N/A'),
                    'notes': getattr(package, 'notes', '')
                }
                
                print("✅ Package details retrieved successfully")
                return package_info
            else:
                print(f"❌ Package {package_id} not found")
                return None
                
        except Exception as e:
            print(f"❌ Error retrieving package details: {e}")
            return None
    
    def get_component_info(self, component_id: str) -> Optional[Dict]:
        """Get additional information about the component"""
        try:
            if self.verbose:
                print(f"   🔍 Getting component details for {component_id}...")
            
            component = self.sdk.component.get_component(component_id=component_id)
            
            if component:
                return {
                    'name': getattr(component, 'name', 'N/A'),
                    'type': getattr(component, 'type', 'N/A'),
                    'description': getattr(component, 'description', ''),
                    'folder_id': getattr(component, 'folder_id', 'N/A'),
                    'current_version': getattr(component, 'current_version', 'N/A'),
                    'version': getattr(component, 'version', 'N/A'),
                    'created_date': getattr(component, 'created_date', 'N/A'),
                    'created_by': getattr(component, 'created_by', 'N/A'),
                    'modified_date': getattr(component, 'modified_date', 'N/A'),
                    'modified_by': getattr(component, 'modified_by', 'N/A')
                }
            else:
                return None
                
        except Exception as e:
            if self.verbose:
                print(f"   ⚠️ Could not get component details: {e}")
            return None
    
    def get_package_versions(self, component_id: str) -> List[Dict]:
        """Get all versions of this package"""
        try:
            if self.verbose:
                print(f"   🔍 Getting package versions for component {component_id}...")
            
            # Query for all packages with this component ID
            query_expression = PackagedComponentSimpleExpression(
                operator=PackagedComponentSimpleExpressionOperator.EQUALS,
                property="componentId",
                argument=[component_id]
            )
            
            query_filter = PackagedComponentQueryConfigQueryFilter(expression=query_expression)
            query_config = PackagedComponentQueryConfig(query_filter=query_filter)
            
            result = self.sdk.packaged_component.query_packaged_component(request_body=query_config)
            
            versions = []
            if hasattr(result, 'result') and result.result:
                # Helper function to convert string booleans to actual booleans (SDK bug workaround)
                def str_to_bool(value):
                    if isinstance(value, bool):
                        return value
                    if isinstance(value, str):
                        return value.lower() in ('true', '1', 'yes', 'on')
                    return bool(value)

                for pkg in result.result:
                    versions.append({
                        'package_id': getattr(pkg, 'package_id', 'N/A'),
                        'package_version': getattr(pkg, 'package_version', 'N/A'),
                        'component_version': getattr(pkg, 'component_version', 'N/A'),
                        'created_date': getattr(pkg, 'created_date', 'N/A'),
                        'created_by': getattr(pkg, 'created_by', 'N/A'),
                        'deleted': str_to_bool(getattr(pkg, 'deleted', False)),
                        'branch_name': getattr(pkg, 'branch_name', 'N/A')
                    })
                
                # Sort by creation date (newest first)
                versions.sort(key=lambda x: x['created_date'] if x['created_date'] != 'N/A' else '', reverse=True)
            
            return versions
            
        except Exception as e:
            if self.verbose:
                print(f"   ⚠️ Could not get package versions: {e}")
            return []
    
    def get_deployment_status(self, package_id: str) -> List[Dict]:
        """Get deployment status across environments"""
        try:
            if self.verbose:
                print(f"   🔍 Getting deployment status for package {package_id}...")
            
            # Query for deployments of this package
            query_expression = DeployedPackageSimpleExpression(
                operator=DeployedPackageSimpleExpressionOperator.EQUALS,
                property=DeployedPackageSimpleExpressionProperty.PACKAGEID,
                argument=[package_id]
            )
            
            query_filter = DeployedPackageQueryConfigQueryFilter(expression=query_expression)
            query_config = DeployedPackageQueryConfig(query_filter=query_filter)
            
            result = self.sdk.deployed_package.query_deployed_package(request_body=query_config)
            
            deployments = []
            if hasattr(result, 'result') and result.result:
                for deployment in result.result:
                    # Get environment name
                    env_name = 'Unknown'
                    env_id = getattr(deployment, 'environment_id', 'N/A')
                    try:
                        env = self.sdk.environment.get_environment(id_=env_id)
                        if env:
                            env_name = getattr(env, 'name', 'Unknown')
                    except:
                        pass
                    
                    deployments.append({
                        'environment_id': env_id,
                        'environment_name': env_name,
                        'deployed_date': getattr(deployment, 'deployed_date', 'N/A'),
                        'deployed_by': getattr(deployment, 'deployed_by', 'N/A'),
                        'listener_status': getattr(deployment, 'listener_status', 'N/A'),
                        'notes': getattr(deployment, 'notes', '')
                    })
            
            return deployments
            
        except Exception as e:
            if self.verbose:
                print(f"   ⚠️ Could not get deployment status: {e}")
            return []
    
    def display_package_info(self, package_info: Dict, detailed: bool = False, show_deployments: bool = False):
        """Display package information in a formatted way"""
        print(f"\n📦 PACKAGE DETAILS")
        print("=" * 60)
        
        print(f"   🆔 Package ID: {package_info['package_id']}")
        print(f"   📄 Component ID: {package_info['component_id']}")
        print(f"   🏷️ Component Type: {package_info['component_type']}")
        print(f"   📦 Package Version: {package_info['package_version']}")
        print(f"   🔢 Component Version: {package_info['component_version']}")
        print(f"   📅 Created: {package_info['created_date']}")
        print(f"   👤 Created By: {package_info['created_by']}")
        
        # Status indicators
        status_indicators = []
        if package_info['deleted']:
            status_indicators.append("🗑️ DELETED")
        if package_info['shareable']:
            status_indicators.append("🤝 SHAREABLE")
        if package_info['fully_publicly_consumable']:
            status_indicators.append("🌍 PUBLIC")
        
        if status_indicators:
            print(f"   📊 Status: {' | '.join(status_indicators)}")
        
        if package_info['branch_name'] != 'N/A':
            print(f"   🌿 Branch: {package_info['branch_name']}")
        
        if package_info['notes']:
            print(f"   📝 Notes: {package_info['notes']}")
        
        # Get component details if detailed view requested
        if detailed and package_info['component_id'] != 'N/A':
            component_info = self.get_component_info(package_info['component_id'])
            if component_info:
                print(f"\n🔧 COMPONENT DETAILS")
                print("-" * 60)
                print(f"   📄 Name: {component_info['name']}")
                print(f"   🏷️ Type: {component_info['type']}")
                if component_info['description']:
                    print(f"   📝 Description: {component_info['description']}")
                print(f"   📁 Folder ID: {component_info['folder_id']}")
                print(f"   🔢 Current Version: {component_info['current_version']}")
                print(f"   📅 Created: {component_info['created_date']}")
                print(f"   👤 Created By: {component_info['created_by']}")
                print(f"   📅 Modified: {component_info['modified_date']}")
                print(f"   👤 Modified By: {component_info['modified_by']}")
            
            # Show package versions
            versions = self.get_package_versions(package_info['component_id'])
            if versions:
                print(f"\n📚 PACKAGE VERSIONS ({len(versions)} total)")
                print("-" * 60)
                for i, version in enumerate(versions[:5]):  # Show up to 5 versions
                    status = " (DELETED)" if version['deleted'] else ""
                    current = " ⭐" if version['package_id'] == package_info['package_id'] else ""
                    print(f"   {i+1}. v{version['package_version']} (comp v{version['component_version']}){current}{status}")
                    print(f"      📅 {version['created_date']} by {version['created_by']}")
                    if version['branch_name'] != 'N/A':
                        print(f"      🌿 Branch: {version['branch_name']}")
                if len(versions) > 5:
                    print(f"   ... and {len(versions) - 5} more version(s)")
        
        # Show deployment status
        if show_deployments:
            deployments = self.get_deployment_status(package_info['package_id'])
            if deployments:
                print(f"\n🚀 DEPLOYMENT STATUS ({len(deployments)} deployment(s))")
                print("-" * 60)
                for i, deployment in enumerate(deployments):
                    print(f"   {i+1}. 🏭 {deployment['environment_name']} ({deployment['environment_id']})")
                    print(f"      📅 Deployed: {deployment['deployed_date']}")
                    print(f"      👤 Deployed By: {deployment['deployed_by']}")
                    if deployment['listener_status'] != 'N/A':
                        print(f"      🔧 Listener: {deployment['listener_status']}")
                    if deployment['notes']:
                        print(f"      📝 Notes: {deployment['notes']}")
            else:
                print(f"\n🚀 DEPLOYMENT STATUS")
                print("-" * 60)
                print("   ⚠️ Package is not currently deployed to any environment")
    
    def export_to_json(self, package_info: Dict, filename: str, include_versions: bool = False, include_deployments: bool = False):
        """Export package details to JSON file"""
        try:
            export_data = {
                'package_info': package_info,
                'export_timestamp': datetime.now().isoformat(),
                'export_tool': 'Boomi SDK - Get Packaged Component'
            }
            
            if include_versions and package_info['component_id'] != 'N/A':
                export_data['versions'] = self.get_package_versions(package_info['component_id'])
            
            if include_deployments:
                export_data['deployments'] = self.get_deployment_status(package_info['package_id'])
            
            # Get component info if available
            if package_info['component_id'] != 'N/A':
                component_info = self.get_component_info(package_info['component_id'])
                if component_info:
                    export_data['component_info'] = component_info
            
            with open(filename, 'w') as f:
                json.dump(export_data, f, indent=2, default=str)
            
            print(f"\n✅ Package details exported to: {filename}")
            return True
            
        except Exception as e:
            print(f"\n❌ Error exporting to JSON: {e}")
            return False


def main():
    """Main execution function"""
    parser = argparse.ArgumentParser(
        description="Retrieve and inspect Boomi packaged component details",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python get_packaged_component.py 91682a5d-5554-4754-9330-553563d58f75
  python get_packaged_component.py 91682a5d-5554-4754-9330-553563d58f75 --detailed --show-deployments
  python get_packaged_component.py 91682a5d-5554-4754-9330-553563d58f75 --export package_details.json
  python get_packaged_component.py 91682a5d-5554-4754-9330-553563d58f75 --detailed --export full_details.json --show-deployments --verbose

Features:
  Basic View        - Package ID, version, component info, creation details
  Detailed View     - Component details, package version history
  Deployment View   - Shows where package is deployed across environments
  Export to JSON    - Save all package details for further analysis
        """
    )
    
    parser.add_argument("package_id", help="Package ID to inspect")
    parser.add_argument("--detailed", action="store_true",
                       help="Show detailed component information and version history")
    parser.add_argument("--show-deployments", action="store_true",
                       help="Show deployment status across environments")
    parser.add_argument("--export", metavar="FILENAME",
                       help="Export package details to JSON file")
    parser.add_argument("--verbose", action="store_true",
                       help="Enable verbose output")
    
    args = parser.parse_args()
    
    print("🚀 Boomi SDK Example: Get Packaged Component")
    print("=" * 60)
    
    try:
        inspector = PackageInspector(verbose=args.verbose)
        
        # Get package details
        package_info = inspector.get_package_details(args.package_id)
        if not package_info:
            print("\n❌ Package not found or inaccessible")
            sys.exit(1)
        
        # Display package information
        inspector.display_package_info(
            package_info=package_info,
            detailed=args.detailed,
            show_deployments=args.show_deployments
        )
        
        # Export to JSON if requested
        if args.export:
            success = inspector.export_to_json(
                package_info=package_info,
                filename=args.export,
                include_versions=args.detailed,
                include_deployments=args.show_deployments
            )
            if not success:
                sys.exit(1)
        
        print(f"\n✅ Package inspection completed successfully!")
        
        # Show summary
        status_msg = ""
        if package_info['deleted']:
            status_msg += " (DELETED)"
        
        print(f"\n📊 SUMMARY:")
        print(f"   📦 Package: {package_info['package_version']}{status_msg}")
        print(f"   🔢 Component Version: {package_info['component_version']}")
        print(f"   🏷️ Type: {package_info['component_type']}")
        print(f"   📅 Created: {package_info['created_date']}")
        
    except KeyboardInterrupt:
        print(f"\n\n⚠️ Operation interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error during package inspection: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()