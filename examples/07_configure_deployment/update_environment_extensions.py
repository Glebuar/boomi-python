#!/usr/bin/env python3
"""
Boomi SDK Example: Update Environment Extensions
================================================

This example demonstrates how to update environment extension values using
the Boomi SDK. Extensions include connections, properties, cross-references,
trading partners, and other environment-specific configurations.

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- Account must have appropriate permissions to modify environment extensions
- Need a valid environment ID to update extensions for

Usage:
    cd examples/environment_management
    PYTHONPATH=../../src python3 update_environment_extensions.py [environment_id]

Features:
- Updates environment extension values (connections, properties, etc.)
- Supports both partial and full updates of extension configurations
- Handles encrypted field values securely
- Demonstrates proper extension data structure for updates
"""

import os
import sys

# Add the src directory to the path to import the SDK
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

from boomi import Boomi

def create_sample_extension_update():
    """Create a sample extension update payload."""
    
    # Sample extension update - this would be customized based on actual needs
    # The structure should match the EnvironmentExtensions model from the OpenAPI spec
    
    extension_update = {
        "@type": "EnvironmentExtensions",
        "connections": {
            "@type": "Connections",
            "connection": [
                {
                    "@type": "Connection",
                    "@id": "sample-connection-id",
                    "@name": "Updated Test Connection", 
                    "field": [
                        {
                            "@type": "Field",
                            "@id": "host",
                            "@value": "updated-host.example.com",
                            "@encryptedValueSet": False,
                            "@usesEncryption": False,
                            "@componentOverride": False,
                            "@useDefault": False
                        },
                        {
                            "@type": "Field",
                            "@id": "port",
                            "@value": "8080",
                            "@encryptedValueSet": False,
                            "@usesEncryption": False,
                            "@componentOverride": False,
                            "@useDefault": False
                        }
                    ]
                }
            ]
        },
        "properties": {
            "@type": "",
            "property": [
                {
                    "@type": "",
                    "@name": "TestProperty",
                    "@value": "UpdatedValue"
                },
                {
                    "@type": "",
                    "@name": "Environment",
                    "@value": "Development"
                }
            ]
        }
    }
    
    return extension_update

def update_environment_extensions(sdk, environment_id, extension_data):
    """Update environment extension values."""
    
    print(f"📝 Updating environment extensions...")
    print(f"   Environment ID: {environment_id}")
    
    try:
        # Call the update environment extensions API
        # Note: The actual model class might need to be imported and used
        # This is a simplified approach showing the general pattern
        
        result = sdk.environment_extensions.update_environment_extensions(
            id_=environment_id,
            environment_extensions=extension_data
        )
        
        print("✅ Environment extensions updated successfully!")
        
        # Parse the response
        response_data = None
        if hasattr(result, '_kwargs'):
            response_data = result._kwargs
            print(f"   Response keys: {list(response_data.keys())}")
        
        return response_data
        
    except Exception as e:
        print(f"❌ Error updating environment extensions: {str(e)}")
        
        if hasattr(e, 'status'):
            if e.status == 403:
                print("\n   Permission denied (403)")
                print("   • Check if your account can modify environment extensions")
            elif e.status == 404:
                print("\n   Not found (404)")
                print("   • The environment ID may not exist")
                print("   • Check the environment ID format")
            elif e.status == 400:
                print("\n   Bad request (400)")
                print("   • Verify the extension data structure is correct")
                print("   • Check that all required fields are provided")
            elif e.status == 409:
                print("\n   Conflict (409)")
                print("   • There may be a conflict with existing configuration")
        
        return None

def demonstrate_connection_update_example():
    """Show an example of updating connection fields."""
    
    print("\n📋 Connection Update Example:")
    print("To update a connection field, you would structure the data like:")
    print("""
    {
        "connections": {
            "connection": [{
                "@id": "your-connection-id",
                "@name": "Connection Name",
                "field": [{
                    "@id": "field-name",
                    "@value": "new-value",
                    "@encryptedValueSet": false,
                    "@usesEncryption": false,
                    "@componentOverride": false,
                    "@useDefault": false
                }]
            }]
        }
    }
    """)

