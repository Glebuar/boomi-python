#!/usr/bin/env python3
"""
Persisted Process Properties Management

This example demonstrates how to manage persisted process properties including:
- Updating property values for processes on an Atom/Runtime
- Managing property configurations
- Property bulk updates

Note: The Persisted Process Properties API works at the Atom/Runtime level.
Properties are updated for all processes deployed on a specific runtime.

Available SDK Operations:
- update_persisted_process_properties: Update properties for an Atom/Runtime

Note: Get/retrieve operations require async endpoints not yet implemented in the SDK.
"""

import os
import sys
import json
import argparse
import time
from typing import Dict, Any, List, Optional, Tuple
from datetime import datetime
from pathlib import Path

# Add the src directory to the path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from boomi import Boomi
from boomi.models import PersistedProcessProperties


class PersistedPropertiesManager:
    """Manages persisted process properties"""
    
    def __init__(self, verbose: bool = False):
        """Initialize the Persisted Properties Manager
        
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
    
    def update_persisted_properties(self, atom_id: str, properties_config: Dict[str, Any]) -> bool:
        """Update persisted properties for an Atom/Runtime

        Args:
            atom_id: Atom/Runtime ID
            properties_config: Properties configuration dictionary

        Returns:
            True if updated successfully, False otherwise
        """
        try:
            self._log(f"Updating persisted properties for atom: {atom_id}")

            # Create PersistedProcessProperties object
            from boomi.models import PersistedProcessProperties

            # Build the properties object from the config
            properties_obj = PersistedProcessProperties(
                atom_id=atom_id,
                **properties_config
            )

            # Update properties using SDK
            result = self.sdk.persisted_process_properties.update_persisted_process_properties(
                id_=atom_id,
                request_body=properties_obj
            )

            self._log("Successfully updated persisted properties")
            return True

        except Exception as e:
            self._log(f"Error updating persisted properties: {e}", "ERROR")
            return False
    
    
    def create_sample_properties_config(self, process_id: str, properties: Dict[str, str]) -> Dict[str, Any]:
        """Create a sample properties configuration for testing

        Args:
            process_id: Process ID to configure properties for
            properties: Dictionary of property name/value pairs

        Returns:
            Properties configuration dictionary
        """
        try:
            self._log(f"Creating properties config for process: {process_id}")

            # Build process properties structure based on OpenAPI spec
            process_properties = []
            for name, value in properties.items():
                process_properties.append({
                    "@type": "",
                    "Name": name,
                    "Value": value
                })

            config = {
                "Process": [{
                    "@type": "DeployedProcess",
                    "processId": process_id,
                    "ProcessProperties": {
                        "@type": "",
                        "ProcessProperty": process_properties
                    }
                }]
            }

            self._log(f"Created config with {len(properties)} properties")
            return config

        except Exception as e:
            self._log(f"Error creating properties config: {e}", "ERROR")
            return {}
    
    def update_single_property(self, atom_id: str, process_id: str,
                              property_name: str, property_value: str) -> bool:
        """Update a single persisted property value for a process on an atom

        Args:
            atom_id: Atom/Runtime ID
            process_id: Process ID
            property_name: Property name
            property_value: New property value

        Returns:
            True if updated successfully, False otherwise
        """
        try:
            self._log(f"Updating property {property_name} = {property_value} for process {process_id}")

            # Create config for single property
            properties_config = self.create_sample_properties_config(
                process_id, {property_name: property_value}
            )

            # Update using the main update method
            return self.update_persisted_properties(atom_id, properties_config)

        except Exception as e:
            self._log(f"Error updating single property: {e}", "ERROR")
            return False
    
    def bulk_update_properties(self, atom_id: str, process_id: str,
                              properties: Dict[str, str]) -> bool:
        """Update multiple properties at once for a process on an atom

        Args:
            atom_id: Atom/Runtime ID
            process_id: Process ID
            properties: Dictionary of property names and values

        Returns:
            True if all updated successfully, False otherwise
        """
        try:
            self._log(f"Bulk updating {len(properties)} properties for process {process_id}")

            # Create config for all properties
            properties_config = self.create_sample_properties_config(process_id, properties)

            # Update using the main update method
            return self.update_persisted_properties(atom_id, properties_config)

        except Exception as e:
            self._log(f"Error in bulk update: {e}", "ERROR")
            return False
    
    def display_update_result(self, atom_id: str, success: bool, config: Dict[str, Any]):
        """Display the result of a property update operation

        Args:
            atom_id: Atom/Runtime ID that was updated
            success: Whether the update succeeded
            config: The configuration that was applied
        """
        print(f"\n{'='*60}")
        print(f"Persisted Properties Update Result")
        print(f"{'='*60}")
        print(f"Atom/Runtime ID: {atom_id}")
        print(f"Status: {'✅ Success' if success else '❌ Failed'}")
        print()

        if success and config:
            print("📋 Configuration Applied:")
            if 'Process' in config:
                for process in config['Process']:
                    process_id = process.get('processId', 'N/A')
                    print(f"  Process ID: {process_id}")

                    props = process.get('ProcessProperties', {}).get('ProcessProperty', [])
                    if props:
                        print(f"  Properties ({len(props)}):")
                        for prop in props:
                            name = prop.get('Name', 'N/A')
                            value = prop.get('Value', 'N/A')
                            print(f"    {name}: {value}")
                    print()

        print(f"{'='*60}")


def main():
    """Main function to handle command-line arguments"""
    parser = argparse.ArgumentParser(
        description="Manage persisted process properties (Update operations only)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Update a single property for a process on an atom
  %(prog)s --update --atom-id ATOM_ID --process-id PROCESS_ID --property "timeout" --value "30000"

  # Bulk update properties for a process on an atom
  %(prog)s --bulk-update --atom-id ATOM_ID --process-id PROCESS_ID --properties '{"timeout": "30000", "retries": "3"}'

Note:
- The Persisted Process Properties API works at the Atom/Runtime level
- You need the Atom/Runtime ID where the process is deployed
- Get/retrieve operations require async endpoints not yet implemented in the SDK
        """
    )

    parser.add_argument('--update', action='store_true',
                       help='Update a single property')
    parser.add_argument('--bulk-update', action='store_true',
                       help='Update multiple properties')

    parser.add_argument('--atom-id', type=str, required=True,
                       help='Atom/Runtime ID (required)')
    parser.add_argument('--process-id', type=str,
                       help='Process ID')
    parser.add_argument('--property', type=str,
                       help='Property name (for single update)')
    parser.add_argument('--value', type=str,
                       help='Property value (for single update)')
    parser.add_argument('--properties', type=str,
                       help='JSON string of properties (for bulk update)')

    parser.add_argument('--verbose', action='store_true',
                       help='Enable verbose output')

    args = parser.parse_args()

    # Validate arguments
    if not any([args.update, args.bulk_update]):
        parser.print_help()
        return 1
    
    try:
        manager = PersistedPropertiesManager(verbose=args.verbose)

        if args.update:
            if not all([args.process_id, args.property, args.value]):
                print("Error: --process-id, --property, and --value are required for single update")
                return 1

            print(f"🔄 Updating single property for process {args.process_id} on atom {args.atom_id}")
            success = manager.update_single_property(
                args.atom_id,
                args.process_id,
                args.property,
                args.value
            )

            config = manager.create_sample_properties_config(
                args.process_id, {args.property: args.value}
            )
            manager.display_update_result(args.atom_id, success, config)

        elif args.bulk_update:
            if not args.process_id or not args.properties:
                print("Error: --process-id and --properties are required for bulk update")
                return 1

            try:
                properties = json.loads(args.properties)
            except json.JSONDecodeError:
                print("Error: Invalid JSON in --properties")
                return 1

            print(f"🔄 Bulk updating {len(properties)} properties for process {args.process_id} on atom {args.atom_id}")
            success = manager.bulk_update_properties(args.atom_id, args.process_id, properties)

            config = manager.create_sample_properties_config(args.process_id, properties)
            manager.display_update_result(args.atom_id, success, config)

        return 0

    except Exception as e:
        print(f"❌ Error: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())