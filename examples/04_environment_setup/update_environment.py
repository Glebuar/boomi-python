#!/usr/bin/env python3
"""
Update Environment

This example demonstrates how to update an environment using the Boomi SDK.
Note: Only the environment name can be modified - classification and ID are immutable.

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET

Usage:
    python update_environment.py ENVIRONMENT_ID NEW_NAME

Endpoint:
- environment.update_environment
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
    # If dotenv is not available, try to load .env manually
    env_file = Path(__file__).parent.parent.parent / '.env'
    if env_file.exists():
        with open(env_file, 'r') as f:
            for line in f:
                if '=' in line and not line.startswith('#'):
                    key, value = line.strip().split('=', 1)
                    os.environ[key] = value.strip('"')

from boomi import Boomi
from boomi.models import Environment as EnvironmentModel

def main():
    if len(sys.argv) != 3:
        print("Usage: python update_environment.py ENVIRONMENT_ID NEW_NAME")
        sys.exit(1)
    
    environment_id = sys.argv[1]
    new_name = sys.argv[2]
    
    # Initialize SDK
    sdk = Boomi(
        account_id=os.getenv("BOOMI_ACCOUNT"),
        username=os.getenv("BOOMI_USER"),
        password=os.getenv("BOOMI_SECRET"),
        timeout=30000,
    )
    
    print(f"🔄 Updating environment name...")
    print(f"   Environment ID: {environment_id}")
    print(f"   New Name: {new_name}")
    
    try:
        # First, get the current environment to preserve its classification
        print(f"📋 Fetching current environment details...")
        current_env = sdk.environment.get_environment(id_=environment_id)

        # API requires all fields including ID and classification
        update_request = EnvironmentModel(
            id_=environment_id,
            name=new_name,
            classification=current_env.classification
        )

        # Make the API call
        updated_environment = sdk.environment.update_environment(
            id_=environment_id,
            request_body=update_request
        )
        
        print("✅ Environment updated successfully!")

        # Parse the response - use modern SDK response format
        if hasattr(updated_environment, 'name'):
            print(f"  🆔 ID: {getattr(updated_environment, 'id_', 'N/A')}")
            print(f"  📛 Name: {getattr(updated_environment, 'name', 'N/A')}")
            print(f"  🏷️  Classification: {getattr(updated_environment, 'classification', 'N/A')}")

            # Verify the name was actually changed
            if updated_environment.name == new_name:
                print("✅ Name update verified!")
            else:
                print("⚠️  Warning: Name may not have been updated as expected")
        else:
            print("⚠️  Unexpected response format")
            
    except Exception as e:
        print(f"❌ Error updating environment: {str(e)}")

if __name__ == "__main__":
    main()