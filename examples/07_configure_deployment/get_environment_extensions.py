#!/usr/bin/env python3
"""
Boomi SDK Example: Get Environment Extensions
=============================================

This example demonstrates how to retrieve environment extension values using
the Boomi SDK. Extensions include connections, properties, cross-references,
trading partners, and other environment-specific configurations.

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- Account must have appropriate permissions to read environment extensions
- Need a valid environment ID to retrieve extensions for

Usage:
    cd examples/environment_management
    PYTHONPATH=../../src python3 get_environment_extensions.py [environment_id]

Features:
- Retrieves all extension values for a specified environment
- Displays connections, properties, cross-references, trading partners
- Shows both plain text and encrypted field values
- Handles different extension types and their configurations
"""

import os
import sys

# Add the src directory to the path to import the SDK
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

from boomi import Boomi

def get_environment_extensions(sdk, environment_id):
    """Retrieve environment extension values."""
    
    print(f"🔍 Retrieving environment extensions...")
    print(f"   Environment ID: {environment_id}")
    
    try:
        # Call the get environment extensions API
        result = sdk.environment_extensions.get_environment_extensions(id_=environment_id)
        
        print("✅ Environment extensions retrieved successfully!")
        
        # Parse the response
        extensions_data = None
        if hasattr(result, '_kwargs') and 'EnvironmentExtensions' in result._kwargs:
            extensions_data = result._kwargs['EnvironmentExtensions']
        elif hasattr(result, '_kwargs'):
            # Response might be directly the extensions data
            extensions_data = result._kwargs
        
        if not extensions_data:
            print("   No extension data found in response")
            if hasattr(result, '_kwargs'):
                print(f"   Response keys: {list(result._kwargs.keys())}")
            return None
        
        return extensions_data
        
    except Exception as e:
        print(f"❌ Error retrieving environment extensions: {str(e)}")
        
        if hasattr(e, 'status'):
            if e.status == 403:
                print("\n   Permission denied (403)")
                print("   • Check if your account can read environment extensions")
            elif e.status == 404:
                print("\n   Not found (404)")
                print("   • The environment ID may not exist")
                print("   • Check the environment ID format")
            elif e.status == 400:
                print("\n   Bad request (400)")
                print("   • Verify the environment ID is valid")
        
        return None

def display_connections(connections_data):
    """Display connection configurations."""
    
    if not connections_data or 'connection' not in connections_data:
        print("   No connections configured")
        return
    
    connections = connections_data['connection']
    if not isinstance(connections, list):
        connections = [connections]
    
    print(f"   Found {len(connections)} connection(s):")
    print("   " + "─" * 60)
    
    for i, conn in enumerate(connections, 1):
        conn_id = conn.get('@id', 'N/A')
        conn_name = conn.get('@name', 'Unnamed Connection')
        
        print(f"   {i}. 🔌 {conn_name}")
        print(f"      ID: {conn_id}")
        
        # Display connection fields
        fields = conn.get('field', [])
        if not isinstance(fields, list):
            fields = [fields]
        
        if fields:
            print(f"      Fields: {len(fields)}")
            for field in fields[:3]:  # Show first 3 fields to avoid clutter
                field_id = field.get('@id', 'N/A')
                field_value = field.get('@value', '')
                encrypted = field.get('@usesEncryption', False)
                
                if encrypted:
                    display_value = "[ENCRYPTED]" if field.get('@encryptedValueSet') else "[NOT SET]"
                else:
                    display_value = field_value or "[EMPTY]"
                
                print(f"        • {field_id}: {display_value}")
            
            if len(fields) > 3:
                print(f"        ... and {len(fields) - 3} more fields")
        
        print()

def display_properties(properties_data):
    """Display dynamic properties."""
    
    if not properties_data or 'property' not in properties_data:
        print("   No properties configured")
        return
    
    properties = properties_data['property']
    if not isinstance(properties, list):
        properties = [properties]
    
    print(f"   Found {len(properties)} property/ies:")
    print("   " + "─" * 60)
    
    for i, prop in enumerate(properties, 1):
        prop_name = prop.get('@name', 'Unnamed Property')
        prop_value = prop.get('@value', '[EMPTY]')
        
        print(f"   {i}. 📋 {prop_name}: {prop_value}")

