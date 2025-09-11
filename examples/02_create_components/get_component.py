#!/usr/bin/env python3
"""
Boomi SDK Example: Get Component with Full Analysis
==================================================

This example demonstrates comprehensive component retrieval with both 
user-friendly formatted output and detailed technical analysis.

Features:
- Retrieves component by ID with optional version
- Shows formatted metadata (name, type, version, dates, folder)
- Displays full XML configuration analysis
- Provides detailed structural analysis for debugging
- Handles different component types (process, connector, profile, etc.)
- Command-line interface with usage help
- Comprehensive error handling

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- Or create a .env file with these variables

Usage:
    python get_component.py COMPONENT_ID [OPTIONS]
    
    Arguments:
    COMPONENT_ID    The component ID to retrieve
    
    Options:
    --version=N     Specific version to retrieve (defaults to latest)
    --detailed      Show detailed structural analysis
    --xml-only      Show only XML configuration
    
    Examples:
    python get_component.py 112b4efe-b173-4258-9492-613ead7d52ce
    python get_component.py 112b4efe-b173-4258-9492-613ead7d52ce --version=1
    python get_component.py 112b4efe-b173-4258-9492-613ead7d52ce --detailed
"""

import os
import sys
from typing import Optional

# Add parent directory to path for imports  
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

# Load environment variables from .env file if available
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv is optional

from boomi import Boomi


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

def format_date(date_str):
    """Format ISO date string to readable format"""
    if date_str and 'T' in date_str:
        return date_str.split('T')[0] + ' ' + date_str.split('T')[1].split('.')[0]
    return date_str or 'N/A'

def analyze_object_structure(obj, prefix="", max_depth=3, current_depth=0):
    """Recursively analyze object structure for detailed analysis"""
    if current_depth >= max_depth:
        return f"{prefix}... (max depth reached)"
    
    result = []
    
    if isinstance(obj, dict):
        result.append(f"{prefix}Dict with {len(obj)} keys:")
        for key, value in list(obj.items())[:5]:  # Show first 5 keys
            if isinstance(value, (dict, list)):
                result.append(f"{prefix}  • {key}: {type(value).__name__}")
                if current_depth < max_depth - 1:
                    sub_analysis = analyze_object_structure(value, prefix + "    ", max_depth, current_depth + 1)
                    if sub_analysis:
                        result.append(sub_analysis)
            else:
                value_preview = str(value)[:50] + "..." if len(str(value)) > 50 else str(value)
                result.append(f"{prefix}  • {key}: {type(value).__name__} = {value_preview}")
        
        if len(obj) > 5:
            result.append(f"{prefix}  ... and {len(obj) - 5} more keys")
    
    elif isinstance(obj, list):
        result.append(f"{prefix}List with {len(obj)} items:")
        for i, item in enumerate(obj[:3]):  # Show first 3 items
            if isinstance(item, (dict, list)):
                result.append(f"{prefix}  [{i}]: {type(item).__name__}")
                if current_depth < max_depth - 1:
                    sub_analysis = analyze_object_structure(item, prefix + "    ", max_depth, current_depth + 1)
                    if sub_analysis:
                        result.append(sub_analysis)
            else:
                item_preview = str(item)[:50] + "..." if len(str(item)) > 50 else str(item)
                result.append(f"{prefix}  [{i}]: {type(item).__name__} = {item_preview}")
        
        if len(obj) > 3:
            result.append(f"{prefix}  ... and {len(obj) - 3} more items")
    
    else:
        value_preview = str(obj)[:100] + "..." if len(str(obj)) > 100 else str(obj)
        result.append(f"{prefix}{type(obj).__name__}: {value_preview}")
    
    return "\n".join(result)

