#!/usr/bin/env python3
"""
Create Environment Atom Attachment

This example demonstrates how to create an attachment between a runtime (atom) and environment.

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET

Usage:
    python create_environment_atom_attachment.py ATOM_ID ENVIRONMENT_ID

Endpoint:
- environment_atom_attachment.create_environment_atom_attachment
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
from boomi.models import EnvironmentAtomAttachment

def main():
    if len(sys.argv) != 3:
        print("Usage: python create_environment_atom_attachment.py ATOM_ID ENVIRONMENT_ID")
        sys.exit(1)
    
    atom_id = sys.argv[1]
    environment_id = sys.argv[2]
    
    # Initialize SDK
    sdk = Boomi(
        account_id=os.getenv("BOOMI_ACCOUNT"),
        username=os.getenv("BOOMI_USER"),
        password=os.getenv("BOOMI_SECRET"),
        timeout=30000,
    )
    
    print(f"🔗 Creating environment-atom attachment...")
    print(f"   Atom ID: {atom_id}")
    print(f"   Environment ID: {environment_id}")
    
    try:
        # Create the attachment request
        attachment_request = EnvironmentAtomAttachment(
            atom_id=atom_id,
            environment_id=environment_id
        )
        
        # Make the API call
        created_attachment = sdk.environment_atom_attachment.create_environment_atom_attachment(
            attachment_request
        )
        
        print("✅ Attachment created successfully!")

        # Parse the response - use modern SDK response format
        if hasattr(created_attachment, 'atom_id'):
            print(f"  🆔 Attachment ID: {getattr(created_attachment, 'id_', 'N/A')}")
            print(f"  🤖 Atom ID: {getattr(created_attachment, 'atom_id', 'N/A')}")
            print(f"  🌍 Environment ID: {getattr(created_attachment, 'environment_id', 'N/A')}")
        else:
            print("⚠️  Unexpected response format")
            # Debug: show available attributes
            if hasattr(created_attachment, '__dict__'):
                print(f"  Available attributes: {[attr for attr in dir(created_attachment) if not attr.startswith('_')]}")
            
    except Exception as e:
        print(f"❌ Error creating attachment: {str(e)}")

if __name__ == "__main__":
    main()