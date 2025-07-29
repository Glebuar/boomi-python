#!/usr/bin/env python3
"""
Boomi SDK Example: Delete Atom
===============================

This example demonstrates how to delete an atom (runtime) using the Boomi SDK.
It includes safety checks, confirmation prompts, and proper error handling.

⚠️  WARNING: This operation permanently deletes an atom from your account.
   Use with extreme caution, especially in production environments.

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- Account must have Runtime Management privilege (not just read access)
- Atom should be OFFLINE before deletion (recommended)

Usage:
    cd examples/atom_management
    PYTHONPATH=../../src python3 delete_atom.py [atom_id]

Features:
- Safety checks before deletion
- Shows atom details before deletion
- Confirms atom is offline (recommended)
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

def get_atom_details(sdk, atom_id):
    """Get atom details for safety checks."""
    
    try:
        result = sdk.atom.get_atom(id_=atom_id)
        
        if hasattr(result, '_kwargs') and 'Atom' in result._kwargs:
            return result._kwargs['Atom']
        
        return None
        
    except Exception as e:
        print(f"❌ Error retrieving atom: {str(e)}")
        return None

def check_environment_attachments(sdk, atom_id):
    """Check if atom is attached to any environments."""
    
    try:
        from boomi.models import (
            EnvironmentAtomAttachmentQueryConfig,
            EnvironmentAtomAttachmentQueryConfigQueryFilter,
            EnvironmentAtomAttachmentSimpleExpression,
            EnvironmentAtomAttachmentSimpleExpressionOperator,
            EnvironmentAtomAttachmentSimpleExpressionProperty
        )
        
        # Query for attachments with this atom ID
        simple_expression = EnvironmentAtomAttachmentSimpleExpression(
            operator=EnvironmentAtomAttachmentSimpleExpressionOperator.EQUALS,
            property=EnvironmentAtomAttachmentSimpleExpressionProperty.ATOM_ID,
            argument=[atom_id]
        )
        
        query_filter = EnvironmentAtomAttachmentQueryConfigQueryFilter(expression=simple_expression)
        query_config = EnvironmentAtomAttachmentQueryConfig(query_filter=query_filter)
        
        result = sdk.environment_atom_attachment.query_environment_atom_attachment(query_config)
        
        attachments = []
        if hasattr(result, '_kwargs') and 'EnvironmentAtomAttachmentQueryResponse' in result._kwargs:
            query_data = result._kwargs['EnvironmentAtomAttachmentQueryResponse']
            
            if 'EnvironmentAtomAttachment' in query_data:
                attachment_data = query_data['EnvironmentAtomAttachment']
                if isinstance(attachment_data, list):
                    attachments = attachment_data
                else:
                    attachments = [attachment_data]
        
        return attachments
        
    except Exception as e:
        print(f"⚠️  Could not check environment attachments: {str(e)}")
        return []

def display_atom_summary(atom_data):
    """Display atom summary for confirmation."""
    
    print("\n📋 Atom to be deleted:")
    print("=" * 70)
    
    atom_name = atom_data.get('@name', 'N/A')
    atom_id = atom_data.get('@id', 'N/A')
    atom_status = atom_data.get('@status', 'N/A')
    atom_type = atom_data.get('@type', 'N/A')
    atom_hostname = atom_data.get('@hostName', 'N/A')
    atom_version = atom_data.get('@currentVersion', 'N/A')
    date_installed = atom_data.get('@dateInstalled', 'N/A')
    created_by = atom_data.get('@createdBy', 'N/A')
    
    # Status icon
    if atom_status == 'ONLINE':
        status_icon = "🟢"
        status_warning = "⚠️  ATOM IS ONLINE - Consider stopping it first!"
    elif atom_status == 'OFFLINE':
        status_icon = "🔴"
        status_warning = "✅ Atom is offline (safe to delete)"
    else:
        status_icon = "⚪"
        status_warning = f"⚠️  Atom status: {atom_status}"
    
    print(f"🤖 Name: {atom_name}")
    print(f"🆔 ID: {atom_id}")
    print(f"📦 Type: {atom_type}")
    print(f"{status_icon} Status: {atom_status}")
    print(f"🖥️  Hostname: {atom_hostname}")
    print(f"📦 Version: {atom_version}")
    print(f"📅 Installed: {date_installed}")
    print(f"👤 Created by: {created_by}")
    
    print(f"\n{status_warning}")
    
    return atom_status

def perform_safety_checks(sdk, atom_id, atom_data):
    """Perform safety checks before deletion."""
    
    print("\n🔍 Performing safety checks...")
    
    safety_issues = []
    warnings = []
    
    # Check 1: Atom status
    atom_status = atom_data.get('@status', 'UNKNOWN')
    if atom_status == 'ONLINE':
        safety_issues.append("Atom is currently ONLINE")
        warnings.append("⚠️  Deleting an online atom may disrupt running processes")
    
    # Check 2: Environment attachments
    attachments = check_environment_attachments(sdk, atom_id)
    if attachments:
        env_count = len(attachments)
        safety_issues.append(f"Atom is attached to {env_count} environment(s)")
        warnings.append(f"⚠️  You may need to detach from environments first")
        
        print(f"   Found {env_count} environment attachment(s):")
        for attachment in attachments[:3]:  # Show first 3
            env_id = attachment.get('@environmentId', 'N/A')
            print(f"     - Environment ID: {env_id}")
        if len(attachments) > 3:
            print(f"     ... and {len(attachments) - 3} more")
    
    # Check 3: Atom type
    atom_type = atom_data.get('@type', 'UNKNOWN')
    if atom_type == 'CLOUD':
        safety_issues.append("This is a Cloud atom")
        warnings.append("⚠️  Cloud atoms may have different deletion requirements")
    
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

def delete_atom_with_confirmation(sdk, atom_id, atom_data):
    """Delete atom with multiple confirmations."""
    
    atom_name = atom_data.get('@name', 'N/A')
    
    print(f"\n🚨 FINAL CONFIRMATION")
    print("=" * 50)
    print(f"You are about to PERMANENTLY DELETE atom:")
    print(f"   Name: {atom_name}")
    print(f"   ID: {atom_id}")
    print()
    print("This action:")
    print("   • CANNOT be undone")
    print("   • Will remove the atom from your account")
    print("   • May affect running processes if atom is online")
    print("   • May affect environment deployments")
    
    # First confirmation
    confirm1 = input(f"\nType 'DELETE' to confirm deletion: ").strip()
    if confirm1 != 'DELETE':
        print("❌ Deletion cancelled - confirmation failed")
        return False
    
    # Second confirmation with atom name
    confirm2 = input(f"Type the atom name '{atom_name}' to confirm: ").strip()
    if confirm2 != atom_name:
        print("❌ Deletion cancelled - atom name mismatch")
        return False
    
    # Final yes/no
    confirm3 = input("Are you absolutely sure? (yes/no): ").strip().lower()
    if confirm3 not in ['yes', 'y']:
        print("❌ Deletion cancelled by user")
        return False
    
    # Perform deletion
    print("\n🗑️  Deleting atom...")
    
    try:
        sdk.atom.delete_atom(id_=atom_id)
        print("✅ Atom deleted successfully!")
        
        # Verify deletion
        print("🔍 Verifying deletion...")
        try:
            sdk.atom.get_atom(id_=atom_id)
            print("⚠️  Atom still exists - deletion may not have completed")
            return False
        except Exception:
            print("✅ Deletion verified - atom no longer exists")
            return True
            
    except Exception as e:
        print(f"❌ Error deleting atom: {str(e)}")
        
        if hasattr(e, 'status'):
            if e.status == 403:
                print("\n   Permission denied (403)")
                print("   • Check if you have Runtime Management privilege")
                print("   • Runtime Management Read Access is not sufficient")
            elif e.status == 404:
                print("\n   Not found (404)")
                print("   • The atom may have already been deleted")
            elif e.status == 409:
                print("\n   Conflict (409)")
                print("   • Atom may be in use or have dependencies")
                print("   • Try stopping the atom first")
                print("   • Check for environment attachments")
            elif e.status == 400:
                print("\n   Bad request (400)")
                print("   • Check the atom ID format")
        
        return False

def main():
    """Main function to demonstrate atom deletion."""
    
    print("🚀 Boomi SDK - Delete Atom")
    print("=" * 40)
    print("⚠️  WARNING: This permanently deletes an atom!")
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
        # Get atom ID from arguments or prompt user
        if len(sys.argv) > 1:
            atom_id = sys.argv[1]
            print(f"📍 Using provided atom ID: {atom_id}")
        else:
            print("💡 Usage: python3 delete_atom.py <atom_id>")
            print()
            print("⚠️  Only provide atoms you are sure you want to delete!")
            print("   You can find atom IDs using list_atoms.py")
            print()
            atom_id = input("Enter atom ID to delete (or 'cancel' to exit): ").strip()
            
            if not atom_id or atom_id.lower() == 'cancel':
                print("❌ Operation cancelled")
                return
        
        print()
        
        # Get atom details
        print("🔍 Retrieving atom details...")
        atom_data = get_atom_details(sdk, atom_id)
        
        if not atom_data:
            print("❌ Could not retrieve atom details - atom may not exist")
            return
        
        # Display atom summary
        atom_status = display_atom_summary(atom_data)
        
        # Perform safety checks
        is_safe = perform_safety_checks(sdk, atom_id, atom_data)
        
        if not is_safe:
            print("\n⚠️  Safety issues detected!")
            proceed = input("Do you want to proceed anyway? (yes/no): ").strip().lower()
            if proceed not in ['yes', 'y']:
                print("❌ Deletion cancelled for safety")
                return
        
        # Perform deletion with confirmations
        success = delete_atom_with_confirmation(sdk, atom_id, atom_data)
        
        if success:
            print("\n🎉 Atom deletion completed successfully!")
            print("\n💡 Next steps:")
            print("   • Verify no processes were disrupted")
            print("   • Check environment deployments if needed")
            print("   • Update any documentation that referenced this atom")
        else:
            print("\n❌ Atom deletion failed or was cancelled")
        
    except KeyboardInterrupt:
        print("\n❌ Operation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Example failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()