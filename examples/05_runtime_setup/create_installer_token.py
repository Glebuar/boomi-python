#!/usr/bin/env python3
"""
Boomi SDK Example: Create Installer Token
==========================================

This example demonstrates how to create installer tokens for new Boomi runtimes
using the Boomi SDK. Installer tokens are used to securely install new atoms,
molecules, or other runtime types on target machines.

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- Account must have appropriate permissions to create installer tokens
- Valid install type (ATOM, MOLECULE, CLOUD, BROKER, GATEWAY)

Usage:
    cd examples/runtime_management
    PYTHONPATH=../../src python3 create_installer_token.py [install_type] [duration_minutes]

Features:
- Creates installer tokens for different runtime types
- Configurable token expiration time (30-1440 minutes)
- Shows token details and usage instructions
- Validates input parameters and handles errors
- Supports all runtime types: ATOM, MOLECULE, CLOUD, BROKER, GATEWAY

Example:
    python3 create_installer_token.py ATOM 60
    
This creates a token for installing a new ATOM that expires in 60 minutes.
"""

import os
import sys
from datetime import datetime, timedelta
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
from boomi.models import InstallerToken, InstallType

def get_install_type_from_input(install_type_str):
    """Convert string input to InstallType enum."""
    
    install_type_str = install_type_str.upper()
    
    # Map common variations
    type_mapping = {
        'ATOM': InstallType.ATOM,
        'MOLECULE': InstallType.MOLECULE, 
        'CLOUD': InstallType.CLOUD,
        'BROKER': InstallType.BROKER,
        'GATEWAY': InstallType.GATEWAY,
        'MOL': InstallType.MOLECULE,  # Common abbreviation
        'GW': InstallType.GATEWAY     # Common abbreviation
    }
    
    if install_type_str in type_mapping:
        return type_mapping[install_type_str]
    
    return None

def validate_duration_minutes(duration):
    """Validate duration is within allowed range (30-1440 minutes)."""
    
    try:
        duration_int = int(duration)
        if 30 <= duration_int <= 1440:
            return duration_int
        else:
            print(f"❌ Duration must be between 30 and 1440 minutes (got {duration_int})")
            print("   • 30 minutes = minimum")
            print("   • 1440 minutes = 24 hours maximum")
            return None
    except ValueError:
        print(f"❌ Invalid duration: '{duration}' (must be a number)")
        return None

def create_installer_token(sdk, install_type, duration_minutes):
    """Create an installer token for the specified runtime type and duration."""
    
    print(f"🔧 Creating installer token...")
    print(f"   Runtime Type: {install_type.value}")
    print(f"   Duration: {duration_minutes} minutes")
    
    try:
        # Create the installer token request
        token_request = InstallerToken(
            install_type=install_type,
            duration_minutes=duration_minutes
        )
        
        # Call the API to create the token
        result = sdk.installer_token.create_installer_token(token_request)
        
        print("✅ Installer token created successfully!")
        
        # Parse the response - use modern SDK response format
        if hasattr(result, 'token'):
            # Direct object access (modern SDK format)
            display_token_details(result)
            show_installation_instructions(result)
            return result
        elif hasattr(result, '_kwargs') and 'InstallerToken' in result._kwargs:
            token_data = result._kwargs['InstallerToken']
            display_token_details(token_data)
            show_installation_instructions(token_data)
            return token_data
        else:
            print("⚠️  Unexpected response format")
            # Debug output
            if hasattr(result, '__dict__'):
                print(f"   Available attributes: {[attr for attr in dir(result) if not attr.startswith('_')]}")
            if hasattr(result, '_kwargs'):
                print(f"   Raw response: {result._kwargs}")
            return None
            
    except Exception as e:
        print(f"❌ Error creating installer token: {str(e)}")
        
        if hasattr(e, 'status'):
            if e.status == 403:
                print("\n   Permission denied (403):")
                print("   • Check if your account can create installer tokens")
                print("   • Verify you have Runtime Management privileges")
            elif e.status == 400:
                print("\n   Bad request (400):")
                print("   • Check the install type and duration parameters")
                print("   • Duration must be between 30-1440 minutes")
        
        return None

def display_token_details(token_data):
    """Display the created token details."""
    
    print("\n📋 Installer Token Details:")
    print("=" * 60)
    
    # Handle both dict and object formats
    if hasattr(token_data, 'token'):
        token = getattr(token_data, 'token', 'N/A')
        install_type = getattr(token_data, 'install_type', 'N/A')
        account_id = getattr(token_data, 'account_id', 'N/A')
        created = getattr(token_data, 'created', 'N/A')
        expiration = getattr(token_data, 'expiration', 'N/A')
        duration_minutes = getattr(token_data, 'duration_minutes', 'N/A')
    else:
        token = token_data.get('@token', token_data.get('token', 'N/A'))
        install_type = token_data.get('@installType', token_data.get('installType', 'N/A'))
        account_id = token_data.get('@accountId', token_data.get('accountId', 'N/A'))
        created = token_data.get('@created', token_data.get('created', 'N/A'))
        expiration = token_data.get('@expiration', token_data.get('expiration', 'N/A'))
        duration_minutes = token_data.get('durationMinutes', 'N/A')
    
    print(f"🎫 Token: {token}")
    print(f"🤖 Runtime Type: {install_type}")
    print(f"🏢 Account ID: {account_id}")
    print(f"📅 Created: {created}")
    print(f"⏰ Expires: {expiration}")
    
    if duration_minutes != 'N/A':
        hours = duration_minutes // 60
        minutes = duration_minutes % 60
        if hours > 0:
            print(f"⏳ Valid for: {duration_minutes} minutes ({hours}h {minutes}m)")
        else:
            print(f"⏳ Valid for: {duration_minutes} minutes")

