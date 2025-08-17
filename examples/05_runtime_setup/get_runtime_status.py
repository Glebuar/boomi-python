#!/usr/bin/env python3
"""
Boomi SDK Example: Get Runtime Status and Details
==============================================

This example demonstrates how to retrieve runtime (runtime) status and detailed
information using the Boomi SDK. It shows how to check runtime health, status,
and operational details.

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- Account must have appropriate permissions to read runtimes
- Need a valid runtime ID to check status

Usage:
    cd examples/runtime_management
    PYTHONPATH=../../src python3 get_runtime_status.py [runtime_id]

Features:
- Retrieves comprehensive runtime status information
- Shows operational details (online/offline, version, capabilities)
- Displays connectivity and performance metrics
- Monitors runtime health indicators
- Provides restart functionality using RuntimeRestartRequest service

Note: This example uses the standard Runtime GET endpoint to retrieve status
information. The runtime status is part of the runtime object data.
"""

import os
import sys
from datetime import datetime

# Add the src directory to the path to import the SDK
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

from boomi import Boomi
from boomi.models import RuntimeRestartRequest

def get_runtime_status_info(sdk, runtime_id):
    """Get comprehensive runtime status information."""
    
    print(f"🔍 Retrieving runtime status information...")
    
    try:
        result = sdk.atom.get_atom(id_=runtime_id)
        
        if hasattr(result, '_kwargs') and 'Atom' in result._kwargs:
            return result._kwargs['Atom']
        elif hasattr(result, '_kwargs'):
            return result._kwargs
        
        return None
        
    except Exception as e:
        print(f"❌ Error retrieving runtime status: {str(e)}")
        
        if hasattr(e, 'status'):
            if e.status == 403:
                print("\\n   Permission denied (403)")
                print("   • Check if you have Runtime Management privilege")
            elif e.status == 404:
                print("\\n   Not found (404)")
                print("   • The runtime ID may not exist")
                print("   • Verify the runtime ID is correct")
        
        return None

def display_status_summary(runtime_data):
    """Display runtime status summary."""
    
    runtime_name = runtime_data.get('@name', 'N/A')
    runtime_id = runtime_data.get('@id', 'N/A')
    runtime_status = runtime_data.get('@status', 'N/A')
    runtime_type = runtime_data.get('@type', 'N/A')
    
    print(f"\\n🤖 Runtime Status Summary")
    print("=" * 70)
    print(f"📛 Name: {runtime_name}")
    print(f"🆔 ID: {runtime_id}")
    print(f"📦 Type: {runtime_type}")
    
    # Status with icon
    if runtime_status == 'ONLINE':
        status_icon = "🟢"
        status_msg = "Runtime is online and ready to process"
    elif runtime_status == 'OFFLINE':
        status_icon = "🔴"
        status_msg = "Runtime is offline and cannot process"
    elif runtime_status == 'STARTING':
        status_icon = "🟡"
        status_msg = "Runtime is starting up"
    elif runtime_status == 'STOPPING':
        status_icon = "🟠"
        status_msg = "Runtime is shutting down"
    elif runtime_status == 'ERROR':
        status_icon = "❌"
        status_msg = "Runtime has encountered an error"
    else:
        status_icon = "⚪"
        status_msg = f"Runtime status: {runtime_status}"
    
    print(f"{status_icon} Status: {runtime_status}")
    print(f"💬 Message: {status_msg}")
    
    return runtime_status

