#!/usr/bin/env python3
"""
Create Environment

This example demonstrates how to create an environment using the Boomi SDK.

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET

Usage:
    python create_environment_single.py ENVIRONMENT_NAME [CLASSIFICATION]

Endpoint:
- environment.create_environment
"""

import os
import sys
import datetime
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

# Load environment variables from .env file if available
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv is optional

from boomi import Boomi
from boomi.models import Environment as EnvironmentModel, EnvironmentClassification

def main():
    if len(sys.argv) < 2:
        print("Usage: python create_environment_single.py ENVIRONMENT_NAME [CLASSIFICATION]")
        sys.exit(1)
    
    env_name = sys.argv[1]
    classification = sys.argv[2] if len(sys.argv) > 2 else "TEST"
    
    # Initialize SDK
    sdk = Boomi(
        account_id=os.getenv("BOOMI_ACCOUNT"),
        username=os.getenv("BOOMI_USER"),
        password=os.getenv("BOOMI_SECRET"),
        timeout=30000,
    )
    
    print(f"🏗️  Creating environment: {env_name}")
    print(f"   Classification: {classification}")
    
    try:
        # Create the environment
        new_environment = EnvironmentModel(
            name=env_name,
            classification=getattr(EnvironmentClassification, classification.upper(), EnvironmentClassification.TEST)
        )
        
        created_environment = sdk.environment.create_environment(new_environment)

        print("✅ Environment created successfully!")

        # Display the created environment details
        print(f"  🆔 ID: {created_environment.id_}")
        print(f"  📛 Name: {created_environment.name}")
        print(f"  🏷️  Classification: {created_environment.classification}")
            
    except Exception as e:
        print(f"❌ Error creating environment: {str(e)}")

if __name__ == "__main__":
    main()