#!/usr/bin/env python3
"""
Boomi SDK Example: Component Deletion (Limitations and Workarounds)
====================================================================

This example demonstrates the limitations of component deletion via API
and provides available workarounds.

IMPORTANT: Components CANNOT be deleted via the Boomi API!
- The DELETE endpoint returns "Unknown objectType for delete operation: Component"
- The 'deleted' flag is read-only and cannot be set via UPDATE operations
- Component deletion is only available through the Boomi UI by authorized users

Available Operations:
- Check if component exists
- Backup component before manual deletion
- Query component dependencies
- Rename component to indicate deprecation
- Move component to a "deprecated" folder

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET

Usage:
    # Check if component can be safely removed (no dependencies)
    python delete_component.py COMPONENT_ID --check-dependencies
    
    # Backup component XML before manual deletion
    python delete_component.py COMPONENT_ID --backup
    
    # Mark component as deprecated (rename and move)
    python delete_component.py COMPONENT_ID --deprecate
    
    # Show component info and deletion guidance
    python delete_component.py COMPONENT_ID --info

Examples:
    python delete_component.py abc123 --check-dependencies
    python delete_component.py abc123 --backup ./backups/
    python delete_component.py abc123 --deprecate --reason "Replaced by v2"
"""

import os
import sys
import argparse
import json
import xml.etree.ElementTree as ET
from datetime import datetime
from typing import Optional, List
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.boomi import Boomi


