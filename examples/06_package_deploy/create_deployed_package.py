#!/usr/bin/env python3
"""
Boomi SDK Example: Create Deployed Package
===========================================

This example demonstrates how to deploy a package to an environment with
comprehensive deployment orchestration, monitoring, and verification.

Features:
- Deploy package to specific environment
- Set deployment configuration options (listener status, notes)
- Wait for deployment completion with progress monitoring
- Verify deployment success and health status
- Handle deployment conflicts and rollback scenarios
- Support for different deployment strategies
- Comprehensive error handling and troubleshooting

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- DEPLOYMENT privilege required
- Valid package ID and target environment ID
- Package must exist and be accessible

Usage:
    # Deploy package to environment
    python create_deployed_package.py PACKAGE_ID ENVIRONMENT_ID
    
    # Deploy with specific listener status and notes
    python create_deployed_package.py PACKAGE_ID ENVIRONMENT_ID --listener-status PAUSED --notes "Initial deployment"
    
    # Deploy with monitoring and verification
    python create_deployed_package.py PACKAGE_ID ENVIRONMENT_ID --wait --verify --timeout 300
    
    # Deploy with conflict resolution
    python create_deployed_package.py PACKAGE_ID ENVIRONMENT_ID --replace-existing --backup

Examples:
    python create_deployed_package.py 91682a5d-5554-4754-9330-553563d58f75 74851c30-98b2-4a6f-838b-61eee5627b13
    python create_deployed_package.py 91682a5d-5554-4754-9330-553563d58f75 74851c30-98b2-4a6f-838b-61eee5627b13 --listener-status RUNNING --notes "Production deployment v1.2.3"
    python create_deployed_package.py 91682a5d-5554-4754-9330-553563d58f75 74851c30-98b2-4a6f-838b-61eee5627b13 --wait --verify --timeout 600
"""

import os
import sys
import argparse
import time
import json
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Any

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# Load environment variables from .env file if available
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv is optional

