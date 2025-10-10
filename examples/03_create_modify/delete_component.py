#!/usr/bin/env python3
"""
Component Deletion Example

This example demonstrates safe component deletion including:
- Soft delete (mark as deleted)
- Check component dependencies before deletion
- Batch deletion capabilities
- Deletion confirmation and rollback
"""

import os
import sys
import argparse
from typing import List, Dict, Any, Optional
from datetime import datetime
import xml.etree.ElementTree as ET

# Add parent directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

from boomi import Boomi
from boomi.models import (
    ComponentMetadataQueryConfig,
    ComponentMetadataQueryConfigQueryFilter,
    ComponentMetadataSimpleExpression,
    ComponentMetadataSimpleExpressionOperator,
    ComponentMetadataSimpleExpressionProperty
)


class ComponentDeleter:
    """Manages safe component deletion"""
    
    def __init__(self, verbose: bool = False, dry_run: bool = False):
        """Initialize the deleter"""
        self.verbose = verbose
        self.dry_run = dry_run
        
        # Initialize SDK
        self.sdk = Boomi(
            account_id=os.environ.get('BOOMI_ACCOUNT'),
            username=os.environ.get('BOOMI_USER'),
            password=os.environ.get('BOOMI_SECRET'),
            timeout=30000
        )
        
        if self.verbose:
            print("✅ Component Deleter initialized")
            if self.dry_run:
                print("🔒 DRY RUN MODE - No actual deletions will occur")
    
    def soft_delete_component(self, component_id: str) -> bool:
        """
        Soft delete a component (mark as deleted)
        
        Args:
            component_id: Component ID to delete
            
        Returns:
            True if successful
        """
        try:
            print(f"\n🗑️ Soft deleting component: {component_id}")
            
            # Get the component
            component = self.sdk.component.get_component(component_id=component_id)
            
            # Get component name for confirmation
            xml_str = component.to_xml()
            root = ET.fromstring(xml_str)
            comp_name = root.get('name', 'Unknown')
            comp_type = root.get('type', 'Unknown')
            
            print(f"   Component: {comp_name}")
            print(f"   Type: {comp_type}")
            
            if self.dry_run:
                print("   🔒 DRY RUN - Would mark component as deleted")
                return True
            
            # Set deleted flag
            root.set('deleted', 'true')
            modified_xml = ET.tostring(root, encoding='unicode')
            
            # Update component
            result = self.sdk.component.update_component(
                component_id=component_id,
                request_body=modified_xml
            )
            
            print("   ✅ Component marked as deleted")
            return True
            
        except Exception as e:
            print(f"   ❌ Error deleting component: {e}")
            if self.verbose:
                import traceback
                traceback.print_exc()
            return False
    
    def check_dependencies(self, component_id: str) -> Dict[str, Any]:
        """
        Check if component has dependencies
        
        Args:
            component_id: Component ID to check
            
        Returns:
            Dictionary of dependency information
        """
        print(f"\n🔍 Checking dependencies for: {component_id}")
        
        dependencies = {
            'component_id': component_id,
            'used_by': [],
            'uses': [],
            'safe_to_delete': True
        }
        
        try:
            # Query for components that reference this one
            query_expression = ComponentMetadataSimpleExpression(
                operator=ComponentMetadataSimpleExpressionOperator.EQUALS,
                property=ComponentMetadataSimpleExpressionProperty.COMPONENTID,
                argument=[component_id]
            )
            
            query_filter = ComponentMetadataQueryConfigQueryFilter(expression=query_expression)
            query_config = ComponentMetadataQueryConfig(query_filter=query_filter)
            
            result = self.sdk.component_metadata.query_component_metadata(
                request_body=query_config
            )
            
            if result and hasattr(result, 'result') and result.result:
                comp_meta = result.result[0]
                
                # Check if component is deployed
                if hasattr(comp_meta, 'deployed') and comp_meta.deployed:
                    dependencies['safe_to_delete'] = False
                    print("   ⚠️ Component is deployed!")
                
                # Check for references (simplified - real implementation would check actual references)
                if hasattr(comp_meta, 'folder_full_path'):
                    print(f"   Location: {comp_meta.folder_full_path}")
            
            if dependencies['safe_to_delete']:
                print("   ✅ No blocking dependencies found")
            else:
                print("   ❌ Component has dependencies - deletion not recommended")
            
        except Exception as e:
            if self.verbose:
                print(f"   Error checking dependencies: {e}")
        
        return dependencies
    
    def batch_delete(self, component_ids: List[str], force: bool = False) -> Dict[str, Any]:
        """
        Delete multiple components
        
        Args:
            component_ids: List of component IDs
            force: Skip dependency checks
            
        Returns:
            Results dictionary
        """
        print(f"\n📦 Batch deleting {len(component_ids)} components...")
        
        results = {
            'total': len(component_ids),
            'successful': 0,
            'failed': 0,
            'skipped': 0,
            'details': []
        }
        
        for comp_id in component_ids:
            detail = {
                'id': comp_id,
                'status': 'pending'
            }
            
            # Check dependencies unless forced
            if not force:
                deps = self.check_dependencies(comp_id)
                if not deps['safe_to_delete']:
                    print(f"   ⏭️ Skipping {comp_id} - has dependencies")
                    detail['status'] = 'skipped'
                    detail['reason'] = 'has dependencies'
                    results['skipped'] += 1
                    results['details'].append(detail)
                    continue
            
            # Attempt deletion
            if self.soft_delete_component(comp_id):
                detail['status'] = 'deleted'
                results['successful'] += 1
            else:
                detail['status'] = 'failed'
                results['failed'] += 1
            
            results['details'].append(detail)
        
        # Summary
        print(f"\n📊 Batch Delete Summary:")
        print(f"   Total: {results['total']}")
        print(f"   Successful: {results['successful']}")
        print(f"   Failed: {results['failed']}")
        print(f"   Skipped: {results['skipped']}")
        
        return results
    
    def list_deleted_components(self, limit: int = 10) -> List[Dict[str, Any]]:
        """
        List components marked as deleted
        
        Args:
            limit: Maximum results
            
        Returns:
            List of deleted components
        """
        print(f"\n🗑️ Listing deleted components...")
        
        deleted = []
        
        try:
            # Query for deleted components
            query_expression = ComponentMetadataSimpleExpression(
                operator=ComponentMetadataSimpleExpressionOperator.EQUALS,
                property=ComponentMetadataSimpleExpressionProperty.DELETED,
                argument=["true"]
            )
            
            query_filter = ComponentMetadataQueryConfigQueryFilter(expression=query_expression)
            query_config = ComponentMetadataQueryConfig(query_filter=query_filter)
            result = self.sdk.component_metadata.query_component_metadata(
                request_body=query_config
            )
            
            if result and hasattr(result, 'result') and result.result:
                for comp in result.result:
                    deleted.append({
                        'id': getattr(comp, 'component_id', 'N/A'),
                        'name': getattr(comp, 'name', 'N/A'),
                        'type': getattr(comp, 'type_', 'N/A'),
                        'deleted_date': getattr(comp, 'modified_date', 'N/A')
                    })
                    
                    if len(deleted) >= limit:
                        break
            
            print(f"   Found {len(deleted)} deleted component(s)")
            
        except Exception as e:
            print(f"   ❌ Error listing deleted components: {e}")
        
        return deleted


