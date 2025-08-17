#!/usr/bin/env python3
"""
Get Runtime Status

This example demonstrates how to get runtime status using the Boomi SDK.

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET

Usage:
    python get_runtime_status_single.py RUNTIME_ID

Endpoint:
- atom.get_atom
"""

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

from boomi import Boomi

def main():
    if len(sys.argv) != 2:
        print("Usage: python get_runtime_status_single.py RUNTIME_ID")
        sys.exit(1)
    
    runtime_id = sys.argv[1]
    
    # Initialize SDK
    sdk = Boomi(
        account_id=os.getenv("BOOMI_ACCOUNT"),
        username=os.getenv("BOOMI_USER"),
        password=os.getenv("BOOMI_SECRET"),
        timeout=30000,
    )
    
    print(f"📊 Getting runtime status: {runtime_id}")
    
    try:
        # Get the runtime details to check status
        result = sdk.atom.get_atom(id_=runtime_id)
        
        print("✅ Runtime status retrieved successfully!")
        
        # Parse the response to show status
        if hasattr(result, '_kwargs') and 'Atom' in result._kwargs:
            atom_data = result._kwargs['Atom']
            
            print(f"  🆔 ID: {atom_data.get('@id', 'N/A')}")
            print(f"  📛 Name: {atom_data.get('@name', 'N/A')}")
            print(f"  📊 Status: {atom_data.get('@status', 'N/A')}")
            print(f"  🏷️  Type: {atom_data.get('@type', 'N/A')}")
        else:
            print("⚠️  Unexpected response format")
            print(f"   Raw response: {result}")
            
    except Exception as e:
        print(f"❌ Error getting runtime status: {str(e)}")

if __name__ == "__main__":
    main()