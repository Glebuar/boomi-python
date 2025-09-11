#!/usr/bin/env python3
"""
Integration Pack Analysis Tool

This example demonstrates how to analyze integration packs including:
- Discovering available integration packs
- Analyzing pack components and dependencies
- Understanding pack structure and configuration
- Identifying component relationships within packs
- Generating pack inventory reports
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
    IntegrationPackQueryConfig,
    IntegrationPackSimpleExpression,
    IntegrationPackSimpleExpressionOperator,
    IntegrationPackSimpleExpressionProperty,
    ComponentMetadataQueryConfig,
    ComponentMetadataSimpleExpression,
    ComponentMetadataSimpleExpressionOperator,
    ComponentMetadataSimpleExpressionProperty
)


class IntegrationPackAnalyzer:
    """Analyzes integration packs and their components"""
    
    def __init__(self, verbose: bool = False):
        """Initialize the analyzer"""
        self.verbose = verbose
        
        # Initialize SDK
        self.sdk = Boomi(
            account_id=os.environ.get('BOOMI_ACCOUNT'),
            username=os.environ.get('BOOMI_USER'),
            password=os.environ.get('BOOMI_SECRET'),
            timeout=30000
        )
        
        if self.verbose:
            print("✅ Integration Pack Analyzer initialized")
    
    def list_integration_packs(self, limit: int = 10) -> List[Dict[str, Any]]:
        """
        List available integration packs
        
        Args:
            limit: Maximum number of packs to return
            
        Returns:
            List of integration pack information
        """
        try:
            if self.verbose:
                print("\n📦 Listing integration packs...")
            
            # Query all integration packs - create a simple expression that matches all
            from boomi.models import IntegrationPackQueryConfigQueryFilter
            
            # Create a simple query that returns all packs (ID is not null)
            simple_expression = IntegrationPackSimpleExpression(
                operator=IntegrationPackSimpleExpressionOperator.ISNOTNULL,
                property=IntegrationPackSimpleExpressionProperty.ID,
                argument=[]
            )
            
            query_filter = IntegrationPackQueryConfigQueryFilter(
                expression=simple_expression
            )
            
            # Query integration packs with proper filter
            query_config = IntegrationPackQueryConfig(query_filter=query_filter)
            result = self.sdk.integration_pack.query_integration_pack(request_body=query_config)
            
            packs = []
            if result and hasattr(result, 'result') and result.result:
                for pack in result.result[:limit]:
                    pack_info = {
                        'id': getattr(pack, 'id_', 'N/A'),
                        'name': getattr(pack, 'name', 'N/A'),
                        'description': getattr(pack, 'description', 'N/A'),
                        'version': getattr(pack, 'version', 'N/A'),
                        'vendor': getattr(pack, 'vendor', 'N/A'),
                        'created': getattr(pack, 'created_date', 'N/A'),
                        'modified': getattr(pack, 'modified_date', 'N/A')
                    }
                    packs.append(pack_info)
            
            print(f"✅ Found {len(packs)} integration pack(s)")
            return packs
            
        except Exception as e:
            print(f"❌ Error listing integration packs: {e}")
            if self.verbose:
                import traceback
                traceback.print_exc()
            return []
    
    def analyze_pack(self, pack_id: str) -> Dict[str, Any]:
        """
        Analyze a specific integration pack
        
        Args:
            pack_id: Integration pack ID
            
        Returns:
            Detailed analysis of the pack
        """
        try:
            print(f"\n🔍 Analyzing integration pack: {pack_id}")
            
            # Get pack details
            pack = self.sdk.integration_pack.get_integration_pack(id_=pack_id)
            
            analysis = {
                'id': pack_id,
                'name': getattr(pack, 'name', 'N/A'),
                'description': getattr(pack, 'description', 'N/A'),
                'version': getattr(pack, 'version', 'N/A'),
                'components': [],
                'statistics': {
                    'total_components': 0,
                    'processes': 0,
                    'connections': 0,
                    'maps': 0,
                    'profiles': 0,
                    'other': 0
                }
            }
            
            # Query components associated with this pack
            if self.verbose:
                print("   Analyzing pack components...")
            
            components = self._get_pack_components(pack_id)
            analysis['components'] = components
            analysis['statistics']['total_components'] = len(components)
            
            # Count component types
            for comp in components:
                comp_type = comp.get('type', 'other').lower()
                if comp_type == 'process':
                    analysis['statistics']['processes'] += 1
                elif comp_type == 'connection':
                    analysis['statistics']['connections'] += 1
                elif comp_type == 'map':
                    analysis['statistics']['maps'] += 1
                elif comp_type == 'profile':
                    analysis['statistics']['profiles'] += 1
                else:
                    analysis['statistics']['other'] += 1
            
            print(f"✅ Analysis complete: {len(components)} components found")
            return analysis
            
        except Exception as e:
            print(f"❌ Error analyzing pack: {e}")
            if self.verbose:
                import traceback
                traceback.print_exc()
            return {}
    
    def _get_pack_components(self, pack_id: str) -> List[Dict[str, Any]]:
        """Get components belonging to an integration pack"""
        try:
            # Note: This would typically filter by pack association
            # For now, we'll query all components as an example
            query_config = ComponentMetadataQueryConfig()
            result = self.sdk.component_metadata.query_component_metadata(request_body=query_config)
            
            components = []
            if result and hasattr(result, 'result') and result.result:
                for comp in result.result[:20]:  # Limit for example
                    comp_info = {
                        'id': getattr(comp, 'id_', 'N/A'),
                        'name': getattr(comp, 'name', 'N/A'),
                        'type': getattr(comp, 'type', 'N/A'),
                        'version': getattr(comp, 'current_version', 'N/A'),
                        'folder': getattr(comp, 'folder_full_path', 'N/A')
                    }
                    components.append(comp_info)
            
            return components
            
        except Exception as e:
            if self.verbose:
                print(f"   Error getting components: {e}")
            return []
    
    def generate_inventory_report(self, output_file: Optional[str] = None) -> Dict[str, Any]:
        """
        Generate an inventory report of all integration packs
        
        Args:
            output_file: Optional file to save report
            
        Returns:
            Inventory report data
        """
        print("\n📊 Generating integration pack inventory report...")
        
        report = {
            'generated': datetime.now().isoformat(),
            'total_packs': 0,
            'packs': [],
            'statistics': {
                'by_vendor': {},
                'by_version': {},
                'total_components': 0
            }
        }
        
        # Get all packs
        packs = self.list_integration_packs(limit=50)
        report['total_packs'] = len(packs)
        
        # Analyze each pack
        for pack in packs:
            if self.verbose:
                print(f"   Analyzing {pack['name']}...")
            
            # Add to report
            report['packs'].append(pack)
            
            # Update statistics
            vendor = pack.get('vendor', 'Unknown')
            version = pack.get('version', 'Unknown')
            
            report['statistics']['by_vendor'][vendor] = \
                report['statistics']['by_vendor'].get(vendor, 0) + 1
            report['statistics']['by_version'][version] = \
                report['statistics']['by_version'].get(version, 0) + 1
        
        # Save report if requested
        if output_file:
            with open(output_file, 'w') as f:
                json.dump(report, f, indent=2)
            print(f"✅ Report saved to: {output_file}")
        
        print(f"✅ Inventory complete: {report['total_packs']} packs")
        return report
    
    def find_pack_dependencies(self, pack_id: str) -> Dict[str, Any]:
        """
        Find dependencies for an integration pack
        
        Args:
            pack_id: Integration pack ID
            
        Returns:
            Dependency information
        """
        print(f"\n🔗 Finding dependencies for pack: {pack_id}")
        
        dependencies = {
            'pack_id': pack_id,
            'internal_dependencies': [],
            'external_dependencies': [],
            'required_connections': [],
            'required_profiles': []
        }
        
        # Get pack components
        components = self._get_pack_components(pack_id)
        
        # Analyze component types to infer dependencies
        for comp in components:
            comp_type = comp.get('type', '').lower()
            
            if comp_type == 'connection':
                dependencies['required_connections'].append(comp['name'])
            elif comp_type == 'profile':
                dependencies['required_profiles'].append(comp['name'])
        
        print(f"✅ Found {len(dependencies['required_connections'])} connection dependencies")
        print(f"✅ Found {len(dependencies['required_profiles'])} profile dependencies")
        
        return dependencies


def main():
    """Main function"""
    parser = argparse.ArgumentParser(
        description='Analyze Boomi integration packs',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # List all integration packs
  %(prog)s --list
  
  # Analyze a specific pack
  %(prog)s --analyze PACK_ID
  
  # Generate inventory report
  %(prog)s --inventory --output report.json
  
  # Find pack dependencies
  %(prog)s --dependencies PACK_ID
  
  # List with limit
  %(prog)s --list --limit 20
  
  # Verbose output
  %(prog)s --list --verbose
"""
    )
    
    # Operations
    parser.add_argument('--list', action='store_true',
                       help='List integration packs')
    parser.add_argument('--analyze', metavar='ID',
                       help='Analyze specific pack')
    parser.add_argument('--inventory', action='store_true',
                       help='Generate inventory report')
    parser.add_argument('--dependencies', metavar='ID',
                       help='Find pack dependencies')
    
    # Options
    parser.add_argument('--limit', type=int, default=10,
                       help='Limit results (default: 10)')
    parser.add_argument('--output', metavar='FILE',
                       help='Output file for reports')
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='Enable verbose output')
    
    args = parser.parse_args()
    
    # Check for at least one operation
    if not any([args.list, args.analyze, args.inventory, args.dependencies]):
        parser.print_help()
        return
    
    # Initialize analyzer
    analyzer = IntegrationPackAnalyzer(verbose=args.verbose)
    
    # Execute operations
    if args.list:
        packs = analyzer.list_integration_packs(limit=args.limit)
        
        if packs:
            print("\n📦 Integration Packs:")
            for i, pack in enumerate(packs, 1):
                print(f"\n{i}. {pack['name']}")
                print(f"   ID: {pack['id']}")
                print(f"   Version: {pack['version']}")
                print(f"   Vendor: {pack['vendor']}")
                description = pack.get('description', 'N/A')
                if description and description != 'N/A' and len(description) > 100:
                    print(f"   Description: {description[:100]}...")
                else:
                    print(f"   Description: {description}")
    
    elif args.analyze:
        analysis = analyzer.analyze_pack(args.analyze)
        
        if analysis:
            print("\n📊 Pack Analysis:")
            print(f"   Name: {analysis['name']}")
            print(f"   Version: {analysis['version']}")
            print(f"   Description: {analysis['description']}")
            print(f"\n   Component Statistics:")
            for key, value in analysis['statistics'].items():
                print(f"      {key}: {value}")
    
    elif args.inventory:
        report = analyzer.generate_inventory_report(output_file=args.output)
        
        print("\n📊 Inventory Summary:")
        print(f"   Total Packs: {report['total_packs']}")
        print(f"   By Vendor:")
        for vendor, count in report['statistics']['by_vendor'].items():
            print(f"      {vendor}: {count}")
    
    elif args.dependencies:
        deps = analyzer.find_pack_dependencies(args.dependencies)
        
        print("\n🔗 Dependencies:")
        print(f"   Required Connections: {len(deps['required_connections'])}")
        for conn in deps['required_connections']:
            print(f"      - {conn}")
        print(f"   Required Profiles: {len(deps['required_profiles'])}")
        for prof in deps['required_profiles']:
            print(f"      - {prof}")


if __name__ == '__main__':
    main()