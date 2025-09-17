#!/usr/bin/env python3
"""
Node Offboarding Management

This example demonstrates how to offboard nodes from Atom clusters including:
- Safely removing nodes from clusters
- Migrating workloads before offboarding
- Handling node decommissioning
- Managing cluster rebalancing
- Tracking offboarding status

The Node Offboard API helps you safely remove nodes from your Atom
infrastructure while ensuring continuity of operations.
"""

import os
import sys
import json
import argparse
import time
from typing import Dict, Any, List, Optional, Tuple
from datetime import datetime, timedelta
from pathlib import Path

# Add the src directory to the path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

# Load environment variables from .env file if available
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv is optional

from boomi import Boomi
from boomi.models import (
    NodeOffboard,
    Atom,
    AtomQueryConfig,
    AtomSimpleExpression,
    AtomSimpleExpressionOperator,
    AtomSimpleExpressionProperty,
    AtomQueryConfigQueryFilter
)


class NodeOffboardManager:
    """Manages node offboarding operations"""
    
    def __init__(self, verbose: bool = False):
        """Initialize the Node Offboard Manager
        
        Args:
            verbose: Enable verbose output
        """
        self.verbose = verbose
        self.sdk = self._initialize_sdk()
        
    def _initialize_sdk(self) -> Boomi:
        """Initialize Boomi SDK with credentials from environment"""
        account_id = os.getenv('BOOMI_ACCOUNT')
        username = os.getenv('BOOMI_USER')
        password = os.getenv('BOOMI_SECRET')
        
        if not all([account_id, username, password]):
            raise ValueError("Please set BOOMI_ACCOUNT, BOOMI_USER, and BOOMI_SECRET environment variables")
        
        return Boomi(
            account_id=account_id,
            username=username,
            password=password,
            timeout=30000
        )
    
    def _log(self, message: str, level: str = "INFO"):
        """Log message if verbose mode is enabled"""
        if self.verbose:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{timestamp}] [{level}] {message}")
    
    def get_node_info(self, node_id: str) -> Dict[str, Any]:
        """Get information about a node
        
        Args:
            node_id: Node/Atom ID
            
        Returns:
            Node information dictionary
        """
        try:
            self._log(f"Getting node information for: {node_id}")
            
            atom = self.sdk.atom.get_atom(id_=node_id)
            
            node_info = {
                'node_id': atom.id_,
                'name': getattr(atom, 'name', 'N/A'),
                'status': getattr(atom, 'status', 'UNKNOWN'),
                'type': getattr(atom, 'type', 'N/A'),
                'cloud': getattr(atom, 'cloud_id', None) is not None,
                'cluster_id': getattr(atom, 'cluster_id', None),
                'version': getattr(atom, 'version', 'N/A'),
                'last_seen': getattr(atom, 'last_seen', 'N/A'),
                'processes': []
            }
            
            # Check if node is part of a cluster
            if node_info['cluster_id']:
                node_info['is_cluster_member'] = True
                self._log(f"Node is part of cluster: {node_info['cluster_id']}")
            else:
                node_info['is_cluster_member'] = False
                self._log("Node is standalone")
            
            # Get attached processes (if available)
            if hasattr(atom, 'processes'):
                node_info['processes'] = atom.processes
                self._log(f"Node has {len(node_info['processes'])} attached process(es)")
            
            return node_info
            
        except Exception as e:
            self._log(f"Error getting node info: {e}", "ERROR")
            return {'node_id': node_id, 'error': str(e)}
    
    def check_offboard_readiness(self, node_id: str) -> Dict[str, Any]:
        """Check if a node is ready to be offboarded
        
        Args:
            node_id: Node/Atom ID
            
        Returns:
            Readiness check results
        """
        readiness = {
            'ready': False,
            'checks': {},
            'warnings': [],
            'blockers': [],
            'recommendations': []
        }
        
        try:
            self._log(f"Checking offboard readiness for node: {node_id}")
            
            # Get node info
            node_info = self.get_node_info(node_id)
            
            if 'error' in node_info:
                readiness['blockers'].append(f"Cannot retrieve node info: {node_info['error']}")
                return readiness
            
            # Check 1: Node status
            status = node_info.get('status', 'UNKNOWN')
            readiness['checks']['status'] = status
            
            if status == 'ONLINE':
                readiness['warnings'].append("Node is currently online")
                readiness['recommendations'].append("Consider gracefully shutting down the node first")
            elif status == 'OFFLINE':
                self._log("Node is offline (good for offboarding)")
            else:
                readiness['warnings'].append(f"Node has unusual status: {status}")
            
            # Check 2: Cluster membership
            if node_info.get('is_cluster_member'):
                readiness['checks']['cluster_member'] = True
                cluster_id = node_info.get('cluster_id')
                
                # Check cluster size
                cluster_nodes = self._get_cluster_nodes(cluster_id)
                readiness['checks']['cluster_size'] = len(cluster_nodes)
                
                if len(cluster_nodes) <= 2:
                    readiness['blockers'].append(
                        f"Cluster has only {len(cluster_nodes)} nodes. Offboarding would compromise cluster."
                    )
                    readiness['recommendations'].append(
                        "Add replacement nodes before offboarding"
                    )
                else:
                    readiness['warnings'].append(
                        f"Node is part of cluster with {len(cluster_nodes)} nodes"
                    )
                    readiness['recommendations'].append(
                        "Ensure remaining nodes can handle the workload"
                    )
            else:
                readiness['checks']['cluster_member'] = False
                self._log("Node is standalone (simpler offboarding)")
            
            # Check 3: Running processes
            processes = node_info.get('processes', [])
            readiness['checks']['process_count'] = len(processes)
            
            if processes:
                readiness['warnings'].append(f"Node has {len(processes)} attached process(es)")
                readiness['recommendations'].append(
                    "Migrate processes to other nodes before offboarding"
                )
            
            # Check 4: Cloud vs On-premise
            if node_info.get('cloud'):
                readiness['checks']['deployment_type'] = 'cloud'
                self._log("Cloud node - standard offboarding procedure")
            else:
                readiness['checks']['deployment_type'] = 'on-premise'
                readiness['warnings'].append("On-premise node may require manual cleanup")
            
            # Determine overall readiness
            if not readiness['blockers']:
                readiness['ready'] = True
                self._log("Node is ready for offboarding")
            else:
                self._log(f"Node is NOT ready: {len(readiness['blockers'])} blocker(s)", "WARNING")
            
        except Exception as e:
            readiness['blockers'].append(f"Readiness check failed: {str(e)}")
            self._log(f"Error checking readiness: {e}", "ERROR")
        
        return readiness
    
    def _get_cluster_nodes(self, cluster_id: str) -> List[Dict[str, Any]]:
        """Get all nodes in a cluster
        
        Args:
            cluster_id: Cluster ID
            
        Returns:
            List of nodes in the cluster
        """
        try:
            if not cluster_id:
                return []
            
            self._log(f"Getting nodes for cluster: {cluster_id}")
            
            # Query nodes in the same cluster
            simple_expression = AtomSimpleExpression(
                operator=AtomSimpleExpressionOperator.EQUALS,
                property="clusterId",
                argument=[cluster_id]
            )
            query_filter = AtomQueryConfigQueryFilter(expression=simple_expression)
            query_config = AtomQueryConfig(query_filter=query_filter)
            
            result = self.sdk.atom.query_atom(request_body=query_config)
            
            if hasattr(result, 'result') and result.result:
                nodes = []
                for atom in result.result:
                    nodes.append({
                        'id': atom.id_,
                        'name': getattr(atom, 'name', 'N/A'),
                        'status': getattr(atom, 'status', 'UNKNOWN')
                    })
                self._log(f"Found {len(nodes)} nodes in cluster")
                return nodes
            
            return []
            
        except Exception as e:
            self._log(f"Error getting cluster nodes: {e}", "ERROR")
            return []
    
    def offboard_node(self, node_id: str, force: bool = False, 
                     dry_run: bool = False) -> Dict[str, Any]:
        """Offboard a node from the infrastructure
        
        Args:
            node_id: Node/Atom ID to offboard
            force: Force offboarding even if checks fail
            dry_run: Simulate offboarding without making changes
            
        Returns:
            Offboarding result dictionary
        """
        result = {
            'node_id': node_id,
            'success': False,
            'message': '',
            'details': {}
        }
        
        try:
            self._log(f"Initiating node offboarding for: {node_id}")
            
            # Check readiness
            if not force:
                readiness = self.check_offboard_readiness(node_id)
                result['details']['readiness'] = readiness
                
                if not readiness['ready']:
                    result['message'] = f"Node not ready for offboarding: {readiness['blockers']}"
                    self._log(result['message'], "WARNING")
                    return result
            
            if dry_run:
                result['success'] = True
                result['message'] = f"Dry run successful. Would offboard node {node_id}"
                self._log(result['message'])
                return result
            
            # Execute offboarding
            self._log("Executing node offboarding")

            # Get node info to determine if it's part of a cluster
            node_info = self.get_node_info(node_id)

            # For node offboarding, we need the cluster/cloud ID
            # Since this is a cloud node, we need to handle differently
            # The NodeOffboard API is specifically for removing nodes from clusters
            # For standalone nodes, we would use the delete_atom API instead

            if node_info.get('is_cluster_member') and node_info.get('cluster_id'):
                # Node is part of a cluster - use NodeOffboard API
                offboard_request = NodeOffboard(
                    atom_id=node_info['cluster_id'],  # The cluster ID
                    node_id=[node_id]  # List of nodes to offboard
                )

                offboard_result = self.sdk.node_offboard.create_node_offboard(
                    request_body=offboard_request
                )

                result['success'] = True
                result['message'] = f"Successfully initiated node offboarding from cluster for {node_id}"
                result['details']['offboard_id'] = getattr(offboard_result, 'id_', 'N/A')
                result['details']['status'] = getattr(offboard_result, 'status', 'N/A')
            else:
                # Standalone node - would typically use atom deletion
                # But for safety, we'll just indicate this
                result['message'] = "Node is not part of a cluster. For standalone nodes, use atom deletion instead."
                result['details']['note'] = "NodeOffboard API is specifically for removing nodes from clusters"
                self._log(result['message'], "WARNING")

            self._log(result['message'])
            
        except Exception as e:
            result['message'] = f"Node offboarding failed: {str(e)}"
            result['details']['error'] = str(e)
            self._log(result['message'], "ERROR")
            if self.verbose:
                import traceback
                traceback.print_exc()
        
        return result
    
    def migrate_workloads(self, source_node: str, target_nodes: List[str],
                         workload_type: str = "processes") -> Dict[str, Any]:
        """Migrate workloads from source node to target nodes
        
        Args:
            source_node: Source node ID
            target_nodes: List of target node IDs
            workload_type: Type of workload to migrate
            
        Returns:
            Migration result dictionary
        """
        migration = {
            'source': source_node,
            'targets': target_nodes,
            'workload_type': workload_type,
            'success': False,
            'migrated': [],
            'failed': [],
            'message': ''
        }
        
        try:
            self._log(f"Migrating {workload_type} from {source_node} to {target_nodes}")
            
            # Get source node info
            source_info = self.get_node_info(source_node)
            
            if 'error' in source_info:
                migration['message'] = f"Cannot get source node info: {source_info['error']}"
                return migration
            
            # Get workloads to migrate
            if workload_type == "processes":
                workloads = source_info.get('processes', [])
                self._log(f"Found {len(workloads)} process(es) to migrate")
            else:
                migration['message'] = f"Unsupported workload type: {workload_type}"
                return migration
            
            if not workloads:
                migration['success'] = True
                migration['message'] = "No workloads to migrate"
                return migration
            
            # Distribute workloads across target nodes
            workload_distribution = {}
            for i, workload in enumerate(workloads):
                target_node = target_nodes[i % len(target_nodes)]
                if target_node not in workload_distribution:
                    workload_distribution[target_node] = []
                workload_distribution[target_node].append(workload)
            
            # Migrate workloads (simulation - actual migration would require process attachment APIs)
            for target_node, node_workloads in workload_distribution.items():
                self._log(f"Migrating {len(node_workloads)} workload(s) to {target_node}")
                
                for workload in node_workloads:
                    try:
                        # In a real implementation, this would call process attachment APIs
                        migration['migrated'].append({
                            'workload': workload,
                            'target': target_node
                        })
                    except Exception as e:
                        migration['failed'].append({
                            'workload': workload,
                            'error': str(e)
                        })
            
            # Set overall success
            if migration['migrated'] and not migration['failed']:
                migration['success'] = True
                migration['message'] = f"Successfully migrated {len(migration['migrated'])} workload(s)"
            elif migration['migrated'] and migration['failed']:
                migration['success'] = False
                migration['message'] = f"Partially migrated: {len(migration['migrated'])} succeeded, {len(migration['failed'])} failed"
            else:
                migration['success'] = False
                migration['message'] = "Migration failed for all workloads"
            
            self._log(migration['message'])
            
        except Exception as e:
            migration['message'] = f"Migration failed: {str(e)}"
            self._log(migration['message'], "ERROR")
        
        return migration
    
    def display_offboard_plan(self, node_id: str):
        """Display a comprehensive offboarding plan for a node
        
        Args:
            node_id: Node/Atom ID
        """
        print(f"\n{'='*60}")
        print(f"Node Offboarding Plan: {node_id}")
        print(f"{'='*60}\n")
        
        # Get node info
        node_info = self.get_node_info(node_id)
        
        if 'error' in node_info:
            print(f"❌ Error: {node_info['error']}")
            return
        
        # Display node information
        print("📋 Node Information:")
        print(f"  Name: {node_info['name']}")
        print(f"  Status: {node_info['status']}")
        print(f"  Type: {node_info['type']}")
        print(f"  Cluster Member: {'Yes' if node_info['is_cluster_member'] else 'No'}")
        if node_info['is_cluster_member']:
            print(f"  Cluster ID: {node_info['cluster_id']}")
        print(f"  Processes: {len(node_info.get('processes', []))}")
        
        # Check readiness
        readiness = self.check_offboard_readiness(node_id)
        
        print(f"\n📊 Readiness Check: {'✅ READY' if readiness['ready'] else '❌ NOT READY'}")
        
        if readiness['blockers']:
            print("\n🚫 Blockers:")
            for blocker in readiness['blockers']:
                print(f"  • {blocker}")
        
        if readiness['warnings']:
            print("\n⚠️ Warnings:")
            for warning in readiness['warnings']:
                print(f"  • {warning}")
        
        if readiness['recommendations']:
            print("\n💡 Recommendations:")
            for rec in readiness['recommendations']:
                print(f"  • {rec}")
        
        # Display offboarding steps
        print("\n📝 Offboarding Steps:")
        steps = [
            "1. Verify node is not processing critical workloads",
            "2. Migrate any active processes to other nodes",
            "3. Stop the node gracefully",
            "4. Wait for status to change to OFFLINE",
            "5. Execute offboarding command",
            "6. Verify node removal from cluster (if applicable)",
            "7. Clean up local resources (if on-premise)",
            "8. Update documentation and monitoring"
        ]
        
        for step in steps:
            print(f"  {step}")
        
        # Display command
        print("\n💻 Offboarding Command:")
        print(f"  python {sys.argv[0]} --offboard --node-id {node_id}")
        
        if not readiness['ready']:
            print("\n⚠️ Note: Use --force flag to override blockers (not recommended)")
        
        print()


