#!/usr/bin/env python3
"""
Boomi SDK Example: Delete Atom
===============================

This example demonstrates how to delete an runtime (runtime) using the Boomi SDK.
It includes safety checks, confirmation prompts, and proper error handling.

⚠️  WARNING: This operation permanently deletes an runtime from your account.
   Use with extreme caution, especially in production environments.

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- Account must have Runtime Management privilege (not just read access)
- Runtime should be OFFLINE before deletion (recommended)

Usage:
    cd examples/runtime_management
    PYTHONPATH=../../src python3 delete_runtime.py [runtime_id]

Features:
- Safety checks before deletion
- Shows runtime details before deletion
- Confirms runtime is offline (recommended)
- Multiple confirmation prompts
- Checks for environment attachments
- Comprehensive error handling
"""

import os
import sys
from datetime import datetime

# Add the src directory to the path to import the SDK
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

from boomi import Boomi

def get_runtime_details(sdk, runtime_id):
    """Get runtime details for safety checks."""
    
    try:
        result = sdk.atom.get_atom(id_=runtime_id)
        
        if hasattr(result, '_kwargs') and 'Atom' in result._kwargs:
            return result._kwargs['Atom']
        
        return None
        
    except Exception as e:
        print(f"❌ Error retrieving runtime: {str(e)}")
        return None

def check_environment_attachments(sdk, runtime_id):
    """Check if runtime is attached to any environments."""
    
    try:
        from boomi.models import (
            EnvironmentAtomAttachmentQueryConfig,
            EnvironmentAtomAttachmentQueryConfigQueryFilter,
            EnvironmentAtomAttachmentSimpleExpression,
            EnvironmentAtomAttachmentSimpleExpressionOperator,
            EnvironmentAtomAttachmentSimpleExpressionProperty
        )
        
        # Query for attachments with this runtime ID
        simple_expression = EnvironmentAtomAttachmentSimpleExpression(
            operator=EnvironmentAtomAttachmentSimpleExpressionOperator.EQUALS,
            property=EnvironmentAtomAttachmentSimpleExpressionProperty.ATOMID,
            argument=[runtime_id]
        )
        
        query_filter = EnvironmentAtomAttachmentQueryConfigQueryFilter(expression=simple_expression)
        query_config = EnvironmentAtomAttachmentQueryConfig(query_filter=query_filter)
        
        result = sdk.environment_atom_attachment.query_environment_atom_attachment(query_config)
        
        # Use modern SDK response format
        attachments = []
        if hasattr(result, 'result') and result.result:
            attachments = result.result if isinstance(result.result, list) else [result.result]
        
        return attachments
        
    except Exception as e:
        print(f"⚠️  Could not check environment attachments: {str(e)}")
        return []

def display_runtime_summary(runtime_data):
    """Display runtime summary for confirmation."""
    
    print("\n📋 Runtime to be deleted:")
    print("=" * 70)
    
    runtime_name = runtime_data.get('@name', 'N/A')
    runtime_id = runtime_data.get('@id', 'N/A')
    runtime_status = runtime_data.get('@status', 'N/A')
    runtime_type = runtime_data.get('@type', 'N/A')
    runtime_hostname = runtime_data.get('@hostName', 'N/A')
    runtime_version = runtime_data.get('@currentVersion', 'N/A')
    date_installed = runtime_data.get('@dateInstalled', 'N/A')
    created_by = runtime_data.get('@createdBy', 'N/A')
    
    # Status icon
    if runtime_status == 'ONLINE':
        status_icon = "🟢"
        status_warning = "⚠️  RUNTIME IS ONLINE - Consider stopping it first!"
    elif runtime_status == 'OFFLINE':
        status_icon = "🔴"
        status_warning = "✅ Runtime is offline (safe to delete)"
    else:
        status_icon = "⚪"
        status_warning = f"⚠️  Runtime status: {runtime_status}"
    
    print(f"🤖 Name: {runtime_name}")
    print(f"🆔 ID: {runtime_id}")
    print(f"📦 Type: {runtime_type}")
    print(f"{status_icon} Status: {runtime_status}")
    print(f"🖥️  Hostname: {runtime_hostname}")
    print(f"📦 Version: {runtime_version}")
    print(f"📅 Installed: {date_installed}")
    print(f"👤 Created by: {created_by}")
    
    print(f"\n{status_warning}")
    
    return runtime_status

def perform_safety_checks(sdk, runtime_id, runtime_data):
    """Perform safety checks before deletion."""
    
    print("\n🔍 Performing safety checks...")
    
    safety_issues = []
    warnings = []
    
    # Check 1: Runtime status
    runtime_status = runtime_data.get('@status', 'UNKNOWN')
    if runtime_status == 'ONLINE':
        safety_issues.append("Runtime is currently ONLINE")
        warnings.append("⚠️  Deleting an online runtime may disrupt running processes")
    
    # Check 2: Environment attachments
    attachments = check_environment_attachments(sdk, runtime_id)
    if attachments:
        env_count = len(attachments)
        safety_issues.append(f"Runtime is attached to {env_count} environment(s)")
        warnings.append(f"⚠️  You may need to detach from environments first")
        
        print(f"   Found {env_count} environment attachment(s):")
        for attachment in attachments[:3]:  # Show first 3
            # Use object attributes for EnvironmentAtomAttachment objects
            env_id = getattr(attachment, 'environment_id', 'N/A')
            print(f"     - Environment ID: {env_id}")
        if len(attachments) > 3:
            print(f"     ... and {len(attachments) - 3} more")
    
    # Check 3: Runtime type
    runtime_type = runtime_data.get('@type', 'UNKNOWN')
    if runtime_type == 'CLOUD':
        safety_issues.append("This is a Cloud runtime")
        warnings.append("⚠️  Cloud runtimes may have different deletion requirements")
    
    # Display results
    if safety_issues:
        print("\n⚠️  Safety Issues Found:")
        for issue in safety_issues:
            print(f"   • {issue}")
    else:
        print("✅ No major safety issues detected")
    
    if warnings:
        print("\n⚠️  Warnings:")
        for warning in warnings:
            print(f"   {warning}")
    
    return len(safety_issues) == 0

