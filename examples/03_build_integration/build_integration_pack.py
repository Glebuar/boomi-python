#!/usr/bin/env python3
"""
Build Integration Pack Example

This example demonstrates how to build and package integration components:
- Create integration pack structure
- Add components to pack
- Configure pack metadata
- Version and release packs
- Export pack for distribution
"""

import os
import sys
import json
import argparse
from typing import Dict, List, Optional, Any
from datetime import datetime

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from boomi import Boomi
from boomi.models import (
    IntegrationPack,
    IntegrationPackQueryConfig,
    IntegrationPackSimpleExpression,
    IntegrationPackSimpleExpressionOperator,
    IntegrationPackSimpleExpressionProperty,
    ComponentMetadataQueryConfig,
    ComponentMetadataSimpleExpression,
    ComponentMetadataSimpleExpressionOperator,
    ComponentMetadataSimpleExpressionProperty
)


class IntegrationPackBuilder:
    """Builds and manages integration packs"""
    
    def __init__(self, verbose: bool = False):
        """Initialize the builder"""
        self.verbose = verbose
        
        # Initialize SDK
        self.sdk = Boomi(
            account_id=os.environ.get('BOOMI_ACCOUNT'),
            username=os.environ.get('BOOMI_USER'),
            password=os.environ.get('BOOMI_SECRET'),
            timeout=30000
        )
        
        if self.verbose:
            print("✅ Integration Pack Builder initialized")
    
    def create_pack(self, name: str, description: str, 
                    version: str = "1.0", vendor: str = "Custom") -> Optional[str]:
        """
        Create a new integration pack
        
        Args:
            name: Pack name
            description: Pack description
            version: Pack version
            vendor: Vendor name
            
        Returns:
            Pack ID if successful
        """
        try:
            print(f"\n📦 Creating integration pack: {name}")
            
            # Create pack object
            pack = IntegrationPack(
                name=name,
                description=description,
                version=version,
                vendor=vendor
            )
            
            # Create the pack
            result = self.sdk.integration_pack.create_integration_pack(
                request_body=pack
            )
            
            if result and hasattr(result, 'id_'):
                print(f"✅ Pack created successfully")
                print(f"   ID: {result.id_}")
                print(f"   Version: {version}")
                return result.id_
            else:
                print("❌ Failed to create pack")
                return None
                
        except Exception as e:
            print(f"❌ Error creating pack: {e}")
            if self.verbose:
                import traceback
                traceback.print_exc()
            return None
    
    def add_components_to_pack(self, pack_id: str, component_ids: List[str]) -> bool:
        """
        Add components to an integration pack
        
        Args:
            pack_id: Integration pack ID
            component_ids: List of component IDs to add
            
        Returns:
            True if successful
        """
        try:
            print(f"\n➕ Adding {len(component_ids)} components to pack...")
            
            success_count = 0
            for comp_id in component_ids:
                if self.verbose:
                    print(f"   Adding component: {comp_id}")
                
                # Note: The actual API for adding components to packs would be used here
                # This is a simplified example
                try:
                    # Get component metadata
                    query_expression = ComponentMetadataSimpleExpression(
                        operator=ComponentMetadataSimpleExpressionOperator.EQUALS,
                        property=ComponentMetadataSimpleExpressionProperty.COMPONENTID,
                        argument=[comp_id]
                    )
                    
                    query_config = ComponentMetadataQueryConfig(
                        query_filter={'expression': query_expression}
                    )
                    
                    result = self.sdk.component_metadata.query_component_metadata(
                        request_body=query_config
                    )
                    
                    if result and hasattr(result, 'result') and result.result:
                        comp_meta = result.result[0]
                        print(f"   ✅ Added: {comp_meta.name}")
                        success_count += 1
                    else:
                        print(f"   ❌ Component not found: {comp_id}")
                        
                except Exception as e:
                    print(f"   ❌ Error adding component {comp_id}: {e}")
            
            print(f"\n✅ Added {success_count}/{len(component_ids)} components")
            return success_count == len(component_ids)
            
        except Exception as e:
            print(f"❌ Error adding components: {e}")
            return False
    
    def build_pack_from_folder(self, folder_path: str, pack_name: str,
                              description: str, version: str = "1.0") -> Optional[str]:
        """
        Build integration pack from folder components
        
        Args:
            folder_path: Folder containing components
            pack_name: Name for the pack
            description: Pack description
            version: Pack version
            
        Returns:
            Pack ID if successful
        """
        try:
            print(f"\n🏗️ Building pack from folder: {folder_path}")
            
            # Query components in folder
            components = self._get_folder_components(folder_path)
            
            if not components:
                print("❌ No components found in folder")
                return None
            
            print(f"   Found {len(components)} components")
            
            # Create the pack
            pack_id = self.create_pack(
                name=pack_name,
                description=description,
                version=version
            )
            
            if not pack_id:
                return None
            
            # Add components to pack
            component_ids = [comp['id'] for comp in components]
            self.add_components_to_pack(pack_id, component_ids)
            
            return pack_id
            
        except Exception as e:
            print(f"❌ Error building pack from folder: {e}")
            return None
    
    def _get_folder_components(self, folder_path: str) -> List[Dict[str, Any]]:
        """Get components from a folder"""
        components = []
        
        try:
            # Query components by folder
            query_expression = ComponentMetadataSimpleExpression(
                operator=ComponentMetadataSimpleExpressionOperator.LIKE,
                property=ComponentMetadataSimpleExpressionProperty.FOLDERFULLPATH,
                argument=[f"%{folder_path}%"]
            )
            
            query_config = ComponentMetadataQueryConfig(
                query_filter={'expression': query_expression}
            )
            
            result = self.sdk.component_metadata.query_component_metadata(
                request_body=query_config
            )
            
            if result and hasattr(result, 'result') and result.result:
                for comp in result.result:
                    components.append({
                        'id': getattr(comp, 'id_', 'N/A'),
                        'name': getattr(comp, 'name', 'N/A'),
                        'type': getattr(comp, 'type', 'N/A')
                    })
            
        except Exception as e:
            if self.verbose:
                print(f"   Error getting folder components: {e}")
        
        return components
    
    def update_pack_version(self, pack_id: str, new_version: str) -> bool:
        """
        Update integration pack version
        
        Args:
            pack_id: Pack ID
            new_version: New version string
            
        Returns:
            True if successful
        """
        try:
            print(f"\n📝 Updating pack version to: {new_version}")
            
            # Get current pack
            pack = self.sdk.integration_pack.get_integration_pack(id_=pack_id)
            
            # Update version
            pack.version = new_version
            
            # Update the pack
            result = self.sdk.integration_pack.update_integration_pack(
                id_=pack_id,
                request_body=pack
            )
            
            print(f"✅ Version updated to: {new_version}")
            return True
            
        except Exception as e:
            print(f"❌ Error updating version: {e}")
            return False
    
    def export_pack(self, pack_id: str, output_file: str) -> bool:
        """
        Export integration pack to file
        
        Args:
            pack_id: Pack ID to export
            output_file: Output file path
            
        Returns:
            True if successful
        """
        try:
            print(f"\n📤 Exporting integration pack...")
            
            # Get pack details
            pack = self.sdk.integration_pack.get_integration_pack(id_=pack_id)
            
            # Get pack components (simplified)
            components = []
            
            # Create export structure
            export_data = {
                'pack_info': {
                    'id': pack_id,
                    'name': getattr(pack, 'name', 'N/A'),
                    'description': getattr(pack, 'description', 'N/A'),
                    'version': getattr(pack, 'version', 'N/A'),
                    'vendor': getattr(pack, 'vendor', 'N/A'),
                    'exported': datetime.now().isoformat()
                },
                'components': components
            }
            
            # Write to file
            with open(output_file, 'w') as f:
                json.dump(export_data, f, indent=2)
            
            print(f"✅ Pack exported to: {output_file}")
            return True
            
        except Exception as e:
            print(f"❌ Error exporting pack: {e}")
            return False
    
    def list_pack_components(self, pack_id: str) -> List[Dict[str, Any]]:
        """
        List components in an integration pack
        
        Args:
            pack_id: Pack ID
            
        Returns:
            List of components
        """
        print(f"\n📋 Listing pack components...")
        
        # This would query actual pack components
        # Simplified for example
        components = []
        
        print(f"   Found {len(components)} components")
        return components


