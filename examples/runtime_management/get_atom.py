#!/usr/bin/env python3
"""
Boomi SDK Example: Get Atom Details
====================================

This example demonstrates how to retrieve specific atom (runtime) details
using the Boomi SDK. It shows how to get comprehensive information about
an atom including its configuration, status, and capabilities.

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- Account must have appropriate permissions to read atom details
- Need a valid atom ID to retrieve

Usage:
    cd examples/atom_management
    PYTHONPATH=../../src python3 get_atom.py [atom_id]

Features:
- Retrieves complete atom information by ID
- Shows atom configuration details
- Displays status, version, and capability information
- Shows installation and environment attachment details
"""

import os
import sys
from datetime import datetime

# Add the src directory to the path to import the SDK
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

from boomi import Boomi

def get_atom_details(sdk, atom_id):
    """Retrieve specific atom details."""
    
    print(f"🔍 Retrieving atom details...")
    print(f"   Atom ID: {atom_id}")
    
    try:
        # Call the get atom API
        result = sdk.atom.get_atom(id_=atom_id)
        
        print("✅ Atom details retrieved successfully!")
        
        # Parse the response
        atom_data = None
        if hasattr(result, '_kwargs') and 'Atom' in result._kwargs:
            atom_data = result._kwargs['Atom']
        elif hasattr(result, '_kwargs'):
            # Response might be directly the atom data
            atom_data = result._kwargs
        
        if not atom_data:
            print("   No atom data found in response")
            if hasattr(result, '_kwargs'):
                print(f"   Response keys: {list(result._kwargs.keys())}")
            return None
        
        return atom_data
        
    except Exception as e:
        print(f"❌ Error retrieving atom: {str(e)}")
        
        if hasattr(e, 'status'):
            if e.status == 403:
                print("\n   Permission denied (403)")
                print("   • Check if your account can read atom details")
                print("   • Verify you have access to this specific atom")
            elif e.status == 404:
                print("\n   Not found (404)")
                print("   • The atom ID may not exist")
                print("   • Check the atom ID format (should be a UUID)")
            elif e.status == 400:
                print("\n   Bad request (400)")
                print("   • Verify the atom ID is in the correct format")
        
        return None

def format_date(date_string):
    """Format ISO date string to readable format."""
    try:
        if date_string:
            dt = datetime.fromisoformat(date_string.replace('Z', '+00:00'))
            return dt.strftime('%Y-%m-%d %H:%M:%S UTC')
    except:
        pass
    return date_string or 'N/A'

def display_atom_details(atom_data):
    """Display atom information in a comprehensive format."""
    
    print("\n📋 Atom Details:")
    print("=" * 70)
    
    # Basic information
    atom_id = atom_data.get('@id', 'N/A')
    atom_name = atom_data.get('@name', 'N/A')
    atom_type = atom_data.get('@type', 'N/A')
    atom_status = atom_data.get('@status', 'N/A')
    
    # Status icon
    if atom_status == 'ONLINE':
        status_icon = "🟢"
    elif atom_status == 'OFFLINE':
        status_icon = "🔴"
    else:
        status_icon = "⚪"
    
    print(f"🤖 Name: {atom_name}")
    print(f"🆔 ID: {atom_id}")
    print(f"📦 Type: {atom_type}")
    print(f"{status_icon} Status: {atom_status}")
    print()
    
    # Host and version information
    print("🖥️  Host Information:")
    print(f"   Hostname: {atom_data.get('@hostName', 'N/A')}")
    print(f"   Current Version: {atom_data.get('@currentVersion', 'N/A')}")
    print(f"   Build Number: {atom_data.get('@buildNumber', 'N/A')}")
    print()
    
    # Installation details
    print("📅 Installation Details:")
    print(f"   Date Installed: {format_date(atom_data.get('@dateInstalled'))}")
    print(f"   Last Modified: {format_date(atom_data.get('@lastModifiedDate'))}")
    print(f"   Created By: {atom_data.get('@createdBy', 'N/A')}")
    print()
    
    # Capabilities
    capabilities = atom_data.get('@capabilities', [])
    if capabilities:
        print("🔧 Capabilities:")
        for cap in capabilities:
            print(f"   • {cap}")
        print()
    
    # Cloud information
    cloud_id = atom_data.get('@cloudId', None)
    if cloud_id:
        print("☁️  Cloud Information:")
        print(f"   Cloud ID: {cloud_id}")
        print(f"   Cloud URL: {atom_data.get('@url', 'N/A')}")
        print()
    
    # Container information
    container_id = atom_data.get('@containerId', None)
    if container_id:
        print("📦 Container Information:")
        print(f"   Container ID: {container_id}")
        print()
    
    # Network information
    print("🌐 Network Configuration:")
    print(f"   Public IP Address: {atom_data.get('@publicIpAddress', 'N/A')}")
    print(f"   Network Addresses: {atom_data.get('@networkAddresses', 'N/A')}")
    print()
    
    # Environment associations
    env_count = atom_data.get('@environmentCount', 0)
    if env_count:
        print(f"🌍 Environment Attachments: {env_count}")
        print("   Use query_environment_atom_attachments.py to see details")
        print()
    
    # Additional properties
    print("🔍 Additional Properties:")
    print(f"   Purge Immediately: {atom_data.get('@purgeImmediately', False)}")
    print(f"   Force Restart: {atom_data.get('@forceRestart', False)}")
    print(f"   Offline Reason: {atom_data.get('@offlineReason', 'N/A')}")
    
    # Check for any additional fields not displayed
    known_fields = {
        '@id', '@name', '@type', '@status', '@hostName', '@currentVersion',
        '@buildNumber', '@dateInstalled', '@lastModifiedDate', '@createdBy',
        '@capabilities', '@cloudId', '@url', '@containerId', '@publicIpAddress',
        '@networkAddresses', '@environmentCount', '@purgeImmediately',
        '@forceRestart', '@offlineReason'
    }
    
    additional_fields = set(atom_data.keys()) - known_fields
    if additional_fields:
        print(f"\n📎 Other Fields: {', '.join(additional_fields)}")

