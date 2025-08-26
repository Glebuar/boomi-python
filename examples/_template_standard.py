#!/usr/bin/env python3
"""
[TEMPLATE] Boomi SDK Example: [Example Name]
==========================================

[Description of what this example does]

Features:
- [Feature 1]
- [Feature 2]

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- [Additional requirements]

Usage:
    python [example_name].py [args]

Examples:
    python [example_name].py [example usage]
"""

import os
import sys
import argparse
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
    print("🚀 Boomi SDK Example: [Example Name]")
    print("=" * 50)
    
    # Validate environment variables
    account_id, username, password = validate_environment()
    
    # Initialize SDK
    try:
        sdk = Boomi(
            account_id=account_id,
            username=username,
            password=password,
            timeout=30000
        )
        print("✅ SDK initialized successfully")
        print(f"🏢 Account: {account_id}")
        print(f"👤 User: {username}")
    except Exception as e:
        print(f"❌ Failed to initialize SDK: {e}")
        sys.exit(1)
    
    try:
        # Example implementation here
        print("\n🔍 [Example operation]...")
        
        # SDK calls and processing
        
        print("✅ [Example operation] completed successfully!")
        
    except Exception as e:
        print(f"❌ Error during [example operation]: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()