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

def list_atoms_by_type(sdk, atom_type):
    """List atoms by type (ATOM, GATEWAY, etc.)."""
    
    print(f"🔍 Querying {atom_type} runtimes...")
    
    try:
        # Create a query to get atoms of specific type
        simple_expression = AtomSimpleExpression(
            operator=AtomSimpleExpressionOperator.EQUALS,
            property=AtomSimpleExpressionProperty.TYPE,
            argument=[atom_type]
        )
        
        query_filter = AtomQueryConfigQueryFilter(expression=simple_expression)
        query_config = AtomQueryConfig(query_filter=query_filter)
        query_response = sdk.atom.query_atom(query_config)
        
        # Parse the response
        atoms = []
        if hasattr(query_response, '_kwargs') and 'AtomQueryResponse' in query_response._kwargs:
            query_data = query_response._kwargs['AtomQueryResponse']
            
            if 'Atom' in query_data:
                atom_data = query_data['Atom']
                if isinstance(atom_data, list):
                    atoms = atom_data
                else:
                    atoms = [atom_data]
        
        return atoms
        
    except Exception as e:
        print(f"❌ Error querying {atom_type} atoms: {str(e)}")
        return []

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
        all_atoms = []
        
        # Query different types of atoms
        atom_types = ["ATOM", "GATEWAY", "MOLECULE"]
        
        for atom_type in atom_types:
            atoms = list_atoms_by_type(sdk, atom_type)
            if atoms:
                display_atoms(atoms, atom_type)
                all_atoms.extend(atoms)
        
        # Overall summary
        if all_atoms:
            print("=" * 100)
            print(f"🎯 Overall Summary:")
            print(f"   Total runtimes: {len(all_atoms)}")
            
            # Count by status
            online = sum(1 for atom in all_atoms if atom.get('@status') == 'ONLINE')
            offline = sum(1 for atom in all_atoms if atom.get('@status') == 'OFFLINE')
            
            print(f"   🟢 Online runtimes: {online}")
            print(f"   🔴 Offline runtimes: {offline}")
            
            # Count by type
            type_counts = {}
            for atom in all_atoms:
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
        
    except Exception as e:
        print(f"❌ Example failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()