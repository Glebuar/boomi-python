#!/usr/bin/env python3
"""
Get Environment

This example demonstrates how to get environment details using the Boomi SDK.

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET

Usage:
    python get_environment_single.py ENVIRONMENT_ID

Endpoint:
- environment.get_environment
"""

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

from boomi import Boomi

def main():
    if len(sys.argv) != 2:
        print("Usage: python get_environment_single.py ENVIRONMENT_ID")
        sys.exit(1)
    
    environment_id = sys.argv[1]
    
    # Initialize SDK
    sdk = Boomi(
        account_id=os.getenv("BOOMI_ACCOUNT"),
        username=os.getenv("BOOMI_USER"),
        password=os.getenv("BOOMI_SECRET"),
        timeout=30000,
    )
    
    print(f"🔍 Getting environment: {environment_id}")
    
    try:
        # Get the environment
        environment = sdk.environment.get_environment(id_=environment_id)
        
        print("✅ Environment retrieved successfully!")
        
        # Parse the response
        if hasattr(environment, '_kwargs') and 'Environment' in environment._kwargs:
            env_data = environment._kwargs['Environment']
            
            print(f"  🆔 ID: {env_data.get('@id', 'N/A')}")
            print(f"  📛 Name: {env_data.get('@name', 'N/A')}")
            print(f"  🏷️  Classification: {env_data.get('@classification', 'N/A')}")
        else:
            print("⚠️  Unexpected response format")
            
    except Exception as e:
        print(f"❌ Error getting environment: {str(e)}")

if __name__ == "__main__":
    main()