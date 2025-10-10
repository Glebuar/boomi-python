#!/usr/bin/env python3
"""
Boomi SDK Example: Manage Roles and Permissions
================================================

This example demonstrates how to manage user roles and permissions in Boomi.

Features:
- List all available roles
- Create custom roles with specific privileges
- Update role permissions
- Delete roles
- Query roles by name or properties

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET

Usage:
    # List all roles
    python manage_roles.py --list
    
    # Create a new role
    python manage_roles.py --create "Integration Developer" --privileges "BUILD,EXECUTE,VIEW_RESULT"
    
    # Create role with description
    python manage_roles.py --create "Test Role" --description "Testing role" --privileges "EXECUTE"
    
    # Delete a role
    python manage_roles.py --delete ROLE_ID
    
    # Query role by exact name
    python manage_roles.py --query "System Admin"

Examples:
    python manage_roles.py --list
    python manage_roles.py --create "API Developer" --privileges "API,BUILD,EXECUTE"
    python manage_roles.py --query "Admin"
"""

import os
import sys
import argparse
from typing import Optional, List

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
    Role,
    RoleQueryConfig,
    RoleQueryConfigQueryFilter,
    RoleSimpleExpression,
    RoleSimpleExpressionOperator,
    RoleSimpleExpressionProperty,
    Privileges,
    Privilege
)


