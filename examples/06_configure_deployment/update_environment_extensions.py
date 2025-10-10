#!/usr/bin/env python3
"""
Update Environment Extensions

This example demonstrates how to get and update environment extensions.
Environment extensions allow you to configure additional settings and
customizations for your Boomi environments.

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET

Usage:
    python update_environment_extensions.py [ENVIRONMENT_ID]

    If ENVIRONMENT_ID is not provided, the script will list available environments.

Examples:
    python update_environment_extensions.py                          # List environments
    python update_environment_extensions.py 74851c30-98b2-4a6f       # Update specific environment

Endpoint:
- environment_extensions.get_environment_extensions
- environment_extensions.update_environment_extensions
"""

import os
import sys
import argparse
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

from boomi import Boomi
from boomi.models import (
    EnvironmentExtensions,
    EnvironmentQueryConfig,
    EnvironmentSimpleExpression,
    EnvironmentSimpleExpressionOperator,
    EnvironmentQueryConfigQueryFilter
)

def list_environments(sdk):
    """List available environments"""
    print("🔍 Querying environments...")

    try:
        # Create query to get all environments
        simple_expression = EnvironmentSimpleExpression(
            operator=EnvironmentSimpleExpressionOperator.LIKE,
            property="name",
            argument=["%"]  # Wildcard to match all
        )
        query_filter = EnvironmentQueryConfigQueryFilter(
            expression=simple_expression
        )
        query_config = EnvironmentQueryConfig(
            query_filter=query_filter
        )

        # Query environments
        result = sdk.environment.query_environment(request_body=query_config)

        if hasattr(result, 'result') and result.result:
            print(f"✅ Found {len(result.result)} environment(s):")
            for env in result.result:
                env_id = getattr(env, 'id_', 'N/A')
                env_name = getattr(env, 'name', 'N/A')
                print(f"   - {env_name} (ID: {env_id})")
            return True
        else:
            print("❌ No environments found")
            return False

    except Exception as e:
        print(f"❌ Error querying environments: {e}")
        return False

def get_environment_extensions(sdk, environment_id):
    """Get current environment extensions"""
    print(f"📋 Getting current environment extensions for: {environment_id}")

    try:
        result = sdk.environment_extensions.get_environment_extensions(id_=environment_id)

        print("✅ Current environment extensions:")
        print(f"   Environment ID: {getattr(result, 'environment_id', 'N/A')}")
        print(f"   Extension Group ID: {getattr(result, 'extension_group_id', 'N/A') or 'None'}")

        # Display all attributes
        for attr in dir(result):
            if not attr.startswith('_') and attr not in ['environment_id', 'extension_group_id', 'id_']:
                value = getattr(result, attr, None)
                if value is not None and not callable(value):
                    print(f"   {attr}: {value}")

        return result

    except Exception as e:
        print(f"❌ Error getting environment extensions: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(
        description="Get and update environment extensions",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                                         # List all environments
  %(prog)s 74851c30-98b2-4a6f-838b-61eee5627b13   # Update specific environment
  %(prog)s --get-only 74851c30-98b2-4a6f          # Only get extensions, don't update
        """
    )

    parser.add_argument('environment_id', nargs='?',
                        help='Environment ID (optional, lists environments if not provided)')
    parser.add_argument('--get-only', action='store_true',
                        help='Only get extensions, do not update')
    parser.add_argument('--extension-group-id', type=str,
                        help='Extension group ID to set')

    args = parser.parse_args()

    if not args.environment_id:
        print("No environment ID provided. Here are the available environments:")
        print()
        # Initialize SDK
        sdk = Boomi(
            account_id=os.getenv("BOOMI_ACCOUNT"),
            username=os.getenv("BOOMI_USER"),
            password=os.getenv("BOOMI_SECRET"),
            timeout=30000,
        )

        # List environments and exit
        list_environments(sdk)
        print()
        print("💡 Run this script with one of the environment IDs above to get/update extensions")
        sys.exit(0)

    environment_id = args.environment_id

    # Initialize SDK
    sdk = Boomi(
        account_id=os.getenv("BOOMI_ACCOUNT"),
        username=os.getenv("BOOMI_USER"),
        password=os.getenv("BOOMI_SECRET"),
        timeout=30000,
    )

    # Get current extensions
    print()
    current = get_environment_extensions(sdk, environment_id)

    if args.get_only:
        sys.exit(0)

    # Update extensions
    print()
    print(f"🔄 Updating environment extensions for: {environment_id}")

    try:
        # Create update request
        extensions_update = EnvironmentExtensions(
            environment_id=environment_id,
            # Add extension properties as needed
        )

        # Add extension group ID if provided
        if args.extension_group_id:
            extensions_update.extension_group_id = args.extension_group_id
            print(f"   Setting extension group ID: {args.extension_group_id}")

        # Update environment extensions
        result = sdk.environment_extensions.update_environment_extensions(
            id_=environment_id,
            request_body=extensions_update
        )

        print("✅ Environment extensions updated successfully!")

        # Show updated extensions
        print()
        get_environment_extensions(sdk, environment_id)

    except Exception as e:
        print(f"❌ Error updating environment extensions: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()