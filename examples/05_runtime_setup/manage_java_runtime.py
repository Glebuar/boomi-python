#!/usr/bin/env python3
"""
Java Runtime Management

This example demonstrates how to manage Java runtime versions including:
- Upgrading Java versions on Atoms
- Rolling back Java versions
- Checking Java compatibility
- Managing JVM settings
- Coordinating Java updates across multiple Atoms

The Java Runtime APIs help you maintain and update the Java environment
for your Atom runtime infrastructure.
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
    JavaUpgrade,
    JavaRollback,
    Atom,
    AtomQueryConfig,
    AtomSimpleExpression,
    AtomSimpleExpressionOperator,
    AtomSimpleExpressionProperty,
    AtomQueryConfigQueryFilter
)


class JavaRuntimeManager:
    """Manages Java runtime versions for Atoms"""
    
    def __init__(self, verbose: bool = False):
        """Initialize the Java Runtime Manager
        
        Args:
            verbose: Enable verbose output
        """
        self.verbose = verbose
        self.sdk = self._initialize_sdk()
        self.java_versions = {
            '8': {'version': '1.8.0', 'lts': True, 'eol': '2030-12'},
            '11': {'version': '11.0', 'lts': True, 'eol': '2026-09'},
            '17': {'version': '17.0', 'lts': True, 'eol': '2029-09'},
            '21': {'version': '21.0', 'lts': True, 'eol': '2031-09'}
        }
        
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
    
    def get_atom_java_info(self, atom_id: str) -> Dict[str, Any]:
        """Get Java runtime information for an Atom
        
        Args:
            atom_id: Atom ID
            
        Returns:
            Dictionary with Java runtime information
        """
        try:
            self._log(f"Getting Java info for Atom: {atom_id}")
            
            atom = self.sdk.atom.get_atom(id_=atom_id)
            
            java_info = {
                'atom_id': atom.id_,
                'atom_name': getattr(atom, 'name', 'N/A'),
                'java_version': getattr(atom, 'java_version', 'Unknown'),
                'jvm_vendor': getattr(atom, 'jvm_vendor', 'Unknown'),
                'jvm_settings': getattr(atom, 'jvm_settings', {}),
                'status': getattr(atom, 'status', 'UNKNOWN')
            }
            
            # Extract Java version details
            if hasattr(atom, 'properties'):
                props = atom.properties if isinstance(atom.properties, dict) else {}
                java_info['java_home'] = props.get('java.home', 'N/A')
                java_info['java_runtime'] = props.get('java.runtime.version', 'N/A')
                java_info['java_vendor'] = props.get('java.vendor', 'N/A')
            
            self._log(f"Java version: {java_info['java_version']}")
            return java_info
            
        except Exception as e:
            self._log(f"Error getting Java info: {e}", "ERROR")
            return {'atom_id': atom_id, 'error': str(e)}
    
    def upgrade_java(self, atom_id: str, target_version: str, 
                    force: bool = False, dry_run: bool = False) -> Dict[str, Any]:
        """Upgrade Java version for an Atom
        
        Args:
            atom_id: Atom ID
            target_version: Target Java version (e.g., '11', '17', '21')
            force: Force upgrade even if compatibility checks fail
            dry_run: Simulate upgrade without making changes
            
        Returns:
            Upgrade result dictionary
        """
        result = {
            'atom_id': atom_id,
            'target_version': target_version,
            'success': False,
            'message': '',
            'details': {}
        }
        
        try:
            self._log(f"Initiating Java upgrade for Atom {atom_id} to version {target_version}")
            
            # Get current Java info
            current_info = self.get_atom_java_info(atom_id)
            result['details']['current'] = current_info
            
            # Check target version validity
            if target_version not in self.java_versions:
                result['message'] = f"Invalid target version: {target_version}"
                self._log(result['message'], "ERROR")
                return result
            
            # Check compatibility
            compatibility = self.check_java_compatibility(atom_id, target_version)
            result['details']['compatibility'] = compatibility
            
            if not compatibility['compatible'] and not force:
                result['message'] = f"Compatibility check failed: {compatibility['reason']}"
                self._log(result['message'], "WARNING")
                return result
            
            if dry_run:
                result['success'] = True
                result['message'] = f"Dry run successful. Would upgrade to Java {target_version}"
                self._log(result['message'])
                return result
            
            # Perform upgrade
            self._log(f"Executing Java upgrade to {target_version}")
            
            upgrade_request = JavaUpgrade(
                atom_id=atom_id,
                target_version=self.java_versions[target_version]['version']
            )
            
            upgrade_result = self.sdk.java_upgrade.create_java_upgrade(
                request_body=upgrade_request
            )
            
            result['success'] = True
            result['message'] = f"Successfully initiated Java upgrade to {target_version}"
            result['details']['upgrade_id'] = getattr(upgrade_result, 'id_', 'N/A')
            self._log(result['message'])
            
        except Exception as e:
            result['message'] = f"Java upgrade failed: {str(e)}"
            result['details']['error'] = str(e)
            self._log(result['message'], "ERROR")
            if self.verbose:
                import traceback
                traceback.print_exc()
        
        return result
    
    def rollback_java(self, atom_id: str, force: bool = False) -> Dict[str, Any]:
        """Rollback Java version for an Atom to previous version
        
        Args:
            atom_id: Atom ID
            force: Force rollback even if checks fail
            
        Returns:
            Rollback result dictionary
        """
        result = {
            'atom_id': atom_id,
            'success': False,
            'message': '',
            'details': {}
        }
        
        try:
            self._log(f"Initiating Java rollback for Atom {atom_id}")
            
            # Get current Java info
            current_info = self.get_atom_java_info(atom_id)
            result['details']['current'] = current_info
            
            # Execute rollback
            self._log("Executing Java rollback")
            
            self.sdk.java_rollback.execute_java_rollback(id_=atom_id)
            
            result['success'] = True
            result['message'] = "Successfully initiated Java rollback"
            self._log(result['message'])
            
            # Wait and verify rollback (optional)
            if not force:
                time.sleep(5)
                new_info = self.get_atom_java_info(atom_id)
                result['details']['after_rollback'] = new_info
            
        except Exception as e:
            result['message'] = f"Java rollback failed: {str(e)}"
            result['details']['error'] = str(e)
            self._log(result['message'], "ERROR")
            if self.verbose:
                import traceback
                traceback.print_exc()
        
        return result
    
    def check_java_compatibility(self, atom_id: str, target_version: str) -> Dict[str, Any]:
        """Check Java version compatibility for an Atom
        
        Args:
            atom_id: Atom ID
            target_version: Target Java version
            
        Returns:
            Compatibility check results
        """
        compatibility = {
            'compatible': True,
            'warnings': [],
            'recommendations': [],
            'reason': ''
        }
        
        try:
            # Get current Java info
            current_info = self.get_atom_java_info(atom_id)
            current_version = current_info.get('java_version', '')
            
            # Extract major version number
            current_major = self._extract_major_version(current_version)
            target_major = int(target_version) if target_version.isdigit() else 0
            
            self._log(f"Current Java: {current_major}, Target: {target_major}")
            
            # Check version progression
            if current_major and target_major:
                if target_major < current_major:
                    compatibility['warnings'].append(
                        f"Downgrading from Java {current_major} to {target_major}"
                    )
                    compatibility['recommendations'].append(
                        "Test thoroughly in non-production environment first"
                    )
                elif target_major - current_major > 1:
                    compatibility['warnings'].append(
                        f"Skipping versions from Java {current_major} to {target_major}"
                    )
                    compatibility['recommendations'].append(
                        "Consider upgrading incrementally through intermediate versions"
                    )
            
            # Check LTS status
            if target_version in self.java_versions:
                target_info = self.java_versions[target_version]
                if not target_info['lts']:
                    compatibility['warnings'].append(
                        f"Java {target_version} is not an LTS version"
                    )
                    compatibility['recommendations'].append(
                        "Consider using an LTS version for production environments"
                    )
                
                # Check EOL date
                eol_date = datetime.strptime(target_info['eol'], '%Y-%m')
                months_until_eol = (eol_date - datetime.now()).days / 30
                
                if months_until_eol < 12:
                    compatibility['warnings'].append(
                        f"Java {target_version} EOL in {months_until_eol:.0f} months"
                    )
                    compatibility['recommendations'].append(
                        "Plan for future upgrade before EOL"
                    )
            
            # Check Atom status
            atom_status = current_info.get('status', 'UNKNOWN')
            if atom_status != 'ONLINE':
                compatibility['compatible'] = False
                compatibility['reason'] = f"Atom is not online (status: {atom_status})"
            
            # Set overall compatibility
            if not compatibility['compatible']:
                self._log(f"Compatibility check failed: {compatibility['reason']}", "WARNING")
            elif compatibility['warnings']:
                self._log(f"Compatibility check passed with {len(compatibility['warnings'])} warning(s)")
            else:
                self._log("Compatibility check passed")
            
        except Exception as e:
            compatibility['compatible'] = False
            compatibility['reason'] = f"Compatibility check error: {str(e)}"
            self._log(compatibility['reason'], "ERROR")
        
        return compatibility
    
    def _extract_major_version(self, version_string: str) -> Optional[int]:
        """Extract major Java version number from version string
        
        Args:
            version_string: Java version string
            
        Returns:
            Major version number or None
        """
        try:
            # Handle different version formats
            if '1.8' in version_string:
                return 8
            elif version_string.startswith('1.'):
                # Old format: 1.x.y -> x is major
                parts = version_string.split('.')
                if len(parts) >= 2:
                    return int(parts[1])
            else:
                # New format: x.y.z -> x is major
                parts = version_string.split('.')
                if parts[0].isdigit():
                    return int(parts[0])
        except:
            pass
        
        return None
    
    def batch_upgrade(self, atom_ids: List[str], target_version: str,
                     parallel: bool = False, delay: int = 60) -> List[Dict[str, Any]]:
        """Upgrade Java version for multiple Atoms
        
        Args:
            atom_ids: List of Atom IDs
            target_version: Target Java version
            parallel: Upgrade in parallel (not recommended)
            delay: Delay between upgrades in seconds
            
        Returns:
            List of upgrade results
        """
        results = []
        
        print(f"\n{'='*60}")
        print(f"Batch Java Upgrade to Version {target_version}")
        print(f"Atoms to upgrade: {len(atom_ids)}")
        print(f"{'='*60}\n")
        
        for i, atom_id in enumerate(atom_ids, 1):
            print(f"[{i}/{len(atom_ids)}] Upgrading Atom: {atom_id}")
            
            result = self.upgrade_java(atom_id, target_version)
            results.append(result)
            
            if result['success']:
                print(f"  ✅ {result['message']}")
            else:
                print(f"  ❌ {result['message']}")
            
            # Add delay between upgrades
            if not parallel and i < len(atom_ids):
                print(f"  ⏳ Waiting {delay} seconds before next upgrade...")
                time.sleep(delay)
        
        # Summary
        successful = sum(1 for r in results if r['success'])
        failed = len(results) - successful
        
        print(f"\n{'='*60}")
        print(f"Batch Upgrade Summary:")
        print(f"  ✅ Successful: {successful}")
        print(f"  ❌ Failed: {failed}")
        print(f"{'='*60}\n")
        
        return results
    
    def display_java_inventory(self, limit: int = 100):
        """Display Java version inventory across all Atoms
        
        Args:
            limit: Maximum number of Atoms to display
        """
        try:
            # Query all online Atoms
            simple_expression = AtomSimpleExpression(
                operator=AtomSimpleExpressionOperator.EQUALS,
                property=AtomSimpleExpressionProperty.STATUS,
                argument=["ONLINE"]
            )
            query_filter = AtomQueryConfigQueryFilter(expression=simple_expression)
            query_config = AtomQueryConfig(query_filter=query_filter)
            
            result = self.sdk.atom.query_atom(request_body=query_config)
            
            if not hasattr(result, 'result') or not result.result:
                print("No online Atoms found")
                return
            
            atoms = result.result[:limit]
            java_versions = {}
            
            print(f"\n{'='*80}")
            print("Java Version Inventory")
            print(f"{'='*80}")
            print(f"{'Atom Name':<30} {'Atom ID':<25} {'Java Version':<15} {'Status':<10}")
            print(f"{'-'*80}")
            
            for atom in atoms:
                atom_name = getattr(atom, 'name', 'N/A')[:28]
                atom_id = str(atom.id_)[:23]
                java_version = getattr(atom, 'java_version', 'Unknown')[:13]
                status = getattr(atom, 'status', 'N/A')[:8]
                
                print(f"{atom_name:<30} {atom_id:<25} {java_version:<15} {status:<10}")
                
                # Track version distribution
                major_version = self._extract_major_version(java_version)
                version_key = f"Java {major_version}" if major_version else "Unknown"
                java_versions[version_key] = java_versions.get(version_key, 0) + 1
            
            # Display summary
            print(f"\n{'='*80}")
            print("Version Distribution:")
            print(f"{'-'*80}")
            
            for version, count in sorted(java_versions.items()):
                percentage = (count / len(atoms)) * 100
                bar = '█' * int(percentage / 2)
                print(f"{version:<15} {count:3} atoms ({percentage:5.1f}%) {bar}")
            
            print(f"{'='*80}")
            print(f"Total Atoms: {len(atoms)}")
            
        except Exception as e:
            print(f"Error displaying Java inventory: {e}")
            if self.verbose:
                import traceback
                traceback.print_exc()


def main():
    """Main function to handle command-line arguments"""
    parser = argparse.ArgumentParser(
        description="Manage Java runtime versions for Atoms",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Check Java version for an Atom
  %(prog)s --check --atom-id YOUR_ATOM_ID
  
  # Upgrade Java version
  %(prog)s --upgrade --atom-id YOUR_ATOM_ID --version 17
  
  # Dry run upgrade
  %(prog)s --upgrade --atom-id YOUR_ATOM_ID --version 17 --dry-run
  
  # Force upgrade (skip compatibility checks)
  %(prog)s --upgrade --atom-id YOUR_ATOM_ID --version 17 --force
  
  # Rollback Java version
  %(prog)s --rollback --atom-id YOUR_ATOM_ID
  
  # Batch upgrade multiple Atoms
  %(prog)s --batch-upgrade --atom-ids ATOM1 ATOM2 ATOM3 --version 17
  
  # Display Java inventory
  %(prog)s --inventory
  
  # Check compatibility
  %(prog)s --check-compatibility --atom-id YOUR_ATOM_ID --version 17
        """
    )
    
    parser.add_argument('--check', action='store_true',
                       help='Check current Java version')
    parser.add_argument('--upgrade', action='store_true',
                       help='Upgrade Java version')
    parser.add_argument('--rollback', action='store_true',
                       help='Rollback Java version to previous')
    parser.add_argument('--batch-upgrade', action='store_true',
                       help='Upgrade multiple Atoms')
    parser.add_argument('--inventory', action='store_true',
                       help='Display Java version inventory')
    parser.add_argument('--check-compatibility', action='store_true',
                       help='Check Java version compatibility')
    
    parser.add_argument('--atom-id', type=str,
                       help='Single Atom ID')
    parser.add_argument('--atom-ids', type=str, nargs='+',
                       help='Multiple Atom IDs for batch operations')
    parser.add_argument('--version', type=str,
                       help='Target Java version (8, 11, 17, 21)')
    
    parser.add_argument('--force', action='store_true',
                       help='Force operation even if checks fail')
    parser.add_argument('--dry-run', action='store_true',
                       help='Simulate operation without making changes')
    parser.add_argument('--delay', type=int, default=60,
                       help='Delay between batch operations in seconds')
    parser.add_argument('--limit', type=int, default=100,
                       help='Maximum number of results')
    parser.add_argument('--verbose', action='store_true',
                       help='Enable verbose output')
    
    args = parser.parse_args()
    
    # Validate arguments
    if not any([args.check, args.upgrade, args.rollback, args.batch_upgrade, 
                args.inventory, args.check_compatibility]):
        parser.print_help()
        return 1
    
    try:
        manager = JavaRuntimeManager(verbose=args.verbose)
        
        if args.check:
            if not args.atom_id:
                print("Error: --atom-id is required for --check")
                return 1
            
            info = manager.get_atom_java_info(args.atom_id)
            print(f"\n{'='*60}")
            print(f"Java Runtime Information")
            print(f"{'='*60}")
            for key, value in info.items():
                if key != 'jvm_settings':
                    print(f"{key:20}: {value}")
            
            if 'jvm_settings' in info and info['jvm_settings']:
                print("\nJVM Settings:")
                for key, value in info['jvm_settings'].items():
                    print(f"  {key}: {value}")
        
        elif args.upgrade:
            if not args.atom_id or not args.version:
                print("Error: --atom-id and --version are required for --upgrade")
                return 1
            
            result = manager.upgrade_java(
                atom_id=args.atom_id,
                target_version=args.version,
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
        
        elif args.rollback:
            if not args.atom_id:
                print("Error: --atom-id is required for --rollback")
                return 1
            
            result = manager.rollback_java(
                atom_id=args.atom_id,
                force=args.force
            )
            
            if result['success']:
                print(f"✅ {result['message']}")
            else:
                print(f"❌ {result['message']}")
        
        elif args.batch_upgrade:
            if not args.atom_ids or not args.version:
                print("Error: --atom-ids and --version are required for --batch-upgrade")
                return 1
            
            results = manager.batch_upgrade(
                atom_ids=args.atom_ids,
                target_version=args.version,
                delay=args.delay
            )
        
        elif args.inventory:
            manager.display_java_inventory(limit=args.limit)
        
        elif args.check_compatibility:
            if not args.atom_id or not args.version:
                print("Error: --atom-id and --version are required for --check-compatibility")
                return 1
            
            compatibility = manager.check_java_compatibility(args.atom_id, args.version)
            
            print(f"\n{'='*60}")
            print(f"Java Compatibility Check")
            print(f"{'='*60}")
            print(f"Atom ID: {args.atom_id}")
            print(f"Target Version: Java {args.version}")
            print(f"Compatible: {'✅ Yes' if compatibility['compatible'] else '❌ No'}")
            
            if compatibility['reason']:
                print(f"Reason: {compatibility['reason']}")
            
            if compatibility['warnings']:
                print("\n⚠️ Warnings:")
                for warning in compatibility['warnings']:
                    print(f"  - {warning}")
            
            if compatibility['recommendations']:
                print("\n📋 Recommendations:")
                for rec in compatibility['recommendations']:
                    print(f"  - {rec}")
        
        return 0
        
    except Exception as e:
        print(f"❌ Error: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())