def show_installation_instructions(token_data):
    """Show instructions for using the installer token."""
    
    print("\n💡 Installation Instructions:")
    print("=" * 60)
    
    # Get token value
    if hasattr(token_data, 'token'):
        token = getattr(token_data, 'token', 'N/A')
        install_type = getattr(token_data, 'install_type', 'N/A')
    else:
        token = token_data.get('@token', token_data.get('token', 'N/A'))
        install_type = token_data.get('@installType', token_data.get('installType', 'N/A'))
    
    print("1. Download the Boomi installer from the Boomi platform")
    print("2. Run the installer on your target machine")
    print("3. When prompted for the installer token, use:")
    print(f"   📋 {token}")
    print("4. Complete the installation following the setup wizard")
    
    print(f"\n🔧 Runtime Type Specific Notes:")
    if install_type == 'ATOM':
        print("   • ATOM: Lightweight runtime for simple integrations")
        print("   • Recommended for: Development, testing, small deployments")
        print("   • Resources: Low memory and CPU requirements")
    elif install_type == 'MOLECULE':
        print("   • MOLECULE: Clustered runtime for high availability")
        print("   • Recommended for: Production, high-volume integrations")
        print("   • Resources: Higher memory and CPU requirements")
    elif install_type == 'CLOUD':
        print("   • CLOUD: Boomi-managed runtime in the cloud")
        print("   • Recommended for: Quick start, no infrastructure management")
        print("   • Resources: Managed by Boomi")
    elif install_type == 'GATEWAY':
        print("   • GATEWAY: API Gateway runtime for API management")
        print("   • Recommended for: API publishing and management")
        print("   • Resources: Moderate memory and CPU requirements")
    elif install_type == 'BROKER':
        print("   • BROKER: Message broker runtime for event-driven integration")
        print("   • Recommended for: Event streaming, message queuing")
        print("   • Resources: Variable based on message volume")
    
    print("\n⚠️  Important:")
    print("   • The token expires after the specified duration")
    print("   • Use the token before it expires")
    print("   • Each token can only be used once")
    print("   • Keep the token secure during installation")

def show_available_types():
    """Display available runtime install types."""
    
    print("\n🤖 Available Runtime Types:")
    print("=" * 40)
    print("• ATOM     - Lightweight runtime")
    print("• MOLECULE - Clustered runtime")  
    print("• CLOUD    - Cloud-managed runtime")
    print("• GATEWAY  - API Gateway runtime")
    print("• BROKER   - Message broker runtime")

def demonstrate_programmatic_usage():
    """Show example of programmatic token creation."""
    
    print("\n📚 Programmatic Usage Example:")
    print("=" * 60)
    print("To create installer tokens programmatically:")
    print("""
    from boomi.models import InstallerToken, InstallType
    
    # Create token for ATOM runtime valid for 2 hours
    token_request = InstallerToken(
        install_type=InstallType.ATOM,
        duration_minutes=120  # 2 hours
    )
    
    # Create the token
    result = sdk.installer_token.create_installer_token(token_request)
    
    # Use the token for installation
    token_value = result.token
    expiration = result.expiration
    """)

def main():
    """Main function to demonstrate installer token creation."""
    
    print("🚀 Boomi SDK - Create Installer Token")
    print("=" * 50)
    
    # Check for required environment variables
    required_vars = ["BOOMI_ACCOUNT", "BOOMI_USER", "BOOMI_SECRET"]
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars:
        print("❌ Missing required environment variables:")
        for var in missing_vars:
            print(f"   - {var}")
        print("\nPlease set these variables in your environment")
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
        install_type = None
        duration_minutes = None
        
        # Parse command line arguments
        if len(sys.argv) >= 3:
            install_type_str = sys.argv[1]
            duration_str = sys.argv[2]
            
            install_type = get_install_type_from_input(install_type_str)
            if not install_type:
                print(f"❌ Invalid install type: '{install_type_str}'")
                show_available_types()
                return
            
            duration_minutes = validate_duration_minutes(duration_str)
            if duration_minutes is None:
                return
                
            print(f"📍 Using provided parameters:")
            print(f"   Runtime Type: {install_type.value}")
            print(f"   Duration: {duration_minutes} minutes")
            
        else:
            # Interactive mode
            print("💡 Usage: python3 create_installer_token.py <install_type> <duration_minutes>")
            print()
            show_available_types()
            print()
            
            # Get install type
            while not install_type:
                install_type_input = input("Enter runtime type (ATOM/MOLECULE/CLOUD/GATEWAY/BROKER): ").strip()
                if not install_type_input:
                    print("❌ Install type is required")
                    continue
                    
                install_type = get_install_type_from_input(install_type_input)
                if not install_type:
                    print(f"❌ Invalid install type: '{install_type_input}'")
                    show_available_types()
            
            # Get duration
            while duration_minutes is None:
                duration_input = input("Enter token duration in minutes (30-1440): ").strip()
                if not duration_input:
                    print("❌ Duration is required")
                    continue
                    
                duration_minutes = validate_duration_minutes(duration_input)
        
        print()
        
        # Create the installer token
        token_data = create_installer_token(sdk, install_type, duration_minutes)
        
        if token_data:
            # Show programmatic example
            demonstrate_programmatic_usage()
            
            print("\n🎉 Token creation completed successfully!")
            print("\n💡 Next steps:")
            print("   • Download the Boomi installer")
            print("   • Run installer on target machine")
            print("   • Use the token when prompted")
            print("   • Complete the runtime setup")
        
    except KeyboardInterrupt:
        print("\n❌ Operation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Example failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()