def display_operational_details(runtime_data):
    """Display detailed operational information."""
    
    print("\\n🔧 Operational Details")
    print("=" * 70)
    
    # System information
    runtime_hostname = runtime_data.get('@hostName', 'N/A')
    runtime_version = runtime_data.get('@currentVersion', 'N/A')
    runtime_os = runtime_data.get('@osName', 'N/A')
    runtime_java = runtime_data.get('@javaVersion', 'N/A')
    
    print(f"🖥️  Hostname: {runtime_hostname}")
    print(f"📦 Version: {runtime_version}")
    print(f"🏗️  Operating System: {runtime_os}")
    print(f"☕ Java Version: {runtime_java}")
    
    # Installation details
    date_installed = runtime_data.get('@dateInstalled', 'N/A')
    created_by = runtime_data.get('@createdBy', 'N/A')
    last_modified = runtime_data.get('@lastModifiedDate', 'N/A')
    
    print(f"\\n📅 Installation Details")
    print(f"   📅 Installed: {format_date(date_installed)}")
    print(f"   👤 Created by: {created_by}")
    print(f"   🔄 Last modified: {format_date(last_modified)}")

def display_connectivity_info(runtime_data):
    """Display connectivity and networking information."""
    
    print("\\n🌐 Connectivity Information")
    print("=" * 70)
    
    # Network details
    runtime_url = runtime_data.get('@atomUrl', 'N/A')
    purge_immediate = runtime_data.get('@purgeImmediately', False)
    force_restart = runtime_data.get('@forceRestart', False)
    
    print(f"🔗 Runtime URL: {runtime_url}")
    print(f"🗑️  Purge Immediately: {purge_immediate}")
    print(f"🔄 Force Restart: {force_restart}")
    
    # Capabilities
    capabilities = runtime_data.get('@capabilities', [])
    if capabilities:
        print(f"\\n🔧 Capabilities:")
        if isinstance(capabilities, list):
            for capability in capabilities:
                print(f"   • {capability}")
        else:
            print(f"   • {capabilities}")
    else:
        print(f"\\n🔧 Capabilities: None specified")

def display_performance_metrics(runtime_data):
    """Display performance and resource information."""
    
    print("\\n📊 Performance Metrics")
    print("=" * 70)
    
    # Memory and resource usage (if available)
    max_memory = runtime_data.get('@maxMemory', 'N/A')
    used_memory = runtime_data.get('@usedMemory', 'N/A')
    free_memory = runtime_data.get('@freeMemory', 'N/A')
    
    if max_memory != 'N/A':
        print(f"💾 Memory - Max: {max_memory}MB, Used: {used_memory}MB, Free: {free_memory}MB")
    else:
        print(f"💾 Memory information: Not available")
    
    # Process counts (if available)
    active_processes = runtime_data.get('@activeProcesses', 'N/A')
    queued_processes = runtime_data.get('@queuedProcesses', 'N/A')
    
    if active_processes != 'N/A':
        print(f"⚙️  Processes - Active: {active_processes}, Queued: {queued_processes}")
    else:
        print(f"⚙️  Process information: Not available")

def check_runtime_health(runtime_status, runtime_data):
    """Analyze runtime health and provide recommendations."""
    
    print("\\n🩺 Health Analysis")
    print("=" * 70)
    
    health_issues = []
    recommendations = []
    
    # Check status
    if runtime_status == 'OFFLINE':
        health_issues.append("Runtime is offline")
        recommendations.append("Start the runtime to enable process execution")
    elif runtime_status == 'ERROR':
        health_issues.append("Runtime is in error state")
        recommendations.append("Check runtime logs and consider restarting")
    elif runtime_status == 'STARTING':
        health_issues.append("Runtime is still starting")
        recommendations.append("Wait for startup to complete")
    elif runtime_status == 'STOPPING':
        health_issues.append("Runtime is shutting down")
        recommendations.append("Wait for shutdown to complete or restart if needed")
    
    # Check version (basic check)
    version = runtime_data.get('@currentVersion', '')
    if version and 'SNAPSHOT' in version:
        health_issues.append("Running development/snapshot version")
        recommendations.append("Consider using a stable release version for production")
    
    # Check last modified date
    last_modified = runtime_data.get('@lastModifiedDate', '')
    if last_modified:
        try:
            dt = datetime.fromisoformat(last_modified.replace('Z', '+00:00'))
            days_old = (datetime.now(dt.tzinfo) - dt).days
            if days_old > 30:
                health_issues.append(f"Configuration last modified {days_old} days ago")
                recommendations.append("Review runtime configuration for updates")
        except:
            pass
    
    # Display results
    if health_issues:
        print("⚠️  Health Issues Found:")
        for issue in health_issues:
            print(f"   • {issue}")
        print("\\n💡 Recommendations:")
        for rec in recommendations:
            print(f"   • {rec}")
    else:
        print("✅ No major health issues detected")
        print("\\n💡 General Tips:")
        print("   • Monitor runtime status regularly")
        print("   • Keep runtime version updated")
        print("   • Check logs for any error messages")

