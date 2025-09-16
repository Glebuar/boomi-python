#!/usr/bin/env python3
"""
Boomi SDK Example: Comprehensive Environment Management
=====================================================

This example provides comprehensive environment management capabilities using the Boomi SDK.
It combines all environment CRUD operations and query functionality into a single tool.

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- Account must have appropriate permissions for environment operations
- Python 3.7+

Usage:
    # List all environments
    PYTHONPATH=../../src python3 manage_environments.py --list
    
    # List environments with filtering
    PYTHONPATH=../../src python3 manage_environments.py --list --classification TEST
    PYTHONPATH=../../src python3 manage_environments.py --list --name-pattern "*Dev*"
    
    # Get specific environment details
    PYTHONPATH=../../src python3 manage_environments.py --get ENVIRONMENT_ID
    
    # Create environment
    PYTHONPATH=../../src python3 manage_environments.py --create "New Environment" --classification TEST
    
    # Update environment name
    PYTHONPATH=../../src python3 manage_environments.py --update ENVIRONMENT_ID --name "Updated Name"
    
    # Delete environment (with confirmation)
    PYTHONPATH=../../src python3 manage_environments.py --delete ENVIRONMENT_ID
    
    # Query environments with custom filters
    PYTHONPATH=../../src python3 manage_environments.py --query --property name --operator LIKE --value "*test*"
    
    # Show environment statistics
    PYTHONPATH=../../src python3 manage_environments.py --stats
    
    # Help and examples
    PYTHONPATH=../../src python3 manage_environments.py --help-examples

Features:
- Complete CRUD operations for environments
- Advanced filtering and querying capabilities
- Environment statistics and analysis
- Detailed information display
- Safe deletion with confirmation
- Comprehensive error handling

Endpoints Used:
- environment.get_environment
- environment.query_environment
- environment.create_environment  
- environment.update_environment
- environment.delete_environment
"""

import os
import sys
import argparse
import time
from datetime import datetime
from typing import List, Optional, Dict, Any

# Add the src directory to the path to import the SDK
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

# Load environment variables from .env file if available
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv is optional

from boomi import Boomi
from boomi.models import (
    Environment as EnvironmentModel,
    EnvironmentClassification,
    EnvironmentQueryConfig,
    EnvironmentQueryConfigQueryFilter,
    EnvironmentSimpleExpression,
    EnvironmentSimpleExpressionOperator,
    EnvironmentSimpleExpressionProperty
)


