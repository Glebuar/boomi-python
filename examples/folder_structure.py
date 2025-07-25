#!/usr/bin/env python3
"""
Boomi SDK Example: Display Account Folder Structure

This example demonstrates how to query and display the hierarchical folder 
structure from the Boomi Platform API using the Python SDK.

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- Or create a .env file with these variables

Usage:
    python folder_structure.py
"""

import os
from boomi import Boomi
from boomi.models import (
    FolderQueryConfig, 
    FolderQueryConfigQueryFilter,
    FolderSimpleExpression,
    FolderSimpleExpressionOperator,
    FolderSimpleExpressionProperty
)

# Load environment variables from .env file if dotenv is available
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv is optional

def build_folder_tree(folders):
    """Build a hierarchical tree structure from flat folder list"""
    
    children_map = {}
    
    # Build children mapping
    for folder in folders:
        parent_id = folder.parent_id or "ROOT"
        if parent_id not in children_map:
            children_map[parent_id] = []
        children_map[parent_id].append(folder)
    
    # Sort children by name for consistent display
    for parent_id in children_map:
        children_map[parent_id].sort(key=lambda f: f.name or "")
    
    return children_map

def print_folder_tree(children_map, parent_id="ROOT", level=0, visited=None):
    """Recursively print the folder tree structure"""
    
    if visited is None:
        visited = set()
    
    # Prevent infinite recursion
    if parent_id in visited or parent_id not in children_map:
        return
    visited.add(parent_id)
    
    indent = "  " * level
    
    for i, folder in enumerate(children_map[parent_id]):
        is_last = i == len(children_map[parent_id]) - 1
        connector = "└── " if is_last else "├── "
        
        folder_info = folder.name
        if folder.deleted:
            folder_info += " (DELETED)"
        
        print(f"{indent}{connector}{folder_info}")
        
        # Recursively print children
        if folder.id_ in children_map:
            print_folder_tree(children_map, folder.id_, level + 1, visited.copy())

def query_folder_structure():
    """Query and display folder structure from Boomi"""
    
    # Check for required environment variables
    account_id = os.getenv("BOOMI_ACCOUNT")
    username = os.getenv("BOOMI_USER") 
    password = os.getenv("BOOMI_SECRET")
    
    if not all([account_id, username, password]):
        print("❌ Error: Missing required environment variables")
        print("   Please set: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET")
        return
    
    print(f"🏢 Account: {account_id}")
    print(f"👤 User: {username}")
    
    # Initialize the Boomi SDK
    sdk = Boomi(
        account_id=account_id,
        username=username, 
        password=password,
        timeout=30000
    )
    
    print("\n🔍 Querying folder structure...")
    
    try:
        # Query all folders using IS_NOT_NULL on id to get all folders
        query_expression = FolderSimpleExpression(
            operator=FolderSimpleExpressionOperator.ISNOTNULL,
            property=FolderSimpleExpressionProperty.ID,
            argument=[]
        )
        
        query_filter = FolderQueryConfigQueryFilter(expression=query_expression)
        query_config = FolderQueryConfig(query_filter=query_filter)
        
        result = sdk.folder.query_folder(request_body=query_config)
        
        # Check results
        if hasattr(result, 'result') and result.result:
            folders = result.result
            active_folders = [f for f in folders if not f.deleted]
            deleted_folders = [f for f in folders if f.deleted]
            
            print(f"✅ Found {len(folders)} folder(s)")
            print(f"📁 Active folders: {len(active_folders)}")
            if deleted_folders:
                print(f"🗑️  Deleted folders: {len(deleted_folders)}")
            
            # Build and display the folder tree
            print("\n📂 Boomi Account Folder Structure:")
            print("=" * 50)
            
            if folders:
                children_map = build_folder_tree(folders)
                print("🏠 Root")
                print_folder_tree(children_map, "ROOT", 0)
            else:
                print("No folders found")
            
            # Display summary
            if folders:
                print(f"\n📊 Folder Summary:")
                print(f"  • Total folders: {len(folders)}")
                print(f"  • Active folders: {len(active_folders)}")
                print(f"  • Deleted folders: {len(deleted_folders)}")
                
                # Show folder depth statistics
                max_depth = 0
                for folder in folders:
                    if folder.full_path:
                        depth = folder.full_path.count('/') if folder.full_path != folder.name else 0
                        max_depth = max(max_depth, depth)
                print(f"  • Maximum folder depth: {max_depth}")
        
        else:
            print("❌ No folders found")
            print("This could mean:")
            print("  • No folders exist in the account")
            print("  • Insufficient permissions to view folders") 
                
    except Exception as e:
        print(f"❌ Error querying folders: {e}")
        print("Please check:")
        print("  • Environment variables are set correctly")
        print("  • Account has permission to query folders")
        print("  • Network connectivity to Boomi API")

def main():
    """Main entry point"""
    print("🚀 Boomi SDK Example: Account Folder Structure")
    print("=" * 50)
    query_folder_structure()

if __name__ == "__main__":
    main()