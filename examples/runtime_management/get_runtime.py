#!/usr/bin/env python3
"""
Boomi SDK Example: Get Runtime Details
====================================

This example demonstrates how to retrieve specific runtime (runtime) details
using the Boomi SDK. It shows how to get comprehensive information about
an runtime including its configuration, status, and capabilities.

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- Account must have appropriate permissions to read runtime details
- Need a valid runtime ID to retrieve

Usage:
    cd examples/runtime_management
    PYTHONPATH=../../src python3 get_runtime.py [runtime_id]

Features:
- Retrieves complete runtime information by ID
- Shows runtime configuration details
- Displays status, version, and capability information
- Shows installation and environment attachment details
"""

import os
import sys
from datetime import datetime

# Add the src directory to the path to import the SDK
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

from boomi import Boomi

def get_runtime_details(sdk, runtime_id):
    """Retrieve specific runtime details."""
    
    print(f"🔍 Retrieving runtime details...")
    print(f"   Runtime ID: {runtime_id}")
    
    try:
        # Call the get atom API
        result = sdk.atom.get_atom(id_=runtime_id)
        
        print("✅ Runtime details retrieved successfully!")
        
        # Parse the response
        runtime_data = None
        if hasattr(result, '_kwargs') and 'Atom' in result._kwargs:
            runtime_data = result._kwargs['Atom']
        elif hasattr(result, '_kwargs'):
            # Response might be directly the runtime data
            runtime_data = result._kwargs
        
        if not runtime_data:
            print("   No runtime data found in response")
            if hasattr(result, '_kwargs'):
                print(f"   Response keys: {list(result._kwargs.keys())}")
            return None
        
        return runtime_data
        
    except Exception as e:
        print(f"❌ Error retrieving runtime: {str(e)}")
        
        if hasattr(e, 'status'):
            if e.status == 403:
                print("\n   Permission denied (403)")
                print("   • Check if your account can read runtime details")
                print("   • Verify you have access to this specific runtime")
            elif e.status == 404:
                print("\n   Not found (404)")
                print("   • The runtime ID may not exist")
                print("   • Check the runtime ID format (should be a UUID)")
            elif e.status == 400:
                print("\n   Bad request (400)")
                print("   • Verify the runtime ID is in the correct format")
        
        return None

def format_date(date_string):
    """Format ISO date string to readable format."""
    try:
        if date_string:
            dt = datetime.fromisoformat(date_string.replace('Z', '+00:00'))
            return dt.strftime('%Y-%m-%d %H:%M:%S UTC')
    except:
        pass
    return date_string or 'N/A'

def display_runtime_details(runtime_data):
    """Display runtime information in a comprehensive format."""
    
    print("\n📋 Runtime Details:")
    print("=" * 70)
    
    # Basic information
    runtime_id = runtime_data.get('@id', 'N/A')
    runtime_name = runtime_data.get('@name', 'N/A')
    runtime_type = runtime_data.get('@type', 'N/A')
    runtime_status = runtime_data.get('@status', 'N/A')
    
    # Status icon
    if runtime_status == 'ONLINE':
        status_icon = "🟢"
    elif runtime_status == 'OFFLINE':
        status_icon = "🔴"
    else:
        status_icon = "⚪"
    
    print(f"🤖 Name: {runtime_name}")
    print(f"🆔 ID: {runtime_id}")
    print(f"📦 Type: {runtime_type}")
    print(f"{status_icon} Status: {runtime_status}")
    print()
    
    # Host and version information
    print("🖥️  Host Information:")
    print(f"   Hostname: {runtime_data.get('@hostName', 'N/A')}")
    print(f"   Current Version: {runtime_data.get('@currentVersion', 'N/A')}")
    print(f"   Build Number: {runtime_data.get('@buildNumber', 'N/A')}")
    print()
    
    # Installation details
    print("📅 Installation Details:")
    print(f"   Date Installed: {format_date(runtime_data.get('@dateInstalled'))}")
    print(f"   Last Modified: {format_date(runtime_data.get('@lastModifiedDate'))}")
    print(f"   Created By: {runtime_data.get('@createdBy', 'N/A')}")
    print()
    
    # Capabilities
    capabilities = runtime_data.get('@capabilities', [])
    if capabilities:
        print("🔧 Capabilities:")
        for cap in capabilities:
            print(f"   • {cap}")
        print()
    
    # Cloud information
    cloud_id = runtime_data.get('@cloudId', None)
    if cloud_id:
        print("☁️  Cloud Information:")
        print(f"   Cloud ID: {cloud_id}")
        print(f"   Cloud URL: {runtime_data.get('@url', 'N/A')}")
        print()
    
    # Container information
    container_id = runtime_data.get('@containerId', None)
    if container_id:
        print("📦 Container Information:")
        print(f"   Container ID: {container_id}")
        print()
    
    # Network information
    print("🌐 Network Configuration:")
    print(f"   Public IP Address: {runtime_data.get('@publicIpAddress', 'N/A')}")
    print(f"   Network Addresses: {runtime_data.get('@networkAddresses', 'N/A')}")
    print()
    
    # Environment associations
    env_count = runtime_data.get('@environmentCount', 0)
    if env_count:
        print(f"🌍 Environment Attachments: {env_count}")
        print("   Use query_environment_atom_attachments.py to see details")
        print()
    
    # Additional properties
    print("🔍 Additional Properties:")
    print(f"   Purge Immediately: {runtime_data.get('@purgeImmediately', False)}")
    print(f"   Force Restart: {runtime_data.get('@forceRestart', False)}")
    print(f"   Offline Reason: {runtime_data.get('@offlineReason', 'N/A')}")
    
    # Check for any additional fields not displayed
    known_fields = {
        '@id', '@name', '@type', '@status', '@hostName', '@currentVersion',
        '@buildNumber', '@dateInstalled', '@lastModifiedDate', '@createdBy',
        '@capabilities', '@cloudId', '@url', '@containerId', '@publicIpAddress',
        '@networkAddresses', '@environmentCount', '@purgeImmediately',
        '@forceRestart', '@offlineReason'
    }
    
    additional_fields = set(runtime_data.keys()) - known_fields
    if additional_fields:
        print(f"\n📎 Other Fields: {', '.join(additional_fields)}")

