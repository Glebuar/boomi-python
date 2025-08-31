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
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# Load environment variables from .env file if available
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv is optional

from src.boomi import Boomi


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
        print(f"❌ Error retrieving environment: {e}")
        
        # Provide helpful troubleshooting hints
        error_msg = str(e)
        if "404" in error_msg or "not found" in error_msg.lower():
            print("🔍 Environment not found - check the environment ID")
        elif "403" in error_msg:
            print("🔍 Permission issue - check your API credentials and account permissions")
        elif "401" in error_msg:
            print("🔍 Authentication failed - verify your credentials")
        else:
            print("🔍 Check network connectivity and API endpoint availability")
            
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()