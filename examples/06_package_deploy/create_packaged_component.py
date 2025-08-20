#!/usr/bin/env python3
"""
Boomi SDK Example: Create Packaged Component
=============================================

This example demonstrates how to create a deployable package from components
using the Boomi SDK. When SDK model issues prevent direct usage, it falls back
to direct API calls.

Features:
- Create packaged components from existing components
- Validate component exists before packaging
- Set package metadata (version, notes, branch)
- Handle SDK model mapping issues gracefully
- Show created package details

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- Appropriate permissions to create packaged components

Usage:
    # Create package from component with auto-generated version
    python create_packaged_component.py COMPONENT_ID
    
    # Create package with custom version and notes
    python create_packaged_component.py COMPONENT_ID --version "1.0.0" --notes "Production release"
    
    # Create package on specific branch
    python create_packaged_component.py COMPONENT_ID --version "1.0.0" --branch "develop"

Examples:
    python create_packaged_component.py 186bc687-95b9-43f2-b64a-c86355ac8cf2
    python create_packaged_component.py 186bc687-95b9-43f2-b64a-c86355ac8cf2 --version "2.0.0" --notes "Enhanced workflow version"
    python create_packaged_component.py 112b4efe-b173-4258-9492-613ead7d52ce --version "1.5.0" --branch "main"
"""

import os
import sys
import argparse
import json
from datetime import datetime
from typing import Optional, Dict, Any

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.boomi import Boomi


class PackagedComponentCreator:
    """Manages packaged component creation operations"""
    
    def __init__(self):
        """Initialize the Boomi SDK client"""
        self.sdk = Boomi(
            account_id=os.getenv("BOOMI_ACCOUNT"),
            username=os.getenv("BOOMI_USER"),
            password=os.getenv("BOOMI_SECRET"),
            timeout=30000
        )
        print("✅ SDK initialized successfully")
    
    def validate_component_exists(self, component_id: str) -> Optional[Dict[str, Any]]:
        """Validate that the component exists and get its details"""
        print(f"\n🔍 Validating component exists: {component_id}")
        
        try:
            # Use SDK to get component - this should work for component validation
            component = self.sdk.component.get_component(component_id=component_id)
            
            if component:
                print("✅ Component found and accessible")
                
                # Extract component details for display
                component_info = {
                    'component_id': component_id,
                    'name': getattr(component, 'name', 'Unknown'),
                    'type': getattr(component, 'type', 'Unknown'),
                    'current_version': getattr(component, 'current_version', 'Unknown')
                }
                return component_info
            else:
                print("❌ Component not found")
                return None
                
        except Exception as e:
            print(f"❌ Failed to validate component: {e}")
            if hasattr(e, 'status') and e.status == 404:
                print("   Component not found or not accessible")
            return None
    
    def create_packaged_component_sdk(self, component_id: str, package_version: str, 
                                     notes: str, branch_name: str) -> Optional[Dict[str, Any]]:
        """Attempt to create packaged component using SDK"""
        print(f"\n📦 Attempting SDK creation...")
        
        try:
            # Due to SDK model issues with required package_id, this will likely fail
            # But we try it first in case the SDK gets fixed
            from src.boomi.models import PackagedComponent
            
            packaged_component = PackagedComponent(
                component_id=component_id,
                component_type='process',  # Default assumption, should be detected from component
                package_version=package_version,
                branch_name=branch_name,
                notes=notes,
                package_id='',  # This causes the issue - SDK requires it but API auto-generates it
                created_by=os.getenv('BOOMI_USER', 'SDK_User'),
                created_date=datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
            )
            
            result = self.sdk.packaged_component.create_packaged_component(request_body=packaged_component)
            print("✅ SDK creation successful!")
            return self._extract_component_dict(result)
            
        except Exception as e:
            print(f"❌ SDK creation failed: {e}")
            print("   Falling back to direct API call...")
            return None
    
    def create_packaged_component_api(self, component_id: str, package_version: str, 
                                     notes: str, branch_name: str) -> Optional[Dict[str, Any]]:
        """Create packaged component using direct API call"""
        print(f"\n📦 Creating via direct API call...")
        
        try:
            import requests
            from requests.auth import HTTPBasicAuth
            
            url = f"https://api.boomi.com/api/rest/v1/{os.getenv('BOOMI_ACCOUNT')}/PackagedComponent"
            auth = HTTPBasicAuth(os.getenv('BOOMI_USER'), os.getenv('BOOMI_SECRET'))
            headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
            
            # Create payload with required fields only
            payload = {
                "@type": "PackagedComponent",
                "componentId": component_id,
                "componentType": "process",  # Could be enhanced to detect actual type
                "packageVersion": package_version,
                "branchName": branch_name,
                "notes": notes
            }
            
            response = requests.post(url, json=payload, auth=auth, headers=headers)
            
            if response.status_code == 200:
                result = response.json()
                print("✅ API creation successful!")
                return result
            else:
                print(f"❌ API creation failed: HTTP {response.status_code}")
                print(f"   Response: {response.text[:200]}")
                return None
                
        except Exception as e:
            print(f"❌ API creation failed: {e}")
            return None
    
    def create_packaged_component(self, component_id: str, package_version: str, 
                                 notes: str, branch_name: str = "main") -> Optional[Dict[str, Any]]:
        """Create packaged component with SDK first, fallback to API"""
        
        # First try SDK (will likely fail due to model issues)
        result = self.create_packaged_component_sdk(component_id, package_version, notes, branch_name)
        
        # If SDK fails, use direct API
        if not result:
            result = self.create_packaged_component_api(component_id, package_version, notes, branch_name)
        
        return result
    
    def display_created_package(self, package_data: Dict[str, Any]) -> None:
        """Display created package information"""
        print("\n🎉 Packaged Component Created Successfully!")
        print("=" * 60)
        
        package_id = package_data.get('packageId', 'N/A')
        package_version = package_data.get('packageVersion', 'N/A')
        component_id = package_data.get('componentId', 'N/A')
        component_version = package_data.get('componentVersion', 'N/A')
        component_type = package_data.get('componentType', 'N/A')
        created_date = package_data.get('createdDate', 'N/A')
        created_by = package_data.get('createdBy', 'N/A')
        branch_name = package_data.get('branchName', 'N/A')
        notes = package_data.get('notes', 'None')
        
        print(f"📦 Package ID: {package_id}")
        print(f"🏷️  Package Version: {package_version}")
        print(f"🔧 Component ID: {component_id}")
        print(f"📊 Component Version: {component_version}")
        print(f"🏗️  Component Type: {component_type}")
        print(f"📅 Created Date: {created_date}")
        print(f"👤 Created By: {created_by}")
        print(f"🌿 Branch: {branch_name}")
        
        if notes and notes != 'None':
            print(f"📝 Notes: {notes}")
        
        print(f"\n💡 Next Steps:")
        print(f"   • Deploy to environment using: promote_package_to_environment.py")
        print(f"   • View package details with: get_packaged_component.py {package_id}")
        print(f"   • Delete if needed with: delete_packaged_component.py {package_id}")
    
    def _extract_component_dict(self, component) -> Dict[str, Any]:
        """Extract dictionary from SDK model object"""
        if hasattr(component, 'to_dict'):
            return component.to_dict()
        else:
            # Extract attributes manually
            comp_dict = {}
            for attr in dir(component):
                if not attr.startswith('_') and not callable(getattr(component, attr)):
                    value = getattr(component, attr)
                    if value is not None:
                        comp_dict[attr] = value
            return comp_dict


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='Create Boomi packaged components from existing components',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  %(prog)s 186bc687-95b9-43f2-b64a-c86355ac8cf2                          # Auto-generated version
  %(prog)s 186bc687-95b9-43f2-b64a-c86355ac8cf2 --version "2.0.0"       # Custom version  
  %(prog)s 112b4efe-b173-4258-9492-613ead7d52ce --version "1.5.0" --notes "Production release"