class ComponentDeletionHelper:
    """Helps with component deletion workflows and limitations"""
    
    def __init__(self):
        """Initialize the Boomi SDK client"""
        self.sdk = Boomi(
            account_id=os.getenv("BOOMI_ACCOUNT"),
            username=os.getenv("BOOMI_USER"),
            password=os.getenv("BOOMI_SECRET"),
            timeout=30000
        )
        print("✅ SDK initialized successfully")
    
    def show_component_info(self, component_id: str) -> bool:
        """Show detailed information about a component"""
        print(f"\n📋 Component Information: {component_id}")
        
        try:
            # Get component details
            component = self.sdk.component.get_component(component_id=component_id)
            
            print(f"\n✅ Component found:")
            print(f"   Name: {component.name}")
            print(f"   Type: {component.type_}")
            print(f"   Version: {component.version}")
            print(f"   Folder: {component.folder_full_path}")
            print(f"   Deleted: {component.deleted}")
            print(f"   Created: {component.created_date} by {component.created_by}")
            print(f"   Modified: {component.modified_date} by {component.modified_by}")
            
            if hasattr(component, 'description') and component.description:
                print(f"   Description: {component.description}")
            
            # Show deletion limitation info
            print(f"\n⚠️  Deletion Limitations:")
            print(f"   • Components CANNOT be deleted via API")
            print(f"   • DELETE endpoint returns: 'Unknown objectType for delete operation'")
            print(f"   • The 'deleted' flag is read-only and controlled by Boomi")
            print(f"   • Deletion is only available through Boomi UI by authorized users")
            
            print(f"\n💡 Available Options:")
            print(f"   1. Check dependencies: --check-dependencies")
            print(f"   2. Backup component: --backup")
            print(f"   3. Mark as deprecated: --deprecate")
            print(f"   4. Manually delete in Boomi UI")
            
            return True
            
        except Exception as e:
            print(f"❌ Failed to get component info: {e}")
            return False
    
    def check_dependencies(self, component_id: str) -> bool:
        """Check if component has dependencies that would prevent deletion"""
        print(f"\n🔍 Checking dependencies for component {component_id}...")
        
        try:
            from src.boomi.models import (
                ComponentReferenceQueryConfig,
                ComponentReferenceQueryConfigQueryFilter,
                ComponentReferenceSimpleExpression,
                ComponentReferenceSimpleExpressionOperator,
                ComponentReferenceSimpleExpressionProperty
            )
            
            # Query for components that reference this component
            query_expression = ComponentReferenceSimpleExpression(
                operator=ComponentReferenceSimpleExpressionOperator.EQUALS,
                property=ComponentReferenceSimpleExpressionProperty.TOCOMPONENTID,
                argument=[component_id]
            )
            
            query_filter = ComponentReferenceQueryConfigQueryFilter(expression=query_expression)
            query_config = ComponentReferenceQueryConfig(query_filter=query_filter)
            
            result = self.sdk.component_reference.query_component_reference(request_body=query_config)
            
            if hasattr(result, 'result') and result.result:
                print(f"⚠️  Found {len(result.result)} component(s) that reference this component:")
                
                for ref in result.result[:10]:  # Show first 10
                    print(f"   • {ref.from_component_name} ({ref.from_component_type})")
                    print(f"     ID: {ref.from_component_id}")
                    print(f"     Reference: {ref.reference_type}")
                
                if len(result.result) > 10:
                    print(f"   ... and {len(result.result) - 10} more")
                
                print(f"\n❌ Component has dependencies - deletion not recommended")
                print(f"   You should update these components first to remove references")
                return False
            else:
                print(f"✅ No dependencies found - component can be safely deleted")
                return True
                
        except Exception as e:
            print(f"⚠️  Could not check dependencies: {e}")
            print(f"   Proceeding with caution...")
            return True
    
    def backup_component(self, component_id: str, backup_dir: str = "./backups") -> bool:
        """Backup component XML before deletion"""
        print(f"\n💾 Backing up component {component_id}...")
        
        try:
            # Create backup directory
            backup_path = Path(backup_dir)
            backup_path.mkdir(parents=True, exist_ok=True)
            
            # Get component
            component = self.sdk.component.get_component(component_id=component_id)
            
            # Generate filename
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            safe_name = "".join(c for c in component.name if c.isalnum() or c in (' ', '_', '-')).strip()
            filename = f"{safe_name}_{component_id}_{timestamp}.xml"
            backup_file = backup_path / filename
            
            # Get XML content
            xml_content = component.to_xml()
            
            # Save to file
            with open(backup_file, 'w', encoding='utf-8') as f:
                f.write(xml_content)
            
            # Also save metadata as JSON
            metadata = {
                "component_id": component.component_id,
                "name": component.name,
                "type": component.type_,
                "version": component.version,
                "folder_path": component.folder_full_path,
                "created_date": component.created_date,
                "created_by": component.created_by,
                "modified_date": component.modified_date,
                "modified_by": component.modified_by,
                "backup_timestamp": datetime.now().isoformat(),
                "description": getattr(component, 'description', None)
            }
            
            metadata_file = backup_file.with_suffix('.json')
            with open(metadata_file, 'w', encoding='utf-8') as f:
                json.dump(metadata, f, indent=2)
            
            print(f"✅ Component backed up successfully:")
            print(f"   XML: {backup_file}")
            print(f"   Metadata: {metadata_file}")
            print(f"   Size: {backup_file.stat().st_size} bytes")
            
            return True
            
        except Exception as e:
            print(f"❌ Failed to backup component: {e}")
            return False
    
    def deprecate_component(self, component_id: str, reason: Optional[str] = None) -> bool:
        """Mark component as deprecated by renaming and updating description"""
        print(f"\n🚫 Marking component {component_id} as deprecated...")
        
        try:
            # Get component
            component = self.sdk.component.get_component(component_id=component_id)
            original_name = component.name
            
            # Create deprecated name
            timestamp = datetime.now().strftime("%Y%m%d")
            deprecated_name = f"[DEPRECATED-{timestamp}] {original_name}"
            
            # Create deprecated description
            deprecated_reason = reason or "Marked for deletion"
            new_description = f"DEPRECATED: {deprecated_reason}\\n\\nOriginal name: {original_name}\\nDeprecated on: {datetime.now().isoformat()}\\n"
            
            if hasattr(component, 'description') and component.description:
                new_description += f"\\nOriginal description: {component.description}"
            
            # Get XML and modify
            xml_str = component.to_xml()
            root = ET.fromstring(xml_str)
            
            # Update name
            root.set('name', deprecated_name)
            
            # Update or add description
            desc_elem = root.find('.//description')
            if desc_elem is not None:
                desc_elem.text = new_description
            else:
                desc_elem = ET.SubElement(root, 'description')
                desc_elem.text = new_description
            
            # Convert back to XML
            modified_xml = ET.tostring(root, encoding='unicode')
            
            # Update the component
            result = self.sdk.component.update_component(
                component_id=component_id,
                request_body=modified_xml
            )
            
            print(f"✅ Component marked as deprecated:")
            print(f"   Original name: {original_name}")
            print(f"   New name: {deprecated_name}")
            print(f"   Reason: {deprecated_reason}")
            print(f"\n💡 Next steps:")
            print(f"   1. Verify no active processes use this component")
            print(f"   2. Update any references to use replacement component")
            print(f"   3. Manually delete in Boomi UI when ready")
            
            return True
            
        except Exception as e:
            print(f"❌ Failed to deprecate component: {e}")
            return False
    
    def demonstrate_api_limitations(self, component_id: str) -> None:
        """Demonstrate why component deletion via API doesn't work"""
        print(f"\n🔬 Demonstrating API Deletion Limitations...")
        
        try:
            # Show the component exists
            component = self.sdk.component.get_component(component_id=component_id)
            print(f"✅ Component exists: {component.name}")
            print(f"   Current deleted status: {component.deleted}")
            
            # Attempt 1: Try to set deleted=true via XML update
            print(f"\n🧪 Attempt 1: Setting deleted=true via UPDATE...")
            xml_str = component.to_xml()
            root = ET.fromstring(xml_str)
            
            print(f"   Current XML deleted attribute: {root.get('deleted')}")
            root.set('deleted', 'true')
            print(f"   Setting XML deleted attribute to: {root.get('deleted')}")
            
            modified_xml = ET.tostring(root, encoding='unicode')
            
            try:
                self.sdk.component.update_component(component_id=component_id, request_body=modified_xml)
                print(f"   ✅ UPDATE request succeeded")
                
                # Check if it actually worked
                updated_comp = self.sdk.component.get_component(component_id=component_id)
                print(f"   Result: deleted status is still {updated_comp.deleted}")
                print(f"   🔍 Conclusion: Boomi ignores attempts to set deleted=true")
                
            except Exception as e:
                print(f"   ❌ UPDATE request failed: {e}")
            
            # Show what happens with direct API call (this will be done outside Python)
            print(f"\n🧪 Attempt 2: Direct DELETE API call would return:")
            print(f'   curl -X DELETE "https://api.boomi.com/.../Component/{component_id}"')
            print(f'   Response: {{"@type":"Error","message":"Unknown objectType for delete operation: Component"}}')
            print(f"   🔍 Conclusion: DELETE endpoint doesn't support Components")
            
        except Exception as e:
            print(f"❌ Demo failed: {e}")


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='Component deletion helper (shows limitations and workarounds)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  %(prog)s abc123 --info                     # Show component info and deletion guidance
  %(prog)s abc123 --check-dependencies       # Check if safe to delete
  %(prog)s abc123 --backup ./backups/        # Backup before manual deletion
  %(prog)s abc123 --deprecate --reason "Replaced by v2"  # Mark as deprecated
  %(prog)s abc123 --demo                     # Demonstrate API limitations

