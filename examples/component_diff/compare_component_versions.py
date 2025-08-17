#!/usr/bin/env python3
"""
Boomi SDK Example: Compare Component Versions

This example demonstrates how to compare different versions of a component using the
ComponentDiffRequest API. This helps you understand what changed between versions.

Features:
- Compare two specific versions of a component
- Shows detailed diff with additions, modifications, and deletions
- Handles various component types (process, connector, profile, etc.)
- Provides both XML and summary views of changes

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- Or create a .env file with these variables

Usage:
    python compare_component_versions.py COMPONENT_ID VERSION1 VERSION2
    
    Arguments:
    COMPONENT_ID     The component ID to compare versions for
    VERSION1         The first version to compare (older version)
    VERSION2         The second version to compare (newer version)
    
    Examples:
    python compare_component_versions.py 112b4efe-b173-4258-9492-613ead7d52ce 1 2
"""

import os
import sys
sys.path.insert(0, '../../src')
from boomi import Boomi

# Load environment variables
try:
    from dotenv import load_dotenv
    load_dotenv('../../.env')
except ImportError:
    pass

def format_date(date_str):
    """Format ISO date string to readable format"""
    if date_str and 'T' in date_str:
        return date_str.split('T')[0] + ' ' + date_str.split('T')[1].split('.')[0]
    return date_str or 'N/A'

def parse_diff_xml(diff_xml):
    """Parse diff XML and extract readable changes"""
    import xml.etree.ElementTree as ET
    
    try:
        root = ET.fromstring(diff_xml)
        
        # Find namespace
        namespace = ""
        if root.tag.startswith('{'):
            namespace = root.tag.split('}')[0] + '}'
        
        changes = {
            'additions': [],
            'modifications': [],
            'deletions': []
        }
        
        # Look for GenericDiff
        generic_diff = root.find(f'{namespace}GenericDiff')
        if generic_diff is None:
            return changes
        
        # Parse additions
        addition = generic_diff.find(f'{namespace}addition')
        if addition is not None:
            total = addition.get('total', '0')
            changes['additions'].append(f"Total additions: {total}")
            for change in addition.findall(f'{namespace}change'):
                change_type = change.get('type', 'N/A')
                particle_name = change.get('changedParticleName', 'N/A')
                new_value = change.find(f'{namespace}newValue')
                if new_value is not None:
                    xpath = new_value.get('xpath', 'N/A')
                    changes['additions'].append(f"Added {change_type} '{particle_name}' at {xpath}")
        
        # Parse modifications
        modification = generic_diff.find(f'{namespace}modification')
        if modification is not None:
            total = modification.get('total', '0')
            changes['modifications'].append(f"Total modifications: {total}")
            for change in modification.findall(f'{namespace}change'):
                change_type = change.get('type', 'N/A')
                particle_name = change.get('changedParticleName', 'N/A')
                old_value = change.find(f'{namespace}oldValue')
                new_value = change.find(f'{namespace}newValue')
                if old_value is not None and new_value is not None:
                    old_text = old_value.text or 'N/A'
                    new_text = new_value.text or 'N/A'
                    xpath = new_value.get('xpath', 'N/A')
                    changes['modifications'].append(f"Modified {change_type} '{particle_name}' at {xpath}: '{old_text}' → '{new_text}'")
        
        # Parse deletions
        deletion = generic_diff.find(f'{namespace}deletion')
        if deletion is not None:
            total = deletion.get('total', '0')
            changes['deletions'].append(f"Total deletions: {total}")
            for change in deletion.findall(f'{namespace}change'):
                change_type = change.get('type', 'N/A')
                particle_name = change.get('changedParticleName', 'N/A')
                old_value = change.find(f'{namespace}oldValue')
                if old_value is not None:
                    xpath = old_value.get('xpath', 'N/A')
                    changes['deletions'].append(f"Deleted {change_type} '{particle_name}' at {xpath}")
        
        return changes
        
    except Exception as e:
        print(f"⚠️ Error parsing diff XML: {e}")
        return {
            'additions': [],
            'modifications': [],
            'deletions': []
        }

