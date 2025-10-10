#!/usr/bin/env python3
"""
Boomi SDK Example: Branch Management
=====================================

This example demonstrates how to manage branches in Boomi for version control
and multi-environment development workflows.

Features:
- List all branches in the account
- Create new feature/development branches
- Get branch details and metadata
- Query branches with filters
- Delete obsolete branches
- Support for GitOps-style workflows

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- Appropriate permissions to manage branches
- Branch functionality enabled (typically Enterprise accounts only)

Usage:
    # List all branches
    python manage_branches.py --list
    
    # Create a new branch
    python manage_branches.py --create "feature-branch-name" --description "Feature description"
    
    # Get branch details
    python manage_branches.py --get "branch-id"
    
    # Query branches by name
    python manage_branches.py --query --name "feature-*"
    
    # Delete a branch
    python manage_branches.py --delete "branch-id"
    
    # Show branch statistics
    python manage_branches.py --stats

Examples:
    python manage_branches.py --list
    python manage_branches.py --create "feature-payment-api" --description "New payment integration"
    python manage_branches.py --query --name "feature-*" --limit 10
    python manage_branches.py --delete "abc123-def456-789"
"""

import os
import sys
import argparse
import json
from datetime import datetime
from typing import Optional, List, Dict, Any

# Add parent directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

# Load environment variables from .env file if available
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv is optional

from boomi import Boomi
from boomi.models import (
    Branch,
    BranchQueryConfig,
    BranchQueryConfigQueryFilter,
    BranchSimpleExpression,
    BranchSimpleExpressionOperator
)