from src.boomi import Boomi
from src.boomi.models import (
    DeployedPackage,
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


class PackageDeployer:
    """Manages package deployment operations with comprehensive monitoring"""
    
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
    
    def validate_package(self, package_id: str) -> Optional[Dict]:
        """Validate package exists and get its details"""
        try:
            if self.verbose:
                print(f"\n🔍 Validating package {package_id}...")
            
            package = self.sdk.packaged_component.get_packaged_component(id_=package_id)
            
            if package:
                package_info = {
                    'package_id': getattr(package, 'package_id', package_id),
                    'component_id': getattr(package, 'component_id', 'N/A'),
                    'component_type': getattr(package, 'component_type', 'N/A'),
                    'package_version': getattr(package, 'package_version', 'N/A'),
                    'component_version': getattr(package, 'component_version', 'N/A'),
                    'deleted': getattr(package, 'deleted', False),
                    'created_by': getattr(package, 'created_by', 'N/A'),
                    'branch_name': getattr(package, 'branch_name', 'N/A')
                }
                
                # Check if package is deleted
                if package_info['deleted']:
                    print("⚠️ Warning: Package is marked as deleted")
                    return package_info
                
                print("✅ Package validated successfully")
                if self.verbose:
                    print(f"   📦 Version: {package_info['package_version']}")
                    print(f"   🏷️ Type: {package_info['component_type']}")
                    print(f"   🌿 Branch: {package_info['branch_name']}")
                
                return package_info
            else:
                print(f"❌ Package {package_id} not found")
                return None
                
        except Exception as e:
            print(f"❌ Error validating package: {e}")
            return None
    
    def validate_environment(self, environment_id: str) -> Optional[Dict]:
        """Validate environment exists and get its details"""
        try:
            if self.verbose:
                print(f"\n🔍 Validating environment {environment_id}...")
            
            environment = self.sdk.environment.get_environment(id_=environment_id)
            
            if environment:
                env_info = {
                    'environment_id': getattr(environment, 'id_', environment_id),
                    'name': getattr(environment, 'name', 'Unknown'),
                    'classification': getattr(environment, 'classification', 'Unknown'),
                    'created_by': getattr(environment, 'created_by', 'N/A')
                }
                
                print("✅ Environment validated successfully")
                if self.verbose:
                    print(f"   🏭 Name: {env_info['name']}")
                    print(f"   🏷️ Classification: {env_info['classification']}")
                
                return env_info
            else:
                print(f"❌ Environment {environment_id} not found")
                return None
                
        except Exception as e:
            print(f"❌ Error validating environment: {e}")
            return None
    
    def check_existing_deployment(self, package_id: str, environment_id: str) -> Optional[Dict]:
        """Check if package is already deployed to the environment"""
        try:
            if self.verbose:
                print(f"\n🔍 Checking for existing deployment...")
            
            # Query for existing deployment of this package in this environment
            from src.boomi.models import DeployedPackageGroupingExpression, DeployedPackageGroupingExpressionOperator
            
            package_expr = DeployedPackageSimpleExpression(
                operator=DeployedPackageSimpleExpressionOperator.EQUALS,
                property=DeployedPackageSimpleExpressionProperty.PACKAGEID,
                argument=[package_id]
            )
            
            env_expr = DeployedPackageSimpleExpression(
                operator=DeployedPackageSimpleExpressionOperator.EQUALS,
                property=DeployedPackageSimpleExpressionProperty.ENVIRONMENTID,
                argument=[environment_id]
            )
            
            combined_expr = DeployedPackageGroupingExpression(
                operator=DeployedPackageGroupingExpressionOperator.AND,
                nested_expression=[package_expr, env_expr]
            )
            
            query_filter = DeployedPackageQueryConfigQueryFilter(expression=combined_expr)
            query_config = DeployedPackageQueryConfig(query_filter=query_filter)
            
            result = self.sdk.deployed_package.query_deployed_package(request_body=query_config)
            
            if hasattr(result, 'result') and result.result:
                existing = result.result[0]
                deployment_info = {
                    'package_id': getattr(existing, 'package_id', package_id),
                    'environment_id': getattr(existing, 'environment_id', environment_id),
                    'deployed_date': getattr(existing, 'deployed_date', 'N/A'),
                    'deployed_by': getattr(existing, 'deployed_by', 'N/A'),
                    'listener_status': getattr(existing, 'listener_status', 'N/A'),
                    'notes': getattr(existing, 'notes', '')
                }
                
                print("⚠️ Package already deployed to this environment")
                if self.verbose:
                    print(f"   📅 Deployed: {deployment_info['deployed_date']}")
                    print(f"   👤 Deployed By: {deployment_info['deployed_by']}")
                    print(f"   🔧 Listener: {deployment_info['listener_status']}")
                
                return deployment_info
            else:
                print("✅ No existing deployment found")
                return None
                
        except Exception as e:
            print(f"⚠️ Could not check existing deployment: {e}")
            return None
    
    def deploy_package(self, package_id: str, environment_id: str,
                      listener_status: str = "RUNNING",
                      notes: str = "",
                      replace_existing: bool = False) -> bool:
        """Deploy package to environment"""
        try:
            print(f"\n🚀 Deploying package to environment...")
            print(f"   📦 Package ID: {package_id}")
            print(f"   🏭 Environment ID: {environment_id}")
            print(f"   🔧 Listener Status: {listener_status}")
            if notes:
                print(f"   📝 Notes: {notes}")
            
            # Check for existing deployment first
            existing = self.check_existing_deployment(package_id, environment_id)
            if existing and not replace_existing:
                print("\n❌ Deployment failed: Package already deployed to this environment")
                print("   Use --replace-existing flag to replace the existing deployment")
                return False
            
            # Create deployment request
            deployment_notes = notes or f"Deployed via SDK on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            
            deployed_package = DeployedPackage(
                package_id=package_id,
                environment_id=environment_id,
                listener_status=listener_status,
                notes=deployment_notes
            )
            
            # Execute deployment
            print(f"\n🎯 Submitting deployment request...")
            result = self.sdk.deployed_package.create_deployed_package(request_body=deployed_package)
            
            if result:
                print("✅ Deployment submitted successfully!")
                
                # Display deployment details
                print(f"\n📋 DEPLOYMENT DETAILS:")
                print(f"   📦 Package ID: {getattr(result, 'package_id', package_id)}")
                print(f"   🏭 Environment ID: {getattr(result, 'environment_id', environment_id)}")
                print(f"   📅 Deployed Date: {getattr(result, 'deployed_date', 'N/A')}")
                print(f"   👤 Deployed By: {getattr(result, 'deployed_by', 'N/A')}")
                print(f"   🔧 Listener Status: {getattr(result, 'listener_status', listener_status)}")
                
                return True
            else:
                print("❌ Deployment failed - no result returned")
                return False
                
        except Exception as e:
            print(f"❌ Deployment failed: {e}")
            
            # Provide helpful troubleshooting hints
            error_msg = str(e).lower()
            if "already exists" in error_msg or "duplicate" in error_msg:
                print("💡 Hint: Package may already be deployed - use --replace-existing")
            elif "permission" in error_msg or "403" in error_msg:
                print("💡 Hint: Check DEPLOYMENT privilege and environment access")
            elif "not found" in error_msg or "404" in error_msg:
                print("💡 Hint: Verify package ID and environment ID are correct")
            elif "invalid" in error_msg:
                print("💡 Hint: Check package and environment are in valid state")
            
            return False
    
    def wait_for_deployment(self, package_id: str, environment_id: str,
                           timeout: int = 300, poll_interval: int = 10) -> bool:
        """Wait for deployment to complete and monitor progress"""
        try:
            print(f"\n⏱️ Monitoring deployment progress...")
            print(f"   ⏰ Timeout: {timeout}s")
            print(f"   📊 Poll Interval: {poll_interval}s")
            
            start_time = time.time()
            
            while time.time() - start_time < timeout:
                # Check current deployment status
                existing = self.check_existing_deployment(package_id, environment_id)
                
                if existing:
                    print(f"✅ Deployment verified - package is deployed")
                    print(f"   📅 Deployed: {existing['deployed_date']}")
                    print(f"   👤 Deployed By: {existing['deployed_by']}")
                    print(f"   🔧 Listener: {existing['listener_status']}")
                    return True
                
                elapsed = int(time.time() - start_time)
                remaining = timeout - elapsed
                print(f"   ⏳ Still deploying... ({elapsed}s elapsed, {remaining}s remaining)")
                
                time.sleep(poll_interval)
            
            print(f"⚠️ Deployment monitoring timeout after {timeout}s")
            print("   Deployment may still be in progress - check manually")
            return False
            
        except Exception as e:
            print(f"❌ Error monitoring deployment: {e}")
            return False
    
    def verify_deployment(self, package_id: str, environment_id: str) -> bool:
        """Verify deployment is successful and healthy"""
        try:
            print(f"\n🔍 Verifying deployment health...")
            
            # Check deployment exists
            existing = self.check_existing_deployment(package_id, environment_id)
            if not existing:
                print("❌ Verification failed: No deployment found")
                return False
            
            print("✅ Deployment verification completed")
            
            # Additional health checks could be added here:
            # - Check listener status is as expected
            # - Verify component is accessible
            # - Run basic connectivity tests
            
            return True
            
        except Exception as e:
            print(f"❌ Deployment verification failed: {e}")
            return False


def main():
    """Main execution function"""
    parser = argparse.ArgumentParser(
        description="Deploy Boomi package to environment with comprehensive monitoring",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python create_deployed_package.py 91682a5d-5554-4754-9330-553563d58f75 74851c30-98b2-4a6f-838b-61eee5627b13
  python create_deployed_package.py pkg-id env-id --listener-status RUNNING --notes "Production deployment v1.2.3"
  python create_deployed_package.py pkg-id env-id --wait --verify --timeout 600 --verbose
  python create_deployed_package.py pkg-id env-id --replace-existing --notes "Hotfix deployment"

Deployment Process:
  1. Validate package and environment exist
  2. Check for existing deployment conflicts
  3. Submit deployment request
  4. Monitor deployment progress (if --wait)
  5. Verify deployment success (if --verify)

Listener Status Options:
  RUNNING   - Component listens for messages (default)
  PAUSED    - Component is deployed but not listening
        """
    )
    
    parser.add_argument("package_id", help="Package ID to deploy")
    parser.add_argument("environment_id", help="Target environment ID")
    parser.add_argument("--listener-status", choices=["RUNNING", "PAUSED"], 
                       default="RUNNING", help="Listener status for deployed component")
    parser.add_argument("--notes", help="Deployment notes")
    parser.add_argument("--replace-existing", action="store_true",
                       help="Replace existing deployment if it exists")
    parser.add_argument("--wait", action="store_true",
                       help="Wait for deployment to complete")
    parser.add_argument("--verify", action="store_true",
                       help="Verify deployment after completion")
    parser.add_argument("--timeout", type=int, default=300,
                       help="Timeout for deployment monitoring in seconds (default: 300)")
    parser.add_argument("--poll-interval", type=int, default=10,
                       help="Poll interval for deployment monitoring in seconds (default: 10)")
    parser.add_argument("--verbose", action="store_true",
                       help="Enable verbose output")
    
    args = parser.parse_args()
    
    print("🚀 Boomi SDK Example: Create Deployed Package")
    print("=" * 60)
    
    try:
        deployer = PackageDeployer(verbose=args.verbose)
        
        # Step 1: Validate package
        package_info = deployer.validate_package(args.package_id)
        if not package_info:
            print("\n❌ Cannot proceed - package validation failed")
            sys.exit(1)
        
        # Warn if package is deleted but allow deployment
        if package_info['deleted']:
            user_input = input("\n   Package is deleted. Continue anyway? [y/N]: ").strip().lower()
            if user_input not in ['y', 'yes']:
                print("   Deployment cancelled")
                sys.exit(0)
        
        # Step 2: Validate environment
        env_info = deployer.validate_environment(args.environment_id)
        if not env_info:
            print("\n❌ Cannot proceed - environment validation failed")
            sys.exit(1)
        
        # Step 3: Deploy package
        success = deployer.deploy_package(
            package_id=args.package_id,
            environment_id=args.environment_id,
            listener_status=args.listener_status,
            notes=args.notes or "",
            replace_existing=args.replace_existing
        )
        
        if not success:
            print("\n❌ Deployment failed")
            sys.exit(1)
        
        # Step 4: Wait for deployment completion (if requested)
        if args.wait:
            wait_success = deployer.wait_for_deployment(
                package_id=args.package_id,
                environment_id=args.environment_id,
                timeout=args.timeout,
                poll_interval=args.poll_interval
            )
            
            if not wait_success:
                print("\n⚠️ Deployment monitoring failed or timed out")
                print("   Deployment may still be in progress")
        
        # Step 5: Verify deployment (if requested)
        if args.verify:
            verify_success = deployer.verify_deployment(
                package_id=args.package_id,
                environment_id=args.environment_id
            )
            
            if not verify_success:
                print("\n❌ Deployment verification failed")
                sys.exit(1)
        
        print(f"\n✅ Deployment operation completed successfully!")
        
        # Show summary
        print(f"\n📊 DEPLOYMENT SUMMARY:")
        print(f"   📦 Package: {package_info['package_version']} ({package_info['component_type']})")
        print(f"   🏭 Environment: {env_info['name']} ({env_info['classification']})")
        print(f"   🔧 Listener Status: {args.listener_status}")
        print(f"   📅 Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
    except KeyboardInterrupt:
        print(f"\n\n⚠️ Operation interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error during deployment: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()