class EnvironmentManager:
    """Comprehensive environment management using Boomi SDK."""
    
    def __init__(self, account_id: str, username: str, password: str, timeout: int = 30000):
        """Initialize the Environment Manager with Boomi SDK."""
        self.sdk = Boomi(
            account_id=account_id,
            username=username,
            password=password,
            timeout=timeout
        )
    
    def list_environments(self, classification: Optional[str] = None, 
                         name_pattern: Optional[str] = None,
                         limit: Optional[int] = None) -> List[Any]:
        """
        List environments with optional filtering.
        
        Args:
            classification: Filter by classification (TEST, PROD, etc.)
            name_pattern: Filter by name pattern (supports wildcards)
            limit: Limit number of results
        
        Returns:
            List of environment objects
        """
        try:
            # Start with no filter - need to create a basic expression for empty query
            from boomi.models import EnvironmentSimpleExpression, EnvironmentSimpleExpressionOperator, EnvironmentSimpleExpressionProperty
            
            # Create default query to get all environments (use ISNOTNULL on ID)
            default_expr = EnvironmentSimpleExpression(
                operator=EnvironmentSimpleExpressionOperator.ISNOTNULL,
                property=EnvironmentSimpleExpressionProperty.ID,
                argument=[]
            )
            
            # Add filters if specified
            if classification or name_pattern:
                if classification and name_pattern:
                    # Both filters - this would need complex grouping
                    print("⚠️  Warning: Using classification filter only (complex filtering not implemented)")
                    filter_expr = EnvironmentSimpleExpression(
                        operator=EnvironmentSimpleExpressionOperator.EQUALS,
                        property=EnvironmentSimpleExpressionProperty.CLASSIFICATION,
                        argument=[classification.upper()]
                    )
                elif classification:
                    filter_expr = EnvironmentSimpleExpression(
                        operator=EnvironmentSimpleExpressionOperator.EQUALS,
                        property=EnvironmentSimpleExpressionProperty.CLASSIFICATION,
                        argument=[classification.upper()]
                    )
                elif name_pattern:
                    # Convert wildcards to LIKE operator format
                    like_pattern = name_pattern.replace('*', '%')
                    filter_expr = EnvironmentSimpleExpression(
                        operator=EnvironmentSimpleExpressionOperator.LIKE,
                        property=EnvironmentSimpleExpressionProperty.NAME,
                        argument=[like_pattern]
                    )
                
                query_filter = EnvironmentQueryConfigQueryFilter(expression=filter_expr)
                query_config = EnvironmentQueryConfig(query_filter=query_filter)
            else:
                # No specific filters - use default query to get all environments
                query_filter = EnvironmentQueryConfigQueryFilter(expression=default_expr)
                query_config = EnvironmentQueryConfig(query_filter=query_filter)
            
            print("🔍 Querying environments...")
            response = self.sdk.environment.query_environment(query_config)
            
            environments = []
            if hasattr(response, 'result') and response.result:
                result_data = response.result
                if isinstance(result_data, list):
                    environments = result_data
                else:
                    environments = [result_data]
            
            if limit and len(environments) > limit:
                environments = environments[:limit]
            
            return environments
            
        except Exception as e:
            print(f"❌ Error listing environments: {e}")
            return []
    
    def get_environment(self, environment_id: str) -> Optional[Any]:
        """
        Get detailed information about a specific environment.
        
        Args:
            environment_id: The environment ID
            
        Returns:
            Environment object or None if not found
        """
        try:
            print(f"🔍 Getting environment details for: {environment_id}")
            environment = self.sdk.environment.get_environment(id_=environment_id)
            return environment
            
        except Exception as e:
            print(f"❌ Error getting environment {environment_id}: {e}")
            if hasattr(e, 'status') and e.status == 404:
                print("   Environment not found")
            return None
    
    def create_environment(self, name: str, classification: str = "TEST") -> Optional[Any]:
        """
        Create a new environment.
        
        Args:
            name: Environment name
            classification: Environment classification (TEST, PROD, etc.)
            
        Returns:
            Created environment object or None if failed
        """
        try:
            print(f"🏗️  Creating environment: {name}")
            print(f"   Classification: {classification}")
            
            # Validate classification
            try:
                class_enum = getattr(EnvironmentClassification, classification.upper())
            except AttributeError:
                print(f"❌ Invalid classification: {classification}")
                print("   Valid options: TEST, PROD, STAGING, DEV")
                return None
            
            new_environment = EnvironmentModel(
                name=name,
                classification=class_enum
            )
            
            created_environment = self.sdk.environment.create_environment(new_environment)
            print("✅ Environment created successfully!")
            return created_environment
            
        except Exception as e:
            print(f"❌ Error creating environment: {e}")
            if hasattr(e, 'status'):
                if e.status == 409:
                    print("   Conflict - environment name may already exist")
                elif e.status == 403:
                    print("   Permission denied - check account permissions")
            return None
    
    def update_environment(self, environment_id: str, new_name: str) -> Optional[Any]:
        """
        Update an environment's name.
        Note: Only the name can be updated - classification is immutable.

        Args:
            environment_id: Environment ID to update
            new_name: New environment name

        Returns:
            Updated environment object or None if failed
        """
        try:
            print(f"🔄 Updating environment: {environment_id}")
            print(f"   New name: {new_name}")

            # Get current environment to get the classification
            current_env = self.get_environment(environment_id)
            if not current_env:
                print("   Failed to get current environment details")
                return None

            # API requires all fields including ID and classification
            update_request = EnvironmentModel(
                id_=environment_id,
                name=new_name,
                classification=current_env.classification
            )

            updated_environment = self.sdk.environment.update_environment(
                id_=environment_id,
                request_body=update_request
            )
            
            print("✅ Environment updated successfully!")
            return updated_environment
            
        except Exception as e:
            print(f"❌ Error updating environment: {e}")
            if hasattr(e, 'status'):
                if e.status == 404:
                    print("   Environment not found")
                elif e.status == 409:
                    print("   Conflict - name may already exist")
                elif e.status == 403:
                    print("   Permission denied")
            return None
    
    def delete_environment(self, environment_id: str, force: bool = False) -> bool:
        """
        Delete an environment.
        WARNING: This is permanent and cannot be undone!
        
        Args:
            environment_id: Environment ID to delete
            force: Skip confirmation prompt
            
        Returns:
            True if deletion successful, False otherwise
        """
        try:
            print(f"🗑️  Preparing to delete environment: {environment_id}")
            
            # Get environment details first
            env = self.get_environment(environment_id)
            if env:
                env_name = getattr(env, 'name', 'Unknown')
                env_class = getattr(env, 'classification', 'Unknown')
                print(f"   Environment: {env_name} ({env_class})")
            
            print("⚠️  WARNING: Deletion is permanent and cannot be undone!")
            
            if not force:
                confirm = input("Type 'DELETE' to confirm deletion: ").strip()
                if confirm != 'DELETE':
                    print("❌ Deletion cancelled")
                    return False
            
            self.sdk.environment.delete_environment(id_=environment_id)
            print("✅ Environment deleted successfully!")
            return True
            
        except Exception as e:
            print(f"❌ Error deleting environment: {e}")
            if hasattr(e, 'status'):
                if e.status == 404:
                    print("   Environment not found")
                elif e.status == 409:
                    print("   Conflict - environment may have attached runtimes or deployed components")
                elif e.status == 403:
                    print("   Permission denied")
            return False
    
    def query_environments(self, property_name: str, operator: str, value: str) -> List[Any]:
        """
        Query environments with custom filters.
        
        Args:
            property_name: Property to filter on (name, classification, etc.)
            operator: Comparison operator (EQUALS, LIKE, etc.)
            value: Value to compare against
            
        Returns:
            List of matching environments
        """
        try:
            print(f"🔍 Querying environments: {property_name} {operator} {value}")
            
            # Map property names
            property_map = {
                'name': EnvironmentSimpleExpressionProperty.NAME,
                'classification': EnvironmentSimpleExpressionProperty.CLASSIFICATION,
                'id': EnvironmentSimpleExpressionProperty.ID
            }
            
            # Map operators
            operator_map = {
                'EQUALS': EnvironmentSimpleExpressionOperator.EQUALS,
                'LIKE': EnvironmentSimpleExpressionOperator.LIKE,
                'CONTAINS': EnvironmentSimpleExpressionOperator.CONTAINS
            }
            
            if property_name not in property_map:
                print(f"❌ Invalid property: {property_name}")
                print(f"   Valid options: {', '.join(property_map.keys())}")
                return []
            
            if operator not in operator_map:
                print(f"❌ Invalid operator: {operator}")
                print(f"   Valid options: {', '.join(operator_map.keys())}")
                return []
            
            filter_expr = EnvironmentSimpleExpression(
                operator=operator_map[operator],
                property=property_map[property_name],
                argument=[value]
            )
            
            query_filter = EnvironmentQueryConfigQueryFilter(expression=filter_expr)
            query_config = EnvironmentQueryConfig(query_filter=query_filter)
            
            response = self.sdk.environment.query_environment(query_config)
            
            environments = []
            if hasattr(response, 'result') and response.result:
                result_data = response.result
                if isinstance(result_data, list):
                    environments = result_data
                else:
                    environments = [result_data]
            
            return environments
            
        except Exception as e:
            print(f"❌ Error querying environments: {e}")
            return []
    
    def get_environment_stats(self) -> Dict[str, Any]:
        """
        Get comprehensive environment statistics.
        
        Returns:
            Dictionary with environment statistics
        """
        try:
            print("📊 Gathering environment statistics...")
            
            # Get all environments
            all_envs = self.list_environments()
            
            if not all_envs:
                return {"total": 0}
            
            stats = {
                "total": len(all_envs),
                "by_classification": {},
                "names": []
            }
            
            # Analyze environments
            for env in all_envs:
                classification = getattr(env, 'classification', 'Unknown')
                name = getattr(env, 'name', 'Unknown')
                
                stats["by_classification"][classification] = stats["by_classification"].get(classification, 0) + 1
                stats["names"].append(name)
            
            return stats
            
        except Exception as e:
            print(f"❌ Error getting environment statistics: {e}")
            return {"error": str(e)}


