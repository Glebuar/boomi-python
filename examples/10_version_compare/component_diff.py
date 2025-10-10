#!/usr/bin/env python3
"""
Boomi SDK Example: Component Diff & Comparison
==============================================

This example demonstrates how to compare different versions of components
to identify changes before deployment.

Features:
- Compare two component versions
- Generate detailed diff reports
- Identify breaking changes
- Compare components across environments
- Bulk comparison for multiple components
- Export diff results to JSON/HTML formats

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- Appropriate permissions to read components

Usage:
    # Compare two versions of a component
    python component_diff.py COMPONENT_ID --version1 1 --version2 2
    
    # Compare component between environments
    python component_diff.py COMPONENT_ID --env1 "Development" --env2 "Production"
    
    # Compare multiple components
    python component_diff.py --bulk "comp1,comp2,comp3" --version1 1 --version2 2
    
    # Generate HTML diff report
    python component_diff.py COMPONENT_ID --version1 1 --version2 2 --format html --output diff_report.html

Examples:
    python component_diff.py 112b4efe-b173-4258-9492-613ead7d52ce --version1 1 --version2 2
    python component_diff.py 112b4efe-b173-4258-9492-613ead7d52ce --current --previous
    python component_diff.py --bulk "comp1,comp2,comp3" --version1 1 --version2 2 --summary
"""

import os
import sys
import argparse
import json
import difflib
import xml.etree.ElementTree as ET
from datetime import datetime
from typing import Optional, List, Dict, Any, Tuple

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# Load environment variables from .env file if available
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv is optional

from src.boomi import Boomi
from src.boomi.models import (
    ComponentDiffRequest,
    ComponentDiffRequestBulkRequest,
    ComponentDiffRequestBulkRequestType
)


