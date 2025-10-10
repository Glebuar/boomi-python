#!/usr/bin/env python3
"""
Boomi SDK Example: List All Runtimes
=============================================

This example demonstrates how to query and list all runtimes in a Boomi account
using the Python SDK. It shows runtime details including name, ID, status, and type.

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- Account must have appropriate permissions to read runtimes
- At least one runtime should be installed in the account

Usage:
    cd examples/runtime_management
    PYTHONPATH=../../src python3 list_runtimes.py

Features:
- Lists all runtimes in the account
- Shows runtime details (ID, name, type, status, hostname, version)
- Categorizes runtimes by status (ONLINE, OFFLINE)
- Shows installation and version information
"""

import os
import sys
from datetime import datetime
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

# Load environment variables from .env file if available
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv is optional

from boomi import Boomi
from boomi.models import (
    AtomQueryConfig,
    AtomQueryConfigQueryFilter,
    AtomSimpleExpression,
    AtomSimpleExpressionOperator,
    AtomSimpleExpressionProperty
)

def list_all_runtimes_sdk(sdk):
    """List all runtimes using SDK with no query filter (works best for atoms)."""
    
    print(f"🔍 Querying all runtimes using SDK...")
    
    try:
        # Create empty query config - no filter needed for atoms
        query_config = AtomQueryConfig()
        query_response = sdk.atom.query_atom(query_config)
        
        # Parse the response - it's an AtomQueryResponse object with 'result' attribute
        runtimes = []
        
        if hasattr(query_response, 'number_of_results'):
            num_results = query_response.number_of_results or 0
            print(f"   Found {num_results} runtimes in account")
        
        if hasattr(query_response, 'result') and query_response.result:
            result_data = query_response.result
            if isinstance(result_data, list):
                runtimes = result_data
            else:
                runtimes = [result_data]
                
            # Show what we found
            for runtime in runtimes:
                name = getattr(runtime, 'name', 'N/A')
                runtime_type = getattr(runtime, 'type_', 'N/A')  
                status = getattr(runtime, 'status', 'N/A')
                print(f"     - {name} ({runtime_type}, {status})")
        else:
            print(f"   No result data found in response")
        
        return runtimes
        
    except Exception as e:
        print(f"❌ Error querying runtimes with SDK: {str(e)}")
        if hasattr(e, 'status'):
            print(f"   Status code: {e.status}")
        return []

def list_runtimes_by_type(runtimes, runtime_type):
    """Filter runtimes by type from the full list."""
    
    filtered_runtimes = []
    for runtime in runtimes:
        # Handle both dict format (for backward compatibility) and object format
        if hasattr(runtime, 'type_'):
            current_type = getattr(runtime, 'type_', '')
        elif hasattr(runtime, 'get'):
            current_type = runtime.get('@type', '')
        else:
            # For objects without get method, try direct attribute access with fallback
            current_type = getattr(runtime, 'type_', '')
            
        if current_type == runtime_type:
            filtered_runtimes.append(runtime)
    
    return filtered_runtimes

def format_date(date_string):
    """Format ISO date string to readable format."""
    try:
        if date_string:
            dt = datetime.fromisoformat(date_string.replace('Z', '+00:00'))
            return dt.strftime('%Y-%m-%d %H:%M:%S UTC')
    except:
        pass
    return date_string or 'N/A'

def display_runtimes(runtimes, runtime_type):
    """Display runtime information in a formatted way."""
    
    if not runtimes:
        print(f"   No {runtime_type} runtimes found")
        return
    
    print(f"\n✅ Found {len(runtimes)} {runtime_type} runtime(s):")
    print("=" * 100)
    
    online_count = 0
    offline_count = 0
    
    for i, runtime in enumerate(runtimes, 1):
        # Handle both dict format (for backward compatibility) and object format
        if hasattr(runtime, 'id_'):
            runtime_id = getattr(runtime, 'id_', 'N/A')
            runtime_name = getattr(runtime, 'name', 'N/A')
            runtime_status = getattr(runtime, 'status', 'N/A')
            runtime_hostname = getattr(runtime, 'host_name', 'N/A')
            runtime_version = getattr(runtime, 'current_version', 'N/A')
            runtime_installed = getattr(runtime, 'date_installed', 'N/A')
            runtime_created_by = getattr(runtime, 'created_by', 'N/A')
            runtime_capabilities = getattr(runtime, 'capabilities', [])
        else:
            runtime_id = runtime.get('@id', 'N/A')
            runtime_name = runtime.get('@name', 'N/A')
            runtime_status = runtime.get('@status', 'N/A')
            runtime_hostname = runtime.get('@hostName', 'N/A')
            runtime_version = runtime.get('@currentVersion', 'N/A')
            runtime_installed = runtime.get('@dateInstalled', 'N/A')
            runtime_created_by = runtime.get('@createdBy', 'N/A')
            runtime_capabilities = runtime.get('@capabilities', [])
        
        # Count status
        if runtime_status == 'ONLINE':
            online_count += 1
            status_icon = "🟢"
        elif runtime_status == 'OFFLINE':
            offline_count += 1
            status_icon = "🔴"
        else:
            status_icon = "⚪"
        
        print(f"{i:2}. 🤖 {runtime_name}")
        print(f"     🆔 ID: {runtime_id}")
        print(f"     {status_icon} Status: {runtime_status}")
        print(f"     🖥️  Hostname: {runtime_hostname}")
        print(f"     📦 Version: {runtime_version}")
        print(f"     📅 Installed: {format_date(runtime_installed)}")
        print(f"     👤 Created by: {runtime_created_by}")
        
        if runtime_capabilities:
            print(f"     🔧 Capabilities: {', '.join(runtime_capabilities)}")
        
        print()
    
    # Status summary
    print("📊 Status Summary:")
    print(f"   🟢 Online: {online_count}")
    print(f"   🔴 Offline: {offline_count}")
    print()

