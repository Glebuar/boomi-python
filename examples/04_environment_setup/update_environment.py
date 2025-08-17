#!/usr/bin/env python3
"""
Update Environment

This example demonstrates how to update an environment using the Boomi SDK.
Note: Only the environment name can be modified - classification and ID are immutable.

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET

Usage:
    python update_environment_single.py ENVIRONMENT_ID NEW_NAME

Endpoint:
- environment.update_environment
"""

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

from boomi import Boomi
from boomi.models import Environment as EnvironmentModel

def main():
    if len(sys.argv) != 3:
        print("Usage: python update_environment_single.py ENVIRONMENT_ID NEW_NAME")
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
        # Create the update request (only name can be updated)
        update_request = EnvironmentModel(name=new_name)
        
        # Make the API call
        updated_environment = sdk.environment.update_environment(
            id_=environment_id,
            request_body=update_request
        )
        
        print("✅ Environment updated successfully!")
        
        # Parse the response
        if hasattr(updated_environment, '_kwargs') and 'Environment' in updated_environment._kwargs:
            env_data = updated_environment._kwargs['Environment']
            
            print(f"  🆔 ID: {env_data.get('@id', 'N/A')}")
            print(f"  📛 Name: {env_data.get('@name', 'N/A')}")
            print(f"  🏷️  Classification: {env_data.get('@classification', 'N/A')}")
            
            # Verify the name was actually changed
            if env_data.get('@name') == new_name:
                print("✅ Name update verified!")
            else:
                print("⚠️  Warning: Name may not have been updated as expected")
        else:
            print("⚠️  Unexpected response format")
            
    except Exception as e:
        print(f"❌ Error updating environment: {str(e)}")

if __name__ == "__main__":
    main()