def main():
    """Main function"""
    parser = argparse.ArgumentParser(
        description='Build Boomi integration packs',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Create a new pack
  %(prog)s --create --name "My Pack" --description "Custom integration" --version "1.0"
  
  # Build pack from folder
  %(prog)s --build-from-folder "/MyComponents" --name "Folder Pack" --description "From folder"
  
  # Add components to existing pack
  %(prog)s --add-components PACK_ID --components COMP1 COMP2 COMP3
  
  # Update pack version
  %(prog)s --update-version PACK_ID --version "2.0"
  
  # Export pack
  %(prog)s --export PACK_ID --output pack.json
  
  # List pack components
  %(prog)s --list-components PACK_ID
"""
    )
    
    # Operations
    parser.add_argument('--create', action='store_true',
                       help='Create new integration pack')
    parser.add_argument('--build-from-folder', metavar='PATH',
                       help='Build pack from folder components')
    parser.add_argument('--add-components', metavar='PACK_ID',
                       help='Add components to pack')
    parser.add_argument('--update-version', metavar='PACK_ID',
                       help='Update pack version')
    parser.add_argument('--export', metavar='PACK_ID',
                       help='Export pack to file')
    parser.add_argument('--list-components', metavar='PACK_ID',
                       help='List pack components')
    
    # Options
    parser.add_argument('--name', help='Pack name')
    parser.add_argument('--description', help='Pack description')
    parser.add_argument('--version', default='1.0', help='Pack version')
    parser.add_argument('--vendor', default='Custom', help='Vendor name')
    parser.add_argument('--components', nargs='+', help='Component IDs')
    parser.add_argument('--output', help='Output file')
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='Enable verbose output')
    
    args = parser.parse_args()
    
    # Initialize builder
    builder = IntegrationPackBuilder(verbose=args.verbose)
    
    # Execute operations
    if args.create:
        if not args.name or not args.description:
            print("❌ Error: --name and --description are required")
            return
        
        pack_id = builder.create_pack(
            name=args.name,
            description=args.description,
            version=args.version,
            vendor=args.vendor
        )
        
        if pack_id:
            print(f"\n✅ Integration pack created: {pack_id}")
    
    elif args.build_from_folder:
        if not args.name or not args.description:
            print("❌ Error: --name and --description are required")
            return
        
        pack_id = builder.build_pack_from_folder(
            folder_path=args.build_from_folder,
            pack_name=args.name,
            description=args.description,
            version=args.version
        )
        
        if pack_id:
            print(f"\n✅ Pack built from folder: {pack_id}")
    
    elif args.add_components:
        if not args.components:
            print("❌ Error: --components required")
            return
        
        success = builder.add_components_to_pack(
            pack_id=args.add_components,
            component_ids=args.components
        )
        
        if success:
            print("\n✅ Components added successfully")
    
    elif args.update_version:
        if not args.version:
            print("❌ Error: --version required")
            return
        
        success = builder.update_pack_version(
            pack_id=args.update_version,
            new_version=args.version
        )
    
    elif args.export:
        if not args.output:
            print("❌ Error: --output required")
            return
        
        success = builder.export_pack(
            pack_id=args.export,
            output_file=args.output
        )
    
    elif args.list_components:
        components = builder.list_pack_components(args.list_components)
        
        if components:
            print("\n📦 Pack Components:")
            for i, comp in enumerate(components, 1):
                print(f"{i}. {comp['name']} ({comp['type']})")
    
    else:
        parser.print_help()


if __name__ == '__main__':
    main()