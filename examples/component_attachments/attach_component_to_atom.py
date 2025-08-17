#!/usr/bin/env python3
"""
Boomi SDK Example: Attach Component to Atom

This example demonstrates how to attach a component to an atom (runtime) using the
ComponentAtomAttachment API. This is essential for deploying components to specific runtimes.

Features:
- Attach a specific component to an atom/runtime
- Shows the attachment ID for future reference
- Handles error cases (component not found, atom not found, etc.)
- Provides clear feedback on attachment success

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- Or create a .env file with these variables

Usage:
    python attach_component_to_atom.py COMPONENT_ID ATOM_ID
    
    Arguments:
    COMPONENT_ID     The component ID to attach
    ATOM_ID          The atom/runtime ID to attach to
    
    Examples:
    python attach_component_to_atom.py 112b4efe-b173-4258-9492-613ead7d52ce 81e9dbc8-4684-4814-897c-0a1af0a6fe51
"""

import os
import sys
sys.path.insert(0, '../../src')
from boomi import Boomi
from boomi.models import ComponentAtomAttachment

# Load environment variables
try:
    from dotenv import load_dotenv
    load_dotenv('../../.env')
except ImportError:
    pass

def format_date(date_str):
    """Format ISO date string to readable format"""
    if date_str and 'T' in date_str:
        return date_str.split('T')[0] + ' ' + date_str.split('T')[1].split('.')[0]
    return date_str or 'N/A'

def attach_component_to_atom(component_id, atom_id):
    """Attach a component to an atom/runtime"""
    
    # Check for required environment variables
    account_id = os.getenv("BOOMI_ACCOUNT")
    username = os.getenv("BOOMI_USER") 
    password = os.getenv("BOOMI_SECRET")
    
    if not all([account_id, username, password]):
        print("❌ Error: Missing required environment variables")
        print("   Please set: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET")
        return False
    
    print(f"🏢 Account: {account_id}")
    print(f"👤 User: {username}")
    print(f"🎯 Component ID: {component_id}")
    print(f"⚛️ Atom ID: {atom_id}")
    
    # Initialize the Boomi SDK
    sdk = Boomi(
        account_id=account_id,
        username=username, 
        password=password,
        timeout=30000
    )
    
    print(f"\n🔍 Verifying component and atom exist...")
    
    try:
        # Verify component exists
        print("📋 Checking component...")
        component = sdk.component.get_component(component_id=component_id)
        component_name = getattr(component, 'name', 'N/A')
        component_type = getattr(component, 'type_', 'N/A')
        print(f"✅ Component found: {component_name} ({component_type})")
        
        # Verify atom exists  
        print("⚛️ Checking atom...")
        atom = sdk.atom.get_atom(atom_id=atom_id)
        atom_name = getattr(atom, 'name', 'N/A')
        atom_status = getattr(atom, 'status', 'N/A')
        print(f"✅ Atom found: {atom_name} ({atom_status})")
        
    except Exception as e:
        print(f"❌ Verification failed: {e}")
        print("Please check that both component and atom IDs are valid")
        return False
    
    print(f"\n🔗 Creating attachment between component and atom...")
    
    try:
        # Create component-atom attachment
        attachment = ComponentAtomAttachment(
            component_id=component_id,
            atom_id=atom_id
        )
        
        result = sdk.component_atom_attachment.create_component_atom_attachment(
            request_body=attachment
        )
        
        print("✅ Attachment created successfully!")
        print(f"📊 Response type: {type(result).__name__}")
        
        # Extract attachment details
        attachment_data = result
        if hasattr(result, '_kwargs') and result._kwargs:
            if 'ComponentAtomAttachment' in result._kwargs:
                attachment_data = result._kwargs['ComponentAtomAttachment']
        
        # Display attachment information
        print(f"\n📋 Attachment Details:")
        print("=" * 50)
        
        if hasattr(attachment_data, 'id_') or hasattr(attachment_data, 'attachment_id'):
            attachment_id = getattr(attachment_data, 'id_', None) or getattr(attachment_data, 'attachment_id', 'N/A')
            print(f"  Attachment ID: {attachment_id}")
        
        print(f"  Component: {component_name} ({component_id})")
        print(f"  Atom: {atom_name} ({atom_id})")
        
        if hasattr(attachment_data, 'component_type'):
            print(f"  Component Type: {getattr(attachment_data, 'component_type', 'N/A')}")
        
        if hasattr(attachment_data, 'created_date'):
            print(f"  Created: {format_date(getattr(attachment_data, 'created_date', 'N/A'))}")
        
        if hasattr(attachment_data, 'created_by'):
            print(f"  Created by: {getattr(attachment_data, 'created_by', 'N/A')}")
        
        print(f"\n🎉 SUCCESS!")
        print(f"📍 Component '{component_name}' is now attached to atom '{atom_name}'")
        print(f"🚀 The component can now be deployed and executed on this runtime")
        
        # Save attachment ID for future reference
        if hasattr(attachment_data, 'id_'):
            attachment_id = getattr(attachment_data, 'id_', 'N/A')
            print(f"\n💡 Save this attachment ID for future reference: {attachment_id}")
            print(f"📝 Use this ID to detach the component later if needed")
        
        return True
        
    except Exception as e:
        error_msg = str(e)
        print(f"❌ Attachment failed: {error_msg}")
        
        # Provide helpful troubleshooting hints
        if "already attached" in error_msg.lower() or "duplicate" in error_msg.lower():
            print("🔍 Component may already be attached to this atom")
            print("💡 Use query_component_atom_attachments.py to check existing attachments")
        elif "403" in error_msg:
            print("🔍 Permission issue - check your API credentials and runtime management permissions")
        elif "400" in error_msg:
            print("🔍 Bad request - check component and atom IDs")
        elif "401" in error_msg:
            print("🔍 Authentication failed - verify your credentials")
        else:
            print("🔍 Check network connectivity and API endpoint availability")
            
        return False

def main():
    """Main entry point"""
    if len(sys.argv) < 3:
        print("❌ Error: Component ID and Atom ID are required")
        print("\nUsage:")
        print(f"  {sys.argv[0]} COMPONENT_ID ATOM_ID")
        print("\nExamples:")
        print(f"  {sys.argv[0]} 112b4efe-b173-4258-9492-613ead7d52ce 81e9dbc8-4684-4814-897c-0a1af0a6fe51")
        print("\n💡 Use list_all_components.py to find component IDs")
        print("💡 Use list_atoms.py to find atom IDs")
        return
    
    component_id = sys.argv[1]
    atom_id = sys.argv[2]
    
    print("🚀 Boomi SDK Example: Attach Component to Atom")
    print("=" * 50)
    print()
    
    success = attach_component_to_atom(component_id, atom_id)
    
    print(f"\n{'='*50}")
    if success:
        print("🌟 Component attachment completed successfully!")
    else:
        print("💥 Component attachment encountered issues")

if __name__ == "__main__":
    main()