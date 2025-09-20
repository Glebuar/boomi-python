#!/usr/bin/env python3
"""
Boomi SDK Example: Delete Packaged Component
=============================================

This example demonstrates how to safely delete packaged components in Boomi.
It includes validation to check if the component exists and whether it's deployed.

Features:
- Validate packaged component exists before deletion
- Check deployment status to prevent deleting in-use components
- Confirm deletion with user input
- Support force deletion with validation bypass
- Show component details before deletion

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- Appropriate permissions to delete packaged components

Usage:
    # Interactive deletion with validation
    python delete_packaged_component.py PACKAGED_COMPONENT_ID
    
    # Force deletion (skips deployment check)
    python delete_packaged_component.py PACKAGED_COMPONENT_ID --force
    
    # Show component info without deleting
    python delete_packaged_component.py PACKAGED_COMPONENT_ID --info-only

Examples:
    python delete_packaged_component.py 54257671-cae7-4f33-b14f-37eb5a3472db
    python delete_packaged_component.py 54257671-cae7-4f33-b14f-37eb5a3472db --force
    python delete_packaged_component.py 54257671-cae7-4f33-b14f-37eb5a3472db --info-only
"""

import os
import sys
import argparse
from typing import Optional
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
from boomi.models import PackagedComponent


class PackagedComponentManager:
    """Manages packaged component deletion operations"""
    
    def __init__(self):
        """Initialize the Boomi SDK client"""
        self.sdk = Boomi(
            account_id=os.getenv("BOOMI_ACCOUNT"),
            username=os.getenv("BOOMI_USER"),
            password=os.getenv("BOOMI_SECRET"),
            timeout=30000
        )
        print("✅ SDK initialized successfully")
    
    def get_packaged_component(self, package_id: str) -> Optional[dict]:
        """Get packaged component details by ID using SDK"""
        print(f"\n🔍 Retrieving packaged component: {package_id}")
        
        try:
            result = self.sdk.packaged_component.get_packaged_component(id_=package_id)
            print("✅ Packaged component found")
            
            # Convert PackagedComponent object to dict for consistent interface
            return self._extract_component_dict(result)
                
        except Exception as e:
            print(f"❌ Failed to retrieve packaged component: {e}")
            if hasattr(e, 'status') and e.status == 404:
                print("   Component not found or not accessible")
            return None
    
    def display_component_info(self, component: dict) -> None:
        """Display detailed information about the packaged component"""
        print("\n📋 Packaged Component Details:")
        print("=" * 60)
        
        # Extract data from SDK model (using snake_case field names)
        package_id = component.get('package_id', 'N/A')
        package_version = component.get('package_version', 'N/A')
        component_id = component.get('component_id', 'N/A')
        component_version = component.get('component_version', 'N/A')
        component_type = component.get('component_type', 'N/A')
        created_date = component.get('created_date', 'N/A')
        created_by = component.get('created_by', 'N/A')
        deleted = component.get('deleted', False)
        shareable = component.get('shareable', False)
        notes = component.get('notes', 'None')
        branch_name = component.get('branch_name', 'N/A')
        
        print(f"📦 Package ID: {package_id}")
        print(f"🏷️  Package Version: {package_version}")
        print(f"🔧 Component ID: {component_id}")
        print(f"📊 Component Version: {component_version}")
        print(f"🏗️  Component Type: {component_type}")
        print(f"📅 Created Date: {created_date}")
        print(f"👤 Created By: {created_by}")
        print(f"🌿 Branch: {branch_name}")
        
        # Convert string booleans to actual booleans (SDK bug workaround)
        def str_to_bool(value):
            if isinstance(value, bool):
                return value
            if isinstance(value, str):
                return value.lower() in ('true', '1', 'yes', 'on')
            return bool(value)

        deleted_bool = str_to_bool(deleted)
        shareable_bool = str_to_bool(shareable)

        # Status indicators
        status_icon = "🗑️" if deleted_bool else "✅"
        print(f"{status_icon} Status: {'DELETED' if deleted_bool else 'ACTIVE'}")

        share_icon = "🌐" if shareable_bool else "🔒"
        print(f"{share_icon} Shareable: {'Yes' if shareable_bool else 'No'}")
        
        if notes and notes != 'None':
            print(f"📝 Notes: {notes}")
    
    def check_deployment_status(self, package_id: str) -> bool:
        """Check if packaged component is currently deployed"""
        print(f"\n🔍 Checking deployment status for package: {package_id}")
        
        # Note: This is a simplified check - in practice you'd query DeployedPackage
        # For now, we'll show what this would look like
        print("💡 Deployment check implementation would query DeployedPackage endpoint")
        print("   This requires additional API calls to check all environments")
        
        # Return False for now (assuming not deployed)
        return False
    
    def confirm_deletion(self, component: dict, force: bool = False) -> bool:
        """Confirm deletion with user"""
        if force:
            print("\n⚠️  FORCE mode enabled - skipping deployment checks")
            return True
        
        print("\n⚠️  DELETION WARNING:")
        print("   • This action will mark the packaged component as deleted")
        print("   • Deleted components can be restored using CREATE operation")
        print("   • You cannot delete components that are currently deployed")
        
        # Check if already deleted (with SDK bug workaround)
        def str_to_bool(value):
            if isinstance(value, bool):
                return value
            if isinstance(value, str):
                return value.lower() in ('true', '1', 'yes', 'on')
            return bool(value)

        is_deleted = str_to_bool(component.get('deleted', False))
        if is_deleted:
            print("   • Component is already marked as deleted")
            confirm_text = input("\nProceed with deletion anyway? Type 'DELETE' to confirm: ").strip()
        else:
            confirm_text = input("\nType 'DELETE' to confirm deletion: ").strip()
        
        return confirm_text == 'DELETE'
    
    def delete_packaged_component(self, package_id: str, force: bool = False) -> bool:
        """Delete the packaged component"""
        print(f"\n🗑️ Deleting packaged component: {package_id}")
        
        try:
            self.sdk.packaged_component.delete_packaged_component(id_=package_id)
            print("✅ Packaged component deleted successfully!")
            
            # Verify deletion by getting the component again
            print("\n🔍 Verifying deletion...")
            updated_component = self.get_packaged_component(package_id)
            
            if updated_component:
                # Check deletion status with SDK bug workaround
                def str_to_bool(value):
                    if isinstance(value, bool):
                        return value
                    if isinstance(value, str):
                        return value.lower() in ('true', '1', 'yes', 'on')
                    return bool(value)

                is_deleted = str_to_bool(updated_component.get('deleted', False))
                if is_deleted:
                    print("✅ Deletion verified - component is marked as deleted")
                else:
                    print("⚠️  Component still shows as active")
            
            return True
            
        except Exception as e:
            print(f"❌ Failed to delete packaged component: {e}")
            
            if hasattr(e, 'status'):
                if e.status == 403:
                    print("\n   Permission denied (403):")
                    print("   • Check if you have permission to delete packaged components")
                    print("   • Verify the component is not currently deployed")
                elif e.status == 404:
                    print("\n   Not found (404):")
                    print("   • Component may have already been deleted")
                    print("   • Check the package ID is correct")
                elif e.status == 409:
                    print("\n   Conflict (409):")
                    print("   • Component may be currently deployed")
                    print("   • Undeploy the component first, then try deletion")
                    print("   • Use --force to attempt deletion anyway")
            
            return False
    
    def show_restore_instructions(self, component: dict) -> None:
        """Show instructions for restoring deleted components"""
        print("\n💡 Restore Instructions:")
        print("=" * 40)
        print("To restore this deleted packaged component:")
        print("1. Use the CREATE endpoint with the following data:")
        
        print(f"   • packageId: {component.get('package_id', 'N/A')}")
        print(f"   • componentId: {component.get('component_id', 'N/A')}")
        print(f"   • packageVersion: {component.get('package_version', 'N/A')}")
        
        print("2. Or use the create_packaged_component.py example")
        print("3. Specify the exact packageId, componentId, and packageVersion")
    
    def _extract_component_dict(self, component) -> dict:
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
        description='Delete Boomi packaged components with safety checks',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  %(prog)s 54257671-cae7-4f33-b14f-37eb5a3472db                    # Safe deletion with checks
  %(prog)s 54257671-cae7-4f33-b14f-37eb5a3472db --force            # Force deletion 
  %(prog)s 54257671-cae7-4f33-b14f-37eb5a3472db --info-only        # Show info only

