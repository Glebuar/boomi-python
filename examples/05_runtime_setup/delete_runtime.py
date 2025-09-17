#!/usr/bin/env python3
"""
Delete Atom/Runtime

This example demonstrates how to delete an atom/runtime using the Boomi SDK.
WARNING: Deletion is permanent and cannot be undone!

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET

Usage:
    python delete_runtime.py ATOM_ID

Endpoint:
- atom.delete_atom
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
        print("Usage: python delete_runtime.py ATOM_ID")
        sys.exit(1)
    
    atom_id = sys.argv[1]
    
    # Initialize SDK
    sdk = Boomi(
        account_id=os.getenv("BOOMI_ACCOUNT"),
        username=os.getenv("BOOMI_USER"),
        password=os.getenv("BOOMI_SECRET"),
        timeout=30000,
    )
    
    print(f"🗑️  Deleting atom/runtime: {atom_id}")
    print("⚠️  WARNING: Deletion is permanent and cannot be undone!")
    
    # Double confirmation for safety
    confirm = input("Type 'DELETE' to confirm deletion: ").strip()
    if confirm != 'DELETE':
        print("❌ Deletion cancelled")
        return
    
    try:
        # Perform the deletion
        sdk.atom.delete_atom(id_=atom_id)
        
        print("✅ Atom deleted successfully!")
        
    except Exception as e:
        print(f"❌ Error deleting atom: {str(e)}")
        if hasattr(e, 'status'):
            if e.status == 400:
                print("   Bad request - atom may not exist or ID is invalid")
            elif e.status == 403:
                print("   Permission denied - check if your account can delete atoms")
            elif e.status == 404:
                print("   Atom not found - it may have already been deleted")
            elif e.status == 409:
                print("   Conflict - atom may be attached to environments")

if __name__ == "__main__":
    main()