def display_cross_references(cross_refs_data):
    """Display cross-reference tables."""
    
    if not cross_refs_data or 'crossReference' not in cross_refs_data:
        print("   No cross-references configured")
        return
    
    cross_refs = cross_refs_data['crossReference']
    if not isinstance(cross_refs, list):
        cross_refs = [cross_refs]
    
    print(f"   Found {len(cross_refs)} cross-reference(s):")
    print("   " + "─" * 60)
    
    for i, xref in enumerate(cross_refs, 1):
        xref_id = xref.get('@id', 'N/A')
        xref_name = xref.get('@name', 'Unnamed Cross Reference')
        override_values = xref.get('@overrideValues', False)
        
        print(f"   {i}. 📊 {xref_name}")
        print(f"      ID: {xref_id}")
        print(f"      Override Values: {override_values}")
        
        # Check for rows
        rows_data = xref.get('CrossReferenceRows', {})
        if 'row' in rows_data:
            rows = rows_data['row']
            if not isinstance(rows, list):
                rows = [rows]
            print(f"      Rows: {len(rows)}")
        else:
            print("      Rows: 0")
        
        print()

def display_trading_partners(partners_data):
    """Display trading partner configurations."""
    
    if not partners_data or 'tradingPartner' not in partners_data:
        print("   No trading partners configured")
        return
    
    partners = partners_data['tradingPartner']
    if not isinstance(partners, list):
        partners = [partners]
    
    print(f"   Found {len(partners)} trading partner(s):")
    print("   " + "─" * 60)
    
    for i, partner in enumerate(partners, 1):
        partner_id = partner.get('@id', 'N/A')
        partner_name = partner.get('@name', 'Unnamed Partner')
        
        print(f"   {i}. 🤝 {partner_name}")
        print(f"      ID: {partner_id}")
        
        # Check for categories
        categories = partner.get('category', [])
        if not isinstance(categories, list):
            categories = [categories]
        
        if categories:
            print(f"      Categories: {len(categories)}")
            for cat in categories[:2]:  # Show first 2 categories
                cat_name = cat.get('@name', 'Unnamed Category')
                print(f"        • {cat_name}")
        
        print()

def display_extensions_summary(extensions_data):
    """Display a comprehensive summary of all extension types."""
    
    print("\n📋 Environment Extensions Summary:")
    print("=" * 70)
    
    # Basic information
    env_id = extensions_data.get('@environmentId', 'N/A')
    ext_group_id = extensions_data.get('@extensionGroupId', 'N/A')
    
    print(f"Environment ID: {env_id}")
    print(f"Extension Group ID: {ext_group_id}")
    print()
    
    # Connections
    if 'connections' in extensions_data:
        print("🔌 CONNECTIONS:")
        display_connections(extensions_data['connections'])
        print()
    
    # Properties
    if 'properties' in extensions_data:
        print("📋 PROPERTIES:")
        display_properties(extensions_data['properties'])
        print()
    
    # Cross References
    if 'crossReferences' in extensions_data:
        print("📊 CROSS REFERENCES:")
        display_cross_references(extensions_data['crossReferences'])
        print()
    
    # Trading Partners
    if 'tradingPartners' in extensions_data:
        print("🤝 TRADING PARTNERS:")
        display_trading_partners(extensions_data['tradingPartners'])
        print()
    
    # Process Properties
    if 'processProperties' in extensions_data:
        proc_props = extensions_data['processProperties']
        if 'ProcessProperty' in proc_props:
            properties = proc_props['ProcessProperty']
            if not isinstance(properties, list):
                properties = [properties]
            print(f"⚙️  PROCESS PROPERTIES: {len(properties)} configured")
            print()
    
    # PGP Certificates
    if 'PGPCertificates' in extensions_data:
        pgp_certs = extensions_data['PGPCertificates']
        if 'PGPCertificate' in pgp_certs:
            certificates = pgp_certs['PGPCertificate']
            if not isinstance(certificates, list):
                certificates = [certificates]
            print(f"🔐 PGP CERTIFICATES: {len(certificates)} configured")
            print()

def main():
    """Main function to demonstrate environment extensions retrieval."""
    
    print("🚀 Boomi SDK - Get Environment Extensions")
    print("=" * 55)
    
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
            print("💡 Usage: python3 get_environment_extensions.py <environment_id>")
            print()
            print("   You can find environment IDs using list_environments.py")
            environment_id = input("Enter environment ID: ").strip()
            
            if not environment_id:
                print("❌ No environment ID provided")
                return
        
        print()
        
        # Retrieve environment extensions
        extensions_data = get_environment_extensions(sdk, environment_id)
        
        if extensions_data:
            # Display comprehensive summary
            display_extensions_summary(extensions_data)
            
            print("💡 Use Cases for Environment Extensions:")
            print("   • Configure connection parameters for different environments")
            print("   • Set environment-specific properties and variables")
            print("   • Manage trading partner configurations")
            print("   • Override cross-reference table values")
            print("   • Configure environment-specific security certificates")
        
    except KeyboardInterrupt:
        print("\n❌ Operation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Example failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()