#!/usr/bin/env python3
"""
Delete Environment

This example demonstrates how to delete an environment using the Boomi SDK.
WARNING: Deletion is permanent and cannot be undone!

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET

Usage:
    python delete_environment_single.py ENVIRONMENT_ID

Endpoint:
- environment.delete_environment
"""

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

# Load environment variables from .env file if available
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv is optional

from boomi import Boomi

def main():
    if len(sys.argv) != 2:
        print("Usage: python delete_environment_single.py ENVIRONMENT_ID")
        sys.exit(1)
    
    environment_id = sys.argv[1]
    
    # Initialize SDK
    sdk = Boomi(
        account_id=os.getenv("BOOMI_ACCOUNT"),
        username=os.getenv("BOOMI_USER"),
        password=os.getenv("BOOMI_SECRET"),
        timeout=30000,
    )
    
    print(f"🗑️  Deleting environment: {environment_id}")
    print("⚠️  WARNING: Deletion is permanent and cannot be undone!")
    
    # Double confirmation for safety
    confirm = input("Type 'DELETE' to confirm deletion: ").strip()
    if confirm != 'DELETE':
        print("❌ Deletion cancelled")
        return
    
    try:
        # Perform the deletion
        sdk.environment.delete_environment(id_=environment_id)

        print("✅ Environment deleted successfully!")

    except Exception as e:
        error_msg = str(e)
        if hasattr(e, 'status'):
            status_code = e.status
            print(f"❌ Error deleting environment: HTTP {status_code}")

            if status_code == 400:
                print("   Bad request - environment ID may be invalid")
            elif status_code == 403:
                print("   Permission denied - check if your account can delete environments")
            elif status_code == 404:
                print("   Environment not found - it may have already been deleted")
            elif status_code == 409:
                print("   Conflict - environment may have attached runtimes or deployed components")
            else:
                print(f"   {error_msg}")
        else:
            print(f"❌ Error deleting environment: {error_msg}")

if __name__ == "__main__":
    main()