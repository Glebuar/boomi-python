#!/usr/bin/env python3
"""
Boomi SDK Example: Clone Component
===================================

This example demonstrates how to clone/copy an existing component.

Features:
- Clone component with new name
- Copy to different folder (optional)
- Preserve component structure and configuration
- Remove references that would conflict

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET

Usage:
    # Clone a component with a new name
    python clone_component.py SOURCE_ID "New Component Name"
    
    # Clone to a specific folder
    python clone_component.py SOURCE_ID "New Component Name" --folder FOLDER_ID
    
    # Clone with description
    python clone_component.py SOURCE_ID "New Component Name" --description "Cloned for testing"

Examples:
    python clone_component.py abc123 "My Process Copy"
    python clone_component.py abc123 "Production Process" --folder def456
"""

import os
import sys
import argparse
import xml.etree.ElementTree as ET
from typing import Optional

# Add parent directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

from boomi import Boomi


class ComponentCloner:
    """Manages component cloning operations"""
    
    def __init__(self):
        """Initialize the Boomi SDK client"""
        self.sdk = Boomi(
            account_id=os.getenv("BOOMI_ACCOUNT"),
            username=os.getenv("BOOMI_USER"),
            password=os.getenv("BOOMI_SECRET"),
            timeout=30000
        )
        print("✅ SDK initialized successfully")
    
    def clone_component(self, 
                       source_id: str, 
                       new_name: str, 
                       folder_id: Optional[str] = None,
                       description: Optional[str] = None) -> Optional[str]:
        """
        Clone a component with a new name
        
        Args:
            source_id: The component ID to clone from
            new_name: The name for the cloned component
            folder_id: Optional folder ID to place the clone in
            description: Optional description for the clone
            
        Returns:
            The new component ID if successful, None otherwise
        """
        print(f"\n🔄 Cloning component {source_id}...")
        
        try:
            # Step 1: Get the source component
            print(f"📥 Retrieving source component...")
            source_component = self.sdk.component.get_component(component_id=source_id)
            
            if not source_component:
                print(f"❌ Component not found: {source_id}")
                return None
            
            # Display source component info
            print(f"✅ Found source component:")
            print(f"   Name: {source_component.name}")
            print(f"   Type: {source_component.type_}")
            print(f"   Folder: {source_component.folder_full_path}")
            if hasattr(source_component, 'description') and source_component.description:
                print(f"   Description: {source_component.description}")
            
            # Step 2: Convert to XML and modify
            print(f"\n🔧 Preparing clone...")
            
            # Get the XML representation
            if hasattr(source_component, 'to_xml'):
                xml_str = source_component.to_xml()
            else:
                print("❌ Component doesn't support XML conversion")
                return None
            
            # Parse the XML
            root = ET.fromstring(xml_str)
            
            # Update the name
            root.set('name', new_name)
            print(f"   ✓ Set new name: {new_name}")
            
            # Remove attributes that should be unique
            attributes_to_remove = [
                'componentId',
                'version',
                'currentVersion',
                'createdDate',
                'createdBy',
                'modifiedDate',
                'modifiedBy'
            ]
            
            for attr in attributes_to_remove:
                if attr in root.attrib:
                    del root.attrib[attr]
            print(f"   ✓ Removed unique identifiers")
            
            # Update folder if specified
            if folder_id:
                root.set('folderId', folder_id)
                print(f"   ✓ Set target folder: {folder_id}")
            
            # Update or add description
            if description:
                # Check if description element exists
                desc_elem = root.find('.//description')
                if desc_elem is not None:
                    desc_elem.text = description
                else:
                    # Add description element if component type supports it
                    desc_elem = ET.SubElement(root, 'description')
                    desc_elem.text = description
                print(f"   ✓ Set description: {description}")
            
            # Convert back to XML string
            new_xml = ET.tostring(root, encoding='unicode')
            
            # Step 3: Create the new component
            print(f"\n📤 Creating cloned component...")
            result = self.sdk.component.create_component(request_body=new_xml)
            
            # Extract the new component ID from the result
            new_component_id = None
            
            if isinstance(result, str):
                # Result is XML string, parse it
                result_root = ET.fromstring(result)
                new_component_id = result_root.get('componentId')
            elif hasattr(result, 'component_id'):
                # Result is a Component object
                new_component_id = result.component_id
            
            if new_component_id:
                print(f"✅ Clone created successfully!")
                print(f"   New component ID: {new_component_id}")
                print(f"   Name: {new_name}")
                
                # Verify the clone
                self._verify_clone(new_component_id)
                
                return new_component_id
            else:
                print(f"⚠️ Component created but couldn't extract ID from response")
                return None
            
        except Exception as e:
            print(f"❌ Failed to clone component: {e}")
            import traceback
            traceback.print_exc()
            return None
    
    def _verify_clone(self, component_id: str) -> bool:
        """Verify the cloned component was created correctly"""
        try:
            print(f"\n🔍 Verifying clone...")
            cloned = self.sdk.component.get_component(component_id=component_id)
            
            if cloned:
                print(f"   ✓ Clone verified:")
                print(f"     Name: {cloned.name}")
                print(f"     Type: {cloned.type_}")
                print(f"     Folder: {cloned.folder_full_path}")
                return True
            else:
                print(f"   ⚠️ Could not verify clone")
                return False
        except Exception as e:
            print(f"   ⚠️ Verification failed: {e}")
            return False
    
    def list_recent_components(self, limit: int = 5) -> None:
        """List recent components that can be cloned"""
        print(f"\n📋 Listing recent components...")
        
        try:
            from boomi.models import (
                ComponentMetadataQueryConfig,
                ComponentMetadataQueryConfigQueryFilter,
                ComponentMetadataSimpleExpression,
                ComponentMetadataSimpleExpressionOperator,
                ComponentMetadataSimpleExpressionProperty
            )
            
            # Query for non-deleted components
            query_expression = ComponentMetadataSimpleExpression(
                operator=ComponentMetadataSimpleExpressionOperator.EQUALS,
                property=ComponentMetadataSimpleExpressionProperty.DELETED,
                argument=["false"]
            )
            
            query_filter = ComponentMetadataQueryConfigQueryFilter(expression=query_expression)
            query_config = ComponentMetadataQueryConfig(query_filter=query_filter)
            
            result = self.sdk.component_metadata.query_component_metadata(request_body=query_config)
            
            if hasattr(result, 'result') and result.result:
                components = result.result[:limit]
                print(f"Found {len(result.result)} components, showing {len(components)}:")
                
                for comp in components:
                    print(f"\n   📄 {comp.name}")
                    print(f"      ID: {comp.component_id}")
                    print(f"      Type: {comp.type_}")
                    print(f"      Folder: {comp.folder_name}")
                    print(f"      Modified: {comp.modified_date}")
            else:
                print("No components found")
                
        except Exception as e:
            print(f"❌ Failed to list components: {e}")


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='Clone a Boomi component with a new name',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  %(prog)s abc123 "My Process Copy"
  %(prog)s abc123 "Production Process" --folder def456
  %(prog)s abc123 "Test Process" --description "Cloned for testing"
  %(prog)s --list  # List available components to clone
        '''
    )
    
    parser.add_argument('source_id', nargs='?',
                       help='The component ID to clone from')
    parser.add_argument('new_name', nargs='?',
                       help='The name for the cloned component')
    parser.add_argument('--folder', metavar='FOLDER_ID',
                       help='Folder ID to place the clone in')
    parser.add_argument('--description',
                       help='Description for the cloned component')
    parser.add_argument('--list', action='store_true',
                       help='List recent components that can be cloned')
    
    args = parser.parse_args()
    
    # Validate environment variables
    required_env = ['BOOMI_ACCOUNT', 'BOOMI_USER', 'BOOMI_SECRET']
    missing = [var for var in required_env if not os.getenv(var)]
    
    if missing:
        print("❌ Missing environment variables:")
        for var in missing:
            print(f"  - {var}")
        print("\n💡 Set these in your .env file or export them")
        sys.exit(1)
    
    # Execute requested operation
    try:
        cloner = ComponentCloner()
        
        if args.list:
            cloner.list_recent_components(limit=10)
            print("\n💡 Use one of the component IDs above as the source_id")
        
        elif args.source_id and args.new_name:
            new_id = cloner.clone_component(
                source_id=args.source_id,
                new_name=args.new_name,
                folder_id=args.folder,
                description=args.description
            )
            
            if new_id:
                print(f"\n✅ Successfully cloned component")
                print(f"   Original: {args.source_id}")
                print(f"   Clone: {new_id}")
                print(f"\n💡 You can now find '{args.new_name}' in your Boomi account")
            else:
                print(f"\n❌ Failed to clone component")
                sys.exit(1)
        
        else:
            # Use defaults if no parameters provided
            if not args.list and not args.source_id and not args.new_name:
                args.source_id = "112b4efe-b173-4258-9492-613ead7d52ce"  # XML Example Test component
                args.new_name = "Cloned XML Example Test (Demo)"
                print(f"ℹ️ No parameters provided, using defaults:")
                print(f"   Source ID: {args.source_id}")
                print(f"   New Name: {args.new_name}")
                print("💡 To clone a different component, run: python clone_component.py SOURCE_ID 'New Name'")
                
                new_id = cloner.clone_component(
                    source_id=args.source_id,
                    new_name=args.new_name,
                    folder_id=args.folder,
                    description=args.description or "Cloned component for demonstration purposes"
                )
                
                if new_id:
                    print(f"\n✅ Successfully cloned component")
                    print(f"   Original: {args.source_id}")
                    print(f"   Clone: {new_id}")
                    print(f"\n💡 You can now find '{args.new_name}' in your Boomi account")
                else:
                    print(f"\n❌ Failed to clone component")
                    sys.exit(1)
            elif not args.list:
                parser.print_help()
                print("\n💡 Use --list to see available components")
    
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()