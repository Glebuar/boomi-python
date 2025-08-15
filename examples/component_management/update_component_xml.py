#!/usr/bin/env python3
"""
Boomi SDK Example: Update Component using Raw XML
==================================================

This example demonstrates how to update Boomi components using the new raw XML
methods that preserve XML structure exactly. This approach works for both simple
and complex components without any XML round-trip issues.

Features:
- Gets component as raw XML (preserves all structure)
- Makes minimal edits using ElementTree
- Updates component with modified XML
- Works with complex nested structures

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- Or create a .env file with these variables

Usage:
    python update_component_xml.py COMPONENT_ID [OPTIONS]
    
    Arguments:
    COMPONENT_ID    The component ID to update
    
    Options:
    --name=NAME     New name for the component
    --desc=DESC     New description for the component
    
    Examples:
    python update_component_xml.py 112b4efe-b173-4258-9492-613ead7d52ce
    python update_component_xml.py f7f52a40-21fa-4850-a415-c88d69c8f5a2 --name="Updated Process"
"""

import os
import sys
from xml.etree import ElementTree as ET

# Add src to path for imports
sys.path.insert(0, '../../src')
from boomi import Boomi

# Load environment variables
try:
    from dotenv import load_dotenv
    load_dotenv('../../.env')
except ImportError:
    pass

def q(ns: str, local: str) -> str:
    """Create qualified name for XML elements with namespace."""
    return f"{{{ns}}}{local}"

def update_component_with_xml(component_id: str, new_name: str = None, new_description: str = None):
    """Update a component using raw XML methods that preserve structure."""
    
    # Check for required environment variables
    account_id = os.getenv("BOOMI_ACCOUNT")
    username = os.getenv("BOOMI_USER")
    password = os.getenv("BOOMI_SECRET")
    
    if not all([account_id, username, password]):
        print("❌ Error: Missing required environment variables")
        print("   Please set: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET")
        return False
    
    print(f"🚀 Boomi SDK - Raw XML Component Update")
    print("=" * 50)
    print(f"🏢 Account: {account_id}")
    print(f"👤 User: {username}")
    print(f"🎯 Component ID: {component_id}")
    
    # Initialize the Boomi SDK
    sdk = Boomi(
        account_id=account_id,
        username=username,
        password=password,
        timeout=30000
    )
    
    try:
        print(f"\n📥 Getting component as XML...")
        
        # Method 1: Get as ElementTree for DOM manipulation
        root = sdk.component.get_component_etree(component_id)
        
        # Extract namespace
        ns = "http://api.platform.boomi.com/"
        
        # Get current values
        original_name = root.get('name', 'Unknown')
        original_version = root.get('version', 'Unknown')
        folder_name = root.get('folderName', 'Unknown')
        
        print(f"✅ Component retrieved successfully!")
        print(f"   Original name: {original_name}")
        print(f"   Version: {original_version}")
        print(f"   Folder: {folder_name}")
        
        # Make changes
        changes_made = []
        
        if new_name:
            print(f"\n📝 Updating name to: {new_name}")
            root.set('name', new_name)
            changes_made.append(f"Name: {original_name} → {new_name}")
        
        if new_description:
            print(f"📝 Updating description to: {new_description}")
            # Find or create description element
            desc_elem = root.find(q(ns, 'description'))
            if desc_elem is None:
                # Create description element after encryptedValues
                encrypted_elem = root.find(q(ns, 'encryptedValues'))
                if encrypted_elem is not None:
                    idx = list(root).index(encrypted_elem) + 1
                    desc_elem = ET.Element(q(ns, 'description'))
                    root.insert(idx, desc_elem)
                else:
                    desc_elem = ET.SubElement(root, q(ns, 'description'))
            desc_elem.text = new_description
            changes_made.append(f"Description updated")
        
        if not changes_made:
            # If no specific changes requested, just update the name slightly
            new_name = f"XML Update Test - {original_name}"
            root.set('name', new_name)
            changes_made.append(f"Name: {original_name} → {new_name}")
        
        print(f"\n🔄 Sending update to API...")
        
        # Update using ElementTree method
        response = sdk.component.update_component_etree(component_id, root)
        
        print("✅ Component updated successfully!")
        
        # Parse response to show results
        response_root = ET.fromstring(response)
        updated_name = response_root.get('name', 'Unknown')
        updated_version = response_root.get('version', 'Unknown')
        updated_folder = response_root.get('folderName', 'Unknown')
        
        print(f"\n📊 Update Results:")
        print("=" * 50)
        print(f"  Updated Name: {updated_name}")
        print(f"  New Version: {updated_version}")
        print(f"  Folder (preserved): {updated_folder}")
        print(f"\n  Changes made:")
        for change in changes_made:
            print(f"    - {change}")
        
        print(f"\n🎉 SUCCESS! Component updated using raw XML methods")
        print(f"   This approach preserves XML structure exactly")
        print(f"   Works for both simple and complex components")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Update failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def parse_arguments():
    """Parse command line arguments."""
    if len(sys.argv) < 2:
        return None, None, None
    
    component_id = sys.argv[1]
    new_name = None
    new_description = None
    
    # Parse optional arguments
    for arg in sys.argv[2:]:
        if arg.startswith('--name='):
            new_name = arg.split('=', 1)[1]
        elif arg.startswith('--desc='):
            new_description = arg.split('=', 1)[1]
    
    return component_id, new_name, new_description

def main():
    """Main entry point."""
    component_id, new_name, new_description = parse_arguments()
    
    if not component_id:
        print("❌ Error: Component ID is required")
        print("\nUsage:")
        print(f"  {sys.argv[0]} COMPONENT_ID [OPTIONS]")
        print("\nOptions:")
        print("  --name=NAME     New name for the component")
        print("  --desc=DESC     New description for the component")
        print("\nExamples:")
        print(f"  {sys.argv[0]} 112b4efe-b173-4258-9492-613ead7d52ce")
        print(f"  {sys.argv[0]} f7f52a40-21fa-4850-a415-c88d69c8f5a2 --name=\"Updated Process\"")
        print(f"  {sys.argv[0]} component-id --name=\"New Name\" --desc=\"New description\"")
        return
    
    success = update_component_with_xml(component_id, new_name, new_description)
    
    if not success:
        print("\n💡 Tip: Make sure the component ID is valid and you have permissions")
        sys.exit(1)

if __name__ == "__main__":
    main()