class RoleManager:
    """Manages role operations in Boomi"""
    
    def __init__(self):
        """Initialize the Boomi SDK client"""
        self.sdk = Boomi(
            account_id=os.getenv("BOOMI_ACCOUNT"),
            username=os.getenv("BOOMI_USER"),
            password=os.getenv("BOOMI_SECRET"),
            timeout=30000
        )
        print("✅ SDK initialized successfully")
    
    def list_all_roles(self) -> List[Role]:
        """List all roles in the account"""
        print("\n👥 Listing all roles...")

        try:
            # Query all roles - use None expression to get all
            query_filter = RoleQueryConfigQueryFilter(expression=None)
            query_config = RoleQueryConfig(query_filter=query_filter)
            
            result = self.sdk.role.query_role(request_body=query_config)
            
            if hasattr(result, 'result') and result.result:
                roles = result.result
                print(f"Found {len(roles)} role(s)")
                
                # Separate custom vs built-in roles
                custom_roles = []
                builtin_roles = []
                
                for role in roles:
                    if hasattr(role, 'account_id') and role.account_id == os.getenv("BOOMI_ACCOUNT"):
                        custom_roles.append(role)
                    else:
                        builtin_roles.append(role)
                
                if custom_roles:
                    print(f"\n📋 Custom Roles ({len(custom_roles)}):")
                    for role in custom_roles:
                        desc = getattr(role, 'description', 'No description')
                        print(f"   🔧 {role.name}")
                        print(f"      ID: {role.id_}")
                        print(f"      Description: {desc}")
                        self._print_role_privileges(role)
                        print()
                
                if builtin_roles:
                    print(f"\n🏢 Built-in Roles ({len(builtin_roles)}):")
                    for role in builtin_roles[:5]:  # Show first 5
                        desc = getattr(role, 'description', 'No description')
                        print(f"   📌 {role.name}")
                        print(f"      Description: {desc}")
                    
                    if len(builtin_roles) > 5:
                        print(f"   ... and {len(builtin_roles) - 5} more built-in roles")
                
                return roles
            else:
                print("No roles found")
                return []
                
        except Exception as e:
            print(f"❌ Failed to list roles: {e}")
            return []
    
    def _print_role_privileges(self, role: Role) -> None:
        """Print role privileges in a readable format"""
        if hasattr(role, 'privileges') and role.privileges:
            if hasattr(role.privileges, 'privilege') and role.privileges.privilege:
                privileges = role.privileges.privilege
                if isinstance(privileges, list):
                    priv_names = [p.name for p in privileges if hasattr(p, 'name')][:5]
                    if priv_names:
                        print(f"      Privileges: {', '.join(priv_names)}")
                        if len(privileges) > 5:
                            print(f"                  ... and {len(privileges) - 5} more")
    
    def create_role(self, name: str, description: Optional[str] = None, privileges: Optional[List[str]] = None) -> Optional[str]:
        """Create a new role with specified privileges"""
        print(f"\n🔨 Creating role: {name}")
        
        try:
            # Build privileges object
            role_privileges = None
            if privileges:
                privilege_objects = []
                for priv_name in privileges:
                    privilege_objects.append(Privilege(name=priv_name))
                
                role_privileges = Privileges(privilege=privilege_objects)
                print(f"   Privileges: {', '.join(privileges)}")
            
            # Create the role
            new_role = Role(
                name=name,
                description=description,
                account_id=os.getenv("BOOMI_ACCOUNT"),
                privileges=role_privileges
            )
            
            created = self.sdk.role.create_role(request_body=new_role)
            
            print(f"✅ Role created successfully!")
            print(f"   Name: {created.name}")
            print(f"   ID: {created.id_}")
            if description:
                print(f"   Description: {description}")
            
            return created.id_
            
        except Exception as e:
            print(f"❌ Failed to create role: {e}")
            return None
    
    def delete_role(self, role_id: str) -> bool:
        """Delete a role by ID"""
        print(f"\n🗑️ Deleting role {role_id}...")
        
        try:
            # Get role details first
            role = self.sdk.role.get_role(id_=role_id)
            print(f"   Role: {role.name}")
            
            # Delete the role
            self.sdk.role.delete_role(id_=role_id)
            print(f"✅ Role deleted successfully")
            return True
            
        except Exception as e:
            print(f"❌ Failed to delete role: {e}")
            return False
    
    def query_roles_by_name(self, name_pattern: str) -> List[Role]:
        """Query roles by exact name"""
        print(f"\n🔍 Searching for roles with exact name: {name_pattern}")

        try:
            # Query for roles with exact name match
            query_expression = RoleSimpleExpression(
                operator=RoleSimpleExpressionOperator.EQUALS,
                property=RoleSimpleExpressionProperty.NAME,
                argument=[name_pattern]
            )
            
            query_filter = RoleQueryConfigQueryFilter(expression=query_expression)
            query_config = RoleQueryConfig(query_filter=query_filter)
            
            result = self.sdk.role.query_role(request_body=query_config)
            
            if hasattr(result, 'result') and result.result:
                roles = result.result
                print(f"Found {len(roles)} matching role(s):")
                
                for role in roles:
                    desc = getattr(role, 'description', 'No description')
                    account_type = "Custom" if (hasattr(role, 'account_id') and role.account_id == os.getenv("BOOMI_ACCOUNT")) else "Built-in"
                    print(f"\n   📋 {role.name} ({account_type})")
                    print(f"      ID: {role.id_}")
                    print(f"      Description: {desc}")
                    self._print_role_privileges(role)
                
                return roles
            else:
                print("No matching roles found")
                return []
                
        except Exception as e:
            print(f"❌ Failed to query roles: {e}")
            return []
    
    def show_available_privileges(self) -> None:
        """Show commonly used privileges"""
        print("\n🔑 Common Boomi Privileges:")
        
        common_privileges = {
            "Basic Access": ["EXECUTE", "VIEW_RESULT", "VIEW_DATA"],
            "Development": ["BUILD", "DEVELOPER", "BUILD_READ_ACCESS"],
            "Administration": ["ACCOUNT_ADMIN", "USER_MANAGEMENT", "ENV_MANAGEMENT"],
            "Runtime Management": ["ATOM_MANAGEMENT", "DEPLOY", "PACKAGE_MANAGEMENT"],
            "API & Integration": ["API", "INTEGRATION_PACK", "SCHEDULE_MAINTENANCE"],
            "Monitoring": ["VIEW_AUDIT_LOGS", "DASHBOARD", "VIEW_RESULT"]
        }
        
        for category, privileges in common_privileges.items():
            print(f"\n   📁 {category}:")
            for priv in privileges:
                print(f"      • {priv}")
        
        print(f"\n💡 To see all privileges in use, check existing roles with --list")


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='Manage Boomi roles and permissions',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  %(prog)s --list                                    # List all roles
  %(prog)s --create "API Developer" --privileges "API,BUILD,EXECUTE"
  %(prog)s --create "Support User" --description "Support team access" --privileges "EXECUTE,VIEW_RESULT"
  %(prog)s --query "Admin"                           # Find roles containing "Admin"
  %(prog)s --delete ROLE_ID                          # Delete specific role
  %(prog)s --privileges-help                         # Show common privileges
        '''
    )
    
    parser.add_argument('--list', action='store_true',
                       help='List all roles')
    parser.add_argument('--create', metavar='NAME',
                       help='Create a new role with the given name')
    parser.add_argument('--description',
                       help='Description for the new role')
    parser.add_argument('--privileges',
                       help='Comma-separated list of privileges (e.g., "BUILD,EXECUTE,API")')
    parser.add_argument('--delete', metavar='ROLE_ID',
                       help='Delete role by ID')
    parser.add_argument('--query', metavar='NAME',
                       help='Search for role by exact name')
    parser.add_argument('--privileges-help', action='store_true',
                       help='Show common privileges and their purposes')
    
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
        manager = RoleManager()
        
        if args.privileges_help:
            manager.show_available_privileges()
        
        elif args.list:
            manager.list_all_roles()
        
        elif args.create:
            # Parse privileges
            privilege_list = []
            if args.privileges:
                privilege_list = [p.strip().upper() for p in args.privileges.split(',')]
            
            role_id = manager.create_role(
                name=args.create,
                description=args.description,
                privileges=privilege_list if privilege_list else None
            )
            
            if role_id:
                print(f"\n✅ Successfully created role")
                print(f"   Role ID: {role_id}")
                print(f"   Name: {args.create}")
        
        elif args.delete:
            if manager.delete_role(args.delete):
                print(f"\n✅ Role deleted successfully")
        
        elif args.query:
            roles = manager.query_roles_by_name(args.query)
            if roles:
                print(f"\n💡 Use --delete ROLE_ID to remove any of these roles")
        
        else:
            parser.print_help()
            print("\n💡 Start with --list to see all available roles")
            print("💡 Use --privileges-help to see common privileges")
    
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()