def display_environment(env: Any, detailed: bool = False) -> None:
    """Display environment information in a formatted way."""
    
    env_id = getattr(env, 'id_', 'N/A')
    env_name = getattr(env, 'name', 'N/A')
    env_class = getattr(env, 'classification', 'N/A')
    
    # Classification-specific icons
    class_icons = {
        'TEST': '🧪',
        'PROD': '🏭',
        'STAGING': '🎭',
        'DEV': '🔧'
    }
    
    icon = class_icons.get(env_class, '📂')
    
    print(f"{icon} {env_name}")
    print(f"   🆔 ID: {env_id}")
    print(f"   🏷️  Classification: {env_class}")
    
    if detailed:
        # Try to get additional details if available
        created_by = getattr(env, 'created_by', None)
        created_date = getattr(env, 'created_date', None)
        
        if created_by:
            print(f"   👤 Created by: {created_by}")
        if created_date:
            print(f"   📅 Created: {created_date}")
    
    print()


def display_environments_list(environments: List[Any], title: str = "Environments", detailed: bool = False) -> None:
    """Display a list of environments in a formatted way."""
    
    if not environments:
        print(f"   No {title.lower()} found")
        return
    
    print(f"\n✅ Found {len(environments)} {title.lower()}:")
    print("=" * 60)
    
    for i, env in enumerate(environments, 1):
        print(f"{i:2}. ", end="")
        display_environment(env, detailed)


