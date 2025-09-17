#!/usr/bin/env python3
"""
Get Atom/Runtime

This example demonstrates how to get atom/runtime details using the Boomi SDK.

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET

Usage:
    python get_runtime.py ATOM_ID

Endpoint:
- atom.get_atom
"""

import os
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

# Load environment variables from .env file if available
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv is optional

from boomi import Boomi

def main():
    if len(sys.argv) != 2:
        print("Usage: python get_runtime.py ATOM_ID")
        sys.exit(1)
    
    atom_id = sys.argv[1]
    
    # Initialize SDK
    sdk = Boomi(
        account_id=os.getenv("BOOMI_ACCOUNT"),
        username=os.getenv("BOOMI_USER"),
        password=os.getenv("BOOMI_SECRET"),
        timeout=30000,
    )
    
    print(f"🔍 Getting atom/runtime details: {atom_id}")
    
    try:
        # Get the atom
        result = sdk.atom.get_atom(id_=atom_id)
        
        print("✅ Atom retrieved successfully!")

        # Parse the response - use modern SDK response format
        if hasattr(result, 'name'):
            print(f"\n📋 Atom Details:")
            print(f"  🆔 ID: {getattr(result, 'id_', 'N/A')}")
            print(f"  📛 Name: {getattr(result, 'name', 'N/A')}")
            print(f"  🏷️  Type: {getattr(result, 'type_', 'N/A')}")
            print(f"  📊 Status: {getattr(result, 'status', 'N/A')}")
            print(f"  🖥️  Host: {getattr(result, 'host_name', 'N/A')}")
            print(f"  📅 Installed: {getattr(result, 'date_installed', 'N/A')}")

            # Show cloud ID if it's a cloud atom
            if hasattr(result, 'cloud_id') and result.cloud_id:
                print(f"  ☁️  Cloud ID: {result.cloud_id}")
        else:
            print("⚠️  Unexpected response format")
            if hasattr(result, '__dict__'):
                print(f"   Available attributes: {[attr for attr in dir(result) if not attr.startswith('_')]}")
            
    except Exception as e:
        print(f"❌ Error getting atom: {str(e)}")
        if hasattr(e, 'status'):
            if e.status == 400:
                print("   Bad request - atom ID may be invalid")
            elif e.status == 404:
                print("   Atom not found")
            elif e.status == 403:
                print("   Permission denied - check account permissions")

if __name__ == "__main__":
    main()