def demonstrate_properties_update_example():
    """Show an example of updating dynamic properties."""
    
    print("\n📋 Properties Update Example:")
    print("To update dynamic properties, you would structure the data like:")
    print("""
    {
        "properties": {
            "property": [{
                "@name": "PropertyName",
                "@value": "PropertyValue"
            }]
        }
    }
    """)

def demonstrate_cross_reference_update_example():
    """Show an example of updating cross-reference tables."""
    
    print("\n📋 Cross Reference Update Example:")
    print("To update cross-reference table data, you would structure like:")
    print("""
    {
        "crossReferences": {
            "crossReference": [{
                "@id": "cross-ref-id",
                "@name": "Cross Reference Name",
                "@overrideValues": true,
                "CrossReferenceRows": {
                    "row": [{
                        "@ref1": "value1",
                        "@ref2": "value2",
                        "@ref3": "value3"
                    }]
                }
            }]
        }
    }
    """)

def get_current_extensions_for_reference(sdk, environment_id):
    """Get current extensions to show what can be updated."""
    
    print(f"🔍 Getting current extensions for reference...")
    
    try:
        result = sdk.environment_extensions.get_environment_extensions(id_=environment_id)
        
        if hasattr(result, '_kwargs') and 'EnvironmentExtensions' in result._kwargs:
            extensions_data = result._kwargs['EnvironmentExtensions']
            
            print("✅ Current extension structure:")
            
            # Show what types of extensions exist
            extension_types = []
            if 'connections' in extensions_data:
                extension_types.append("Connections")
            if 'properties' in extensions_data:
                extension_types.append("Properties")
            if 'crossReferences' in extensions_data:
                extension_types.append("Cross References")
            if 'tradingPartners' in extensions_data:
                extension_types.append("Trading Partners")
            if 'processProperties' in extensions_data:
                extension_types.append("Process Properties")
            
            if extension_types:
                print(f"   Available extension types: {', '.join(extension_types)}")
            else:
                print("   No extensions currently configured")
            
            return extensions_data
        
    except Exception as e:
        print(f"   Could not retrieve current extensions: {str(e)}")
    
    return None

def main():
    """Main function to demonstrate environment extensions updating."""
    
    print("🚀 Boomi SDK - Update Environment Extensions")
    print("=" * 58)
    
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
        # Get environment ID from arguments or prompt user
        if len(sys.argv) > 1:
            environment_id = sys.argv[1]
            print(f"📍 Using provided environment ID: {environment_id}")
        else:
            print("💡 Usage: python3 update_environment_extensions.py <environment_id>")
            print()
            print("   You can find environment IDs using list_environments.py")
            environment_id = input("Enter environment ID: ").strip()
            
            if not environment_id:
                print("❌ No environment ID provided")
                return
        
        print()
        
        # Get current extensions for reference
        current_extensions = get_current_extensions_for_reference(sdk, environment_id)
        print()
        
        # Show examples of different update types
        print("📚 Environment Extension Update Examples:")
        print("=" * 60)
        
        demonstrate_connection_update_example()
        demonstrate_properties_update_example()
        demonstrate_cross_reference_update_example()
        
        print("\n⚠️  IMPORTANT NOTES:")
        print("   • Extension updates require the exact structure from the OpenAPI spec")
        print("   • You must import the proper model classes from boomi.models")
        print("   • Use get_environment_extensions.py to see current structure first")
        print("   • Updates can be partial (specific fields) or complete replacements")
        print("   • Encrypted fields require special handling for security")
        
        print("\n💡 Recommended workflow:")
        print("   1. Use get_environment_extensions.py to see current values")
        print("   2. Modify only the fields you need to change")
        print("   3. Preserve the exact JSON structure and field names")
        print("   4. Test updates in a development environment first")
        
        print("\n🔧 For actual implementation:")
        print("   • Import EnvironmentExtensions model from boomi.models")
        print("   • Structure your data according to the OpenAPI specification")
        print("   • Use the proper model objects instead of raw dictionaries")
        print("   • Handle encrypted fields with appropriate security measures")
        
        # Note: This example shows the pattern but doesn't perform actual updates
        # to avoid accidentally modifying production configurations
        print("\n✅ Example completed - no actual updates performed for safety")
        
    except KeyboardInterrupt:
        print("\n❌ Operation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Example failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()