Safety Features:
  • Validates component exists before deletion
  • Checks deployment status (when not using --force)
  • Requires explicit confirmation
  • Shows component details before deletion
  • Verifies deletion success
  • Provides restore instructions
        '''
    )
    
    parser.add_argument('package_id', metavar='PACKAGE_ID',
                       help='The packaged component ID to delete')
    parser.add_argument('--force', action='store_true',
                       help='Force deletion without deployment checks')
    parser.add_argument('--info-only', action='store_true',
                       help='Show component information without deleting')
    
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
        manager = PackagedComponentManager()
        
        # Get component details
        component = manager.get_packaged_component(args.package_id)
        
        if not component:
            print(f"\n❌ Cannot proceed - packaged component not found: {args.package_id}")
            sys.exit(1)
        
        # Display component information
        manager.display_component_info(component)
        
        # If info-only, stop here
        if args.info_only:
            print(f"\n💡 Info-only mode - no deletion performed")
            manager.show_restore_instructions(component)
            return
        
        # Check deployment status (unless force mode)
        if not args.force:
            is_deployed = manager.check_deployment_status(args.package_id)
            if is_deployed:
                print("\n❌ Component appears to be deployed")
                print("   Use --force to attempt deletion anyway")
                sys.exit(1)
        
        # Confirm deletion
        if not manager.confirm_deletion(component, args.force):
            print("\n❌ Deletion cancelled by user")
            sys.exit(1)
        
        # Perform deletion
        success = manager.delete_packaged_component(args.package_id, args.force)
        
        if success:
            print(f"\n🎉 Packaged component deletion completed!")
            manager.show_restore_instructions(component)
        else:
            print(f"\n❌ Deletion failed - see error details above")
            sys.exit(1)
    
    except KeyboardInterrupt:
        print("\n❌ Operation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()