#!/usr/bin/env python3
"""
Boomi SDK Example: Update Runtime Configuration
=============================================

This example demonstrates how to update runtime configuration
using the Boomi SDK. It shows how to modify runtime properties like name,
purge settings, and force restart options.

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- Account must have appropriate permissions to modify runtimes
- Need a valid runtime ID to update

Usage:
    cd examples/runtime_management
    PYTHONPATH=../../src python3 update_runtime.py [runtime_id]

Features:
- Updates runtime configuration properties
- Demonstrates safe update patterns
- Shows how to change runtime name and settings
- Handles update validation and error cases

IMPORTANT: This example updates real runtime configurations. Use with caution
in production environments.
"""

import os
import sys
from datetime import datetime

# Add the src directory to the path to import the SDK
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

from boomi import Boomi
from boomi.models import Atom

def get_current_runtime(sdk, runtime_id):
    """Get current runtime configuration before updating."""
    
    print(f"🔍 Retrieving current runtime configuration...")
    
    try:
        result = sdk.atom.get_atom(id_=runtime_id)
        
        if hasattr(result, '_kwargs') and 'Atom' in result._kwargs:
            return result._kwargs['Atom']
        elif hasattr(result, '_kwargs'):
            return result._kwargs
        
        return None
        
    except Exception as e:
        print(f"❌ Error retrieving runtime: {str(e)}")
        return None

def create_runtime_update(current_runtime):
    """Create a runtime update object based on current configuration."""
    
    # Extract current values
    runtime_id = current_runtime.get('@id')
    current_name = current_runtime.get('@name', 'Unknown Runtime')
    current_purge = current_runtime.get('@purgeImmediate', False)
    current_purge_history_days = int(current_runtime.get('@purgeHistoryDays', 30))
    current_force_restart_ms = int(current_runtime.get('@forceRestartTime', 0))
    current_force_restart_minutes = current_force_restart_ms / 60000 if current_force_restart_ms > 0 else 0
    
    print("\n📋 Current Configuration:")
    print(f"   Name: {current_name}")
    print(f"   Purge Immediately: {current_purge}")
    print(f"   Purge History Days: {current_purge_history_days} days")
    print(f"   Force Restart Time: {current_force_restart_minutes:.1f} minutes ({current_force_restart_ms}ms)")
    
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
    
    purge_days_input = input(f"   Purge history days (0-9999, 0=disabled) [{current_purge_history_days}]: ").strip()
    if purge_days_input:
        try:
            new_purge_history_days = int(purge_days_input)
            if new_purge_history_days < 0:
                print("   ⚠️  Purge history days cannot be negative, using 0")
                new_purge_history_days = 0
            elif new_purge_history_days > 9999:
                print("   ⚠️  Purge history days cannot exceed 9999, using 9999")
                new_purge_history_days = 9999
        except ValueError:
            print("   ⚠️  Invalid number, keeping current value")
            new_purge_history_days = current_purge_history_days
    else:
        new_purge_history_days = current_purge_history_days
    
    force_restart_input = input(f"   Force restart time in minutes (0 to disable) [{current_force_restart_minutes:.1f}]: ").strip()
    if force_restart_input:
        try:
            new_force_restart_minutes = float(force_restart_input)
            if new_force_restart_minutes < 0:
                print("   ⚠️  Force restart time cannot be negative, using 0")
                new_force_restart_minutes = 0
        except ValueError:
            print("   ⚠️  Invalid number, keeping current value")
            new_force_restart_minutes = current_force_restart_minutes
    else:
        new_force_restart_minutes = current_force_restart_minutes
    
    # Send the minute value directly to API (no conversion)
    # Based on testing: API expects minutes and converts internally to milliseconds
    new_force_restart_time = int(new_force_restart_minutes)
    
    # Check if any changes were made (compare force restart in minutes)
    if (new_name == current_name and 
        new_purge == current_purge and 
        new_purge_history_days == current_purge_history_days and
        new_force_restart_minutes == current_force_restart_minutes):
        print("\n⚠️  No changes specified")
        return None
    
    # Create runtime update object
    # Note: Only name, purgeHistoryDays, purgeImmediate, forceRestartTime can be updated
    runtime_update = Atom(
        id_=runtime_id,
        name=new_name,
        purge_immediate=new_purge,  # Use purge_immediate, not purge_immediately
        purge_history_days=new_purge_history_days,  # Days to keep history (0-9999)
        force_restart_time=new_force_restart_time  # Minutes (API converts to milliseconds internally)
    )
    
    print("\n📝 Changes to apply:")
    if new_name != current_name:
        print(f"   Name: {current_name} → {new_name}")
    if new_purge != current_purge:
        print(f"   Purge Immediately: {current_purge} → {new_purge}")
    if new_purge_history_days != current_purge_history_days:
        print(f"   Purge History Days: {current_purge_history_days} → {new_purge_history_days} days")
    if new_force_restart_minutes != current_force_restart_minutes:
        print(f"   Force Restart Time: {current_force_restart_minutes:.1f} min → {new_force_restart_minutes:.1f} min")
    
    return runtime_update