def get_sample_atom_id(sdk):
    """Get a sample atom ID for demonstration."""
    
    try:
        from boomi.models import (
            AtomQueryConfig,
            AtomQueryConfigQueryFilter,
            AtomSimpleExpression,
            AtomSimpleExpressionOperator,
            AtomSimpleExpressionProperty
        )
        
        # Query for any atom
        simple_expression = AtomSimpleExpression(
            operator=AtomSimpleExpressionOperator.EQUALS,
            property=AtomSimpleExpressionProperty.TYPE,
            argument=["ATOM"]
        )
        
        query_filter = AtomQueryConfigQueryFilter(expression=simple_expression)
        query_config = AtomQueryConfig(query_filter=query_filter)
        
        result = sdk.atom.query_atom(query_config)
        
        # Use modern SDK response format
        if hasattr(result, 'result') and result.result:
            atoms = result.result if isinstance(result.result, list) else [result.result]
            if atoms:
                # Use object attributes instead of dict access
                first_atom = atoms[0]
                atom_id = getattr(first_atom, 'id_', 'N/A')
                atom_name = getattr(first_atom, 'name', 'N/A')
                return atom_id, atom_name
        
    except Exception as e:
        print(f"   Could not retrieve sample atom: {str(e)}")
    
    return None, None

def main():
    """Main function to demonstrate atom detail retrieval."""
    
    print("🚀 Boomi SDK - Get Atom Details")
    print("=" * 50)
    
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
        # Get atom ID from arguments or find a sample
        if len(sys.argv) > 1:
            atom_id = sys.argv[1]
            print(f"📍 Using provided atom ID: {atom_id}")
        else:
            print("💡 Usage: python3 get_atom.py <atom_id>")
            print()
            print("   Looking for a sample atom...")
            
            sample_id, sample_name = get_sample_atom_id(sdk)
            if sample_id:
                print(f"   Found atom: {sample_name}")
                atom_id = input(f"   Use this atom? (Y/n) or enter atom ID: ").strip()
                
                if not atom_id or atom_id.lower() == 'y':
                    atom_id = sample_id
                elif atom_id.lower() == 'n':
                    atom_id = input("Enter atom ID: ").strip()
            else:
                print("   No atoms found for demonstration")
                atom_id = input("Enter atom ID: ").strip()
            
            if not atom_id:
                print("❌ No atom ID provided")
                return
        
        print()
        
        # Retrieve atom details
        atom_data = get_atom_details(sdk, atom_id)
        
        if atom_data:
            # Display comprehensive details
            display_atom_details(atom_data)
            
            print("\n💡 Use Cases:")
            print("   • Check atom status before deploying processes")
            print("   • Verify atom version compatibility")
            print("   • Monitor atom health and connectivity")
            print("   • Troubleshoot offline atoms")
            print("   • Audit atom configurations")
            print()
            
            print("🔗 Related Examples:")
            print("   • list_atoms.py - List all atoms in the account")
            print("   • update_atom.py - Update atom configuration")
            print("   • get_atom_status.py - Get detailed status information")
            print("   • delete_atom.py - Remove an atom from the account")
        
    except KeyboardInterrupt:
        print("\n❌ Operation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Example failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()