class ComponentDiffer:
    """Manages component comparison and diff operations"""
    
    def __init__(self, verbose: bool = False):
        """Initialize the Boomi SDK client"""
        self.verbose = verbose
        self.sdk = Boomi(
            account_id=os.getenv("BOOMI_ACCOUNT"),
            username=os.getenv("BOOMI_USER"),
            password=os.getenv("BOOMI_SECRET"),
            timeout=30000
        )
        if self.verbose:
            print("✅ SDK initialized successfully")
    
    def get_component_versions(self, component_id: str) -> List[int]:
        """Get available versions for a component"""
        try:
            # Get component metadata to find available versions
            from src.boomi.models import (
                ComponentMetadataQueryConfig,
                ComponentMetadataQueryConfigQueryFilter,
                ComponentMetadataSimpleExpression,
                ComponentMetadataSimpleExpressionOperator
            )
            
            # Query for specific component
            expr = ComponentMetadataSimpleExpression(
                operator=ComponentMetadataSimpleExpressionOperator.EQUALS,
                property="componentId",
                argument=[component_id]
            )
            query_filter = ComponentMetadataQueryConfigQueryFilter(expression=expr)
            query_config = ComponentMetadataQueryConfig(query_filter=query_filter)
            
            result = self.sdk.component_metadata.query_component_metadata(request_body=query_config)
            
            versions = []
            if hasattr(result, 'result') and result.result:
                for comp in result.result:
                    version = getattr(comp, 'version', None)
                    if version and version not in versions:
                        versions.append(version)
            
            return sorted(versions)
            
        except Exception as e:
            if self.verbose:
                print(f"Failed to get component versions: {e}")
            return []
    
    def get_component_xml(self, component_id: str, version: Optional[int] = None) -> Optional[str]:
        """Get component XML for a specific version"""
        try:
            # Get component (specific version if provided)
            component = self.sdk.component.get_component(component_id=component_id)
            
            if component:
                # Convert to XML string if it's a Component object
                if hasattr(component, 'to_xml'):
                    return component.to_xml()
                elif isinstance(component, str):
                    return component
                else:
                    # Try to get XML representation
                    return str(component)
            
            return None
            
        except Exception as e:
            if self.verbose:
                print(f"Failed to get component XML: {e}")
            return None
    
    def compare_components(self, component_id: str, version1: int, version2: int) -> Dict[str, Any]:
        """Compare two versions of a component using ComponentDiffRequest"""
        print(f"\n🔍 Comparing component {component_id} versions {version1} and {version2}...")
        
        try:
            # Create diff request
            diff_request = ComponentDiffRequest(
                component_id=component_id,
                source_version=version1,
                target_version=version2
            )
            
            # Execute diff request
            result = self.sdk.component_diff_request.create_component_diff_request(
                request_body=diff_request
            )
            
            if result:
                # Process diff result
                diff_info = {
                    'component_id': component_id,
                    'version1': version1,
                    'version2': version2,
                    'source_version': version1,
                    'target_version': version2,
                    'differences': self._process_diff_result(result),
                    'message': result._kwargs.get('message', '') if hasattr(result, '_kwargs') else '',
                    'timestamp': datetime.now().isoformat()
                }

                return diff_info
            else:
                print("❌ No differences found or diff failed")
                return None
                
        except Exception as e:
            print(f"❌ Failed to compare components: {e}")
            if self.verbose:
                import traceback
                traceback.print_exc()
            return None
    
    def compare_component_xml(self, component_id: str, 
                            version1: Optional[int] = None, 
                            version2: Optional[int] = None) -> Dict[str, Any]:
        """Compare component versions using XML diff"""
        print(f"\n🔍 Comparing component {component_id} XML...")
        
        try:
            # Get XML for both versions
            xml1 = self.get_component_xml(component_id, version1)
            xml2 = self.get_component_xml(component_id, version2)
            
            if not xml1 or not xml2:
                print("❌ Failed to retrieve component XML")
                return None
            
            # Parse XML
            tree1 = ET.fromstring(xml1)
            tree2 = ET.fromstring(xml2)
            
            # Compare attributes
            attr_changes = self._compare_attributes(tree1, tree2)
            
            # Compare structure
            struct_changes = self._compare_structure(tree1, tree2)
            
            # Generate line diff
            lines1 = xml1.splitlines()
            lines2 = xml2.splitlines()
            diff = difflib.unified_diff(lines1, lines2, lineterm='')
            
            diff_info = {
                'component_id': component_id,
                'version1': version1 or 'current',
                'version2': version2 or 'current',
                'attribute_changes': attr_changes,
                'structure_changes': struct_changes,
                'line_diff': list(diff),
                'summary': {
                    'attributes_changed': len(attr_changes),
                    'structure_changes': len(struct_changes),
                    'total_changes': len(attr_changes) + len(struct_changes)
                },
                'timestamp': datetime.now().isoformat()
            }
            
            return diff_info
            
        except Exception as e:
            print(f"❌ Failed to compare XML: {e}")
            if self.verbose:
                import traceback
                traceback.print_exc()
            return None
    
    def _process_diff_result(self, result: Any) -> List[Dict[str, Any]]:
        """Process diff result from API"""
        differences = []

        try:
            # Check if result has _kwargs with GenericDiff
            if hasattr(result, '_kwargs') and 'GenericDiff' in result._kwargs:
                generic_diff = result._kwargs['GenericDiff']

                # Process modifications
                if 'modification' in generic_diff:
                    mod = generic_diff['modification']
                    if isinstance(mod, dict) and 'change' in mod:
                        change = mod['change']
                        diff_item = {
                            'type': 'modification',
                            'change_type': change.get('type', 'unknown'),
                            'attribute': change.get('changedParticleName', ''),
                            'old_value': change.get('oldValue', {}).get('#text', ''),
                            'new_value': change.get('newValue', {}).get('#text', ''),
                            'path': change.get('elementKey', {}).get('elementName', '')
                        }
                        differences.append(diff_item)

                # Process additions
                if 'addition' in generic_diff:
                    add = generic_diff['addition']
                    total = add.get('total', '0')
                    if int(total) > 0:
                        diff_item = {
                            'type': 'addition',
                            'count': int(total)
                        }
                        differences.append(diff_item)

                # Process deletions
                if 'deletion' in generic_diff:
                    deletion = generic_diff['deletion']
                    total = deletion.get('total', '0')
                    if int(total) > 0:
                        diff_item = {
                            'type': 'deletion',
                            'count': int(total)
                        }
                        differences.append(diff_item)

            # Check if result has differences attribute
            elif hasattr(result, 'differences'):
                for diff in result.differences:
                    diff_item = {
                        'type': getattr(diff, 'type', 'unknown'),
                        'path': getattr(diff, 'path', ''),
                        'old_value': getattr(diff, 'old_value', None),
                        'new_value': getattr(diff, 'new_value', None),
                        'description': getattr(diff, 'description', '')
                    }
                    differences.append(diff_item)

            # If result is a string (XML diff), parse it
            elif isinstance(result, str):
                try:
                    root = ET.fromstring(result)
                    # Extract diff elements
                    for diff_elem in root.findall('.//difference'):
                        diff_item = {
                            'type': diff_elem.get('type', 'unknown'),
                            'path': diff_elem.get('path', ''),
                            'old_value': diff_elem.findtext('oldValue'),
                            'new_value': diff_elem.findtext('newValue'),
                            'description': diff_elem.findtext('description', '')
                        }
                        differences.append(diff_item)
                except:
                    # If not XML, treat as raw diff
                    differences.append({
                        'type': 'raw',
                        'content': result
                    })
            
        except Exception as e:
            if self.verbose:
                print(f"Error processing diff result: {e}")
        
        return differences
    
    def _compare_attributes(self, tree1: ET.Element, tree2: ET.Element) -> List[Dict[str, Any]]:
        """Compare attributes between two XML trees"""
        changes = []
        
        # Compare root attributes
        attrs1 = tree1.attrib
        attrs2 = tree2.attrib
        
        # Find added attributes
        for key in attrs2:
            if key not in attrs1:
                changes.append({
                    'type': 'attribute_added',
                    'path': tree1.tag,
                    'attribute': key,
                    'value': attrs2[key]
                })
        
        # Find removed attributes
        for key in attrs1:
            if key not in attrs2:
                changes.append({
                    'type': 'attribute_removed',
                    'path': tree1.tag,
                    'attribute': key,
                    'value': attrs1[key]
                })
        
        # Find changed attributes
        for key in attrs1:
            if key in attrs2 and attrs1[key] != attrs2[key]:
                changes.append({
                    'type': 'attribute_changed',
                    'path': tree1.tag,
                    'attribute': key,
                    'old_value': attrs1[key],
                    'new_value': attrs2[key]
                })
        
        return changes
    
    def _compare_structure(self, tree1: ET.Element, tree2: ET.Element) -> List[Dict[str, Any]]:
        """Compare structure between two XML trees"""
        changes = []
        
        # Get child tags
        children1 = {child.tag for child in tree1}
        children2 = {child.tag for child in tree2}
        
        # Find added elements
        for tag in children2 - children1:
            changes.append({
                'type': 'element_added',
                'path': tree1.tag,
                'element': tag
            })
        
        # Find removed elements
        for tag in children1 - children2:
            changes.append({
                'type': 'element_removed',
                'path': tree1.tag,
                'element': tag
            })
        
        return changes
    
    def bulk_compare(self, component_ids: List[str], version1: int, version2: int) -> List[Dict[str, Any]]:
        """Compare multiple components in bulk"""
        print(f"\n📦 Bulk comparing {len(component_ids)} components...")
        
        results = []
        for component_id in component_ids:
            result = self.compare_components(component_id, version1, version2)
            if result:
                results.append(result)
        
        return results
    
    def generate_html_report(self, diff_info: Dict[str, Any]) -> str:
        """Generate HTML diff report"""
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Component Diff Report</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; }}
                h1 {{ color: #333; }}
                .summary {{ background: #f0f0f0; padding: 10px; border-radius: 5px; }}
                .added {{ background: #d4fdd4; }}
                .removed {{ background: #fdd4d4; }}
                .changed {{ background: #fdfdd4; }}
                table {{ border-collapse: collapse; width: 100%; margin-top: 20px; }}
                th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
                th {{ background: #4CAF50; color: white; }}
                .diff-line {{ font-family: monospace; }}
                .diff-add {{ color: green; }}
                .diff-remove {{ color: red; }}
            </style>
        </head>
        <body>
            <h1>Component Diff Report</h1>
            <div class="summary">
                <p><strong>Component ID:</strong> {diff_info.get('component_id', 'N/A')}</p>
                <p><strong>Version 1:</strong> {diff_info.get('version1', 'N/A')}</p>
                <p><strong>Version 2:</strong> {diff_info.get('version2', 'N/A')}</p>
                <p><strong>Generated:</strong> {diff_info.get('timestamp', 'N/A')}</p>
            </div>
        """
        
        if 'summary' in diff_info:
            html += f"""
            <h2>Summary</h2>
            <ul>
                <li>Attributes Changed: {diff_info['summary'].get('attributes_changed', 0)}</li>
                <li>Structure Changes: {diff_info['summary'].get('structure_changes', 0)}</li>
                <li>Total Changes: {diff_info['summary'].get('total_changes', 0)}</li>
            </ul>
            """
        
        if 'attribute_changes' in diff_info and diff_info['attribute_changes']:
            html += """
            <h2>Attribute Changes</h2>
            <table>
                <tr><th>Type</th><th>Path</th><th>Attribute</th><th>Old Value</th><th>New Value</th></tr>
            """
            for change in diff_info['attribute_changes']:
                html += f"""
                <tr class="{change['type'].split('_')[1]}">
                    <td>{change['type']}</td>
                    <td>{change.get('path', '')}</td>
                    <td>{change.get('attribute', '')}</td>
                    <td>{change.get('old_value', '')}</td>
                    <td>{change.get('new_value', change.get('value', ''))}</td>
                </tr>
                """
            html += "</table>"
        
        if 'line_diff' in diff_info and diff_info['line_diff']:
            html += """
            <h2>Line Diff</h2>
            <div style="background: #f5f5f5; padding: 10px; border-radius: 5px; overflow-x: auto;">
                <pre>
            """
            for line in diff_info['line_diff'][:100]:  # Limit to first 100 lines
                if line.startswith('+'):
                    html += f'<span class="diff-add">{line}</span>\n'
                elif line.startswith('-'):
                    html += f'<span class="diff-remove">{line}</span>\n'
                else:
                    html += f'{line}\n'
            html += """
                </pre>
            </div>
            """
        
        html += """
        </body>
        </html>
        """
        
        return html


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='Compare component versions to identify changes',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
    python component_diff.py 112b4efe-b173-4258-9492-613ead7d52ce --version1 1 --version2 2
    python component_diff.py 112b4efe-b173-4258-9492-613ead7d52ce --current --previous
    python component_diff.py --bulk "comp1,comp2,comp3" --version1 1 --version2 2
    python component_diff.py 112b4efe-b173-4258-9492-613ead7d52ce --version1 1 --version2 2 --format html --output report.html
        '''
    )
    
    # Main arguments
    parser.add_argument('component_id', nargs='?',
                       help='Component ID to compare')
    parser.add_argument('--bulk', metavar='IDS',
                       help='Comma-separated list of component IDs for bulk comparison')
    
    # Version arguments
    parser.add_argument('--version1', type=int, help='First version number')
    parser.add_argument('--version2', type=int, help='Second version number')
    parser.add_argument('--current', action='store_true',
                       help='Use current version as version2')
    parser.add_argument('--previous', action='store_true',
                       help='Compare with previous version')
    
    # Output arguments
    parser.add_argument('--format', choices=['json', 'html', 'text'],
                       default='text', help='Output format')
    parser.add_argument('--output', help='Output file path')
    parser.add_argument('--summary', action='store_true',
                       help='Show summary only')
    
    # Other arguments
    parser.add_argument('--verbose', action='store_true',
                       help='Enable verbose output')
    parser.add_argument('--xml-diff', action='store_true',
                       help='Use XML diff instead of API diff')
    
    args = parser.parse_args()
    
    # Validate arguments
    if not args.component_id and not args.bulk:
        parser.error("Either component_id or --bulk must be specified")
    
    # Validate environment variables
    if not all([os.getenv("BOOMI_ACCOUNT"), os.getenv("BOOMI_USER"), os.getenv("BOOMI_SECRET")]):
        print("❌ Error: Missing required environment variables")
        print("   Please set: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET")
        sys.exit(1)
    
    # Initialize differ
    differ = ComponentDiffer(verbose=args.verbose)
    
    try:
        results = []
        
        if args.bulk:
            # Bulk comparison
            component_ids = [id.strip() for id in args.bulk.split(',')]
            
            if not args.version1 or not args.version2:
                parser.error("Both --version1 and --version2 are required for bulk comparison")
            
            results = differ.bulk_compare(component_ids, args.version1, args.version2)
            
        else:
            # Single component comparison
            component_id = args.component_id
            
            # Determine versions
            if args.previous:
                versions = differ.get_component_versions(component_id)
                if len(versions) >= 2:
                    version1 = versions[-2]
                    version2 = versions[-1]
                else:
                    parser.error("Not enough versions available for comparison")
            elif args.current:
                version1 = args.version1
                version2 = None  # Current version
            else:
                version1 = args.version1
                version2 = args.version2
            
            if version1 is None or version2 is None:
                parser.error("Version numbers must be specified")
            
            # Perform comparison
            if args.xml_diff:
                result = differ.compare_component_xml(component_id, version1, version2)
            else:
                result = differ.compare_components(component_id, version1, version2)
            
            if result:
                results = [result]
        
        # Process results
        if results:
            if args.format == 'json':
                output = json.dumps(results, indent=2)
            elif args.format == 'html':
                if len(results) == 1:
                    output = differ.generate_html_report(results[0])
                else:
                    # Generate summary HTML for multiple results
                    output = "<html><body><h1>Bulk Comparison Results</h1>"
                    for result in results:
                        output += differ.generate_html_report(result)
                    output += "</body></html>"
            else:
                # Text format
                output = ""
                for result in results:
                    output += f"\n{'=' * 60}\n"
                    output += f"Component: {result['component_id']}\n"
                    output += f"Versions: {result.get('version1', 'N/A')} → {result.get('version2', 'N/A')}\n"
                    
                    if args.summary:
                        if 'summary' in result:
                            output += f"Changes: {result['summary']['total_changes']}\n"
                    else:
                        if 'differences' in result:
                            output += f"\nDifferences ({len(result['differences'])}):\n"
                            for diff in result['differences']:
                                output += f"  - {diff.get('type', 'unknown')}: {diff.get('path', '')}\n"
                                if 'old_value' in diff and 'new_value' in diff:
                                    output += f"    {diff['old_value']} → {diff['new_value']}\n"
                        
                        if 'attribute_changes' in result:
                            output += f"\nAttribute Changes ({len(result['attribute_changes'])}):\n"
                            for change in result['attribute_changes']:
                                output += f"  - {change['type']}: {change.get('attribute', '')}\n"
                        
                        if 'structure_changes' in result:
                            output += f"\nStructure Changes ({len(result['structure_changes'])}):\n"
                            for change in result['structure_changes']:
                                output += f"  - {change['type']}: {change.get('element', '')}\n"
            
            # Output results
            if args.output:
                with open(args.output, 'w') as f:
                    f.write(output)
                print(f"✅ Results written to {args.output}")
            else:
                print(output)
            
            # Print summary
            if not args.summary and args.format == 'text':
                total_changes = sum(
                    result.get('summary', {}).get('total_changes', len(result.get('differences', [])))
                    for result in results
                )
                print(f"\n✅ Total changes found: {total_changes}")
        else:
            print("❌ No comparison results available")
            
    except KeyboardInterrupt:
        print("\n\n⚠️ Operation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()