class BranchManager:
    """Manages Boomi branch operations"""
    
    def __init__(self, verbose: bool = False):
        """Initialize the Boomi SDK client"""
        self.verbose = verbose
        self.sdk = Boomi(
            account_id=os.getenv("BOOMI_ACCOUNT"),
            username=os.getenv("BOOMI_USER"),
            password=os.getenv("BOOMI_SECRET"),
            timeout=30000
        )
        if self.verbose:
            print("✅ SDK initialized successfully")
    
    def list_branches(self, limit: Optional[int] = None) -> List[Dict[str, Any]]:
        """List all branches in the account"""
        print("\n🔍 Listing branches...")
        
        try:
            # Query all branches - use a simple expression that returns all
            all_expr = BranchSimpleExpression(
                operator=BranchSimpleExpressionOperator.ISNOTNULL,
                property="id",
                argument=[]
            )
            query_filter = BranchQueryConfigQueryFilter(expression=all_expr)
            query_config = BranchQueryConfig(query_filter=query_filter)
            result = self.sdk.branch.query_branch(request_body=query_config)
            
            branches = []
            if hasattr(result, 'result') and result.result:
                for branch in result.result[:limit] if limit else result.result:
                    branch_info = {
                        'id': getattr(branch, 'id_', 'N/A'),
                        'name': getattr(branch, 'name', 'N/A'),
                        'description': getattr(branch, 'description', ''),
                        'created_date': getattr(branch, 'created_date', 'N/A'),
                        'created_by': getattr(branch, 'created_by', 'N/A'),
                        'modified_date': getattr(branch, 'modified_date', 'N/A'),
                        'modified_by': getattr(branch, 'modified_by', 'N/A'),
                        'is_default': getattr(branch, 'is_default', False),
                        'parent_branch_id': getattr(branch, 'parent_branch_id', None)
                    }
                    branches.append(branch_info)
            
            return branches
            
        except Exception as e:
            error_msg = str(e)
            if "400" in error_msg:
                print(f"❌ Failed to list branches: Branch API not available")
                print("💡 Note: Branch functionality may not be enabled for this account type")
                print("   Branches are typically available in Enterprise accounts with Git integration")
            else:
                print(f"❌ Failed to list branches: {e}")
            return []
    
    def create_branch(self, name: str, description: Optional[str] = None,
                     parent_branch_id: Optional[str] = None) -> Optional[Dict[str, Any]]:
        """Create a new branch"""
        print(f"\n📝 Creating branch: {name}")
        
        try:
            # Create branch object
            branch = Branch(
                name=name,
                description=description or f"Branch created on {datetime.now().isoformat()}"
            )
            
            # Set parent branch if provided
            if parent_branch_id:
                branch.parent_branch_id = parent_branch_id
            
            # Create the branch
            result = self.sdk.branch.create_branch(request_body=branch)
            
            if result:
                branch_info = {
                    'id': getattr(result, 'id_', 'N/A'),
                    'name': getattr(result, 'name', 'N/A'),
                    'description': getattr(result, 'description', ''),
                    'created_date': getattr(result, 'created_date', 'N/A'),
                    'created_by': getattr(result, 'created_by', 'N/A')
                }
                print(f"✅ Branch created successfully: {branch_info['id']}")
                return branch_info
            else:
                print("❌ Failed to create branch")
                return None
                
        except Exception as e:
            error_msg = str(e)
            if "400" in error_msg:
                print(f"❌ Failed to create branch: Branch API not available")
                print("💡 Note: Branch functionality may not be enabled for this account type")
            else:
                print(f"❌ Failed to create branch: {e}")
            if self.verbose:
                import traceback
                traceback.print_exc()
            return None
    
    def get_branch(self, branch_id: str) -> Optional[Dict[str, Any]]:
        """Get details of a specific branch"""
        print(f"\n🔍 Getting branch details: {branch_id}")
        
        try:
            result = self.sdk.branch.get_branch(id_=branch_id)
            
            if result:
                branch_info = {
                    'id': getattr(result, 'id_', 'N/A'),
                    'name': getattr(result, 'name', 'N/A'),
                    'description': getattr(result, 'description', ''),
                    'created_date': getattr(result, 'created_date', 'N/A'),
                    'created_by': getattr(result, 'created_by', 'N/A'),
                    'modified_date': getattr(result, 'modified_date', 'N/A'),
                    'modified_by': getattr(result, 'modified_by', 'N/A'),
                    'is_default': getattr(result, 'is_default', False),
                    'parent_branch_id': getattr(result, 'parent_branch_id', None)
                }
                return branch_info
            else:
                print(f"❌ Branch not found: {branch_id}")
                return None
                
        except Exception as e:
            error_msg = str(e)
            if "400" in error_msg:
                print(f"❌ Failed to get branch: Branch API not available")
                print("💡 Note: Branch functionality may not be enabled for this account type")
            else:
                print(f"❌ Failed to get branch: {e}")
            return None
    
    def query_branches(self, name_pattern: Optional[str] = None,
                      created_by: Optional[str] = None,
                      limit: Optional[int] = None) -> List[Dict[str, Any]]:
        """Query branches with filters"""
        print("\n🔍 Querying branches...")
        
        try:
            # Build query filter
            expressions = []
            
            if name_pattern:
                # Query by name pattern
                name_expr = BranchSimpleExpression(
                    operator=BranchSimpleExpressionOperator.LIKE,
                    property="name",
                    argument=[name_pattern]
                )
                expressions.append(name_expr)
            
            if created_by:
                # Query by creator
                creator_expr = BranchSimpleExpression(
                    operator=BranchSimpleExpressionOperator.EQUALS,
                    property="createdBy",
                    argument=[created_by]
                )
                expressions.append(creator_expr)
            
            # Create query config
            if expressions:
                from boomi.models import BranchGroupingExpression, BranchGroupingExpressionOperator
                
                if len(expressions) == 1:
                    query_filter = BranchQueryConfigQueryFilter(expression=expressions[0])
                else:
                    # Combine with AND
                    combined_expr = BranchGroupingExpression(
                        operator=BranchGroupingExpressionOperator.AND,
                        nested_expression=expressions
                    )
                    query_filter = BranchQueryConfigQueryFilter(expression=combined_expr)
                
                query_config = BranchQueryConfig(query_filter=query_filter)
            else:
                # Query all branches
                all_expr = BranchSimpleExpression(
                    operator=BranchSimpleExpressionOperator.ISNOTNULL,
                    property="id",
                    argument=[]
                )
                query_filter = BranchQueryConfigQueryFilter(expression=all_expr)
                query_config = BranchQueryConfig(query_filter=query_filter)
            
            result = self.sdk.branch.query_branch(request_body=query_config)
            
            branches = []
            if hasattr(result, 'result') and result.result:
                for branch in result.result[:limit] if limit else result.result:
                    branch_info = {
                        'id': getattr(branch, 'id_', 'N/A'),
                        'name': getattr(branch, 'name', 'N/A'),
                        'description': getattr(branch, 'description', ''),
                        'created_date': getattr(branch, 'created_date', 'N/A'),
                        'created_by': getattr(branch, 'created_by', 'N/A'),
                        'is_default': getattr(branch, 'is_default', False)
                    }
                    branches.append(branch_info)
            
            return branches
            
        except Exception as e:
            print(f"❌ Failed to query branches: {e}")
            if self.verbose:
                import traceback
                traceback.print_exc()
            return []
    
    def delete_branch(self, branch_id: str) -> bool:
        """Delete a branch"""
        print(f"\n🗑️ Deleting branch: {branch_id}")
        
        try:
            # Get branch details first
            branch = self.get_branch(branch_id)
            if not branch:
                return False
            
            if branch.get('is_default'):
                print("❌ Cannot delete default branch")
                return False
            
            # Delete the branch
            self.sdk.branch.delete_branch(id_=branch_id)
            print(f"✅ Branch deleted successfully: {branch['name']}")
            return True
            
        except Exception as e:
            print(f"❌ Failed to delete branch: {e}")
            return False
    
    def show_statistics(self) -> None:
        """Show branch statistics"""
        print("\n📊 Branch Statistics")
        print("=" * 50)
        
        branches = self.list_branches()
        
        if branches:
            # Count statistics
            total_branches = len(branches)
            default_branches = sum(1 for b in branches if b.get('is_default'))
            feature_branches = sum(1 for b in branches if 'feature' in b['name'].lower())
            
            # Group by creator
            creators = {}
            for branch in branches:
                creator = branch.get('created_by', 'Unknown')
                creators[creator] = creators.get(creator, 0) + 1
            
            print(f"Total branches: {total_branches}")
            print(f"Default branches: {default_branches}")
            print(f"Feature branches: {feature_branches}")
            print(f"\nBranches by creator:")
            for creator, count in sorted(creators.items(), key=lambda x: x[1], reverse=True):
                print(f"  {creator}: {count}")
            
            # Recent branches
            print(f"\nMost recent branches:")
            sorted_branches = sorted(branches, 
                                    key=lambda x: x.get('created_date', ''), 
                                    reverse=True)
            for branch in sorted_branches[:5]:
                print(f"  - {branch['name']} (created: {branch.get('created_date', 'N/A')[:10]})")
        else:
            print("No branches found")


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='Manage Boomi branches for version control',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
    python manage_branches.py --list
    python manage_branches.py --create "feature-payment-api" --description "New payment integration"
    python manage_branches.py --get "abc123-def456-789"
    python manage_branches.py --query --name "feature-*"
    python manage_branches.py --delete "abc123-def456-789"
    python manage_branches.py --stats
        '''
    )
    
    # Action arguments
    parser.add_argument('--list', action='store_true',
                       help='List all branches')
    parser.add_argument('--create', metavar='NAME',
                       help='Create a new branch with the given name')
    parser.add_argument('--get', metavar='ID',
                       help='Get details of a specific branch')
    parser.add_argument('--query', action='store_true',
                       help='Query branches with filters')
    parser.add_argument('--delete', metavar='ID',
                       help='Delete a branch by ID')
    parser.add_argument('--stats', action='store_true',
                       help='Show branch statistics')
    
    # Additional arguments
    parser.add_argument('--description', help='Branch description (for create)')
    parser.add_argument('--parent-branch', help='Parent branch ID (for create)')
    parser.add_argument('--name', help='Name pattern for query (supports wildcards)')
    parser.add_argument('--created-by', help='Filter by creator (for query)')
    parser.add_argument('--limit', type=int, help='Limit number of results')
    parser.add_argument('--verbose', action='store_true', help='Enable verbose output')
    parser.add_argument('--json', action='store_true', help='Output in JSON format')
    
    args = parser.parse_args()
    
    # Validate environment variables
    if not all([os.getenv("BOOMI_ACCOUNT"), os.getenv("BOOMI_USER"), os.getenv("BOOMI_SECRET")]):
        print("❌ Error: Missing required environment variables")
        print("   Please set: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET")
        sys.exit(1)
    
    # Initialize manager
    manager = BranchManager(verbose=args.verbose)
    
    try:
        if args.list:
            # List branches
            branches = manager.list_branches(limit=args.limit)
            
            if args.json:
                print(json.dumps(branches, indent=2))
            else:
                if branches:
                    print(f"\n📋 Found {len(branches)} branch(es):")
                    for branch in branches:
                        default_marker = " [DEFAULT]" if branch.get('is_default') else ""
                        print(f"\n  Branch: {branch['name']}{default_marker}")
                        print(f"  ID: {branch['id']}")
                        print(f"  Description: {branch.get('description', 'No description')}")
                        print(f"  Created: {branch.get('created_date', 'N/A')[:10]} by {branch.get('created_by', 'N/A')}")
                else:
                    print("No branches found")
        
        elif args.create:
            # Create branch
            result = manager.create_branch(
                name=args.create,
                description=args.description,
                parent_branch_id=args.parent_branch
            )
            
            if args.json:
                print(json.dumps(result, indent=2))
            elif result:
                print(f"\n📋 Branch created:")
                print(f"  Name: {result['name']}")
                print(f"  ID: {result['id']}")
                print(f"  Description: {result.get('description', '')}")
        
        elif args.get:
            # Get branch details
            branch = manager.get_branch(args.get)
            
            if args.json:
                print(json.dumps(branch, indent=2))
            elif branch:
                print(f"\n📋 Branch Details:")
                print(f"  Name: {branch['name']}")
                print(f"  ID: {branch['id']}")
                print(f"  Description: {branch.get('description', 'No description')}")
                print(f"  Default: {branch.get('is_default', False)}")
                print(f"  Parent Branch: {branch.get('parent_branch_id', 'None')}")
                print(f"  Created: {branch.get('created_date', 'N/A')} by {branch.get('created_by', 'N/A')}")
                print(f"  Modified: {branch.get('modified_date', 'N/A')} by {branch.get('modified_by', 'N/A')}")
        
        elif args.query:
            # Query branches
            branches = manager.query_branches(
                name_pattern=args.name,
                created_by=args.created_by,
                limit=args.limit
            )
            
            if args.json:
                print(json.dumps(branches, indent=2))
            else:
                if branches:
                    print(f"\n📋 Found {len(branches)} matching branch(es):")
                    for branch in branches:
                        default_marker = " [DEFAULT]" if branch.get('is_default') else ""
                        print(f"\n  Branch: {branch['name']}{default_marker}")
                        print(f"  ID: {branch['id']}")
                        print(f"  Created: {branch.get('created_date', 'N/A')[:10]} by {branch.get('created_by', 'N/A')}")
                else:
                    print("No matching branches found")
        
        elif args.delete:
            # Delete branch
            success = manager.delete_branch(args.delete)
            if not success and not args.json:
                sys.exit(1)
        
        elif args.stats:
            # Show statistics
            manager.show_statistics()
        
        else:
            parser.print_help()
            
    except KeyboardInterrupt:
        print("\n\n⚠️ Operation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()