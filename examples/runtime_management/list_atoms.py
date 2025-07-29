#!/usr/bin/env python3
"""
Boomi SDK Example: List All Atoms (Runtimes)
=============================================

This example demonstrates how to query and list all atoms (runtimes) in a Boomi account
using the Python SDK. It shows atom details including name, ID, status, and type.

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- Account must have appropriate permissions to read atoms
- At least one atom should be installed in the account

Usage:
    cd examples/utilities
    PYTHONPATH=../../src python3 list_atoms.py

Features:
- Lists all atoms in the account
- Shows atom details (ID, name, type, status, hostname, version)
- Categorizes atoms by status (ONLINE, OFFLINE)
- Shows installation and version information
"""

import os
import sys
from datetime import datetime

# Add the src directory to the path to import the SDK
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

from boomi import Boomi
from boomi.models import (
    AtomQueryConfig,
    AtomQueryConfigQueryFilter,
    AtomSimpleExpression,
    AtomSimpleExpressionOperator,
    AtomSimpleExpressionProperty
)

def list_all_atoms_sdk(sdk):
    """List all atoms using SDK with no query filter (works best for atoms)."""
    
    print(f"🔍 Querying all runtimes using SDK...")
    
    try:
        # Create empty query config - no filter needed for atoms
        query_config = AtomQueryConfig()
        query_response = sdk.atom.query_atom(query_config)
        
        # Parse the response - it's an AtomQueryResponse object with 'result' attribute
        atoms = []
        
        if hasattr(query_response, 'number_of_results'):
            num_results = query_response.number_of_results or 0
            print(f"   Found {num_results} atoms in account")
        
        if hasattr(query_response, 'result') and query_response.result:
            result_data = query_response.result
            if isinstance(result_data, list):
                atoms = result_data
            else:
                atoms = [result_data]
                
            # Show what we found
            for atom in atoms:
                name = getattr(atom, 'name', 'N/A')
                atom_type = getattr(atom, 'type_', 'N/A')  
                status = getattr(atom, 'status', 'N/A')
                print(f"     - {name} ({atom_type}, {status})")
        else:
            print(f"   No result data found in response")
        
        return atoms
        
    except Exception as e:
        print(f"❌ Error querying atoms with SDK: {str(e)}")
        if hasattr(e, 'status'):
            print(f"   Status code: {e.status}")
        return []

def list_atoms_by_type(atoms, atom_type):
    """Filter atoms by type from the full list."""
    
    filtered_atoms = []
    for atom in atoms:
        # Handle both dict format (for backward compatibility) and object format
        if hasattr(atom, 'type_'):
            current_type = getattr(atom, 'type_', '')
        elif hasattr(atom, 'get'):
            current_type = atom.get('@type', '')
        else:
            # For objects without get method, try direct attribute access with fallback
            current_type = getattr(atom, 'type_', '')
            
        if current_type == atom_type:
            filtered_atoms.append(atom)
    
    return filtered_atoms

def format_date(date_string):
    """Format ISO date string to readable format."""
    try:
        if date_string:
            dt = datetime.fromisoformat(date_string.replace('Z', '+00:00'))
            return dt.strftime('%Y-%m-%d %H:%M:%S UTC')
    except:
        pass
    return date_string or 'N/A'