def display_stats(stats: Dict[str, Any]) -> None:
    """Display environment statistics."""
    
    if "error" in stats:
        print(f"❌ Error in statistics: {stats['error']}")
        return
    
    if stats.get("total", 0) == 0:
        print("📊 No environments found")
        return
    
    print(f"\n📊 Environment Statistics:")
    print("=" * 40)
    print(f"   Total environments: {stats['total']}")
    
    if "by_classification" in stats:
        print(f"\n   By Classification:")
        for classification, count in stats["by_classification"].items():
            icon = {'TEST': '🧪', 'PROD': '🏭', 'STAGING': '🎭', 'DEV': '🔧'}.get(classification, '📂')
            print(f"     {icon} {classification}: {count}")
    
    print(f"\n💡 Tips:")
    print(f"   • TEST environments are for development and testing")
    print(f"   • PROD environments are for production deployments")
    print(f"   • Environment names must be unique within an account")
    print(f"   • Only environment names can be updated after creation")


def show_help_examples():
    """Show comprehensive usage examples."""
    
    examples = """
🚀 Environment Management Examples
=================================

LISTING ENVIRONMENTS:
  # List all environments
  python3 manage_environments.py --list
  
  # List only TEST environments
  python3 manage_environments.py --list --classification TEST
  
  # List environments with name pattern
  python3 manage_environments.py --list --name-pattern "*dev*"
  
  # List with limit
  python3 manage_environments.py --list --limit 5

ENVIRONMENT DETAILS:
  # Get specific environment
  python3 manage_environments.py --get 12345678-1234-1234-1234-123456789012
  
  # Get with detailed information
  python3 manage_environments.py --get 12345678-1234-1234-1234-123456789012 --detailed

CREATING ENVIRONMENTS:
  # Create TEST environment
  python3 manage_environments.py --create "My Test Environment"
  
  # Create PROD environment
  python3 manage_environments.py --create "Production Env" --classification PROD

UPDATING ENVIRONMENTS:
  # Update environment name
  python3 manage_environments.py --update 12345678-1234-1234-1234-123456789012 --name "New Name"

DELETING ENVIRONMENTS:
  # Delete with confirmation prompt
  python3 manage_environments.py --delete 12345678-1234-1234-1234-123456789012
  
  # Delete without confirmation (dangerous!)
  python3 manage_environments.py --delete 12345678-1234-1234-1234-123456789012 --force

QUERYING WITH FILTERS:
  # Query by name pattern
  python3 manage_environments.py --query --property name --operator LIKE --value "%test%"
  
  # Query by classification
  python3 manage_environments.py --query --property classification --operator EQUALS --value "PROD"

STATISTICS:
  # Show environment statistics
  python3 manage_environments.py --stats

COMMON WORKFLOWS:
  # Create development environment and get details
  python3 manage_environments.py --create "Dev Environment" --classification TEST
  python3 manage_environments.py --list --name-pattern "*Dev*"
  
  # Update environment name and verify
  python3 manage_environments.py --update ENV_ID --name "Updated Name"
  python3 manage_environments.py --get ENV_ID

NOTES:
  • Environment IDs are UUIDs (36 characters with hyphens)
  • Classifications: TEST, PROD, STAGING, DEV
  • Only environment names can be updated after creation
  • Deletion requires confirmation unless --force is used
  • Use quotes around names with spaces
"""
    
    print(examples)


