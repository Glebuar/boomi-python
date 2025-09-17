#!/usr/bin/env python3
"""
Get Runtime Status

This example demonstrates how to get runtime status using the Boomi SDK.

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET

Usage:
    python get_runtime_status.py RUNTIME_ID

Endpoint:
- atom.get_atom
"""

import os
import sys
from pathlib import Path
from datetime import datetime, timezone

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

# Load environment variables from .env file if available
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv is optional

from boomi import Boomi

def main():
    if len(sys.argv) != 2:
        runtime_id = "2d4d5da4-0dfe-41f8-914b-f5f5120ad90a"  # US Test AZURE AKS runtime
        print(f"ℹ️ No runtime_id provided, using default: {runtime_id}")
        print("💡 To use a different runtime, run: python get_runtime_status.py YOUR_RUNTIME_ID")
    else:
        runtime_id = sys.argv[1]
    
    # Initialize SDK
    sdk = Boomi(
        account_id=os.getenv("BOOMI_ACCOUNT"),
        username=os.getenv("BOOMI_USER"),
        password=os.getenv("BOOMI_SECRET"),
        timeout=30000,
    )
    
    print(f"📊 Getting runtime status: {runtime_id}")
    
    try:
        # Get the runtime details to check status
        result = sdk.atom.get_atom(id_=runtime_id)
        
        print("✅ Runtime status retrieved successfully!")

        # Parse the response - use modern SDK response format
        if hasattr(result, 'name'):
            status = getattr(result, 'status', 'UNKNOWN')

            # Determine status emoji
            status_emoji = {
                'ONLINE': '🟢',
                'OFFLINE': '🔴',
                'PAUSED': '⏸️',
                'UNKNOWN': '❓'
            }.get(status, '❓')

            print(f"\n📋 Runtime Status Report:")
            print(f"  {status_emoji} Status: {status}")
            print(f"  📛 Name: {getattr(result, 'name', 'N/A')}")
            print(f"  🆔 ID: {getattr(result, 'id_', 'N/A')}")
            print(f"  🏷️  Type: {getattr(result, 'type_', 'N/A')}")

            # Additional status details
            print(f"\n📊 Additional Details:")
            print(f"  🖥️  Host: {getattr(result, 'host_name', 'N/A')}")
            print(f"  📅 Installed: {getattr(result, 'date_installed', 'N/A')}")

            # Show last heartbeat if available
            if hasattr(result, 'last_restart'):
                print(f"  🔄 Last Restart: {getattr(result, 'last_restart', 'N/A')}")

            # Health check analysis
            print(f"\n💡 Status Analysis:")
            if status == 'ONLINE':
                print("  ✅ Runtime is operational and ready to process integrations")
            elif status == 'OFFLINE':
                print("  ⚠️  Runtime is not available - check connectivity or restart")
            elif status == 'PAUSED':
                print("  ⏸️  Runtime is paused - resume to process integrations")
            else:
                print("  ❓ Status unknown - verify runtime configuration")
        else:
            print("⚠️  Unexpected response format")
            if hasattr(result, '__dict__'):
                print(f"   Available attributes: {[attr for attr in dir(result) if not attr.startswith('_')]}")
            
    except Exception as e:
        print(f"❌ Error getting runtime status: {str(e)}")

if __name__ == "__main__":
    main()