def display_atoms(atoms, atom_type):
    """Display atom information in a formatted way."""
    
    if not atoms:
        print(f"   No {atom_type} runtimes found")
        return
    
    print(f"\n✅ Found {len(atoms)} {atom_type} runtime(s):")
    print("=" * 100)
    
    online_count = 0
    offline_count = 0
    
    for i, atom in enumerate(atoms, 1):
        # Handle both dict format (for backward compatibility) and object format
        if hasattr(atom, 'id_'):
            atom_id = getattr(atom, 'id_', 'N/A')
            atom_name = getattr(atom, 'name', 'N/A')
            atom_status = getattr(atom, 'status', 'N/A')
            atom_hostname = getattr(atom, 'host_name', 'N/A')
            atom_version = getattr(atom, 'current_version', 'N/A')
            atom_installed = getattr(atom, 'date_installed', 'N/A')
            atom_created_by = getattr(atom, 'created_by', 'N/A')
            atom_capabilities = getattr(atom, 'capabilities', [])
        else:
            atom_id = atom.get('@id', 'N/A')
            atom_name = atom.get('@name', 'N/A')
            atom_status = atom.get('@status', 'N/A')
            atom_hostname = atom.get('@hostName', 'N/A')
            atom_version = atom.get('@currentVersion', 'N/A')
            atom_installed = atom.get('@dateInstalled', 'N/A')
            atom_created_by = atom.get('@createdBy', 'N/A')
            atom_capabilities = atom.get('@capabilities', [])
        
        # Count status
        if atom_status == 'ONLINE':
            online_count += 1
            status_icon = "🟢"
        elif atom_status == 'OFFLINE':
            offline_count += 1
            status_icon = "🔴"
        else:
            status_icon = "⚪"
        
        print(f"{i:2}. 🤖 {atom_name}")
        print(f"     🆔 ID: {atom_id}")
        print(f"     {status_icon} Status: {atom_status}")
        print(f"     🖥️  Hostname: {atom_hostname}")
        print(f"     📦 Version: {atom_version}")
        print(f"     📅 Installed: {format_date(atom_installed)}")
        print(f"     👤 Created by: {atom_created_by}")
        
        if atom_capabilities:
            print(f"     🔧 Capabilities: {', '.join(atom_capabilities)}")
        
        print()
    
    # Status summary
    print("📊 Status Summary:")
    print(f"   🟢 Online: {online_count}")
    print(f"   🔴 Offline: {offline_count}")
    print()

def main():
    """Main function to demonstrate atom listing."""
    
    print("🚀 Boomi SDK - List All Atoms (Runtimes) Example")
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
        # Get all atoms using SDK
        all_atoms = list_all_atoms_sdk(sdk)
        
        if all_atoms:
            # Group atoms by type and display
            atom_types = ["ATOM", "CLOUD", "MOLECULE", "GATEWAY"]
            
            for atom_type in atom_types:
                filtered_atoms = list_atoms_by_type(all_atoms, atom_type)
                if filtered_atoms:
                    display_atoms(filtered_atoms, atom_type)
        
        # Overall summary
        if all_atoms:
            print("=" * 100)
            print(f"🎯 Overall Summary:")
            print(f"   Total runtimes: {len(all_atoms)}")
            
            # Count by status
            online = 0
            offline = 0
            for atom in all_atoms:
                if hasattr(atom, 'status'):
                    status = atom.status
                else:
                    status = atom.get('@status', '')
                    
                if status == 'ONLINE':
                    online += 1
                elif status == 'OFFLINE':
                    offline += 1
            
            print(f"   🟢 Online runtimes: {online}")
            print(f"   🔴 Offline runtimes: {offline}")
            
            # Count by type
            type_counts = {}
            for atom in all_atoms:
                if hasattr(atom, 'type_'):
                    atom_type = atom.type_
                else:
                    atom_type = atom.get('@type', 'Unknown')
                type_counts[atom_type] = type_counts.get(atom_type, 0) + 1
            
            print(f"\n   📋 By Type:")
            for atom_type, count in type_counts.items():
                print(f"     • {atom_type}: {count}")
            
            print(f"\n💡 Tips:")
            print(f"   • Online atoms can execute processes")
            print(f"   • Offline atoms need to be started to be used")
            print(f"   • Atom IDs are needed for environment attachments")
            print(f"   • Check atom versions for compatibility")
        else:
            print("❌ No atoms found in the account")
            print("\n💡 To use Boomi:")
            print("   • Install at least one Atom (runtime)")
            print("   • Atoms can be downloaded from the Boomi platform")
            print("   • Cloud atoms are also available as an alternative")
        
        print("\n🔧 Technical Note:")
        print("   Uses SDK with empty AtomQueryConfig (no filter needed for atom queries)")  
        print("   Fixed SDK issue: AtomQueryConfig.query_filter is now optional")
        print("   Atoms are grouped by type (ATOM, CLOUD, MOLECULE, GATEWAY) for display")
        
    except Exception as e:
        print(f"❌ Example failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()