def main():
    """Main function to demonstrate runtime listing."""
    
    print("🚀 Boomi SDK - List All Runtimes (Runtimes) Example")
    print("=" * 60)
    
    # Check for required environment variables
    required_vars = ["BOOMI_ACCOUNT", "BOOMI_USER", "BOOMI_SECRET"]
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars:
        print("❌ Missing required environment variables:")
        for var in missing_vars:
            print(f"   - {var}")
        print("\nPlease set these variables in your environment")
        sys.exit(1)
    
    # Initialize the Boomi SDK
    sdk = Boomi(
        account_id=os.getenv("BOOMI_ACCOUNT"),
        username=os.getenv("BOOMI_USER"),
        password=os.getenv("BOOMI_SECRET"),
        timeout=30000,
    )
    
    print("✅ SDK initialized successfully!")
    print()
    
    try:
        # Get all runtimes using SDK
        all_runtimes = list_all_runtimes_sdk(sdk)
        
        if all_runtimes:
            # Group runtimes by type and display
            runtime_types = ["ATOM", "CLOUD", "MOLECULE", "GATEWAY"]
            
            for runtime_type in runtime_types:
                filtered_runtimes = list_runtimes_by_type(all_runtimes, runtime_type)
                if filtered_runtimes:
                    display_runtimes(filtered_runtimes, runtime_type)
        
        # Overall summary
        if all_runtimes:
            print("=" * 100)
            print(f"🎯 Overall Summary:")
            print(f"   Total runtimes: {len(all_runtimes)}")
            
            # Count by status
            online = 0
            offline = 0
            for runtime in all_runtimes:
                if hasattr(runtime, 'status'):
                    status = runtime.status
                else:
                    status = runtime.get('@status', '')
                    
                if status == 'ONLINE':
                    online += 1
                elif status == 'OFFLINE':
                    offline += 1
            
            print(f"   🟢 Online runtimes: {online}")
            print(f"   🔴 Offline runtimes: {offline}")
            
            # Count by type
            type_counts = {}
            for runtime in all_runtimes:
                if hasattr(runtime, 'type_'):
                    runtime_type = runtime.type_
                else:
                    runtime_type = runtime.get('@type', 'Unknown')
                type_counts[runtime_type] = type_counts.get(runtime_type, 0) + 1
            
            print(f"\n   📋 By Type:")
            for runtime_type, count in type_counts.items():
                print(f"     • {runtime_type}: {count}")
            
            print(f"\n💡 Tips:")
            print(f"   • Online runtimes can execute processes")
            print(f"   • Offline runtimes need to be started to be used")
            print(f"   • Runtime IDs are needed for environment attachments")
            print(f"   • Check runtime versions for compatibility")
        else:
            print("❌ No runtimes found in the account")
            print("\n💡 To use Boomi:")
            print("   • Install at least one Runtime (runtime)")
            print("   • Runtimes can be downloaded from the Boomi platform")
            print("   • Cloud runtimes are also available as an alternative")
        
        print("\n🔧 Technical Note:")
        print("   Uses SDK with empty AtomQueryConfig (no filter needed for runtime queries)")  
        print("   Fixed SDK issue: AtomQueryConfig.query_filter is now optional")
        print("   Runtimes are grouped by type (ATOM, CLOUD, MOLECULE, GATEWAY) for display")
        
    except Exception as e:
        print(f"❌ Example failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()