def get_sample_runtime_id(sdk):
    """Get a sample runtime ID for demonstration."""
    
    try:
        from boomi.models import (
            AtomQueryConfig,
            AtomQueryConfigQueryFilter,
            AtomSimpleExpression,
            AtomSimpleExpressionOperator,
            AtomSimpleExpressionProperty
        )
        
        # Query for any runtime
        simple_expression = AtomSimpleExpression(
            operator=AtomSimpleExpressionOperator.EQUALS,
            property=AtomSimpleExpressionProperty.TYPE,
            argument=["ATOM"]
        )
        
        query_filter = AtomQueryConfigQueryFilter(expression=simple_expression)
        query_config = AtomQueryConfig(query_filter=query_filter)
        
        result = sdk.atom.query_atom(query_config)
        
        # Use modern SDK response format
        if hasattr(result, 'result') and result.result:
            runtimes = result.result if isinstance(result.result, list) else [result.result]
            if runtimes:
                # Use object attributes instead of dict access
                first_runtime = runtimes[0]
                runtime_id = getattr(first_runtime, 'id_', 'N/A')
                runtime_name = getattr(first_runtime, 'name', 'N/A')
                return runtime_id, runtime_name
        
    except Exception as e:
        print(f"   Could not retrieve sample runtime: {str(e)}")
    
    return None, None

def main():
    """Main function to demonstrate runtime detail retrieval."""
    
    print("🚀 Boomi SDK - Get Runtime Details")
    print("=" * 50)
    
    # Check for required environment variables
    required_vars = ["BOOMI_ACCOUNT", "BOOMI_USER", "BOOMI_SECRET"]
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars:
        print("❌ Missing required environment variables:")
        for var in missing_vars:
            print(f"   - {var}")
        sys.exit(1)
    
    # Initialize the SDK
    sdk = Boomi(
        account_id=os.getenv("BOOMI_ACCOUNT"),
        username=os.getenv("BOOMI_USER"),
        password=os.getenv("BOOMI_SECRET"),
        timeout=30000,
    )
    
    print("✅ SDK initialized successfully!")
    print()
    
    try:
        # Get runtime ID from arguments or find a sample
        if len(sys.argv) > 1:
            runtime_id = sys.argv[1]
            print(f"📍 Using provided runtime ID: {runtime_id}")
        else:
            print("💡 Usage: python3 get_runtime.py <runtime_id>")
            print()
            print("   Looking for a sample runtime...")
            
            sample_id, sample_name = get_sample_runtime_id(sdk)
            if sample_id:
                print(f"   Found runtime: {sample_name}")
                runtime_id = input(f"   Use this runtime? (Y/n) or enter runtime ID: ").strip()
                
                if not runtime_id or runtime_id.lower() == 'y':
                    runtime_id = sample_id
                elif runtime_id.lower() == 'n':
                    runtime_id = input("Enter runtime ID: ").strip()
            else:
                print("   No runtimes found for demonstration")
                runtime_id = input("Enter runtime ID: ").strip()
            
            if not runtime_id:
                print("❌ No runtime ID provided")
                return
        
        print()
        
        # Retrieve runtime details
        runtime_data = get_runtime_details(sdk, runtime_id)
        
        if runtime_data:
            # Display comprehensive details
            display_runtime_details(runtime_data)
            
            print("\n💡 Use Cases:")
            print("   • Check runtime status before deploying processes")
            print("   • Verify runtime version compatibility")
            print("   • Monitor runtime health and connectivity")
            print("   • Troubleshoot offline runtimes")
            print("   • Audit runtime configurations")
            print()
            
            print("🔗 Related Examples:")
            print("   • list_runtimes.py - List all runtimes in the account")
            print("   • update_runtime.py - Update runtime configuration")
            print("   • get_runtime_status.py - Get detailed status information")
            print("   • delete_runtime.py - Remove a runtime from the account")
        
    except KeyboardInterrupt:
        print("\n❌ Operation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Example failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()