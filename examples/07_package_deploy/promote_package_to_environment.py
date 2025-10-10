#!/usr/bin/env python3
"""
Boomi SDK Example: Promote Package to Environment
================================================

This example demonstrates how to promote a deployed package from one environment 
to another. This is essential for CI/CD workflows (Dev→QA→Prod).

Features:
- Find deployed package in source environment
- Create deployment in target environment
- Handle environment-specific configurations
- Validate promotion prerequisites
- Monitor promotion progress
- Support for different promotion strategies

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- DEPLOYMENT privilege required
- Valid package ID and source environment
- Target environment must exist and be accessible

Usage:
    # Promote package from one environment to another
    python promote_package_to_environment.py PACKAGE_ID SOURCE_ENV_ID TARGET_ENV_ID
    
    # Promote with specific listener status
    python promote_package_to_environment.py PACKAGE_ID SOURCE_ENV_ID TARGET_ENV_ID --listener-status PAUSED
    
    # Promote with custom notes
    python promote_package_to_environment.py PACKAGE_ID SOURCE_ENV_ID TARGET_ENV_ID --notes "Promoting to production"
    
    # Preview promotion (no actual deployment)
    python promote_package_to_environment.py PACKAGE_ID SOURCE_ENV_ID TARGET_ENV_ID --preview-only

Examples:
    python promote_package_to_environment.py "91682a5d-5554-4754-9330-553563d58f75" "dev-env-id" "qa-env-id"
    python promote_package_to_environment.py "91682a5d-5554-4754-9330-553563d58f75" "qa-env-id" "prod-env-id" --listener-status RUNNING --notes "Production release v1.2.3"
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
from boomi.models import (
    DeployedPackage,
    DeployedPackageQueryConfig,
    DeployedPackageQueryConfigQueryFilter,
    DeployedPackageSimpleExpression,
    DeployedPackageSimpleExpressionOperator,
    DeployedPackageSimpleExpressionProperty,
    DeployedPackageGroupingExpression,
    DeployedPackageGroupingExpressionOperator
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


class PackagePromoter:
    """Manages package promotion between environments"""
    
    def __init__(self):
        """Initialize the Boomi SDK client"""
        account_id, username, password = validate_environment()
        
        self.sdk = Boomi(
            account_id=account_id,
            username=username,
            password=password,
            timeout=30000
        )
        print("✅ SDK initialized successfully")
    
    def find_deployed_package(self, package_id: str, source_env_id: str) -> Optional[Dict]:
        """Find deployed package in source environment"""
        try:
            print(f"\n🔍 Searching for package {package_id} in source environment...")
            
            # Create query to find the specific deployed package
            package_expr = DeployedPackageSimpleExpression(
                operator=DeployedPackageSimpleExpressionOperator.EQUALS,
                property=DeployedPackageSimpleExpressionProperty.PACKAGEID,
                argument=[package_id]
            )
            
            env_expr = DeployedPackageSimpleExpression(
                operator=DeployedPackageSimpleExpressionOperator.EQUALS,
                property=DeployedPackageSimpleExpressionProperty.ENVIRONMENTID,
                argument=[source_env_id]
            )
            
            # Combine expressions with AND
            combined_expr = DeployedPackageGroupingExpression(
                operator=DeployedPackageGroupingExpressionOperator.AND,
                nested_expression=[package_expr, env_expr]
            )
            
            query_filter = DeployedPackageQueryConfigQueryFilter(expression=combined_expr)
            query_config = DeployedPackageQueryConfig(query_filter=query_filter)
            
            result = self.sdk.deployed_package.query_deployed_package(request_body=query_config)
            
            if hasattr(result, 'result') and result.result:
                deployed_pkg = result.result[0]  # Should be only one match
                print(f"✅ Found deployed package in source environment")
                
                # Extract package information
                pkg_info = {
                    'package_id': getattr(deployed_pkg, 'package_id', package_id),
                    'component_id': getattr(deployed_pkg, 'component_id', 'N/A'),
                    'environment_id': getattr(deployed_pkg, 'environment_id', source_env_id),
                    'listener_status': getattr(deployed_pkg, 'listener_status', 'RUNNING'),
                    'deployed_date': getattr(deployed_pkg, 'deployed_date', 'N/A'),
                    'deployed_by': getattr(deployed_pkg, 'deployed_by', 'N/A'),
                    'notes': getattr(deployed_pkg, 'notes', '')
                }
                
                return pkg_info
            else:
                print(f"❌ Package {package_id} not found in source environment {source_env_id}")
                return None
                
        except Exception as e:
            print(f"❌ Error finding deployed package: {e}")
            return None
    
    def check_target_environment(self, target_env_id: str) -> bool:
        """Verify target environment exists and is accessible"""
        try:
            print(f"\n🔍 Validating target environment {target_env_id}...")
            
            env = self.sdk.environment.get_environment(id_=target_env_id)
            if env:
                env_name = getattr(env, 'name', 'Unknown')
                env_classification = getattr(env, 'classification', 'Unknown')
                print(f"✅ Target environment verified: {env_name} ({env_classification})")
                return True
            else:
                print(f"❌ Target environment {target_env_id} not found")
                return False
                
        except Exception as e:
            print(f"❌ Error validating target environment: {e}")
            return False
    
    def promote_package(self, package_info: Dict, target_env_id: str, 
                       listener_status: str = "RUNNING", 
                       notes: str = "", 
                       preview_only: bool = False) -> bool:
        """Promote package to target environment"""
        try:
            if preview_only:
                print(f"\n📋 PROMOTION PREVIEW (no actual deployment)")
            else:
                print(f"\n🚀 Promoting package to target environment...")
                
            print(f"   📦 Package ID: {package_info['package_id']}")
            print(f"   📄 Component ID: {package_info['component_id']}")
            print(f"   🎯 Target Environment: {target_env_id}")
            print(f"   🔧 Listener Status: {listener_status}")
            if notes:
                print(f"   📝 Notes: {notes}")
                
            if preview_only:
                print("✅ Promotion preview completed - no actual deployment performed")
                return True
            
            # Create deployment in target environment
            promotion_notes = notes or f"Promoted from environment {package_info['environment_id']} on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            
            deployed_package = DeployedPackage(
                package_id=package_info['package_id'],
                environment_id=target_env_id,
                listener_status=listener_status,
                notes=promotion_notes
            )
            
            result = self.sdk.deployed_package.create_deployed_package(request_body=deployed_package)
            
            if result:
                print("✅ Package promoted successfully!")
                
                # Display promotion details
                print(f"\n📋 PROMOTION DETAILS:")
                print(f"   📦 Package ID: {getattr(result, 'package_id', 'N/A')}")
                print(f"   🎯 Environment: {getattr(result, 'environment_id', target_env_id)}")
                print(f"   📅 Deployed Date: {getattr(result, 'deployed_date', 'N/A')}")
                print(f"   👤 Deployed By: {getattr(result, 'deployed_by', 'N/A')}")
                print(f"   🔧 Listener Status: {getattr(result, 'listener_status', listener_status)}")
                return True
            else:
                print("❌ Promotion failed - no result returned")
                return False
                
        except Exception as e:
            print(f"❌ Error during promotion: {e}")
            
            # Provide helpful troubleshooting hints
            error_msg = str(e)
            if "already exists" in error_msg.lower() or "duplicate" in error_msg.lower():
                print("🔍 Package may already be deployed to target environment")
                print("💡 Use query_deployed_packages.py to check existing deployments")
            elif "environment" in error_msg.lower():
                print("🔍 Environment access issue - verify environment ID and permissions")
            elif "package" in error_msg.lower():
                print("🔍 Package issue - verify package ID and source deployment")
            elif "403" in error_msg:
                print("🔍 Permission issue - check DEPLOYMENT privilege")
            elif "404" in error_msg:
                print("🔍 Resource not found - check package and environment IDs")
                
            return False


def main():
    """Main execution function"""
    parser = argparse.ArgumentParser(
        description="Promote deployed package from source to target environment",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python promote_package_to_environment.py pkg-123 dev-env qa-env
  python promote_package_to_environment.py pkg-123 qa-env prod-env --listener-status RUNNING --notes "Production release"
  python promote_package_to_environment.py pkg-123 dev-env qa-env --preview-only
        """
    )
    
    parser.add_argument("package_id", help="Package ID to promote")
    parser.add_argument("source_env_id", help="Source environment ID")
    parser.add_argument("target_env_id", help="Target environment ID")
    parser.add_argument("--listener-status", choices=["RUNNING", "PAUSED"], 
                       default="RUNNING", help="Listener status in target environment")
    parser.add_argument("--notes", help="Deployment notes")
    parser.add_argument("--preview-only", action="store_true", 
                       help="Preview promotion without actual deployment")
    
    args = parser.parse_args()
    
    print("🚀 Boomi SDK Example: Promote Package to Environment")
    print("=" * 60)
    
    try:
        promoter = PackagePromoter()
        
        # Step 1: Find package in source environment
        package_info = promoter.find_deployed_package(args.package_id, args.source_env_id)
        if not package_info:
            print(f"\n❌ Cannot proceed - package not found in source environment")
            sys.exit(1)
        
        # Step 2: Validate target environment
        if not promoter.check_target_environment(args.target_env_id):
            print(f"\n❌ Cannot proceed - target environment validation failed")
            sys.exit(1)
        
        # Step 3: Promote package
        success = promoter.promote_package(
            package_info=package_info,
            target_env_id=args.target_env_id,
            listener_status=args.listener_status,
            notes=args.notes or "",
            preview_only=args.preview_only
        )
        
        if success:
            print(f"\n✅ Package promotion {'previewed' if args.preview_only else 'completed'} successfully!")
        else:
            print(f"\n❌ Package promotion failed")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ Error during package promotion: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()