def main():
    """Main function for environment management CLI."""
    
    parser = argparse.ArgumentParser(
        description="Comprehensive Environment Management using Boomi SDK",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Use --help-examples for detailed usage examples"
    )
    
    # Main actions (mutually exclusive)
    action_group = parser.add_mutually_exclusive_group(required=True)
    action_group.add_argument('--list', action='store_true', 
                             help='List environments')
    action_group.add_argument('--get', metavar='ENV_ID', 
                             help='Get specific environment details')
    action_group.add_argument('--create', metavar='NAME', 
                             help='Create new environment')
    action_group.add_argument('--update', metavar='ENV_ID', 
                             help='Update environment')
    action_group.add_argument('--delete', metavar='ENV_ID', 
                             help='Delete environment')
    action_group.add_argument('--query', action='store_true', 
                             help='Query environments with custom filters')
    action_group.add_argument('--stats', action='store_true', 
                             help='Show environment statistics')
    action_group.add_argument('--help-examples', action='store_true', 
                             help='Show detailed usage examples')
    
    # Options for list
    parser.add_argument('--classification', choices=['TEST', 'PROD', 'STAGING', 'DEV'], 
                       help='Filter by classification')
    parser.add_argument('--name-pattern', 
                       help='Filter by name pattern (supports wildcards)')
    parser.add_argument('--limit', type=int, 
                       help='Limit number of results')
    
    # Options for get
    parser.add_argument('--detailed', action='store_true', 
                       help='Show detailed information')
    
    # Options for create (use different dest to avoid conflict)
    parser.add_argument('--create-classification', 
                       choices=['TEST', 'PROD', 'STAGING', 'DEV'], 
                       default='TEST', help='Environment classification for create (default: TEST)')
    
    # Options for update
    parser.add_argument('--name', help='New environment name')
    
    # Options for delete
    parser.add_argument('--force', action='store_true', 
                       help='Skip confirmation prompt')
    
    # Options for query
    parser.add_argument('--property', choices=['name', 'classification', 'id'], 
                       help='Property to filter on')
    parser.add_argument('--operator', choices=['EQUALS', 'LIKE', 'CONTAINS'], 
                       help='Comparison operator')
    parser.add_argument('--value', help='Value to compare against')
    
    args = parser.parse_args()
    
    # Show examples and exit
    if args.help_examples:
        show_help_examples()
        return
    
    print("🚀 Boomi SDK - Environment Management Tool")
    print("=" * 50)
    
    # Check for required environment variables
    required_vars = ["BOOMI_ACCOUNT", "BOOMI_USER", "BOOMI_SECRET"]
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars:
        print("❌ Missing required environment variables:")
        for var in missing_vars:
            print(f"   - {var}")
        print("\nPlease set these variables in your environment")
        sys.exit(1)
    
    try:
        # Initialize Environment Manager
        env_manager = EnvironmentManager(
            account_id=os.getenv("BOOMI_ACCOUNT"),
            username=os.getenv("BOOMI_USER"), 
            password=os.getenv("BOOMI_SECRET"),
            timeout=30000
        )
        
        print("✅ SDK initialized successfully!")
        print()
        
        # Execute requested action
        if args.list:
            print("📋 Listing Environments")
            print("-" * 25)
            
            environments = env_manager.list_environments(
                classification=args.classification,
                name_pattern=args.name_pattern,
                limit=args.limit
            )
            
            display_environments_list(environments, "Environments", args.detailed)
            
            if environments:
                # Show summary
                total = len(environments)
                by_class = {}
                for env in environments:
                    classification = getattr(env, 'classification', 'Unknown')
                    by_class[classification] = by_class.get(classification, 0) + 1
                
                print("=" * 60)
                print(f"📊 Summary: {total} environment(s)")
                for classification, count in by_class.items():
                    print(f"   {classification}: {count}")
        
        elif args.get:
            print(f"🔍 Environment Details")
            print("-" * 25)
            
            environment = env_manager.get_environment(args.get)
            if environment:
                display_environment(environment, detailed=True)
                
                # Show additional details if available
                try:
                    # Try to get runtime attachments count
                    print("🔗 Additional Information:")
                    print("   (Use manage_runtimes.py to see runtime attachments)")
                    print("   (Use manage_components.py to see deployed components)")
                except:
                    pass
        
        elif args.create:
            print(f"🏗️  Creating Environment")
            print("-" * 25)
            
            created_env = env_manager.create_environment(
                name=args.create,
                classification=getattr(args, 'create_classification', 'TEST')
            )
            
            if created_env:
                display_environment(created_env, detailed=True)
        
        elif args.update:
            if not args.name:
                print("❌ --name is required for update operation")
                sys.exit(1)
            
            print(f"🔄 Updating Environment")
            print("-" * 25)
            
            updated_env = env_manager.update_environment(
                environment_id=args.update,
                new_name=args.name
            )
            
            if updated_env:
                display_environment(updated_env, detailed=True)
        
        elif args.delete:
            print(f"🗑️  Deleting Environment")
            print("-" * 25)
            
            success = env_manager.delete_environment(
                environment_id=args.delete,
                force=args.force
            )
            
            if success:
                print("\n💡 Tip: Use --list to verify the environment was deleted")
        
        elif args.query:
            if not all([args.property, args.operator, args.value]):
                print("❌ --property, --operator, and --value are all required for query")
                sys.exit(1)
            
            print(f"🔍 Querying Environments")
            print("-" * 25)
            
            environments = env_manager.query_environments(
                property_name=args.property,
                operator=args.operator,
                value=args.value
            )
            
            display_environments_list(environments, "Matching Environments")
        
        elif args.stats:
            print(f"📊 Environment Statistics")
            print("-" * 25)
            
            stats = env_manager.get_environment_stats()
            display_stats(stats)
    
    except KeyboardInterrupt:
        print("\n⏸️  Operation interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()