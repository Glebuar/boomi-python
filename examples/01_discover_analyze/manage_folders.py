#!/usr/bin/env python3
"""
Boomi SDK Example: Manage Folders
==================================

This example demonstrates how to organize components using folders.

Features:
- Create folder hierarchies
- Move components between folders
- Query folder contents
- Delete empty folders
- Restore deleted folders

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET

Usage:
    # List all folders
    python manage_folders.py --list
    
    # Create a folder hierarchy
    python manage_folders.py --create "Production/APIs/v1"
    
    # Query folder contents
    python manage_folders.py --query "Production"
    
    # Move a component to a folder
    python manage_folders.py --move-component COMP_ID --to-folder FOLDER_ID
    
    # Delete an empty folder
    python manage_folders.py --delete FOLDER_ID
    
    # Restore a deleted folder
    python manage_folders.py --restore FOLDER_ID
"""

import os
import sys
import argparse
from typing import Optional, List

# Add parent directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

from boomi import Boomi
from boomi.models import (
    Folder,
    FolderQueryConfig,
    FolderQueryConfigQueryFilter,
    FolderSimpleExpression,
    FolderSimpleExpressionOperator,
    FolderSimpleExpressionProperty,
    ComponentMetadataQueryConfig,
    ComponentMetadataQueryConfigQueryFilter,
    ComponentMetadataSimpleExpression,
    ComponentMetadataSimpleExpressionOperator,
    ComponentMetadataSimpleExpressionProperty
)


