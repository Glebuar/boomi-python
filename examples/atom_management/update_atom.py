#!/usr/bin/env python3
"""
Boomi SDK Example: Update Atom Configuration
=============================================

This example demonstrates how to update atom (runtime) configuration
using the Boomi SDK. It shows how to modify atom properties like name,
purge settings, and force restart options.

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- Account must have appropriate permissions to modify atoms
- Need a valid atom ID to update

Usage:
    cd examples/atom_management
    PYTHONPATH=../../src python3 update_atom.py [atom_id]

Features:
- Updates atom configuration properties
- Demonstrates safe update patterns
- Shows how to change atom name and settings
- Handles update validation and error cases

IMPORTANT: This example updates real atom configurations. Use with caution
in production environments.
"""

import os
import sys
from datetime import datetime

# Add the src directory to the path to import the SDK
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

from boomi import Boomi
from boomi.models import Atom

def get_current_atom(sdk, atom_id):
    """Get current atom configuration before updating."""
    
    print(f"🔍 Retrieving current atom configuration...")
    
    try:
        result = sdk.atom.get_atom(id_=atom_id)
        
        if hasattr(result, '_kwargs') and 'Atom' in result._kwargs:
            return result._kwargs['Atom']
        elif hasattr(result, '_kwargs'):
            return result._kwargs
        
        return None
        
    except Exception as e:
        print(f"❌ Error retrieving atom: {str(e)}")
        return None

def create_atom_update(current_atom):
    """Create an atom update object based on current configuration."""
    
    # Extract current values
    atom_id = current_atom.get('@id')
    current_name = current_atom.get('@name', 'Unknown Atom')
    current_purge = current_atom.get('@purgeImmediately', False)
    current_force_restart = current_atom.get('@forceRestart', False)
    
    print("\n📋 Current Configuration:")
    print(f"   Name: {current_name}")
    print(f"   Purge Immediately: {current_purge}")
    print(f"   Force Restart: {current_force_restart}")
    
    # Prompt for changes
    print("\n✏️  Enter new values (press Enter to keep current):")
    
    new_name = input(f"   New name [{current_name}]: ").strip()
    if not new_name:
        new_name = current_name
    
    purge_input = input(f"   Purge immediately (true/false) [{current_purge}]: ").strip().lower()
    if purge_input in ['true', 't', 'yes', 'y', '1']:
        new_purge = True
    elif purge_input in ['false', 'f', 'no', 'n', '0']:
        new_purge = False
    else:
        new_purge = current_purge
    
    force_restart_input = input(f"   Force restart (true/false) [{current_force_restart}]: ").strip().lower()
    if force_restart_input in ['true', 't', 'yes', 'y', '1']:
        new_force_restart = True
    elif force_restart_input in ['false', 'f', 'no', 'n', '0']:
        new_force_restart = False
    else:
        new_force_restart = current_force_restart
    
    # Check if any changes were made
    if (new_name == current_name and 
        new_purge == current_purge and 
        new_force_restart == current_force_restart):
        print("\n⚠️  No changes specified")
        return None
    
    # Create atom update object
    # Note: Only name, purgeHistoryDays, purgeImmediate, forceRestartTime can be updated
    atom_update = Atom(
        id_=atom_id,
        name=new_name,
        purge_immediate=new_purge,  # Use purge_immediate, not purge_immediately
        force_restart_time=0 if not new_force_restart else 180000  # Default restart time
    )
    
    print("\n📝 Changes to apply:")
    if new_name != current_name:
        print(f"   Name: {current_name} → {new_name}")
    if new_purge != current_purge:
        print(f"   Purge Immediately: {current_purge} → {new_purge}")
    if new_force_restart != current_force_restart:
        print(f"   Force Restart: {current_force_restart} → {new_force_restart}")
    
    return atom_update

