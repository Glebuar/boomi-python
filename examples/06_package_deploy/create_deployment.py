#!/usr/bin/env python3
"""
Boomi SDK Example: Create Deployment (Modern DeployedPackage API)
================================================================

This example demonstrates how to create deployments using the modern DeployedPackage API.
The legacy Deployment API is deprecated - this example uses the recommended approach.

Features:
- Deploy packaged components to environments
- Configure listener status (running/paused)
- Query existing deployments
- Bulk deployment operations
- Support for different deployment strategies

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- DEPLOYMENT privilege required
- Valid package ID
- Valid environment ID

Usage:
    # Deploy existing packaged component
    python create_deployment.py --package-id PACKAGE_ID --environment-id ENV_ID

    # Deploy with listener paused
    python create_deployment.py --package-id PACKAGE_ID --environment-id ENV_ID --listener-status PAUSED
    
    # Query existing deployments
    python create_deployment.py --query --environment-id ENV_ID
    
    # Query all deployments
    python create_deployment.py --query-all

Examples:
    python create_deployment.py --package-id "91682a5d-5554-4754-9330-553563d58f75" --environment-id "74851c30-98b2-4a6f-838b-61eee5627b13"
    python create_deployment.py --query --environment-id "74851c30-98b2-4a6f-838b-61eee5627b13"
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
    DeployedPackage,
    DeployedPackageQueryConfig,
    DeployedPackageQueryConfigQueryFilter,
    DeployedPackageSimpleExpression,
    DeployedPackageSimpleExpressionOperator,
    DeployedPackageSimpleExpressionProperty,
    QuerySort,
    SortField
)


class DeploymentManager:
    """Manages deployment operations using the modern DeployedPackage API"""
    
    def __init__(self):
        """Initialize the Boomi SDK client"""
        self.sdk = Boomi(
            account_id=os.getenv("BOOMI_ACCOUNT"),
            username=os.getenv("BOOMI_USER"),
            password=os.getenv("BOOMI_SECRET"),
            timeout=30000
        )
        print("✅ SDK initialized successfully")
    
    def deploy_package(self, package_id: str, environment_id: str, 
                      listener_status: Optional[str] = None,
                      notes: Optional[str] = None) -> Optional[Dict[str, Any]]:
        """Deploy an existing packaged component to an environment"""
        print(f"\n📦 Deploying package {package_id} to environment {environment_id}")
        
        try:
            # Create deployment request
            deployed_package = DeployedPackage(
                package_id=package_id,
                environment_id=environment_id
            )
            
            # Add listener status if specified
            if listener_status:
                deployed_package.listener_status = listener_status.upper()
                print(f"   📢 Listener status: {listener_status.upper()}")
            
            # Add notes if specified
            if notes:
                deployed_package.notes = notes
                print(f"   📝 Notes: {notes}")
            
            # Execute deployment
            result = self.sdk.deployed_package.create_deployed_package(request_body=deployed_package)
            
            if result:
                deployment_info = self._extract_deployment_info(result)
                print(f"✅ Package deployed successfully!")
                print(f"   🆔 Deployment ID: {deployment_info.get('id', 'N/A')}")
                print(f"   📦 Package ID: {deployment_info.get('package_id', 'N/A')}")
                print(f"   🌍 Environment: {deployment_info.get('environment_id', 'N/A')}")
                print(f"   📅 Deployed: {deployment_info.get('deployed_date', 'N/A')}")
                if deployment_info.get('listener_status'):
                    print(f"   📢 Listener Status: {deployment_info.get('listener_status')}")
                
                return deployment_info
            else:
                print("❌ Deployment failed: No result returned")
                return None
                
        except Exception as e:
            print(f"❌ Package deployment failed: {e}")
            return None
    
    
    def query_deployments(self, environment_id: Optional[str] = None,
                         package_id: Optional[str] = None,
                         limit: int = 10) -> List[Dict[str, Any]]:
        """Query existing deployments with optional filtering"""
        print(f"\n🔍 Querying deployments")
        if environment_id:
            print(f"   🌍 Environment filter: {environment_id}")
        if package_id:
            print(f"   📦 Package filter: {package_id}")
        
        try:
            # Build query expressions
            expressions = []
            
            if environment_id:
                env_expression = DeployedPackageSimpleExpression(
                    operator=DeployedPackageSimpleExpressionOperator.EQUALS,
                    property=DeployedPackageSimpleExpressionProperty.ENVIRONMENTID,
                    argument=[environment_id]
                )
                expressions.append(env_expression)
            
            if package_id:
                pkg_expression = DeployedPackageSimpleExpression(
                    operator=DeployedPackageSimpleExpressionOperator.EQUALS,
                    property=DeployedPackageSimpleExpressionProperty.PACKAGEID,
                    argument=[package_id]
                )
                expressions.append(pkg_expression)
            
            # Create query config
            query_config = DeployedPackageQueryConfig()
            
            if expressions:
                if len(expressions) == 1:
                    query_filter = DeployedPackageQueryConfigQueryFilter(
                        expression=expressions[0]
                    )
                else:
                    # Multiple filters - use AND logic
                    from src.boomi.models import DeployedPackageGroupingExpression
                    grouping_expression = DeployedPackageGroupingExpression(
                        operator="and",
                        nested_expression=expressions
                    )
                    query_filter = DeployedPackageQueryConfigQueryFilter(
                        expression=grouping_expression
                    )
                
                query_config.query_filter = query_filter
            
            # Add sorting by deployment date (newest first)
            # Note: Skip sorting for now as field names may vary
            # sort_field = SortField(field_name="deployedDate", sort_order="DESC") 
            # query_sort = QuerySort(sort_field=[sort_field])
            # query_config.query_sort = query_sort
            
            # Execute query
            result = self.sdk.deployed_package.query_deployed_package(request_body=query_config)
            
            if result and hasattr(result, 'result') and result.result:
                deployments = []
                for deployment in result.result[:limit]:
                    deployment_info = self._extract_deployment_info(deployment)
                    deployments.append(deployment_info)
                
                total_count = getattr(result, 'number_of_results', len(deployments))
                print(f"✅ Found {total_count} deployment(s)")
                
                return deployments
            else:
                print("✅ No deployments found")
                return []
                
        except Exception as e:
            print(f"❌ Query deployments failed: {e}")
            return []
    
    def get_deployment(self, deployment_id: str) -> Optional[Dict[str, Any]]:
        """Get details of a specific deployment"""
        print(f"\n🔍 Getting deployment {deployment_id}")
        
        try:
            result = self.sdk.deployed_package.get_deployed_package(id_=deployment_id)
            
            if result:
                deployment_info = self._extract_deployment_info(result)
                print(f"✅ Deployment found!")
                return deployment_info
            else:
                print("❌ Deployment not found")
                return None
                
        except Exception as e:
            print(f"❌ Get deployment failed: {e}")
            return None
    
    def delete_deployment(self, deployment_id: str) -> bool:
        """Undeploy a package from an environment"""
        print(f"\n🗑️ Undeploying package {deployment_id}")
        
        try:
            self.sdk.deployed_package.delete_deployed_package(id_=deployment_id)
            print(f"✅ Package undeployed successfully!")
            return True
        except Exception as e:
            print(f"❌ Undeploy failed: {e}")
            return False
    
    def _extract_deployment_info(self, deployment) -> Dict[str, Any]:
        """Extract deployment information into a standardized dict"""
        info = {}
        
        # Handle different attribute names
        for attr in dir(deployment):
            if not attr.startswith('_') and not callable(getattr(deployment, attr)):
                value = getattr(deployment, attr)
                if value is not None:
                    info[attr] = value
        
        # Standardize common fields
        deployment_dict = {
            'id': info.get('id') or info.get('deployment_id'),
            'package_id': info.get('package_id'),
            'component_id': info.get('component_id'),
            'environment_id': info.get('environment_id'),
            'deployed_date': info.get('deployed_date'),
            'deployed_by': info.get('deployed_by'),
            'listener_status': info.get('listener_status'),
            'notes': info.get('notes'),
            'version': info.get('version'),
            'package_version': info.get('package_version')
        }
        
        # Remove None values
        return {k: v for k, v in deployment_dict.items() if v is not None}
    
    def display_deployment_summary(self, deployment: Dict[str, Any]) -> None:
        """Display formatted deployment summary"""
        print(f"\n📋 Deployment Summary:")
        print("=" * 60)
        
        deployment_id = deployment.get('id', 'N/A')
        package_id = deployment.get('package_id', 'N/A')
        component_id = deployment.get('component_id', 'N/A')
        environment_id = deployment.get('environment_id', 'N/A')
        deployed_date = deployment.get('deployed_date', 'N/A')
        deployed_by = deployment.get('deployed_by', 'N/A')
        listener_status = deployment.get('listener_status', 'N/A')
        notes = deployment.get('notes', '')
        
        print(f"🆔 Deployment ID: {deployment_id}")
        if package_id != 'N/A':
            print(f"📦 Package ID: {package_id}")
        if component_id != 'N/A':
            print(f"🔧 Component ID: {component_id}")
        print(f"🌍 Environment ID: {environment_id}")
        print(f"📅 Deployed: {self._format_datetime(deployed_date)} by {deployed_by}")
        if listener_status != 'N/A':
            status_icon = '🟢' if listener_status == 'RUNNING' else '⏸️'
            print(f"📢 Listener Status: {status_icon} {listener_status}")
        if notes:
            print(f"📝 Notes: {notes}")
    
    def _format_datetime(self, datetime_string: str) -> str:
        """Format ISO datetime string to readable format"""
        try:
            if datetime_string and datetime_string != 'N/A':
                dt = datetime.fromisoformat(datetime_string.replace('Z', '+00:00'))
                return dt.strftime('%Y-%m-%d %H:%M:%S UTC')
        except:
            pass
        return datetime_string or 'N/A'


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='Create and manage Boomi deployments using DeployedPackage API',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  %(prog)s --package-id "pkg-123" --environment-id "env-456"              # Deploy package
  %(prog)s --package-id "pkg-123" --environment-id "env-456" --listener-status PAUSED  # Deploy paused
  %(prog)s --query --environment-id "env-456"                             # Query deployments
  %(prog)s --get-deployment "deployment-123"                              # Get specific deployment
  %(prog)s --undeploy "deployment-123"                                    # Undeploy package

Deployment Methods:
  • Package deployment: Deploy existing packaged component
  • Listener control: Deploy with RUNNING or PAUSED status
  
Notes:
  • The legacy Deployment API is deprecated
  • This uses the modern DeployedPackage API
  • Requires DEPLOYMENT privilege in Boomi
        '''
    )
    
    # Operation mode (mutually exclusive)
    operation_group = parser.add_mutually_exclusive_group(required=True)
    operation_group.add_argument('--package-id', metavar='ID',
                                help='Deploy existing packaged component')
    operation_group.add_argument('--query', action='store_true',
                                help='Query existing deployments')
    operation_group.add_argument('--query-all', action='store_true',
                                help='Query all deployments')
    operation_group.add_argument('--get-deployment', metavar='ID',
                                help='Get specific deployment by ID')
    operation_group.add_argument('--undeploy', metavar='ID',
                                help='Undeploy package by deployment ID')
    
    # Required for deployment operations
    parser.add_argument('--environment-id', metavar='ID',
                       help='Target environment ID (required for deploy operations)')
    
    # Optional deployment settings
    parser.add_argument('--listener-status', choices=['RUNNING', 'PAUSED'], metavar='STATUS',
                       help='Listener status for process deployments (RUNNING/PAUSED)')
    parser.add_argument('--notes', metavar='TEXT',
                       help='Deployment notes/comments')
    
    # Query options
    parser.add_argument('--limit', type=int, default=10, metavar='N',
                       help='Maximum results to return (default: 10)')
    parser.add_argument('--summary', action='store_true',
                       help='Show detailed summary for each deployment')
    
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
    
    # Validate required arguments for deployment operations
    if args.package_id and not args.environment_id:
        print("❌ --environment-id is required for deployment operations")
        sys.exit(1)
    
    # Execute operation
    try:
        manager = DeploymentManager()
        
        print(f"\n📦 Boomi Deployment Manager (DeployedPackage API)")
        print("=" * 55)
        
        if args.package_id:
            # Deploy existing package
            result = manager.deploy_package(
                args.package_id,
                args.environment_id,
                args.listener_status,
                args.notes
            )
            if result and args.summary:
                manager.display_deployment_summary(result)
        
        
        elif args.query or args.query_all:
            # Query deployments
            env_filter = args.environment_id if args.query else None
            deployments = manager.query_deployments(
                environment_id=env_filter,
                limit=args.limit
            )
            
            if deployments:
                print(f"\n📋 Found {len(deployments)} deployment(s):")
                for i, deployment in enumerate(deployments, 1):
                    print(f"\n{i}. Deployment {deployment.get('id', 'Unknown')}")
                    if args.summary:
                        manager.display_deployment_summary(deployment)
                    else:
                        pkg_id = deployment.get('package_id', 'N/A')
                        comp_id = deployment.get('component_id', 'N/A')
                        env_id = deployment.get('environment_id', 'N/A')
                        deployed_date = deployment.get('deployed_date', 'N/A')
                        
                        print(f"   📦 Package: {pkg_id}")
                        if comp_id != 'N/A':
                            print(f"   🔧 Component: {comp_id}")
                        print(f"   🌍 Environment: {env_id}")
                        print(f"   📅 Deployed: {manager._format_datetime(deployed_date)}")
        
        elif args.get_deployment:
            # Get specific deployment
            deployment = manager.get_deployment(args.get_deployment)
            if deployment:
                manager.display_deployment_summary(deployment)
        
        elif args.undeploy:
            # Undeploy package
            success = manager.delete_deployment(args.undeploy)
            if not success:
                sys.exit(1)
        
        print(f"\n🎉 Operation completed successfully!")
        
    except KeyboardInterrupt:
        print("\n❌ Operation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()