def compare_component_versions(component_id, version1, version2):
    """Compare two versions of a component"""
    
    # Check for required environment variables
    account_id = os.getenv("BOOMI_ACCOUNT")
    username = os.getenv("BOOMI_USER") 
    password = os.getenv("BOOMI_SECRET")
    
    if not all([account_id, username, password]):
        print("❌ Error: Missing required environment variables")
        print("   Please set: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET")
        return False
    
    print(f"🏢 Account: {account_id}")
    print(f"👤 User: {username}")
    print(f"🎯 Component ID: {component_id}")
    print(f"📊 Comparing version {version1} → version {version2}")
    
    # Initialize the Boomi SDK
    sdk = Boomi(
        account_id=account_id,
        username=username, 
        password=password,
        timeout=30000
    )
    
    print(f"\n🔍 Getting component information...")
    
    try:
        # Get component details
        component = sdk.component.get_component(component_id=component_id)
        component_name = getattr(component, 'name', 'N/A')
        component_type = getattr(component, 'type_', 'N/A')
        current_version = getattr(component, 'version', 'N/A')
        
        print(f"✅ Component found: {component_name} ({component_type})")
        print(f"📌 Current version: {current_version}")
        
        # Validate versions exist
        if int(version2) > int(current_version):
            print(f"⚠️ Warning: Version {version2} is higher than current version {current_version}")
            print(f"   This comparison may not work as expected")
        
    except Exception as e:
        print(f"❌ Failed to get component: {e}")
        print("Please check that the component ID is valid")
        return False
    
    print(f"\n🔄 Creating diff request...")
    
    try:
        # Create proper ComponentDiffRequest with the correct structure
        from boomi.models import ComponentDiffRequest
        
        diff_request = ComponentDiffRequest(
            component_id=component_id,
            source_version=int(version1),
            target_version=int(version2)
        )
        
        result = sdk.component_diff_request.create_component_diff_request(
            request_body=diff_request
        )
        
        print("✅ Diff request created successfully!")
        print(f"📊 Response type: {type(result).__name__}")
        
        # Extract and display diff details
        print(f"\n📋 Component Diff Results:")
        print("=" * 60)
        print(f"  Component: {component_name}")
        print(f"  Type: {component_type}")
        print(f"  Comparing: v{version1} → v{version2}")
        
        # Check if we have a proper diff response
        if hasattr(result, 'component_diff_response'):
            diff_response = result.component_diff_response
            
            # Show diff message
            if hasattr(diff_response, 'message'):
                print(f"  Message: {diff_response.message}")
            
            # Extract generic diff details
            if hasattr(diff_response, 'generic_diff') and diff_response.generic_diff:
                generic_diff = diff_response.generic_diff
                print(f"\n📊 Detailed Diff Analysis:")
                
                # Additions
                if hasattr(generic_diff, 'addition') and generic_diff.addition:
                    addition = generic_diff.addition
                    total = getattr(addition, 'total', 0)
                    changes = getattr(addition, 'change', [])
                    print(f"  ➕ Additions: {total}")
                    if changes:
                        for i, change in enumerate(changes[:5], 1):  # Show first 5
                            change_type = getattr(change, 'type_', 'N/A')
                            particle = getattr(change, 'changed_particle_name', 'N/A')
                            print(f"     {i}. Added {change_type}: {particle}")
                
                # Deletions
                if hasattr(generic_diff, 'deletion') and generic_diff.deletion:
                    deletion = generic_diff.deletion
                    total = getattr(deletion, 'total', 0)
                    changes = getattr(deletion, 'change', [])
                    print(f"  ➖ Deletions: {total}")
                    if changes:
                        for i, change in enumerate(changes[:5], 1):  # Show first 5
                            change_type = getattr(change, 'type_', 'N/A')
                            particle = getattr(change, 'changed_particle_name', 'N/A')
                            print(f"     {i}. Deleted {change_type}: {particle}")
                
                # Modifications
                if hasattr(generic_diff, 'modification') and generic_diff.modification:
                    modification = generic_diff.modification
                    total = getattr(modification, 'total', 0)
                    changes = getattr(modification, 'change', [])
                    print(f"  🔄 Modifications: {total}")
                    if changes:
                        for i, change in enumerate(changes[:5], 1):  # Show first 5
                            change_type = getattr(change, 'type_', 'N/A')
                            particle = getattr(change, 'changed_particle_name', 'N/A')
                            old_val = getattr(change, 'old_value', 'N/A')
                            new_val = getattr(change, 'new_value', 'N/A')
                            print(f"     {i}. Modified {change_type}: {particle}")
                            if old_val != 'N/A' and new_val != 'N/A':
                                print(f"        '{old_val}' → '{new_val}'")
                
                print(f"\n💡 Summary:")
                print(f"  • Total changes: {(getattr(generic_diff.addition, 'total', 0) if hasattr(generic_diff, 'addition') and generic_diff.addition else 0) + (getattr(generic_diff.deletion, 'total', 0) if hasattr(generic_diff, 'deletion') and generic_diff.deletion else 0) + (getattr(generic_diff.modification, 'total', 0) if hasattr(generic_diff, 'modification') and generic_diff.modification else 0)}")
                print(f"  • Version {version1} to {version2} shows significant changes")
                print(f"  • Review changes before deploying newer version")
        else:
            print(f"  ⚠️ No detailed diff data available")
            print(f"  Response type: {type(result).__name__}")
            if hasattr(result, '_kwargs'):
                print(f"  Available fields: {list(result._kwargs.keys())}")
        
        return True
        
    except Exception as e:
        error_msg = str(e)
        print(f"❌ Diff request failed: {error_msg}")
        
        # Provide helpful troubleshooting hints
        if "404" in error_msg or "not found" in error_msg.lower():
            print("🔍 Component not found - check the component ID")
        elif "403" in error_msg:
            print("🔍 Permission issue - check your API credentials and component access")
        elif "400" in error_msg:
            print("🔍 Bad request - check component ID and version format")
        elif "401" in error_msg:
            print("🔍 Authentication failed - verify your credentials")
        else:
            print("🔍 Check network connectivity and API endpoint availability")
            
        return False

