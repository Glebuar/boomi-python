#!/usr/bin/env python3
"""
Detach Runtime from Environment

This example demonstrates how to detach a runtime (atom) from an environment
by deleting the environment-atom attachment.

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET

Usage:
    python detach_runtime_from_environment.py ATTACHMENT_ID

Endpoint:
- environment_atom_attachment.delete_environment_atom_attachment
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
        print("Usage: python detach_runtime_from_environment.py ATTACHMENT_ID")
        sys.exit(1)
    
    attachment_id = sys.argv[1]
    
    # Initialize SDK
    sdk = Boomi(
        account_id=os.getenv("BOOMI_ACCOUNT"),
        username=os.getenv("BOOMI_USER"),
        password=os.getenv("BOOMI_SECRET"),
        timeout=30000,
    )
    
    print(f"🔗 Detaching runtime from environment...")
    print(f"   Attachment ID: {attachment_id}")

    try:
        # Delete the attachment
        result = sdk.environment_atom_attachment.delete_environment_atom_attachment(id_=attachment_id)

        print("✅ Runtime successfully detached from environment!")
        print("   The atom is now available to be attached to another environment.")
        
    except Exception as e:
        print(f"❌ Error detaching runtime: {str(e)}")
        if hasattr(e, 'status'):
            if e.status == 400:
                print("   Bad request - attachment ID may be invalid")
            elif e.status == 404:
                print("   Attachment not found - may have already been deleted")
            elif e.status == 403:
                print("   Permission denied - check account permissions")

if __name__ == "__main__":
    main()