def print_component_metadata(component):
    """Print formatted component metadata information"""
    print("📋 Component Metadata:")
    print("=" * 50)
    print(f"  Name: {getattr(component, 'name', 'N/A')}")
    print(f"  Component ID: {getattr(component, 'component_id', 'N/A')}")
    print(f"  Type: {getattr(component, 'type_', 'N/A')}")
    print(f"  Version: {getattr(component, 'version', 'N/A')}")
    
    # Status information
    current_version = getattr(component, 'current_version', 'false')
    deleted = getattr(component, 'deleted', 'false')
    status_parts = []
    
    if str(current_version).lower() == 'true':
        status_parts.append("CURRENT")
    if str(deleted).lower() == 'true':
        status_parts.append("DELETED")
    
    if status_parts:
        print(f"  Status: {' | '.join(status_parts)}")
    
    print(f"  Created: {format_date(getattr(component, 'created_date', 'N/A'))} by {getattr(component, 'created_by', 'N/A')}")
    print(f"  Modified: {format_date(getattr(component, 'modified_date', 'N/A'))} by {getattr(component, 'modified_by', 'N/A')}")
    
    # Folder information
    folder_path = getattr(component, 'folder_full_path', None) or getattr(component, 'folder_name', None)
    if folder_path:
        print(f"  Folder: {folder_path}")
    
    # Branch information
    branch_name = getattr(component, 'branch_name', None)
    if branch_name and branch_name != 'main':
        print(f"  Branch: {branch_name}")
    
    # Description
    description = getattr(component, 'description', None)
    if description:
        print(f"  Description: {description}")

def print_component_xml(component, detailed=False):
    """Print component XML configuration with optional detailed analysis"""
    print("\n🔧 Component Configuration:")
    print("=" * 50)
    
    # Check for XML object
    obj = getattr(component, 'object', None)
    if obj:
        print("📄 Component has XML configuration object")
        
        if detailed:
            # Detailed structural analysis
            print("\n🔍 Detailed XML Structure Analysis:")
            print("-" * 40)
            analysis = analyze_object_structure(obj)
            print(analysis)
        else:
            # Basic structure info
            if hasattr(obj, '__dict__'):
                obj_dict = obj.__dict__ if hasattr(obj, '__dict__') else {}
                print(f"📊 Configuration contains {len(obj_dict)} top-level elements")
                
                # Show top-level keys
                if obj_dict:
                    print("🔑 Top-level configuration elements:")
                    for key in sorted(obj_dict.keys()):
                        if not key.startswith('_'):
                            value = obj_dict[key]
                            value_type = type(value).__name__
                            if isinstance(value, (dict, list)):
                                count = len(value) if hasattr(value, '__len__') else 0
                                print(f"    • {key}: {value_type} ({count} items)")
                            else:
                                print(f"    • {key}: {value_type}")
            else:
                print(f"📄 Configuration object type: {type(obj).__name__}")
    else:
        print("❌ No XML configuration object found")
    
    # Check for encrypted values
    encrypted_values = getattr(component, 'encrypted_values', None)
    if encrypted_values:
        print(f"\n🔒 Component has encrypted values configured")
    
    # Check for process overrides
    process_overrides = getattr(component, 'process_overrides', None)
    if process_overrides:
        print(f"\n⚙️ Component has process overrides configured")

def print_raw_response_structure(result):
    """Print raw response structure for debugging"""
    print("\n🔍 Raw Response Structure:")
    print("-" * 40)
    if hasattr(result, '__dict__'):
        for key, value in result.__dict__.items():
            if not key.startswith('_'):
                print(f"  {key}: {type(value).__name__}")
                if key == 'object' and value:
                    print("    📄 XML Configuration Object Found!")

