#!/usr/bin/env python3
"""
Boomi SDK Example: Query Environment-Runtime Attachments (Fixed Version)
========================================================================

This example demonstrates how to query environment-runtime attachments using the Boomi SDK.
It shows which runtimes are attached to which environments.

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- Account must have appropriate permissions to read attachments
- At least one runtime should be attached to an environment

Usage:
    cd examples/environment_management
    PYTHONPATH=../../src python3 query_environment_runtime_attachments_fixed.py

Features:
- Lists all environment-runtime attachments
- Shows which runtimes are attached to which environments
- Displays attachment details (runtime ID, environment ID, attachment ID)
- Uses working query approach that gets results
"""

import os
import sys

# Add the src directory to the path to import the SDK
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

from boomi import Boomi
from boomi.models import (
    EnvironmentQueryConfig,
    EnvironmentQueryConfigQueryFilter,
    EnvironmentSimpleExpression,
    EnvironmentSimpleExpressionOperator,
    EnvironmentSimpleExpressionProperty,
    EnvironmentAtomAttachmentQueryConfig,
    EnvironmentAtomAttachmentQueryConfigQueryFilter,
    EnvironmentAtomAttachmentSimpleExpression,
    EnvironmentAtomAttachmentSimpleExpressionOperator,
    EnvironmentAtomAttachmentSimpleExpressionProperty
)

def query_all_attachments(sdk):
    """Query all environment-runtime attachments by checking each environment."""
    
    print("🔍 Querying all environment-runtime attachments...")
    
    try:
        # Step 1: Get all environments (TEST and PROD)
        all_environments = []
        
        # Query TEST environments
        test_expression = EnvironmentSimpleExpression(
            operator=EnvironmentSimpleExpressionOperator.CONTAINS,
            property=EnvironmentSimpleExpressionProperty.CLASSIFICATION,
            argument=["TEST"]
        )
        test_filter = EnvironmentQueryConfigQueryFilter(expression=test_expression)
        test_config = EnvironmentQueryConfig(query_filter=test_filter)
        test_response = sdk.environment.query_environment(test_config)
        
        if test_response and hasattr(test_response, 'result') and test_response.result:
            test_envs = test_response.result if isinstance(test_response.result, list) else [test_response.result]
            all_environments.extend(test_envs)
        
        # Query PROD environments
        prod_expression = EnvironmentSimpleExpression(
            operator=EnvironmentSimpleExpressionOperator.EQUALS,
            property=EnvironmentSimpleExpressionProperty.CLASSIFICATION,
            argument=["PROD"]
        )
        prod_filter = EnvironmentQueryConfigQueryFilter(expression=prod_expression)
        prod_config = EnvironmentQueryConfig(query_filter=prod_filter)
        prod_response = sdk.environment.query_environment(prod_config)
        
        if prod_response and hasattr(prod_response, 'result') and prod_response.result:
            prod_envs = prod_response.result if isinstance(prod_response.result, list) else [prod_response.result]
            all_environments.extend(prod_envs)
        
        print(f"   Found {len(all_environments)} environments to check")
        
        # Step 2: Query attachments for each environment
        all_attachments = []
        
        for env in all_environments:
            env_id = getattr(env, 'id_', 'unknown')
            env_name = getattr(env, 'name', 'unknown')
            env_class = getattr(env, 'classification', 'unknown')
            
            print(f"     Checking {env_class} environment: {env_name}")
            
            try:
                # Query attachments for this specific environment
                attachment_expression = EnvironmentAtomAttachmentSimpleExpression(
                    operator=EnvironmentAtomAttachmentSimpleExpressionOperator.EQUALS,
                    property=EnvironmentAtomAttachmentSimpleExpressionProperty.ENVIRONMENTID,
                    argument=[env_id]
                )
                
                attachment_filter = EnvironmentAtomAttachmentQueryConfigQueryFilter(expression=attachment_expression)
                attachment_config = EnvironmentAtomAttachmentQueryConfig(query_filter=attachment_filter)
                
                attachment_response = sdk.environment_atom_attachment.query_environment_atom_attachment(attachment_config)
                
                if attachment_response and hasattr(attachment_response, 'result') and attachment_response.result:
                    env_attachments = attachment_response.result if isinstance(attachment_response.result, list) else [attachment_response.result]
                    print(f"       ✅ Found {len(env_attachments)} attachment(s)")
                    
                    # Add environment info to each attachment for display
                    for attachment in env_attachments:
                        attachment._environment_name = env_name
                        attachment._environment_class = env_class
                    
                    all_attachments.extend(env_attachments)
                else:
                    print(f"       ❌ No attachments")
                    
            except Exception as env_error:
                print(f"       ❌ Error: {str(env_error)}")
        
        print(f"\n📊 Total attachments found: {len(all_attachments)}")
        return all_attachments
        
    except Exception as e:
        print(f"❌ Error querying attachments: {str(e)}")
        return []

