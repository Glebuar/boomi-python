#!/usr/bin/env python3
"""
Boomi SDK Example: Get Component with Detailed Analysis

This example demonstrates detailed component retrieval and analysis,
showing the internal structure and configuration of Boomi components.
"""

import os
import sys
import json
sys.path.insert(0, '../../src')
from boomi import Boomi

# Load environment variables
try:
    from dotenv import load_dotenv
    load_dotenv('../../.env')
except ImportError:
    pass

def analyze_object_structure(obj, prefix="", max_depth=3, current_depth=0):
    """Recursively analyze object structure"""
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

def get_detailed_component(component_id):
    """Retrieve and analyze component in detail"""
    
    # Check environment variables
    account_id = os.getenv("BOOMI_ACCOUNT")
    username = os.getenv("BOOMI_USER") 
    password = os.getenv("BOOMI_SECRET")
    
    if not all([account_id, username, password]):
        print("❌ Missing environment variables")
        return False
    
    print(f"🚀 Detailed Component Analysis")
    print(f"🎯 Component ID: {component_id}")
    print("=" * 60)
    
    # Initialize SDK
    sdk = Boomi(
        account_id=account_id,
        username=username, 
        password=password,
        timeout=30000
    )
    
    try:
        # Get component
        result = sdk.component.get_component(component_id=component_id)
        
        print("✅ Component retrieved successfully!")
        print(f"📊 Response type: {type(result).__name__}")
        
        # Analyze the result structure
        print("\n🔍 Raw Response Structure:")
        print("-" * 40)
        if hasattr(result, '__dict__'):
            for key, value in result.__dict__.items():
                if not key.startswith('_'):
                    print(f"  {key}: {type(value).__name__}")
                    if key == 'object' and value:
                        print("    📄 XML Configuration Object Found!")
                        # Analyze the XML object structure
                        analysis = analyze_object_structure(value, "      ")
                        print(analysis)
        
        # Try to access component details
        component = result
        if hasattr(result, '_kwargs') and 'Component' in result._kwargs:
            component = result._kwargs['Component']
        
        print(f"\n📋 Component Details:")
        print("-" * 40)
        print(f"  Name: {getattr(component, 'name', 'N/A')}")
        print(f"  ID: {getattr(component, 'component_id', 'N/A')}")
        print(f"  Type: {getattr(component, 'type', 'N/A')}")
        print(f"  Version: {getattr(component, 'version', 'N/A')}")
        print(f"  Folder: {getattr(component, 'folder_full_path', 'N/A')}")
        
        # Analyze the object field in detail
        obj = getattr(component, 'object', None)
        if obj:
            print(f"\n🔧 XML Configuration Analysis:")
            print("-" * 40)
            analysis = analyze_object_structure(obj)
            print(analysis)
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python get_component_detailed.py COMPONENT_ID")
        sys.exit(1)
    
    component_id = sys.argv[1]
    get_detailed_component(component_id)