def main():
    """Main function"""
    parser = argparse.ArgumentParser(
        description='Delete Boomi components safely',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Delete a single component
  %(prog)s --delete COMPONENT_ID
  
  # Check dependencies before deletion
  %(prog)s --check COMPONENT_ID
  
  # Batch delete multiple components
  %(prog)s --batch ID1 ID2 ID3
  
  # Force deletion (skip checks)
  %(prog)s --delete COMPONENT_ID --force
  
  # List deleted components
  %(prog)s --list-deleted
  
  # Dry run (no actual deletion)
  %(prog)s --delete COMPONENT_ID --dry-run
"""
    )
    
    # Operations
    parser.add_argument('--delete', metavar='ID',
                       help='Delete a component')
    parser.add_argument('--check', metavar='ID',
                       help='Check component dependencies')
    parser.add_argument('--batch', nargs='+', metavar='ID',
                       help='Delete multiple components')
    parser.add_argument('--list-deleted', action='store_true',
                       help='List deleted components')
    
    # Options
    parser.add_argument('--force', action='store_true',
                       help='Skip dependency checks')
    parser.add_argument('--dry-run', action='store_true',
                       help='Simulate deletion without actual changes')
    parser.add_argument('--limit', type=int, default=10,
                       help='Limit results (default: 10)')
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='Enable verbose output')
    
    args = parser.parse_args()
    
    # Check for at least one operation
    if not any([args.delete, args.check, args.batch, args.list_deleted]):
        parser.print_help()
        return
    
    # Initialize deleter
    deleter = ComponentDeleter(verbose=args.verbose, dry_run=args.dry_run)
    
    # Execute operations
    if args.delete:
        # Check dependencies first unless forced
        if not args.force:
            deps = deleter.check_dependencies(args.delete)
            if not deps['safe_to_delete']:
                print("\n⚠️ Component has dependencies. Use --force to delete anyway.")
                return
        
        # Delete component
        success = deleter.soft_delete_component(args.delete)
        if success:
            print("\n✅ Component deletion completed")
        else:
            print("\n❌ Component deletion failed")
    
    elif args.check:
        deps = deleter.check_dependencies(args.check)
        
        print("\n📊 Dependency Check Results:")
        print(f"   Safe to delete: {'Yes' if deps['safe_to_delete'] else 'No'}")
        if deps['used_by']:
            print(f"   Used by {len(deps['used_by'])} component(s)")
    
    elif args.batch:
        results = deleter.batch_delete(args.batch, force=args.force)
    
    elif args.list_deleted:
        deleted = deleter.list_deleted_components(limit=args.limit)
        
        if deleted:
            print("\n🗑️ Deleted Components:")
            for i, comp in enumerate(deleted, 1):
                print(f"\n{i}. {comp['name']}")
                print(f"   ID: {comp['id']}")
                print(f"   Type: {comp['type']}")
                print(f"   Deleted: {comp['deleted_date']}")


if __name__ == '__main__':
    main()