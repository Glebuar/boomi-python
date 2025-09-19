#!/usr/bin/env python3
"""
Create Component Atom Attachment

This example demonstrates how to attach a component directly to an atom/runtime.

NOTE: This API only works for accounts that do NOT use environments.
For accounts with environments, use ComponentEnvironmentAttachment instead.

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- Account must not use environments

Usage:
    python attach_component_to_atom.py COMPONENT_ID ATOM_ID

Endpoint:
- component_atom_attachment.create_component_atom_attachment
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
from boomi.models import ComponentAtomAttachment

def main():
    if len(sys.argv) != 3:
        print("Usage: python create_component_atom_attachment.py COMPONENT_ID ATOM_ID")
        sys.exit(1)
    
    component_id = sys.argv[1]
    atom_id = sys.argv[2]
    
    # Initialize SDK
    sdk = Boomi(
        account_id=os.getenv("BOOMI_ACCOUNT"),
        username=os.getenv("BOOMI_USER"),
        password=os.getenv("BOOMI_SECRET"),
        timeout=30000,
    )
    
    print(f"🔗 Creating component-atom attachment...")
    print(f"   Component ID: {component_id}")
    print(f"   Atom ID: {atom_id}")
    
    try:
        # Create the attachment
        attachment_request = ComponentAtomAttachment(
            component_id=component_id,
            atom_id=atom_id
        )
        
        result = sdk.component_atom_attachment.create_component_atom_attachment(
            attachment_request
        )
        
        print("✅ Component attached to atom successfully!")
        print(f"   Attachment result: {result}")
        
    except Exception as e:
        print(f"❌ Error creating attachment: {str(e)}")
        if hasattr(e, 'status'):
            if e.status == 409:
                print("   Component may already be attached to this atom")
            elif e.status == 400:
                error_msg = str(e)
                if "uses environments" in error_msg:
                    print("   ⚠️ This account uses environments.")
                    print("   Use ComponentEnvironmentAttachment API instead")
                else:
                    print("   Invalid request - check component and atom IDs")

if __name__ == "__main__":
    main()