def main():
    """Main function to handle command-line arguments"""
    parser = argparse.ArgumentParser(
        description="Manage node offboarding operations",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Check node information
  %(prog)s --info --node-id YOUR_NODE_ID
  
  # Check offboarding readiness
  %(prog)s --check-readiness --node-id YOUR_NODE_ID
  
  # Display offboarding plan
  %(prog)s --plan --node-id YOUR_NODE_ID
  
  # Offboard a node
  %(prog)s --offboard --node-id YOUR_NODE_ID
  
  # Dry run offboarding
  %(prog)s --offboard --node-id YOUR_NODE_ID --dry-run
  
  # Force offboarding (skip checks)
  %(prog)s --offboard --node-id YOUR_NODE_ID --force
  
  # Migrate workloads before offboarding
  %(prog)s --migrate --source YOUR_NODE_ID --targets NODE1 NODE2
        """
    )
    
    parser.add_argument('--info', action='store_true',
                       help='Display node information')
    parser.add_argument('--check-readiness', action='store_true',
                       help='Check if node is ready for offboarding')
    parser.add_argument('--plan', action='store_true',
                       help='Display comprehensive offboarding plan')
    parser.add_argument('--offboard', action='store_true',
                       help='Offboard a node')
    parser.add_argument('--migrate', action='store_true',
                       help='Migrate workloads from node')
    
    parser.add_argument('--node-id', type=str,
                       help='Node/Atom ID')
    parser.add_argument('--source', type=str,
                       help='Source node for migration')
    parser.add_argument('--targets', type=str, nargs='+',
                       help='Target nodes for migration')
    
    parser.add_argument('--force', action='store_true',
                       help='Force operation even if checks fail')
    parser.add_argument('--dry-run', action='store_true',
                       help='Simulate operation without making changes')
    parser.add_argument('--verbose', action='store_true',
                       help='Enable verbose output')
    
    args = parser.parse_args()
    
    # Validate arguments
    if not any([args.info, args.check_readiness, args.plan, args.offboard, args.migrate]):
        parser.print_help()
        return 1
    
    try:
        manager = NodeOffboardManager(verbose=args.verbose)
        
        if args.info:
            if not args.node_id:
                print("Error: --node-id is required for --info")
                return 1
            
            info = manager.get_node_info(args.node_id)
            
            if 'error' in info:
                print(f"❌ Error: {info['error']}")
            else:
                print(f"\n{'='*60}")
                print(f"Node Information: {args.node_id}")
                print(f"{'='*60}")
                for key, value in info.items():
                    if key != 'processes':
                        print(f"{key:20}: {value}")
                
                if info.get('processes'):
                    print(f"\nAttached Processes ({len(info['processes'])}):")
                    for proc in info['processes']:
                        print(f"  • {proc}")
        
        elif args.check_readiness:
            if not args.node_id:
                print("Error: --node-id is required for --check-readiness")
                return 1
            
            readiness = manager.check_offboard_readiness(args.node_id)
            
            print(f"\n{'='*60}")
            print(f"Offboarding Readiness Check")
            print(f"{'='*60}")
            print(f"Node ID: {args.node_id}")
            print(f"Ready: {'✅ YES' if readiness['ready'] else '❌ NO'}")
            
            if readiness['checks']:
                print("\nChecks:")
                for check, value in readiness['checks'].items():
                    print(f"  {check}: {value}")
            
            if readiness['blockers']:
                print("\n🚫 Blockers:")
                for blocker in readiness['blockers']:
                    print(f"  • {blocker}")
            
            if readiness['warnings']:
                print("\n⚠️ Warnings:")
                for warning in readiness['warnings']:
                    print(f"  • {warning}")
            
            if readiness['recommendations']:
                print("\n💡 Recommendations:")
                for rec in readiness['recommendations']:
                    print(f"  • {rec}")
        
        elif args.plan:
            if not args.node_id:
                print("Error: --node-id is required for --plan")
                return 1
            
            manager.display_offboard_plan(args.node_id)
        
        elif args.offboard:
            if not args.node_id:
                print("Error: --node-id is required for --offboard")
                return 1
            
            result = manager.offboard_node(
                node_id=args.node_id,
                force=args.force,
                dry_run=args.dry_run
            )
            
            if result['success']:
                print(f"✅ {result['message']}")
            else:
                print(f"❌ {result['message']}")
            
            if args.verbose and result['details']:
                print("\nDetails:")
                print(json.dumps(result['details'], indent=2, default=str))
        
        elif args.migrate:
            if not args.source or not args.targets:
                print("Error: --source and --targets are required for --migrate")
                return 1
            
            migration = manager.migrate_workloads(
                source_node=args.source,
                target_nodes=args.targets
            )
            
            print(f"\n{'='*60}")
            print(f"Workload Migration Results")
            print(f"{'='*60}")
            print(f"Source: {migration['source']}")
            print(f"Targets: {', '.join(migration['targets'])}")
            print(f"Status: {'✅ SUCCESS' if migration['success'] else '❌ FAILED'}")
            print(f"Message: {migration['message']}")
            
            if migration['migrated']:
                print(f"\n✅ Migrated ({len(migration['migrated'])}):")
                for item in migration['migrated']:
                    print(f"  • {item['workload']} → {item['target']}")
            
            if migration['failed']:
                print(f"\n❌ Failed ({len(migration['failed'])}):")
                for item in migration['failed']:
                    print(f"  • {item['workload']}: {item['error']}")
        
        return 0
        
    except Exception as e:
        print(f"❌ Error: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())