#!/usr/bin/env python3
"""
Get Atom/Runtime

This example demonstrates how to get atom/runtime details using the Boomi SDK.

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET

Usage:
    python get_atom_single.py ATOM_ID

Endpoint:
- atom.get_atom
"""

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

from boomi import Boomi

def main():
    if len(sys.argv) != 2:
        print("Usage: python get_atom_single.py ATOM_ID")
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
        
        # Parse the response
        if hasattr(result, '_kwargs') and 'Atom' in result._kwargs:
            atom_data = result._kwargs['Atom']
            
            print(f"  🆔 ID: {atom_data.get('@id', 'N/A')}")
            print(f"  📛 Name: {atom_data.get('@name', 'N/A')}")
            print(f"  🏷️  Type: {atom_data.get('@type', 'N/A')}")
            print(f"  📊 Status: {atom_data.get('@status', 'N/A')}")
        else:
            print("⚠️  Unexpected response format")
            print(f"   Raw response: {result}")
            
    except Exception as e:
        print(f"❌ Error getting atom: {str(e)}")
        if hasattr(e, 'status'):
            if e.status == 404:
                print("   Atom not found")

if __name__ == "__main__":
    main()