def restart_runtime_option(sdk, runtime_id):
    """Offer runtime restart functionality."""
    
    print("\\n🔄 Restart Options")
    print("=" * 70)
    print("Would you like to restart this runtime?")
    print("⚠️  Note: Restarting will interrupt any running processes")
    
    restart = input("\\nRestart runtime? (y/N): ").strip().lower()
    if restart == 'y':
        try:
            restart_request = RuntimeRestartRequest(runtime_id=runtime_id)
            result = sdk.runtime_restart_request.create_runtime_restart_request(restart_request)
            
            if hasattr(result, '_kwargs'):
                response_data = result._kwargs
                status_code = response_data.get('@statusCode', 'N/A')
                message = response_data.get('@message', 'No message')
                print(f"\\n✅ Restart request submitted!")
                print(f"📋 Status Code: {status_code}")
                print(f"💬 Message: {message}")
                print("\\n💡 Note: Use this script again to check if restart completed")
            else:
                print(f"\\n✅ Restart request submitted successfully!")
                
        except Exception as e:
            print(f"\\n❌ Error restarting runtime: {str(e)}")
            if hasattr(e, 'status'):
                if e.status == 403:
                    print("   • Check if you have Runtime Management privilege")
    else:
        print("❌ Restart cancelled")

def format_date(date_string):
    """Format ISO date string to readable format."""
    try:
        if date_string and date_string != 'N/A':
            dt = datetime.fromisoformat(date_string.replace('Z', '+00:00'))
            return dt.strftime('%Y-%m-%d %H:%M:%S UTC')
    except:
        pass
    return date_string or 'N/A'

def main():
    """Main function to demonstrate runtime status checking."""
    
    print("🚀 Boomi SDK - Get Runtime Status and Details")
    print("=" * 60)
    
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
        # Get runtime ID from arguments or prompt user
        if len(sys.argv) > 1:
            runtime_id = sys.argv[1]
            print(f"📍 Using provided runtime ID: {runtime_id}")
        else:
            print("💡 Usage: python3 get_runtime_status.py <runtime_id>")
            print()
            print("   You can find runtime IDs using list_runtimes.py")
            runtime_id = input("Enter runtime ID to check status: ").strip()
            
            if not runtime_id:
                print("❌ No runtime ID provided")
                return
        
        print()
        
        # Get runtime status information
        runtime_data = get_runtime_status_info(sdk, runtime_id)
        if not runtime_data:
            print("❌ Could not retrieve runtime status information")
            return
        
        # Display comprehensive status information
        runtime_status = display_status_summary(runtime_data)
        display_operational_details(runtime_data)
        display_connectivity_info(runtime_data)
        display_performance_metrics(runtime_data)
        check_runtime_health(runtime_status, runtime_data)
        
        # Offer restart option if runtime has issues
        if runtime_status in ['OFFLINE', 'ERROR', 'STOPPING']:
            restart_runtime_option(sdk, runtime_id)
        
        print("\\n🎯 Status Check Complete!")
        print("\\n💡 Next Steps:")
        print("   • Monitor runtime status regularly")
        print("   • Check runtime logs if issues are found")
        print("   • Update runtime version if outdated")
        print("   • Verify environment attachments are working")
        
    except KeyboardInterrupt:
        print("\\n❌ Operation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Example failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()