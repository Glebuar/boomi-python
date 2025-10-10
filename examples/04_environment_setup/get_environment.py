#!/usr/bin/env python3
"""
Boomi SDK Example: Get Environment
=================================

This example demonstrates how to retrieve environment details using the Boomi SDK.

Features:
- Get environment by ID
- Display environment metadata
- Show environment classification and properties

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- ENVIRONMENT ACCESS privilege required

Usage:
    python get_environment.py ENVIRONMENT_ID

Examples:
    python get_environment.py 74851c30-98b2-4a6f-838b-61eee5627b13
"""

import os
import sys
from typing import Optional

# Add parent directory to path for imports
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

# Load environment variables from .env file if available
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv is optional

from boomi import Boomi


def validate_environment() -> tuple[str, str, str]:
    """Validate required environment variables and return credentials"""
    account_id = os.getenv("BOOMI_ACCOUNT")
    username = os.getenv("BOOMI_USER") 
    password = os.getenv("BOOMI_SECRET")
    
    if not all([account_id, username, password]):
        print("❌ Error: Missing required environment variables")
        print("   Please set: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET")
        print("   You can also create a .env file with these variables")
        sys.exit(1)
    
    return account_id, username, password


def main():
    """Main execution function"""
    if len(sys.argv) != 2:
        environment_id = "74851c30-98b2-4a6f-838b-61eee5627b13"  # Development environment
        print(f"ℹ️ No environment_id provided, using default: {environment_id}")
        print("💡 To use a different environment, run: python get_environment.py YOUR_ENV_ID")
    else:
        environment_id = sys.argv[1]
    
    print("🚀 Boomi SDK Example: Get Environment")
    print("=" * 45)
    
    # Validate environment variables
    account_id, username, password = validate_environment()
    
    print(f"🏢 Account: {account_id}")
    print(f"👤 User: {username}")
    print(f"🎯 Environment ID: {environment_id}")
    
    # Initialize SDK
    try:
        sdk = Boomi(
            account_id=account_id,
            username=username,
            password=password,
            timeout=30000
        )
        print("✅ SDK initialized successfully")
    except Exception as e:
        print(f"❌ Failed to initialize SDK: {e}")
        sys.exit(1)
    
    try:
        # Get environment details
        print(f"\n🔍 Retrieving environment details...")
        
        environment = sdk.environment.get_environment(id_=environment_id)
        
        print("✅ Environment retrieved successfully!")
        print(f"📊 Response type: {type(environment).__name__}")
        
        # Display environment information
        print("\n" + "="*60)
        print("📋 ENVIRONMENT DETAILS")
        print("="*60)
        
        # Handle both object and legacy response formats
        if hasattr(environment, 'name'):
            # Modern SDK response
            print(f"  🆔 ID: {getattr(environment, 'id_', 'N/A')}")
            print(f"  📛 Name: {getattr(environment, 'name', 'N/A')}")
            print(f"  🏷️  Classification: {getattr(environment, 'classification', 'N/A')}")
            if hasattr(environment, 'description') and environment.description:
                print(f"  📝 Description: {environment.description}")
        elif hasattr(environment, '_kwargs') and 'Environment' in environment._kwargs:
            # Legacy response format
            env_data = environment._kwargs['Environment']
            print(f"  🆔 ID: {env_data.get('@id', 'N/A')}")
            print(f"  📛 Name: {env_data.get('@name', 'N/A')}")
            print(f"  🏷️  Classification: {env_data.get('@classification', 'N/A')}")
        else:
            print("⚠️ Unexpected response format")
            print(f"Available attributes: {[attr for attr in dir(environment) if not attr.startswith('_')]}")
            
        print("\n✅ Environment details retrieved successfully!")
            
    except Exception as e:
        error_msg = str(e)

        # Check for status code in exception
        if hasattr(e, 'status'):
            status_code = e.status
            print(f"❌ Error retrieving environment: HTTP {status_code}")

            if status_code == 400:
                print("🔍 Bad request - environment ID may be invalid or malformed")
            elif status_code == 404:
                print("🔍 Environment not found - check the environment ID")
            elif status_code == 403:
                print("🔍 Permission issue - check your API credentials and account permissions")
            elif status_code == 401:
                print("🔍 Authentication failed - verify your credentials")
            else:
                print(f"🔍 {error_msg}")
        else:
            print(f"❌ Error retrieving environment: {error_msg}")
            print("🔍 Check network connectivity and API endpoint availability")
            
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()