#!/usr/bin/env python3
"""
Delete Environment Atom Attachment

This example demonstrates how to delete an environment-atom attachment.

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET

Usage:
    python delete_environment_atom_attachment.py ATTACHMENT_ID

Endpoint:
- environment_atom_attachment.delete_environment_atom_attachment
"""

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

from boomi import Boomi

def main():
    if len(sys.argv) != 2:
        print("Usage: python delete_environment_atom_attachment.py ATTACHMENT_ID")
        sys.exit(1)
    
    attachment_id = sys.argv[1]
    
    # Initialize SDK
    sdk = Boomi(
        account_id=os.getenv("BOOMI_ACCOUNT"),
        username=os.getenv("BOOMI_USER"),
        password=os.getenv("BOOMI_SECRET"),
        timeout=30000,
    )
    
    print(f"🗑️ Deleting environment-atom attachment: {attachment_id}")
    
    try:
        # Delete the attachment
        result = sdk.environment_atom_attachment.delete_environment_atom_attachment(id_=attachment_id)
        
        print("✅ Environment-atom attachment deleted successfully!")
        print(f"   Result: {result}")
        
    except Exception as e:
        print(f"❌ Error deleting attachment: {str(e)}")
        if hasattr(e, 'status'):
            if e.status == 404:
                print("   Attachment not found - may have already been deleted")
            elif e.status == 403:
                print("   Permission denied - check account permissions")

if __name__ == "__main__":
    main()