Component Types Supported:
  • process - Business processes
  • connector - Data connectors
  • webservice - Web services
  • flowservice - Flow services
        '''
    )
    
    parser.add_argument('component_id', metavar='COMPONENT_ID',
                       help='The component ID to package')
    parser.add_argument('--version', metavar='VERSION',
                       help='Package version (e.g., "1.0.0", "v2", etc.)')
    parser.add_argument('--notes', metavar='NOTES', default='',
                       help='Package description notes')
    parser.add_argument('--branch', metavar='BRANCH', default='main',
                       help='Branch name (default: main)')
    parser.add_argument('--validate-only', action='store_true',
                       help='Only validate component exists, do not create package')
    
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
    
    # Generate version if not provided
    if not args.version:
        import time
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        microseconds = int(time.time() * 1000000) % 1000000
        args.version = f"SDK_Gen_{timestamp}_{microseconds:06d}"
        print(f"💡 Auto-generated version: {args.version}")
    
    # Execute operation
    try:
        creator = PackagedComponentCreator()
        
        # Validate component exists
        component_info = creator.validate_component_exists(args.component_id)
        
        if not component_info:
            print(f"\n❌ Cannot proceed - component not found or not accessible: {args.component_id}")
            print("   • Check the component ID is correct")
            print("   • Ensure you have access to the component")
            print("   • Verify the component is not deleted")
            sys.exit(1)
        
        print(f"\n📋 Component Details:")
        print(f"   • Name: {component_info.get('name', 'Unknown')}")
        print(f"   • Type: {component_info.get('type', 'Unknown')}")
        print(f"   • Version: {component_info.get('current_version', 'Unknown')}")
        
        # If validate-only, stop here
        if args.validate_only:
            print(f"\n✅ Validation complete - component is accessible")
            return
        
        # Create packaged component
        print(f"\n🚀 Creating Packaged Component")
        print("=" * 50)
        
        result = creator.create_packaged_component(
            component_id=args.component_id,
            package_version=args.version,
            notes=args.notes,
            branch_name=args.branch
        )
        
        if result:
            creator.display_created_package(result)
            print(f"\n✅ Packaged component creation completed successfully!")
        else:
            print(f"\n❌ Failed to create packaged component")
            print("   • Check your permissions")
            print("   • Verify the component is not already packaged with this version")
            print("   • Try with a different version number")
            sys.exit(1)
    
    except KeyboardInterrupt:
        print("\n❌ Operation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()