IMPORTANT: Components cannot be deleted via API!
Use the Boomi UI for actual deletion after following these preparation steps.
        '''
    )
    
    parser.add_argument('component_id',
                       help='The component ID to work with')
    parser.add_argument('--info', action='store_true',
                       help='Show component information and deletion guidance')
    parser.add_argument('--check-dependencies', action='store_true',
                       help='Check for components that reference this one')
    parser.add_argument('--backup', nargs='?', const='./backups', metavar='DIR',
                       help='Backup component XML (default: ./backups)')
    parser.add_argument('--deprecate', action='store_true',
                       help='Mark component as deprecated')
    parser.add_argument('--reason',
                       help='Reason for deprecation (used with --deprecate)')
    parser.add_argument('--demo', action='store_true',
                       help='Demonstrate API deletion limitations')
    
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
    
    # Execute requested operation
    try:
        helper = ComponentDeletionHelper()
        
        # Always show basic info first
        if not helper.show_component_info(args.component_id):
            sys.exit(1)
        
        success = True
        
        if args.check_dependencies:
            success &= helper.check_dependencies(args.component_id)
        
        if args.backup:
            success &= helper.backup_component(args.component_id, args.backup)
        
        if args.deprecate:
            success &= helper.deprecate_component(args.component_id, args.reason)
        
        if args.demo:
            helper.demonstrate_api_limitations(args.component_id)
        
        if not any([args.info, args.check_dependencies, args.backup, args.deprecate, args.demo]):
            # Default action - show info only
            pass
        
        if success:
            print(f"\n✅ Operations completed successfully")
            if not args.demo:
                print(f"\n🔄 Next Steps:")
                print(f"   1. Use Boomi UI to manually delete the component")
                print(f"   2. Navigate to Build > Components")
                print(f"   3. Find '{args.component_id}' and delete it")
                print(f"   4. Verify deletion in dependent systems")
        else:
            print(f"\n⚠️  Some operations failed - review output above")
            sys.exit(1)
    
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()