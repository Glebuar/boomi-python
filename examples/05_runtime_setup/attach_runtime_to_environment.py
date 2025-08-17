#!/usr/bin/env python3
"""
Boomi SDK Example: Attach Runtime to Environment
===============================================

This example demonstrates how to attach a runtime to an environment
using the Boomi SDK. This is essential for deployment and execution of processes.

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- Account must have appropriate permissions to manage environments and runtimes
- At least one runtime must be available in the account

Usage:
    cd examples/environment_management
    PYTHONPATH=../../src python3 attach_runtime_to_environment.py [runtime_id] [environment_id]

Features:
- Lists available runtimes and environments
- Creates attachment between runtime and environment
- Shows attachment details and verification
- Creates test environment if none provided
- Handles account type limitations (Basic vs Unlimited environment support)
"""

import os
import sys

# Add the src directory to the path to import the SDK
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

from boomi import Boomi
from boomi.models import (
    Environment as EnvironmentModel,
    EnvironmentClassification, 
    EnvironmentAtomAttachment,
    AtomQueryConfig,
    AtomQueryConfigQueryFilter,
    AtomSimpleExpression,
    AtomSimpleExpressionOperator,
    AtomSimpleExpressionProperty,
    EnvironmentAtomAttachmentQueryConfig,
    EnvironmentAtomAttachmentQueryConfigQueryFilter,
    EnvironmentAtomAttachmentSimpleExpression,
    EnvironmentAtomAttachmentSimpleExpressionOperator,
    EnvironmentAtomAttachmentSimpleExpressionProperty
)
import datetime

def list_available_runtimes(sdk):
    """List all available runtimes in the account."""
    
    print("🔍 Retrieving available runtimes...")
    
    try:
        # Create a query to get runtimes - filter by type containing "ATOM"
        # This should match most runtime types (ATOM, GATEWAY, etc.)
        simple_expression = AtomSimpleExpression(
            operator=AtomSimpleExpressionOperator.CONTAINS,
            property=AtomSimpleExpressionProperty.TYPE,
            argument=["ATOM"]
        )
        
        query_filter = AtomQueryConfigQueryFilter(expression=simple_expression)
        query_config = AtomQueryConfig(query_filter=query_filter)
        query_response = sdk.atom.query_atom(query_config)
        
        # Use modern SDK response format
        runtimes = []
        if hasattr(query_response, 'result') and query_response.result:
            runtimes = query_response.result if isinstance(query_response.result, list) else [query_response.result]
        
        if not runtimes:
            print("❌ No runtimes found in the account")
            print("   • Make sure you have at least one installed runtime")
            print("   • Check if your account has permission to view runtimes")
            return []
        
        print(f"\n✅ Found {len(runtimes)} runtime(s):")
        print("-" * 80)
        
        for i, runtime in enumerate(runtimes, 1):
            runtime_id = runtime.get('@id', 'N/A')
            runtime_name = runtime.get('@name', 'N/A')
            runtime_type = runtime.get('@type', 'N/A')
            runtime_status = runtime.get('@status', 'N/A')
            
            print(f"{i:2}. {runtime_name}")
            print(f"    ID: {runtime_id}")
            print(f"    Type: {runtime_type}")
            print(f"    Status: {runtime_status}")
            print()
        
        return runtimes
        
    except Exception as e:
        print(f"❌ Error querying runtimes: {str(e)}")
        if hasattr(e, 'status'):
            if e.status == 403:
                print("   Permission denied - check if your account can read runtimes")
        return []

def list_available_environments(sdk):
    """List all available environments in the account."""
    
    print("🔍 Retrieving available environments...")
    
    try:
        from boomi.models import EnvironmentQueryConfig
        
        # Query all environments
        query_config = EnvironmentQueryConfig()
        query_response = sdk.environment.query_environment(query_config)
        
        # Use modern SDK response format
        environments = []
        if hasattr(query_response, 'result') and query_response.result:
            environments = query_response.result if isinstance(query_response.result, list) else [query_response.result]
        
        if not environments:
            print("❌ No environments found")
            return []
        
        print(f"\n✅ Found {len(environments)} environment(s):")
        print("-" * 80)
        
        for i, env in enumerate(environments, 1):
            # Use object attributes for Environment objects
            env_id = getattr(env, 'id_', 'N/A')
            env_name = getattr(env, 'name', 'N/A')
            env_class = getattr(env, 'classification', 'N/A')
            
            print(f"{i:2}. {env_name}")
            print(f"    ID: {env_id}")
            print(f"    Classification: {env_class}")
            print()
        
        return environments
        
    except Exception as e:
        print(f"❌ Error querying environments: {str(e)}")
        return []

