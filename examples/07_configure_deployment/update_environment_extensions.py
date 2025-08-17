#!/usr/bin/env python3
"""
Update Environment Extensions

This example demonstrates how to update environment extensions.

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET

Usage:
    python update_environment_extensions_single.py ENVIRONMENT_ID

Endpoint:
- environment_extensions.update_environment_extensions
"""

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

from boomi import Boomi
from boomi.models import EnvironmentExtensions

def main():
    if len(sys.argv) != 2:
        print("Usage: python update_environment_extensions_single.py ENVIRONMENT_ID")
        sys.exit(1)
    
    environment_id = sys.argv[1]
    
    # Initialize SDK
    sdk = Boomi(
        account_id=os.getenv("BOOMI_ACCOUNT"),
        username=os.getenv("BOOMI_USER"),
        password=os.getenv("BOOMI_SECRET"),
        timeout=30000,
    )
    
    print(f"🔄 Updating environment extensions: {environment_id}")
    
    try:
        # Create update request - example extension configuration
        extensions_update = EnvironmentExtensions(
            environment_id=environment_id,
            # Add extension properties as needed
        )
        
        # Update environment extensions
        result = sdk.environment_extensions.update_environment_extensions(
            id_=environment_id,
            request_body=extensions_update
        )
        
        print("✅ Environment extensions updated successfully!")
        print(f"   Result: {result}")
        
    except Exception as e:
        print(f"❌ Error updating environment extensions: {str(e)}")

if __name__ == "__main__":
    main()