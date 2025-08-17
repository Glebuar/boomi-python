#!/usr/bin/env python3
"""
Update Runtime

This example demonstrates how to update a runtime using the Boomi SDK.

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET

Usage:
    python update_runtime_single.py RUNTIME_ID

Endpoint:
- atom.update_atom
"""

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

from boomi import Boomi
from boomi.models import Atom

def main():
    if len(sys.argv) != 2:
        print("Usage: python update_runtime_single.py RUNTIME_ID")
        sys.exit(1)
    
    runtime_id = sys.argv[1]
    
    # Initialize SDK
    sdk = Boomi(
        account_id=os.getenv("BOOMI_ACCOUNT"),
        username=os.getenv("BOOMI_USER"),
        password=os.getenv("BOOMI_SECRET"),
        timeout=30000,
    )
    
    print(f"🔄 Updating runtime: {runtime_id}")
    
    try:
        # Create update request (example: update description)
        runtime_update = Atom(
            description="Updated via SDK"
        )
        
        # Update the runtime
        result = sdk.atom.update_atom(
            id_=runtime_id, 
            request_body=runtime_update
        )
        
        print("✅ Runtime updated successfully!")
        print(f"   Result: {result}")
        
    except Exception as e:
        print(f"❌ Error updating runtime: {str(e)}")

if __name__ == "__main__":
    main()