def update_atom(sdk, atom_id, atom_update):
    """Update atom configuration."""
    
    print(f"\n📤 Updating atom configuration...")
    
    try:
        # Call the update atom API
        result = sdk.atom.update_atom(id_=atom_id, request_body=atom_update)
        
        print("✅ Atom updated successfully!")
        
        # Parse the response
        updated_atom = None
        if hasattr(result, '_kwargs') and 'Atom' in result._kwargs:
            updated_atom = result._kwargs['Atom']
        elif hasattr(result, '_kwargs'):
            updated_atom = result._kwargs
        
        return updated_atom
        
    except Exception as e:
        print(f"❌ Error updating atom: {str(e)}")
        
        if hasattr(e, 'status'):
            if e.status == 403:
                print("\n   Permission denied (403)")
                print("   • Check if your account can modify atoms")
                print("   • Some properties may be read-only")
            elif e.status == 404:
                print("\n   Not found (404)")
                print("   • The atom ID may not exist")
            elif e.status == 400:
                print("\n   Bad request (400)")
                print("   • Check the update data format")
                print("   • Some properties may have validation rules")
            elif e.status == 409:
                print("\n   Conflict (409)")
                print("   • The atom may be in use or locked")
                print("   • Try again later")
        
        return None

def display_update_result(updated_atom):
    """Display the updated atom configuration."""
    
    print("\n✅ Updated Atom Configuration:")
    print("=" * 60)
    
    # Handle both dict and object formats
    if hasattr(updated_atom, 'name'):
        name = getattr(updated_atom, 'name', 'N/A')
        atom_id = getattr(updated_atom, 'id_', 'N/A')
        last_modified = getattr(updated_atom, 'last_modified_date', 'N/A')
        purge_immediate = getattr(updated_atom, 'purge_immediate', False)
        force_restart_time = getattr(updated_atom, 'force_restart_time', 0)
        status = getattr(updated_atom, 'status', 'N/A')
    else:
        name = updated_atom.get('@name', 'N/A')
        atom_id = updated_atom.get('@id', 'N/A')
        last_modified = updated_atom.get('@lastModifiedDate', 'N/A')
        purge_immediate = updated_atom.get('@purgeImmediately', False)
        force_restart_time = updated_atom.get('@forceRestart', 0)
        status = updated_atom.get('@status', 'N/A')
    
    print(f"🤖 Name: {name}")
    print(f"🆔 ID: {atom_id}")
    print(f"📅 Last Modified: {last_modified}")
    print(f"⚙️  Purge Immediately: {purge_immediate}")
    print(f"🔄 Force Restart Time: {force_restart_time}ms")
    
    # Status check
    status_icon = "🟢" if status == "ONLINE" else "🔴" if status == "OFFLINE" else "⚪"
    print(f"{status_icon} Status: {status}")

def demonstrate_programmatic_update():
    """Show example of programmatic atom update."""
    
    print("\n📚 Programmatic Update Example:")
    print("=" * 60)
    print("To update an atom programmatically without user input:")
    print("""
    # Create atom update object (only these fields can be updated)
    atom_update = Atom(
        id_=atom_id,
        name="Production Atom - Updated",
        purge_immediate=True,
        force_restart_time=180000  # 3 minutes in milliseconds
    )
    
    # Apply the update
    updated_atom = sdk.atom.update_atom(
        id_=atom_id,
        request_body=atom_update
    )
    """)

def main():
    """Main function to demonstrate atom updating."""
    
    print("🚀 Boomi SDK - Update Atom Configuration")
    print("=" * 55)
    
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
            print("💡 Usage: python3 update_atom.py <atom_id>")
            print()
            print("   You can find atom IDs using list_atoms.py")
            atom_id = input("Enter atom ID to update: ").strip()
            
            if not atom_id:
                print("❌ No atom ID provided")
                return
        
        print()
        
        # Get current atom configuration
        current_atom = get_current_atom(sdk, atom_id)
        if not current_atom:
            print("❌ Could not retrieve atom configuration")
            return
        
        # Create update object with user input
        atom_update = create_atom_update(current_atom)
        if not atom_update:
            print("ℹ️  No update performed")
            return
        
        # Confirm update
        confirm = input("\n⚠️  Apply these changes? (y/N): ").strip().lower()
        if confirm != 'y':
            print("❌ Update cancelled")
            return
        
        # Update the atom
        updated_atom = update_atom(sdk, atom_id, atom_update)
        
        if updated_atom:
            # Display results
            display_update_result(updated_atom)
            
            print("\n💡 Update Notes:")
            print("   • Name changes take effect immediately")
            print("   • Purge settings affect execution history retention")
            print("   • Force restart may interrupt running processes")
            print("   • Some properties may require atom restart")
            
            # Show programmatic example
            demonstrate_programmatic_update()
        
    except KeyboardInterrupt:
        print("\n❌ Operation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Example failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()