def delete_runtime_with_confirmation(sdk, runtime_id, runtime_data):
    """Delete runtime with multiple confirmations."""
    
    runtime_name = runtime_data.get('@name', 'N/A')
    
    print(f"\n🚨 FINAL CONFIRMATION")
    print("=" * 50)
    print(f"You are about to PERMANENTLY DELETE runtime:")
    print(f"   Name: {runtime_name}")
    print(f"   ID: {runtime_id}")
    print()
    print("This action:")
    print("   • CANNOT be undone")
    print("   • Will remove the runtime from your account")
    print("   • May affect running processes if runtime is online")
    print("   • May affect environment deployments")
    
    # First confirmation
    confirm1 = input(f"\nType 'DELETE' to confirm deletion: ").strip()
    if confirm1 != 'DELETE':
        print("❌ Deletion cancelled - confirmation failed")
        return False
    
    # Second confirmation with runtime name
    confirm2 = input(f"Type the runtime name '{runtime_name}' to confirm: ").strip()
    if confirm2 != runtime_name:
        print("❌ Deletion cancelled - runtime name mismatch")
        return False
    
    # Final yes/no
    confirm3 = input("Are you absolutely sure? (yes/no): ").strip().lower()
    if confirm3 not in ['yes', 'y']:
        print("❌ Deletion cancelled by user")
        return False
    
    # Perform deletion
    print("\n🗑️  Deleting runtime...")
    
    try:
        sdk.atom.delete_atom(id_=runtime_id)
        print("✅ Runtime deleted successfully!")
        
        # Verify deletion
        print("🔍 Verifying deletion...")
        try:
            sdk.atom.get_atom(id_=runtime_id)
            print("⚠️  Runtime still exists - deletion may not have completed")
            return False
        except Exception:
            print("✅ Deletion verified - runtime no longer exists")
            return True
            
    except Exception as e:
        print(f"❌ Error deleting runtime: {str(e)}")
        
        if hasattr(e, 'status'):
            if e.status == 403:
                print("\n   Permission denied (403)")
                print("   • Check if you have Runtime Management privilege")
                print("   • Runtime Management Read Access is not sufficient")
            elif e.status == 404:
                print("\n   Not found (404)")
                print("   • The runtime may have already been deleted")
            elif e.status == 409:
                print("\n   Conflict (409)")
                print("   • Runtime may be in use or have dependencies")
                print("   • Try stopping the runtime first")
                print("   • Check for environment attachments")
            elif e.status == 400:
                print("\n   Bad request (400)")
                print("   • Check the runtime ID format")
        
        return False

def main():
    """Main function to demonstrate runtime deletion."""
    
    print("🚀 Boomi SDK - Delete Runtime")
    print("=" * 40)
    print("⚠️  WARNING: This permanently deletes a runtime!")
    print()
    
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
        # Get runtime ID from arguments or prompt user
        if len(sys.argv) > 1:
            runtime_id = sys.argv[1]
            print(f"📍 Using provided runtime ID: {runtime_id}")
        else:
            print("💡 Usage: python3 delete_runtime.py <runtime_id>")
            print()
            print("⚠️  Only provide runtimes you are sure you want to delete!")
            print("   You can find runtime IDs using list_runtimes.py")
            print()
            runtime_id = input("Enter runtime ID to delete (or 'cancel' to exit): ").strip()
            
            if not runtime_id or runtime_id.lower() == 'cancel':
                print("❌ Operation cancelled")
                return
        
        print()
        
        # Get runtime details
        print("🔍 Retrieving runtime details...")
        runtime_data = get_runtime_details(sdk, runtime_id)
        
        if not runtime_data:
            print("❌ Could not retrieve runtime details - runtime may not exist")
            return
        
        # Display runtime summary
        runtime_status = display_runtime_summary(runtime_data)
        
        # Perform safety checks
        is_safe = perform_safety_checks(sdk, runtime_id, runtime_data)
        
        if not is_safe:
            print("\n⚠️  Safety issues detected!")
            proceed = input("Do you want to proceed anyway? (yes/no): ").strip().lower()
            if proceed not in ['yes', 'y']:
                print("❌ Deletion cancelled for safety")
                return
        
        # Perform deletion with confirmations
        success = delete_runtime_with_confirmation(sdk, runtime_id, runtime_data)
        
        if success:
            print("\n🎉 Runtime deletion completed successfully!")
            print("\n💡 Next steps:")
            print("   • Verify no processes were disrupted")
            print("   • Check environment deployments if needed")
            print("   • Update any documentation that referenced this runtime")
        else:
            print("\n❌ Runtime deletion failed or was cancelled")
        
    except KeyboardInterrupt:
        print("\n❌ Operation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Example failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()