def get_component(component_id, version=None, detailed=False, xml_only=False):
    """Retrieve and display component with specified options"""
    
    # Validate environment variables
    account_id, username, password = validate_environment()
    
    if not xml_only:
        print(f"🏢 Account: {account_id}")
        print(f"👤 User: {username}")
        print(f"🎯 Target Component ID: {component_id}")
        if version:
            print(f"📌 Specific Version: {version}")
        else:
            print(f"📌 Version: Latest")
    
    # Initialize SDK
    try:
        sdk = Boomi(
            account_id=account_id,
            username=username,
            password=password,
            timeout=30000
        )
        if not xml_only:
            print("✅ SDK initialized successfully")
    except Exception as e:
        print(f"❌ Failed to initialize SDK: {e}")
        return False
    
    if not xml_only:
        print(f"\n🔍 Retrieving component...")
    
    try:
        # Construct component identifier
        if version:
            component_identifier = f"{component_id}~{version}"
        else:
            component_identifier = component_id
        
        # Get the component
        result = sdk.component.get_component(component_id=component_identifier)
        
        if not xml_only:
            print("✅ Component retrieved successfully!")
            print(f"📊 Response type: {type(result).__name__}")
        
        # Handle response - check if it's wrapped in _kwargs
        component = None
        if hasattr(result, '_kwargs') and result._kwargs:
            if 'Component' in result._kwargs:
                component = result._kwargs['Component']
            else:
                # Try to find the component in the response
                for key, value in result._kwargs.items():
                    if hasattr(value, 'component_id') or hasattr(value, 'name'):
                        component = value
                        break
        else:
            component = result
        
        if component:
            if xml_only:
                # Only show XML configuration
                print_component_xml(component, detailed=detailed)
            else:
                # Show metadata
                print_component_metadata(component)
                
                # Show XML configuration
                print_component_xml(component, detailed=detailed)
                
                # Show raw structure if detailed mode
                if detailed:
                    print_raw_response_structure(result)
                
                print(f"\n🎉 SUCCESS!")
                print(f"📍 Component '{getattr(component, 'name', 'N/A')}' retrieved successfully")
                print(f"🔧 Component contains full XML configuration for deployment/analysis")
            
            return True
        else:
            print("❌ No component data found in response")
            if detailed:
                print("Response structure:")
                if hasattr(result, '__dict__'):
                    for key, value in result.__dict__.items():
                        if not key.startswith('_'):
                            print(f"  {key}: {type(value).__name__}")
            return False
            
    except Exception as e:
        error_msg = str(e)
        print(f"❌ Component retrieval failed: {error_msg}")
        
        # Provide helpful troubleshooting hints
        if "404" in error_msg or "not found" in error_msg.lower():
            print("🔍 Component not found - check the component ID")
            print("💡 Use list_all_components.py to find valid component IDs")
        elif "403" in error_msg:
            print("🔍 Permission issue - check your API credentials and account permissions")
        elif "400" in error_msg:
            print("🔍 Bad request - check component ID format")
            if version:
                print("💡 Version format should be a number (e.g., 1, 2, 3)")
        elif "401" in error_msg:
            print("🔍 Authentication failed - verify your credentials")
        else:
            print("🔍 Check network connectivity and API endpoint availability")
            
        return False

def main():
    """Main entry point with argument parsing"""
    if len(sys.argv) < 2:
        print("❌ Error: Component ID is required")
        print("\nUsage:")
        print(f"  {sys.argv[0]} COMPONENT_ID [OPTIONS]")
        print("\nOptions:")
        print("  --version=N     Specific version to retrieve")
        print("  --detailed      Show detailed structural analysis")
        print("  --xml-only      Show only XML configuration")
        print("\nExamples:")
        print(f"  {sys.argv[0]} 112b4efe-b173-4258-9492-613ead7d52ce")
        print(f"  {sys.argv[0]} 112b4efe-b173-4258-9492-613ead7d52ce --version=1")
        print(f"  {sys.argv[0]} 112b4efe-b173-4258-9492-613ead7d52ce --detailed")
        print(f"  {sys.argv[0]} 112b4efe-b173-4258-9492-613ead7d52ce --xml-only")
        print("\n💡 Use list_all_components.py to find component IDs")
        return
    
    component_id = sys.argv[1]
    
    # Parse options
    version = None
    detailed = False
    xml_only = False
    
    for arg in sys.argv[2:]:
        if arg.startswith('--version='):
            version = arg.split('=')[1]
        elif arg == '--detailed':
            detailed = True
        elif arg == '--xml-only':
            xml_only = True
        else:
            print(f"❌ Unknown option: {arg}")
            return
    
    if not xml_only:
        print("🚀 Boomi SDK Example: Get Component")
        print("=" * 45)
        if detailed:
            print("🔍 Mode: Detailed Analysis")
        print()
    
    success = get_component(component_id, version, detailed, xml_only)
    
    if not xml_only:
        print(f"\n{'='*45}")
        if success:
            print("🌟 Component retrieval completed successfully!")
        else:
            print("💥 Component retrieval encountered issues")

if __name__ == "__main__":
    main()