def get_runtime_name(sdk, runtime_id):
    """Get runtime name from ID."""
    try:
        runtime = sdk.atom.get_atom(id_=runtime_id)
        if hasattr(runtime, '_kwargs') and 'Atom' in runtime._kwargs:
            return runtime._kwargs['Atom'].get('@name', 'Unknown')
        elif hasattr(runtime, 'name'):
            return runtime.name
    except:
        pass
    return f"Runtime-{runtime_id[:8]}..."

def display_attachments(sdk, attachments):
    """Display attachment information in a formatted way."""
    
    if not attachments:
        print("\n❌ No environment-runtime attachments found")
        print("\n💡 This could mean:")
        print("   • No runtimes are currently attached to environments")
        print("   • There are permission issues reading attachments")
        print("   • All runtimes are running without environment attachments")
        return
    
    print(f"\n✅ Found {len(attachments)} environment-runtime attachment(s):")
    print("=" * 100)
    
    for i, attachment in enumerate(attachments, 1):
        # Get attachment details
        runtime_id = getattr(attachment, 'atom_id', 'N/A')
        env_id = getattr(attachment, 'environment_id', 'N/A')
        attachment_id = getattr(attachment, 'id_', 'N/A')
        
        # Get environment details from our added attributes
        env_name = getattr(attachment, '_environment_name', 'Unknown')
        env_class = getattr(attachment, '_environment_class', 'Unknown')
        
        # Get runtime name
        runtime_name = get_runtime_name(sdk, runtime_id)
        
        # Status icon based on classification
        class_icon = "🔴" if env_class == "PROD" else "🟡" if env_class == "TEST" else "⚪"
        
        print(f"{i:2}. {class_icon} Attachment: {attachment_id[:30]}...")
        print(f"     🤖 Runtime: {runtime_name}")
        print(f"        🆔 Runtime ID: {runtime_id}")
        print(f"     📂 Environment: {env_name} ({env_class})")
        print(f"        🆔 Environment ID: {env_id}")
        print()
    
    # Summary by environment classification
    test_count = sum(1 for a in attachments if getattr(a, '_environment_class', '') == 'TEST')
    prod_count = sum(1 for a in attachments if getattr(a, '_environment_class', '') == 'PROD')
    
    print("📊 Summary:")
    print(f"   🟡 TEST environment attachments: {test_count}")
    print(f"   🔴 PROD environment attachments: {prod_count}")
    print(f"   📋 Total attachments: {len(attachments)}")

def main():
    """Main function to demonstrate attachment querying."""
    
    print("🚀 Boomi SDK - Query Environment-Runtime Attachments (Fixed)")
    print("=" * 70)
    
    # Check for required environment variables
    required_vars = ["BOOMI_ACCOUNT", "BOOMI_USER", "BOOMI_SECRET"]
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars:
        print("❌ Missing required environment variables:")
        for var in missing_vars:
            print(f"   - {var}")
        sys.exit(1)
    
    # Initialize the SDK
    sdk = Boomi(
        account_id=os.getenv("BOOMI_ACCOUNT"),
        username=os.getenv("BOOMI_USER"),
        password=os.getenv("BOOMI_SECRET"),
        timeout=30000,
    )
    
    print("✅ SDK initialized successfully!")
    print()
    
    try:
        # Query all attachments using the working approach
        attachments = query_all_attachments(sdk)
        
        # Display results
        display_attachments(sdk, attachments)
        
        if attachments:
            print("\n💡 Use Cases for Attachment Information:")
            print("   • Verify deployment targets before process execution")
            print("   • Audit runtime distribution across environments")
            print("   • Troubleshoot deployment and execution issues")
            print("   • Plan runtime resource allocation")
            print("   • Monitor environment-runtime relationships")
        else:
            print("\n💡 Next Steps:")
            print("   • Attach runtimes to environments for process deployment")
            print("   • Use simple_attach_runtime.py to create attachments")
            print("   • Ensure runtimes are online and environments exist")
        
    except Exception as e:
        print(f"❌ Example failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()