def check_existing_attachments(sdk, runtime_id=None, environment_id=None):
    """Check for existing runtime-environment attachments."""
    
    print("🔗 Checking existing runtime-environment attachments...")
    
    try:
        # Query existing attachments - use a filter to get all attachments
        # Filter by environment ID contains any character to get all attachments
        simple_expression = EnvironmentAtomAttachmentSimpleExpression(
            operator=EnvironmentAtomAttachmentSimpleExpressionOperator.CONTAINS,
            property=EnvironmentAtomAttachmentSimpleExpressionProperty.ENVIRONMENT_ID,
            argument=[""]
        )
        
        query_filter = EnvironmentAtomAttachmentQueryConfigQueryFilter(expression=simple_expression)
        query_config = EnvironmentAtomAttachmentQueryConfig(query_filter=query_filter)
        query_response = sdk.environment_atom_attachment.query_environment_atom_attachment(query_config)
        
        # Use modern SDK response format
        attachments = []
        if hasattr(query_response, 'result') and query_response.result:
            attachments = query_response.result if isinstance(query_response.result, list) else [query_response.result]
        
        if attachments:
            print(f"\n📋 Found {len(attachments)} existing attachment(s):")
            print("-" * 60)
            
            for attachment in attachments:
                # Use object attributes for EnvironmentAtomAttachment objects
                att_id = getattr(attachment, 'id_', 'N/A')
                att_atom_id = getattr(attachment, 'atom_id', 'N/A')
                att_env_id = getattr(attachment, 'environment_id', 'N/A')
                
                print(f"  Attachment ID: {att_id}")
                print(f"  Runtime ID: {att_atom_id}")
                print(f"  Environment ID: {att_env_id}")
                
                # Check if this is the combination we're trying to create
                if runtime_id and environment_id:
                    if att_atom_id == runtime_id and att_env_id == environment_id:
                        print("  ⚠️  This runtime is already attached to this environment!")
                        return True, attachments
                
                print()
        else:
            print("   No existing attachments found")
        
        return False, attachments
        
    except Exception as e:
        print(f"❌ Error checking attachments: {str(e)}")
        return False, []

def create_runtime_environment_attachment(sdk, runtime_id, environment_id):
    """Create the attachment between runtime and environment."""
    
    print(f"🔗 Creating attachment...")
    print(f"   Runtime ID: {runtime_id}")
    print(f"   Environment ID: {environment_id}")
    
    try:
        # Create the attachment request
        attachment_request = EnvironmentAtomAttachment(
            atom_id=runtime_id,
            environment_id=environment_id
        )
        
        # Make the API call
        created_attachment = sdk.environment_atom_attachment.create_environment_atom_attachment(
            attachment_request
        )
        
        print("\n✅ Attachment created successfully!")
        
        # Parse the response
        if hasattr(created_attachment, '_kwargs') and 'EnvironmentAtomAttachment' in created_attachment._kwargs:
            attachment_data = created_attachment._kwargs['EnvironmentAtomAttachment']
            
            print("\n📋 Attachment Details:")
            print("=" * 50)
            print(f"  🆔 Attachment ID: {attachment_data.get('@id', 'N/A')}")
            print(f"  🤖 Runtime ID: {attachment_data.get('@atomId', 'N/A')}")
            print(f"  🌍 Environment ID: {attachment_data.get('@environmentId', 'N/A')}")
            print("=" * 50)
            
            return created_attachment
        else:
            print("⚠️  Unexpected response format")
            if hasattr(created_attachment, '_kwargs'):
                print(f"   Raw response: {created_attachment._kwargs}")
            return created_attachment
        
    except Exception as e:
        print(f"❌ Error creating attachment: {str(e)}")
        
        if hasattr(e, 'status'):
            if e.status == 403:
                print("\n   Permission denied (403):")
                print("   • Check if your account can manage environment attachments")
                print("   • Verify you have the correct role assignments")
            elif e.status == 409:
                print("\n   Conflict (409):")
                print("   • The runtime may already be attached to this environment")
                print("   • For Basic accounts: only one runtime per environment allowed")
            elif e.status == 404:
                print("\n   Not found (404):")
                print("   • Verify the runtime ID and environment ID are correct")
                print("   • Check if the runtime and environment exist")
            elif e.status == 400:
                print("\n   Bad request (400):")
                print("   • Check the request format and IDs")
        
        return None