def main():
    """Main entry point"""
    if len(sys.argv) < 4:
        print("❌ Error: Component ID and two version numbers are required")
        print("\nUsage:")
        print(f"  {sys.argv[0]} COMPONENT_ID VERSION1 VERSION2")
        print("\nArguments:")
        print("  COMPONENT_ID     The component ID to compare versions for")
        print("  VERSION1         The first version to compare (older version)")
        print("  VERSION2         The second version to compare (newer version)")
        print("\nExamples:")
        print(f"  {sys.argv[0]} 112b4efe-b173-4258-9492-613ead7d52ce 1 2")
        print("\n💡 Use list_all_components.py to find component IDs")
        print("💡 Use get_component_by_id.py to see available versions")
        return
    
    component_id = sys.argv[1]
    version1 = sys.argv[2]
    version2 = sys.argv[3]
    
    # Validate version numbers
    try:
        v1 = int(version1)
        v2 = int(version2)
        if v1 >= v2:
            print("⚠️ Warning: Version1 should typically be older than Version2")
            print(f"   You specified v{v1} → v{v2}")
    except ValueError:
        print("❌ Error: Version numbers must be integers")
        return
    
    print("🚀 Boomi SDK Example: Compare Component Versions")
    print("=" * 55)
    print()
    
    success = compare_component_versions(component_id, version1, version2)
    
    print(f"\n{'='*55}")
    if success:
        print("🌟 Component version comparison completed successfully!")
    else:
        print("💥 Component version comparison encountered issues")

if __name__ == "__main__":
    main()