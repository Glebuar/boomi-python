#!/usr/bin/env python3
"""
Boomi SDK Example: Component Dependencies Analyzer
==================================================

This example demonstrates how to analyze component dependencies to understand
the impact of changes and maintain integration integrity.

Features:
- Find all components that reference a target component
- Build complete dependency graphs
- Identify circular dependencies
- Perform impact analysis for changes
- Export dependency maps in various formats
- Batch analysis for multiple components
- Visualize dependency relationships

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- Appropriate permissions to read components and references

IMPORTANT: Default Component IDs
---------------------------------
This example includes hardcoded component IDs for demonstration purposes.
These are actual components from a test account that have real dependencies:
- 0864f99a-917f-457d-abc6-2762c0bb9b88: "Boomi Hiring to HR Employee Details Map" (2 dependencies)
- a2a93fdc-682a-475d-afe5-aaac8a33df63: "[Intapp Walls] Create Client" (1 dependency)

**REPLACE THESE WITH YOUR OWN COMPONENT IDs FOR PRODUCTION USE**

Usage:
    # Find what uses a component
    python analyze_dependencies.py COMPONENT_ID --what-uses
    
    # Find what a component uses (requires parentVersion)
    python analyze_dependencies.py COMPONENT_ID --what-it-uses
    
    # Build full dependency graph
    python analyze_dependencies.py COMPONENT_ID --full-graph
    
    # Analyze impact of changes
    python analyze_dependencies.py COMPONENT_ID --impact-analysis
    
    # Export dependency map
    python analyze_dependencies.py COMPONENT_ID --export json --output deps.json
    
    # Batch analysis
    python analyze_dependencies.py --batch "comp1,comp2,comp3" --what-uses

Examples with Real Components (from test account):
    # Component with 2 dependencies
    python analyze_dependencies.py 0864f99a-917f-457d-abc6-2762c0bb9b88 --what-uses
    
    # Component with 1 dependency
    python analyze_dependencies.py a2a93fdc-682a-475d-afe5-aaac8a33df63 --what-uses
    
    # Full dependency graph
    python analyze_dependencies.py 0864f99a-917f-457d-abc6-2762c0bb9b88 --full-graph --depth 3
    
    # Impact analysis for deletion
    python analyze_dependencies.py 0864f99a-917f-457d-abc6-2762c0bb9b88 --impact-analysis --change-type delete
    
    # Batch analysis
    python analyze_dependencies.py --batch "0864f99a-917f-457d-abc6-2762c0bb9b88,a2a93fdc-682a-475d-afe5-aaac8a33df63" --what-uses
"""

import os
import sys
import argparse
import json
from datetime import datetime
from typing import Optional, List, Dict, Any, Set, Tuple
from collections import defaultdict, deque

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
    ComponentReferenceQueryConfig,
    ComponentReferenceQueryConfigQueryFilter,
    ComponentReferenceSimpleExpression,
    ComponentReferenceSimpleExpressionOperator,
    ComponentReferenceSimpleExpressionProperty,
    ComponentReferenceGroupingExpression,
    ComponentReferenceGroupingExpressionOperator
)