def update_runtime(sdk, runtime_id, runtime_update):
    """Update runtime configuration."""
    
    print(f"\n📤 Updating runtime configuration...")
    
    try:
        # Call the update runtime API
        result = sdk.atom.update_atom(id_=runtime_id, request_body=runtime_update)
        
        print("✅ Runtime updated successfully!")
        
        # Parse the response
        updated_runtime = None
        if hasattr(result, '_kwargs') and 'Atom' in result._kwargs:
            updated_runtime = result._kwargs['Atom']
        elif hasattr(result, '_kwargs'):
            updated_runtime = result._kwargs
        
        return updated_runtime
        
    except Exception as e:
        print(f"❌ Error updating runtime: {str(e)}")
        
        if hasattr(e, 'status'):
            if e.status == 403:
                print("\n   Permission denied (403)")
                print("   • Check if your account can modify runtimes")
                print("   • Some properties may be read-only")
            elif e.status == 404:
                print("\n   Not found (404)")
                print("   • The runtime ID may not exist")
            elif e.status == 400:
                print("\n   Bad request (400)")
                print("   • Check the update data format")
                print("   • Some properties may have validation rules")
            elif e.status == 409:
                print("\n   Conflict (409)")
                print("   • The runtime may be in use or locked")
                print("   • Try again later")
        
        return None

def display_update_result(updated_runtime):
    """Display the updated runtime configuration."""
    
    print("\n✅ Updated Runtime Configuration:")
    print("=" * 60)
    
    # Handle both dict and object formats
    if hasattr(updated_runtime, 'name'):
        name = getattr(updated_runtime, 'name', 'N/A')
        runtime_id = getattr(updated_runtime, 'id_', 'N/A')
        last_modified = getattr(updated_runtime, 'last_modified_date', 'N/A')
        purge_immediate = getattr(updated_runtime, 'purge_immediate', False)
        purge_history_days = getattr(updated_runtime, 'purge_history_days', 30)
        force_restart_time = getattr(updated_runtime, 'force_restart_time', 0)
        status = getattr(updated_runtime, 'status', 'N/A')
    else:
        name = updated_runtime.get('@name', 'N/A')
        runtime_id = updated_runtime.get('@id', 'N/A')
        last_modified = updated_runtime.get('@lastModifiedDate', 'N/A')
        purge_immediate = updated_runtime.get('@purgeImmediate', False)
        purge_history_days = updated_runtime.get('@purgeHistoryDays', 30)
        force_restart_time = updated_runtime.get('@forceRestartTime', 0)
        status = updated_runtime.get('@status', 'N/A')
    
    print(f"🤖 Name: {name}")
    print(f"🆔 ID: {runtime_id}")
    print(f"📅 Last Modified: {last_modified}")
    print(f"⚙️  Purge Immediately: {purge_immediate}")
    print(f"📋 Purge History Days: {purge_history_days} days")
    force_restart_time_int = int(force_restart_time) if force_restart_time else 0
    force_restart_minutes = force_restart_time_int / 60000 if force_restart_time_int > 0 else 0
    print(f"🔄 Force Restart Time: {force_restart_minutes:.1f} minutes ({force_restart_time}ms)")
    
    # Status check
    status_icon = "🟢" if status == "ONLINE" else "🔴" if status == "OFFLINE" else "⚪"
    print(f"{status_icon} Status: {status}")

def demonstrate_programmatic_update():
    """Show example of programmatic runtime update."""
    
    print("\n📚 Programmatic Update Example:")
    print("=" * 60)
    print("To update a runtime programmatically without user input:")
    print("""
    # Create runtime update object (only these fields can be updated)
    runtime_update = Atom(
        id_=runtime_id,
        name="Production Runtime - Updated",
        purge_immediate=True,
        purge_history_days=90,     # Keep history for 90 days
        force_restart_time=1       # 1 minute (API expects minutes)
    )
    
    # Apply the update
    updated_runtime = sdk.atom.update_atom(
        id_=runtime_id,
        request_body=runtime_update
    )
    """)

def main():
    """Main function to demonstrate runtime updating."""
    
    print("🚀 Boomi SDK - Update Runtime Configuration")
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
        # Get runtime ID from arguments or prompt user
        if len(sys.argv) > 1:
            runtime_id = sys.argv[1]
            print(f"📍 Using provided runtime ID: {runtime_id}")
        else:
            print("💡 Usage: python3 update_runtime.py <runtime_id>")
            print()
            print("   You can find runtime IDs using list_runtimes.py")
            runtime_id = input("Enter runtime ID to update: ").strip()
            
            if not runtime_id:
                print("❌ No runtime ID provided")
                return
        
        print()
        
        # Get current runtime configuration
        current_runtime = get_current_runtime(sdk, runtime_id)
        if not current_runtime:
            print("❌ Could not retrieve runtime configuration")
            return
        
        # Create update object with user input
        runtime_update = create_runtime_update(current_runtime)
        if not runtime_update:
            print("ℹ️  No update performed")
            return
        
        # Confirm update
        confirm = input("\n⚠️  Apply these changes? (y/N): ").strip().lower()
        if confirm != 'y':
            print("❌ Update cancelled")
            return
        
        # Update the runtime
        updated_runtime = update_runtime(sdk, runtime_id, runtime_update)
        
        if updated_runtime:
            # Display results
            display_update_result(updated_runtime)
            
            print("\n💡 Update Notes:")
            print("   • Name changes take effect immediately")
            print("   • Purge settings affect execution history retention")
            print("   • Purge history days: 0=disabled, 1-9999=days to keep data")
            print("   • Force restart may interrupt running processes")
            print("   • Force restart time changes take effect on next restart")
            print("   • Some properties may require runtime restart")
            print("   ⚠️  Note: Force restart time may take a moment to reflect correctly")
            
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