def create_test_environment(sdk):
    """Create a test environment for demonstration."""
    
    print("🏗️  Creating a test environment for the attachment demonstration...")
    
    try:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        environment_name = f"SDK_Attachment_Test_{timestamp}"
        
        new_environment = EnvironmentModel(
            name=environment_name,
            classification=EnvironmentClassification.TEST
        )
        
        created_environment = sdk.environment.create_environment(new_environment)
        
        if hasattr(created_environment, '_kwargs') and 'Environment' in created_environment._kwargs:
            env_data = created_environment._kwargs['Environment']
            env_id = env_data.get('@id')
            env_name = env_data.get('@name')
            
            print(f"✅ Created test environment: {env_name}")
            print(f"   ID: {env_id}")
            return env_id, env_name
        else:
            print("❌ Could not extract environment details from response")
            return None, None
            
    except Exception as e:
        print(f"❌ Error creating test environment: {str(e)}")
        return None, None

def main():
    """Main function to demonstrate runtime-environment attachment."""
    
    print("🚀 Boomi SDK - Attach Runtime to Environment Example")
    print("=" * 60)
    
    # Check for required environment variables
    required_vars = ["BOOMI_ACCOUNT", "BOOMI_USER", "BOOMI_SECRET"]
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars:
        print("❌ Missing required environment variables:")
        for var in missing_vars:
            print(f"   - {var}")
        print("\nPlease set these variables in your environment")
        sys.exit(1)
    
    # Initialize the Boomi SDK
    sdk = Boomi(
        account_id=os.getenv("BOOMI_ACCOUNT"),
        username=os.getenv("BOOMI_USER"),
        password=os.getenv("BOOMI_SECRET"),
        timeout=30000,
    )
    
    print("✅ SDK initialized successfully!")
    print()
    
    try:
        runtime_id = None
        environment_id = None
        created_test_env = False
        
        # Parse command line arguments
        if len(sys.argv) >= 3:
            runtime_id = sys.argv[1]
            environment_id = sys.argv[2]
            print(f"📍 Using provided Runtime ID: {runtime_id}")
            print(f"📍 Using provided Environment ID: {environment_id}")
        else:
            # Step 1: List available runtimes
            runtimes = list_available_runtimes(sdk)
            if not runtimes:
                print("❌ No runtimes available for attachment")
                return
            
            # Step 2: List available environments
            environments = list_available_environments(sdk)
            if not environments:
                print("🏗️  No environments found - creating a test environment")
                environment_id, _ = create_test_environment(sdk)
                if not environment_id:
                    print("❌ Could not create test environment")
                    return
                created_test_env = True
            else:
                # Use the first environment for demonstration
                environment_id = environments[0].get('@id')
                print(f"📍 Using first environment: {environments[0].get('@name', 'Unknown')}")
            
            # Use the first runtime for demonstration
            runtime_id = runtimes[0].get('@id')
            print(f"📍 Using first runtime: {runtimes[0].get('@name', 'Unknown')}")
        
        print()
        
        # Step 3: Check for existing attachments
        already_attached, existing = check_existing_attachments(sdk, runtime_id, environment_id)
        
        if already_attached:
            print("⚠️  Runtime is already attached to this environment!")
            print("   Note: Attachment will move the runtime if it's attached elsewhere")
        
        print()
        
        # Step 4: Create the attachment
        attachment = create_runtime_environment_attachment(sdk, runtime_id, environment_id)
        
        if attachment:
            print(f"\n🎉 Successfully attached runtime to environment!")
            
            # Step 5: Verify the attachment was created
            print("\n🔍 Verifying attachment...")
            _, updated_attachments = check_existing_attachments(sdk)
            
        # Clean up test environment if we created one
        if created_test_env:
            print("\n" + "=" * 60)
            response = input("Would you like to delete the test environment? (y/n): ")
            
            if response.lower() == 'y':
                print(f"\n🗑️  Deleting test environment...")
                # Note: This will also remove the attachment
                sdk.environment.delete_environment(id_=environment_id)
                print("✅ Test environment deleted successfully!")
            else:
                print(f"💡 Test environment kept with ID: {environment_id}")
                print("   Remember: The runtime is now attached to this environment")
        
    except KeyboardInterrupt:
        print("\n❌ Operation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Example failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()