class FolderManager:
    """Manages folder operations in Boomi"""
    
    def __init__(self):
        """Initialize the Boomi SDK client"""
        self.sdk = Boomi(
            account_id=os.getenv("BOOMI_ACCOUNT"),
            username=os.getenv("BOOMI_USER"),
            password=os.getenv("BOOMI_SECRET"),
            timeout=30000
        )
        print("✅ SDK initialized successfully")
    
    def list_all_folders(self, include_deleted: bool = False) -> List[Folder]:
        """List all folders in the account"""
        print("\n📂 Listing all folders...")
        
        # Query for all folders
        if include_deleted:
            # Query all folders including deleted ones
            query_expression = FolderSimpleExpression(
                operator=FolderSimpleExpressionOperator.ISNOTNULL,
                property=FolderSimpleExpressionProperty.ID,
                argument=[]
            )
        else:
            # Query only non-deleted folders
            query_expression = FolderSimpleExpression(
                operator=FolderSimpleExpressionOperator.EQUALS,
                property=FolderSimpleExpressionProperty.DELETED,
                argument=["false"]
            )
        
        query_filter = FolderQueryConfigQueryFilter(expression=query_expression)
        query_config = FolderQueryConfig(query_filter=query_filter)
        
        result = self.sdk.folder.query_folder(request_body=query_config)
        
        if hasattr(result, 'result') and result.result:
            folders = result.result
            print(f"Found {len(folders)} folder(s)")
            
            # Display folder hierarchy
            self._display_folder_tree(folders)
            return folders
        else:
            print("No folders found")
            return []
    
    def _display_folder_tree(self, folders: List[Folder], indent: str = "") -> None:
        """Display folders in a tree structure"""
        # Group folders by parent
        folder_dict = {f.id_: f for f in folders}
        children = {}
        roots = []
        
        for folder in folders:
            if not folder.parent_id or folder.parent_id not in folder_dict:
                roots.append(folder)
            else:
                if folder.parent_id not in children:
                    children[folder.parent_id] = []
                children[folder.parent_id].append(folder)
        
        # Display tree starting from roots
        for root in sorted(roots, key=lambda f: f.name):
            self._print_folder_node(root, children, "")
    
    def _print_folder_node(self, folder: Folder, children: dict, indent: str) -> None:
        """Print a folder node and its children"""
        status = "🗑️ [DELETED]" if folder.deleted else ""
        print(f"{indent}📁 {folder.name} {status}")
        
        if folder.id_ in children:
            for child in sorted(children[folder.id_], key=lambda f: f.name):
                self._print_folder_node(child, children, indent + "  ")
    
    def create_folder_hierarchy(self, path: str) -> Optional[Folder]:
        """Create a folder hierarchy from a path like 'Parent/Child/GrandChild'"""
        print(f"\n🔨 Creating folder hierarchy: {path}")
        
        parts = path.split('/')
        parent_id = None
        last_folder = None
        
        for i, part in enumerate(parts):
            current_path = '/'.join(parts[:i+1])
            
            # Check if folder already exists
            existing = self._find_folder_by_path(current_path)
            if existing:
                print(f"  ✓ Folder already exists: {current_path}")
                parent_id = existing.id_
                last_folder = existing
            else:
                # Create the folder
                new_folder = Folder(
                    name=part,
                    parent_id=parent_id
                )
                
                try:
                    created = self.sdk.folder.create_folder(request_body=new_folder)
                    print(f"  ✅ Created: {created.full_path}")
                    parent_id = created.id_
                    last_folder = created
                except Exception as e:
                    print(f"  ❌ Failed to create {part}: {e}")
                    return None
        
        return last_folder
    
    def _find_folder_by_path(self, path: str) -> Optional[Folder]:
        """Find a folder by its full path"""
        query_expression = FolderSimpleExpression(
            operator=FolderSimpleExpressionOperator.EQUALS,
            property=FolderSimpleExpressionProperty.FULLPATH,
            argument=[path]
        )
        
        query_filter = FolderQueryConfigQueryFilter(expression=query_expression)
        query_config = FolderQueryConfig(query_filter=query_filter)
        
        result = self.sdk.folder.query_folder(request_body=query_config)
        
        if hasattr(result, 'result') and result.result and len(result.result) > 0:
            # Filter out deleted folders
            active_folders = [f for f in result.result if not f.deleted]
            return active_folders[0] if active_folders else None
        return None
    
    def query_folder_contents(self, folder_name: str) -> None:
        """Query and display contents of a folder"""
        print(f"\n🔍 Querying folder contents: {folder_name}")
        
        # Find the folder
        query_expression = FolderSimpleExpression(
            operator=FolderSimpleExpressionOperator.LIKE,
            property=FolderSimpleExpressionProperty.NAME,
            argument=[f"%{folder_name}%"]
        )
        
        query_filter = FolderQueryConfigQueryFilter(expression=query_expression)
        query_config = FolderQueryConfig(query_filter=query_filter)
        
        result = self.sdk.folder.query_folder(request_body=query_config)
        
        if not result.result:
            print(f"❌ Folder not found: {folder_name}")
            return
        
        # Get the first matching non-deleted folder
        target_folder = None
        for folder in result.result:
            if not folder.deleted:
                target_folder = folder
                break
        
        if not target_folder:
            print(f"❌ No active folder found with name: {folder_name}")
            return
        
        print(f"\n📁 Folder: {target_folder.full_path}")
        print(f"   ID: {target_folder.id_}")
        
        # Query components in this folder
        print("\n📦 Components in folder:")
        self._list_components_in_folder(target_folder.id_)
        
        # Query sub-folders
        print("\n📂 Sub-folders:")
        self._list_subfolders(target_folder)
    
    def _list_components_in_folder(self, folder_id: str) -> None:
        """List all components in a folder"""
        try:
            query_expression = ComponentMetadataSimpleExpression(
                operator=ComponentMetadataSimpleExpressionOperator.EQUALS,
                property=ComponentMetadataSimpleExpressionProperty.FOLDERID,
                argument=[folder_id]
            )
            
            query_filter = ComponentMetadataQueryConfigQueryFilter(expression=query_expression)
            query_config = ComponentMetadataQueryConfig(query_filter=query_filter)
            
            result = self.sdk.component_metadata.query_component_metadata(request_body=query_config)
            
            if hasattr(result, 'result') and result.result:
                for comp in result.result:
                    print(f"   📄 {comp.name} ({comp.type_})")
            else:
                print("   (No components in this folder)")
        except Exception as e:
            print(f"   ⚠️ Could not query components: {e}")
    
    def _list_subfolders(self, parent_folder: Folder) -> None:
        """List all sub-folders of a parent folder"""
        try:
            # Use parentName property instead of parentId (API limitation with parentId)
            query_expression = FolderSimpleExpression(
                operator=FolderSimpleExpressionOperator.EQUALS,
                property=FolderSimpleExpressionProperty.PARENTNAME,
                argument=[parent_folder.name]
            )
            
            query_filter = FolderQueryConfigQueryFilter(expression=query_expression)
            query_config = FolderQueryConfig(query_filter=query_filter)
            
            result = self.sdk.folder.query_folder(request_body=query_config)
            
            if hasattr(result, 'result') and result.result:
                active_folders = [f for f in result.result if not f.deleted]
                for folder in active_folders:
                    print(f"   📁 {folder.name}")
            else:
                print("   (No sub-folders)")
        except Exception as e:
            print(f"   ⚠️ Could not query sub-folders: {e}")
    
    def move_component_to_folder(self, component_id: str, folder_id: str) -> bool:
        """Move a component to a different folder"""
        print(f"\n📦 Moving component {component_id} to folder {folder_id}...")
        
        try:
            # Get the target folder details
            folder = self.sdk.folder.get_folder(id_=folder_id)
            print(f"  Target folder: {folder.full_path}")
            
            # Note: Component updates require raw XML, so this is a simplified example
            # In a real scenario, you would need to:
            # 1. Get the component XML using component.get_component
            # 2. Parse and modify the XML to update the folderId
            # 3. Send the updated XML using component.update_component
            
            print(f"  ⚠️ Note: Moving components requires XML manipulation")
            print(f"  This would update component's folderId to: {folder_id}")
            return False
            
        except Exception as e:
            print(f"  ❌ Failed to get folder details: {e}")
            return False
    
    def delete_folder(self, folder_id: str) -> bool:
        """Delete an empty folder"""
        print(f"\n🗑️ Deleting folder {folder_id}...")
        
        try:
            # Get folder details first
            folder = self.sdk.folder.get_folder(id_=folder_id)
            print(f"  Folder: {folder.full_path}")
            
            # Delete the folder
            self.sdk.folder.delete_folder(id_=folder_id)
            print(f"  ✅ Folder deleted successfully")
            print(f"  💡 Tip: Use --restore {folder_id} to restore this folder")
            return True
            
        except Exception as e:
            print(f"  ❌ Failed to delete folder: {e}")
            print(f"  Note: Folders with components or deployed processes cannot be deleted")
            return False
    
    def restore_folder(self, folder_id: str) -> bool:
        """Restore a deleted folder"""
        print(f"\n♻️ Restoring folder {folder_id}...")
        
        try:
            # To restore, we create with the same ID
            restored_folder = Folder(
                id_=folder_id
            )
            
            restored = self.sdk.folder.create_folder(request_body=restored_folder)
            print(f"  ✅ Folder restored: {restored.full_path}")
            print(f"  Note: All components in the folder have also been restored")
            return True
            
        except Exception as e:
            print(f"  ❌ Failed to restore folder: {e}")
            return False


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='Manage Boomi folders and component organization',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  %(prog)s --list                              # List all folders
  %(prog)s --list --include-deleted            # Include deleted folders
  %(prog)s --create "Production/APIs/v1"       # Create folder hierarchy
  %(prog)s --query "Production"                # Query folder contents
  %(prog)s --delete FOLDER_ID                  # Delete a folder
  %(prog)s --restore FOLDER_ID                 # Restore deleted folder
  %(prog)s --move-component COMP_ID --to-folder FOLDER_ID  # Move component
        '''
    )
    
    parser.add_argument('--list', action='store_true',
                       help='List all folders in tree view')
    parser.add_argument('--include-deleted', action='store_true',
                       help='Include deleted folders when listing')
    parser.add_argument('--create', metavar='PATH',
                       help='Create folder hierarchy (e.g., "Parent/Child")')
    parser.add_argument('--query', metavar='NAME',
                       help='Query folder contents by name')
    parser.add_argument('--delete', metavar='ID',
                       help='Delete an empty folder by ID')
    parser.add_argument('--restore', metavar='ID',
                       help='Restore a deleted folder by ID')
    parser.add_argument('--move-component', metavar='COMP_ID',
                       help='Component ID to move')
    parser.add_argument('--to-folder', metavar='FOLDER_ID',
                       help='Target folder ID for move operation')
    
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
        manager = FolderManager()
        
        if args.list:
            manager.list_all_folders(include_deleted=args.include_deleted)
        
        elif args.create:
            folder = manager.create_folder_hierarchy(args.create)
            if folder:
                print(f"\n✅ Successfully created folder hierarchy")
                print(f"   Final folder ID: {folder.id_}")
        
        elif args.query:
            manager.query_folder_contents(args.query)
        
        elif args.delete:
            if manager.delete_folder(args.delete):
                print("\n✅ Folder deleted successfully")
        
        elif args.restore:
            if manager.restore_folder(args.restore):
                print("\n✅ Folder restored successfully")
        
        elif args.move_component and args.to_folder:
            if manager.move_component_to_folder(args.move_component, args.to_folder):
                print("\n✅ Component moved successfully")
        
        elif args.move_component or args.to_folder:
            print("❌ Both --move-component and --to-folder are required for move operation")
            sys.exit(1)
        
        else:
            parser.print_help()
            print("\n💡 Run with -h for more examples")
    
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()