class DependencyAnalyzer:
    """Analyzes component dependencies and relationships"""
    
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
        
        # Cache for component metadata
        self.component_cache = {}
        self.dependency_cache = {}
    
    def find_what_uses(self, component_id: str) -> List[Dict[str, Any]]:
        """Find all components that reference/use the target component"""
        print(f"\n🔍 Finding components that use: {component_id}")
        
        try:
            # Check cache first
            cache_key = f"uses_{component_id}"
            if cache_key in self.dependency_cache:
                return self.dependency_cache[cache_key]
            
            # Query for components that reference this component
            simple_expression = ComponentReferenceSimpleExpression(
                operator=ComponentReferenceSimpleExpressionOperator.EQUALS,
                property=ComponentReferenceSimpleExpressionProperty.COMPONENTID,
                argument=[component_id]
            )
            
            query_filter = ComponentReferenceQueryConfigQueryFilter(
                expression=simple_expression
            )
            
            query_config = ComponentReferenceQueryConfig(
                query_filter=query_filter
            )
            
            result = self.sdk.component_reference.query_component_reference(
                request_body=query_config
            )
            
            components = []
            # SDK is now fixed - access result.result for ComponentReference objects
            if hasattr(result, 'result') and result.result:
                for component_ref in result.result:
                    if hasattr(component_ref, 'references') and component_ref.references:
                        # SDK fix now properly handles single reference as dict
                        for ref in component_ref.references:
                            component_info = {
                                'component_id': getattr(ref, 'parent_component_id', 'N/A'),
                                'component_name': f"Parent Component {getattr(ref, 'parent_component_id', 'N/A')}",
                                'component_type': getattr(ref, 'type_', 'N/A'),
                                'reference_type': getattr(ref, 'type_', 'N/A'),
                                'reference_count': 1,
                                'parent_version': getattr(ref, 'parent_version', 'N/A')
                            }
                            components.append(component_info)
                            
                            # Add to cache
                            self.component_cache[component_info['component_id']] = component_info
            
            # Cache the result
            self.dependency_cache[cache_key] = components
            return components
            
        except Exception as e:
            print(f"❌ Failed to find what uses component: {e}")
            if self.verbose:
                import traceback
                traceback.print_exc()
            return []
    
    def find_what_it_uses(self, component_id: str) -> List[Dict[str, Any]]:
        """Find all components that are used by the target component"""
        print(f"\n🔍 Finding components used by: {component_id}")
        
        try:
            # Check cache first
            cache_key = f"used_by_{component_id}"
            if cache_key in self.dependency_cache:
                return self.dependency_cache[cache_key]
            
            # Query for components referenced by this component
            simple_expression = ComponentReferenceSimpleExpression(
                operator=ComponentReferenceSimpleExpressionOperator.EQUALS,
                property=ComponentReferenceSimpleExpressionProperty.PARENTCOMPONENTID,
                argument=[component_id]
            )
            
            query_filter = ComponentReferenceQueryConfigQueryFilter(
                expression=simple_expression
            )
            
            query_config = ComponentReferenceQueryConfig(
                query_filter=query_filter
            )
            
            result = self.sdk.component_reference.query_component_reference(
                request_body=query_config
            )
            
            components = []
            # SDK is now fixed - access result.result for ComponentReference objects
            if hasattr(result, 'result') and result.result:
                for component_ref in result.result:
                    if hasattr(component_ref, 'references') and component_ref.references:
                        # SDK fix now properly handles single reference as dict
                        for ref in component_ref.references:
                            component_info = {
                                'component_id': getattr(ref, 'component_id', 'N/A'),
                                'component_name': f"Component {getattr(ref, 'component_id', 'N/A')}",
                                'component_type': getattr(ref, 'type_', 'N/A'),
                                'reference_type': getattr(ref, 'type_', 'N/A'),
                                'reference_count': 1,
                                'parent_component_id': getattr(ref, 'parent_component_id', 'N/A'),
                                'parent_version': getattr(ref, 'parent_version', 'N/A')
                            }
                            components.append(component_info)
                            
                            # Add to cache
                            self.component_cache[component_info['component_id']] = component_info
            
            # Cache the result
            self.dependency_cache[cache_key] = components
            return components
            
        except Exception as e:
            print(f"❌ Failed to find what component uses: {e}")
            if self.verbose:
                import traceback
                traceback.print_exc()
            return []
    
    def build_dependency_graph(self, component_id: str, depth: int = 2, 
                             direction: str = 'both') -> Dict[str, Any]:
        """Build a complete dependency graph for a component"""
        print(f"\n🔍 Building dependency graph for: {component_id} (depth: {depth})")
        
        graph = {
            'root': component_id,
            'nodes': {},
            'edges': [],
            'statistics': {
                'total_nodes': 0,
                'total_edges': 0,
                'max_depth_reached': 0,
                'circular_dependencies': []
            }
        }
        
        visited = set()
        queue = deque([(component_id, 0)])
        
        while queue:
            current_id, current_depth = queue.popleft()
            
            if current_id in visited or current_depth > depth:
                continue
            
            visited.add(current_id)
            
            # Add node to graph
            if current_id not in graph['nodes']:
                graph['nodes'][current_id] = {
                    'id': current_id,
                    'depth': current_depth,
                    'uses': [],
                    'used_by': [],
                    'metadata': self.component_cache.get(current_id, {})
                }
            
            graph['statistics']['max_depth_reached'] = max(
                graph['statistics']['max_depth_reached'], 
                current_depth
            )
            
            # Get dependencies based on direction
            if direction in ['both', 'upstream']:
                # What uses this component (upstream dependencies)
                upstream = self.find_what_uses(current_id)
                for comp in upstream:
                    comp_id = comp['component_id']
                    
                    # Add edge
                    edge = {'from': comp_id, 'to': current_id, 'type': 'uses'}
                    if edge not in graph['edges']:
                        graph['edges'].append(edge)
                    
                    # Update node relationships
                    if comp_id not in graph['nodes'][current_id]['used_by']:
                        graph['nodes'][current_id]['used_by'].append(comp_id)
                    
                    # Add to queue for further exploration
                    if comp_id not in visited and current_depth < depth:
                        queue.append((comp_id, current_depth + 1))
            
            if direction in ['both', 'downstream']:
                # What this component uses (downstream dependencies)
                downstream = self.find_what_it_uses(current_id)
                for comp in downstream:
                    comp_id = comp['component_id']
                    
                    # Add edge
                    edge = {'from': current_id, 'to': comp_id, 'type': 'uses'}
                    if edge not in graph['edges']:
                        graph['edges'].append(edge)
                    
                    # Update node relationships
                    if comp_id not in graph['nodes'][current_id]['uses']:
                        graph['nodes'][current_id]['uses'].append(comp_id)
                    
                    # Add to queue for further exploration
                    if comp_id not in visited and current_depth < depth:
                        queue.append((comp_id, current_depth + 1))
        
        # Update statistics
        graph['statistics']['total_nodes'] = len(graph['nodes'])
        graph['statistics']['total_edges'] = len(graph['edges'])
        
        # Detect circular dependencies
        graph['statistics']['circular_dependencies'] = self._detect_cycles(graph)
        
        return graph
    
    def _detect_cycles(self, graph: Dict[str, Any]) -> List[List[str]]:
        """Detect circular dependencies in the graph"""
        cycles = []
        
        # Build adjacency list
        adj_list = defaultdict(list)
        for edge in graph['edges']:
            adj_list[edge['from']].append(edge['to'])
        
        # DFS to detect cycles
        visited = set()
        rec_stack = set()
        path = []
        
        def dfs(node):
            visited.add(node)
            rec_stack.add(node)
            path.append(node)
            
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
                elif neighbor in rec_stack:
                    # Found a cycle
                    cycle_start = path.index(neighbor)
                    cycle = path[cycle_start:] + [neighbor]
                    if cycle not in cycles:
                        cycles.append(cycle)
            
            path.pop()
            rec_stack.remove(node)
            return False
        
        # Check all nodes
        for node in graph['nodes']:
            if node not in visited:
                dfs(node)
        
        return cycles
    
    def analyze_impact(self, component_id: str, change_type: str = 'modify') -> Dict[str, Any]:
        """Analyze the impact of changes to a component"""
        print(f"\n🔍 Analyzing impact of {change_type} on: {component_id}")
        
        impact = {
            'component_id': component_id,
            'change_type': change_type,
            'direct_impact': [],
            'indirect_impact': [],
            'risk_level': 'low',
            'recommendations': [],
            'statistics': {}
        }
        
        # Get direct dependencies
        direct_deps = self.find_what_uses(component_id)
        impact['direct_impact'] = direct_deps
        
        # Get indirect dependencies (2 levels deep)
        indirect_deps = set()
        for dep in direct_deps:
            second_level = self.find_what_uses(dep['component_id'])
            for comp in second_level:
                if comp['component_id'] != component_id:  # Avoid cycles
                    indirect_deps.add(comp['component_id'])
        
        impact['indirect_impact'] = list(indirect_deps)
        
        # Calculate statistics
        impact['statistics'] = {
            'direct_components_affected': len(direct_deps),
            'indirect_components_affected': len(indirect_deps),
            'total_components_affected': len(direct_deps) + len(indirect_deps),
            'component_types_affected': len(set(d['component_type'] for d in direct_deps))
        }
        
        # Determine risk level
        total_affected = impact['statistics']['total_components_affected']
        if total_affected == 0:
            impact['risk_level'] = 'none'
        elif total_affected <= 3:
            impact['risk_level'] = 'low'
        elif total_affected <= 10:
            impact['risk_level'] = 'medium'
        else:
            impact['risk_level'] = 'high'
        
        # Generate recommendations
        if change_type == 'delete':
            if total_affected > 0:
                impact['recommendations'].append(
                    f"⚠️ Cannot safely delete: {total_affected} components depend on this"
                )
                impact['recommendations'].append(
                    "Consider deprecating instead of deleting"
                )
        elif change_type == 'modify':
            if total_affected > 10:
                impact['recommendations'].append(
                    "High impact change - consider phased rollout"
                )
            if total_affected > 0:
                impact['recommendations'].append(
                    f"Test all {total_affected} dependent components"
                )
                impact['recommendations'].append(
                    "Document changes and notify component owners"
                )
        
        return impact
    
    def batch_analyze(self, component_ids: List[str], 
                     analysis_type: str = 'what-uses') -> List[Dict[str, Any]]:
        """Perform batch analysis on multiple components"""
        print(f"\n📦 Batch analyzing {len(component_ids)} components...")
        
        results = []
        for component_id in component_ids:
            if analysis_type == 'what-uses':
                deps = self.find_what_uses(component_id)
                results.append({
                    'component_id': component_id,
                    'analysis_type': 'what-uses',
                    'dependencies': deps,
                    'count': len(deps)
                })
            elif analysis_type == 'what-it-uses':
                deps = self.find_what_it_uses(component_id)
                results.append({
                    'component_id': component_id,
                    'analysis_type': 'what-it-uses',
                    'dependencies': deps,
                    'count': len(deps)
                })
            elif analysis_type == 'impact':
                impact = self.analyze_impact(component_id)
                results.append(impact)
        
        return results
    
    def export_dependency_map(self, graph: Dict[str, Any], format: str) -> str:
        """Export dependency map in various formats"""
        if format == 'json':
            return json.dumps(graph, indent=2)
        
        elif format == 'dot':
            # GraphViz DOT format
            dot = "digraph Dependencies {\n"
            dot += "  rankdir=LR;\n"
            dot += "  node [shape=box];\n"
            
            # Add nodes
            for node_id, node_data in graph['nodes'].items():
                label = node_data['metadata'].get('component_name', node_id)
                dot += f'  "{node_id}" [label="{label}"];\n'
            
            # Add edges
            for edge in graph['edges']:
                dot += f'  "{edge["from"]}" -> "{edge["to"]}";\n'
            
            dot += "}\n"
            return dot
        
        elif format == 'mermaid':
            # Mermaid diagram format
            mermaid = "graph LR\n"
            
            # Add nodes and edges
            for edge in graph['edges']:
                from_label = graph['nodes'][edge['from']]['metadata'].get(
                    'component_name', edge['from']
                )
                to_label = graph['nodes'][edge['to']]['metadata'].get(
                    'component_name', edge['to']
                )
                mermaid += f"  {edge['from']}[{from_label}] --> {edge['to']}[{to_label}]\n"
            
            return mermaid
        
        else:
            return str(graph)


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='Analyze component dependencies and relationships',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
    python analyze_dependencies.py 112b4efe-b173-4258-9492-613ead7d52ce --what-uses
    python analyze_dependencies.py 112b4efe-b173-4258-9492-613ead7d52ce --what-it-uses
    python analyze_dependencies.py 112b4efe-b173-4258-9492-613ead7d52ce --full-graph --depth 3
    python analyze_dependencies.py 112b4efe-b173-4258-9492-613ead7d52ce --impact-analysis
    python analyze_dependencies.py --batch "comp1,comp2,comp3" --what-uses
        '''
    )
    
    # Main arguments
    parser.add_argument('component_id', nargs='?',
                       help='Component ID to analyze')
    parser.add_argument('--batch', metavar='IDS',
                       help='Comma-separated list of component IDs for batch analysis')
    
    # Analysis type arguments
    parser.add_argument('--what-uses', action='store_true',
                       help='Find components that use this component')
    parser.add_argument('--what-it-uses', action='store_true',
                       help='Find components that this component uses')
    parser.add_argument('--full-graph', action='store_true',
                       help='Build full dependency graph')
    parser.add_argument('--impact-analysis', action='store_true',
                       help='Analyze impact of changes')
    
    # Graph options
    parser.add_argument('--depth', type=int, default=2,
                       help='Depth for dependency graph (default: 2)')
    parser.add_argument('--direction', choices=['both', 'upstream', 'downstream'],
                       default='both', help='Direction for graph traversal')
    
    # Impact analysis options
    parser.add_argument('--change-type', choices=['modify', 'delete', 'deprecate'],
                       default='modify', help='Type of change for impact analysis')
    
    # Output options
    parser.add_argument('--export', choices=['json', 'dot', 'mermaid'],
                       help='Export format for dependency map')
    parser.add_argument('--output', help='Output file path')
    parser.add_argument('--verbose', action='store_true',
                       help='Enable verbose output')
    parser.add_argument('--json', action='store_true',
                       help='Output in JSON format')
    
    args = parser.parse_args()
    
    # Validate arguments - use default component ID if none provided
    if not args.component_id and not args.batch:
        # Default component with actual dependencies for demonstration
        # This is "Boomi Hiring to HR Employee Details Map" which has 2 parent components
        args.component_id = "0864f99a-917f-457d-abc6-2762c0bb9b88"
        print(f"ℹ️ No component_id provided, using default: {args.component_id}")
        print("   (Boomi Hiring to HR Employee Details Map - has 2 dependencies)")
        print("💡 IMPORTANT: Replace this component ID with your own component ID for production use")
        print("   Example: python analyze_dependencies.py YOUR_COMPONENT_ID --what-uses")
    
    # Set default operation if none specified
    if not any([args.what_uses, args.what_it_uses, args.full_graph, args.impact_analysis]):
        args.what_uses = True
        print("ℹ️ No operation specified, using default: --what-uses")
        print("💡 Available operations: --what-uses, --what-it-uses, --full-graph, --impact-analysis")
    
    # Validate environment variables
    if not all([os.getenv("BOOMI_ACCOUNT"), os.getenv("BOOMI_USER"), os.getenv("BOOMI_SECRET")]):
        print("❌ Error: Missing required environment variables")
        print("   Please set: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET")
        sys.exit(1)
    
    # Initialize analyzer
    analyzer = DependencyAnalyzer(verbose=args.verbose)
    
    try:
        results = None
        
        if args.batch:
            # Batch analysis
            component_ids = [id.strip() for id in args.batch.split(',')]
            
            if args.what_uses:
                results = analyzer.batch_analyze(component_ids, 'what-uses')
            elif args.what_it_uses:
                results = analyzer.batch_analyze(component_ids, 'what-it-uses')
            elif args.impact_analysis:
                results = analyzer.batch_analyze(component_ids, 'impact')
            else:
                parser.error("Specify analysis type for batch processing")
            
        else:
            # Single component analysis
            component_id = args.component_id
            
            if args.what_uses:
                deps = analyzer.find_what_uses(component_id)
                results = {
                    'component_id': component_id,
                    'analysis': 'what-uses',
                    'dependencies': deps,
                    'count': len(deps)
                }
                
            elif args.what_it_uses:
                deps = analyzer.find_what_it_uses(component_id)
                results = {
                    'component_id': component_id,
                    'analysis': 'what-it-uses',
                    'dependencies': deps,
                    'count': len(deps)
                }
                
            elif args.full_graph:
                graph = analyzer.build_dependency_graph(
                    component_id, 
                    depth=args.depth,
                    direction=args.direction
                )
                results = graph
                
            elif args.impact_analysis:
                impact = analyzer.analyze_impact(component_id, args.change_type)
                results = impact
                
            else:
                # Default to showing what uses the component
                deps = analyzer.find_what_uses(component_id)
                results = {
                    'component_id': component_id,
                    'analysis': 'what-uses',
                    'dependencies': deps,
                    'count': len(deps)
                }
        
        # Format and output results
        if results:
            if args.json or args.export == 'json':
                output = json.dumps(results, indent=2)
            elif args.export:
                output = analyzer.export_dependency_map(results, args.export)
            else:
                # Text format
                output = format_text_output(results)
            
            # Save or print output
            if args.output:
                with open(args.output, 'w') as f:
                    f.write(output)
                print(f"✅ Results written to {args.output}")
            else:
                print(output)
        else:
            print("❌ No results available")
            
    except KeyboardInterrupt:
        print("\n\n⚠️ Operation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


def format_text_output(results: Any) -> str:
    """Format results as human-readable text"""
    output = []
    
    if isinstance(results, dict):
        if 'analysis' in results:
            # Simple dependency analysis
            output.append(f"\n{'=' * 60}")
            output.append(f"Component: {results['component_id']}")
            output.append(f"Analysis: {results['analysis']}")
            output.append(f"Dependencies found: {results['count']}")
            
            if results['dependencies']:
                output.append("\nDependencies:")
                for dep in results['dependencies']:
                    output.append(f"  - {dep.get('component_name', 'Unknown')} ({dep.get('component_id', 'N/A')})")
                    output.append(f"    Type: {dep.get('component_type', 'N/A')}")
                    if 'reference_type' in dep:
                        output.append(f"    Reference: {dep['reference_type']}")
        
        elif 'change_type' in results:
            # Impact analysis
            output.append(f"\n{'=' * 60}")
            output.append(f"Impact Analysis: {results['component_id']}")
            output.append(f"Change Type: {results['change_type']}")
            output.append(f"Risk Level: {results['risk_level'].upper()}")
            
            output.append("\nStatistics:")
            for key, value in results['statistics'].items():
                output.append(f"  {key}: {value}")
            
            if results['recommendations']:
                output.append("\nRecommendations:")
                for rec in results['recommendations']:
                    output.append(f"  • {rec}")
            
            if results['direct_impact']:
                output.append(f"\nDirect Impact ({len(results['direct_impact'])} components):")
                for comp in results['direct_impact'][:5]:  # Show first 5
                    output.append(f"  - {comp.get('component_name', 'Unknown')}")
        
        elif 'nodes' in results:
            # Dependency graph
            output.append(f"\n{'=' * 60}")
            output.append(f"Dependency Graph: {results['root']}")
            output.append("\nStatistics:")
            for key, value in results['statistics'].items():
                output.append(f"  {key}: {value}")
            
            if results['statistics']['circular_dependencies']:
                output.append("\n⚠️ Circular Dependencies Detected:")
                for cycle in results['statistics']['circular_dependencies']:
                    output.append(f"  {' -> '.join(cycle)}")
            
            output.append(f"\nNodes ({len(results['nodes'])}):")
            for node_id, node_data in list(results['nodes'].items())[:10]:  # Show first 10
                output.append(f"  - {node_id} (depth: {node_data['depth']})")
                if node_data['uses']:
                    output.append(f"    Uses: {len(node_data['uses'])} components")
                if node_data['used_by']:
                    output.append(f"    Used by: {len(node_data['used_by'])} components")
    
    elif isinstance(results, list):
        # Batch results
        output.append(f"\n{'=' * 60}")
        output.append(f"Batch Analysis Results ({len(results)} components)")
        
        for result in results:
            if 'analysis_type' in result:
                output.append(f"\n{result['component_id']}: {result['count']} dependencies")
            elif 'risk_level' in result:
                output.append(f"\n{result['component_id']}: Risk Level = {result['risk_level'].upper()}")
                output.append(f"  Affected: {result['statistics']['total_components_affected']} components")
    
    return '\n'.join(output)


if __name__ == "__main__":
    main()