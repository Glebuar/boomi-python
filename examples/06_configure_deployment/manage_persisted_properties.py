#!/usr/bin/env python3
"""
Persisted Process Properties Management

This example demonstrates how to manage persisted process properties including:
- Getting property values for processes on an Atom/Runtime (async operation)
- Updating property values for processes on an Atom/Runtime
- Managing property configurations
- Property bulk updates

Note: The Persisted Process Properties API works at the Atom/Runtime level.
Properties are managed for all processes deployed on a specific runtime.

Available SDK Operations:
- async_get_persisted_process_properties: Get properties for an Atom/Runtime (returns token)
- async_token_persisted_process_properties: Get results using token
- update_persisted_process_properties: Update properties for an Atom/Runtime
"""

import os
import sys
import json
import argparse
import time
from typing import Dict, Any, List, Optional
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
    
    def get_persisted_properties(self, atom_id: str, timeout: int = 30) -> Optional[Dict[str, Any]]:
        """Get persisted properties for an Atom/Runtime (async operation)

        Args:
            atom_id: Atom/Runtime ID
            timeout: Timeout in seconds for async operation

        Returns:
            Properties dictionary or None if failed
        """
        try:
            self._log(f"Initiating async request for persisted properties: {atom_id}")

            # Initiate async request
            token_result = self.sdk.persisted_process_properties.async_get_persisted_process_properties(
                id_=atom_id
            )

            if not hasattr(token_result, 'async_token') or not token_result.async_token:
                self._log("Failed to get async token", "ERROR")
                return None

            token = token_result.async_token.token
            self._log(f"Got async token: {token}")

            # Poll for results
            start_time = time.time()
            poll_interval = 2

            while time.time() - start_time < timeout:
                time.sleep(poll_interval)

                try:
                    self._log(f"Polling for results (attempt {int((time.time() - start_time) / poll_interval)})")
                    response = self.sdk.persisted_process_properties.async_token_persisted_process_properties(
                        token=token
                    )

                    if response:
                        self._log("Successfully retrieved persisted properties")
                        return self._parse_properties(response)

                except Exception as e:
                    # Still waiting for results
                    if "202" in str(e) or "not ready" in str(e).lower():
                        self._log("Results not ready yet, continuing to poll...")
                        continue
                    else:
                        self._log(f"Error polling for results: {e}", "ERROR")
                        return None

            self._log(f"Timeout waiting for properties after {timeout} seconds", "ERROR")
            return None

        except Exception as e:
            self._log(f"Error getting persisted properties: {e}", "ERROR")
            return None

    def _parse_properties(self, response: Any) -> Dict[str, Any]:
        """Parse persisted properties response

        Args:
            response: API response object

        Returns:
            Parsed properties dictionary
        """
        properties = {
            'values': {},
            'metadata': {},
            'raw_data': {}
        }

        try:
            # Handle different response formats
            if hasattr(response, '__dict__'):
                raw_data = response.__dict__
            elif isinstance(response, dict):
                raw_data = response
            else:
                raw_data = {'response': str(response)}

            properties['raw_data'] = raw_data

            # Extract property values
            if 'result' in raw_data and 'PersistedProcessProperties' in raw_data['result']:
                props_data = raw_data['result']['PersistedProcessProperties']
                properties['metadata']['atom_id'] = props_data.get('atomId')

                # Parse process properties
                if 'processes' in props_data:
                    processes = props_data['processes']
                    if not isinstance(processes, list):
                        processes = [processes]

                    for process in processes:
                        process_id = process.get('processId')
                        if process_id and 'PersistedProcessProperties' in process:
                            process_props = process['PersistedProcessProperties'].get('ProcessProperty', [])
                            if not isinstance(process_props, list):
                                process_props = [process_props]

                            for prop in process_props:
                                name = prop.get('name')
                                value = prop.get('value')
                                if name:
                                    properties['values'][name] = value

        except Exception as e:
            self._log(f"Error parsing properties: {e}", "WARNING")

        return properties

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

    # DEFAULT IDs FOR TESTING - REPLACE WITH YOUR ACTUAL IDs
    # These are example IDs that may work in a test environment
    # You MUST replace these with your actual Atom/Runtime and Process IDs
    DEFAULT_ATOM_ID = "3456789a-bcde-f012-3456-789abcdef012"  # Replace with your Atom/Runtime ID
    DEFAULT_PROCESS_ID = "6841b8e2-755e-4ab1-bd31-fcfc9bf7893d"  # Replace with your Process ID

    parser = argparse.ArgumentParser(
        description="Manage persisted process properties",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f"""
Examples:
  # Get properties for an atom/runtime
  %(prog)s --get --atom-id ATOM_ID
  %(prog)s --get  # Uses default: {DEFAULT_ATOM_ID}

  # Update a single property for a process on an atom
  %(prog)s --update --atom-id ATOM_ID --process-id PROCESS_ID --property "timeout" --value "30000"
  %(prog)s --update --property "timeout" --value "30000"  # Uses defaults

  # Bulk update properties for a process on an atom
  %(prog)s --bulk-update --atom-id ATOM_ID --process-id PROCESS_ID --properties '{{"timeout": "30000", "retries": "3"}}'
  %(prog)s --bulk-update --properties '{{"timeout": "30000", "retries": "3"}}'  # Uses defaults

Note:
- The Persisted Process Properties API works at the Atom/Runtime level
- You need the Atom/Runtime ID where the process is deployed
- Get operations are async and may take a few seconds to complete
- Default IDs are provided for testing but MUST be replaced with your actual IDs
        """
    )

    parser.add_argument('--get', action='store_true',
                       help='Get persisted properties for an atom')
    parser.add_argument('--update', action='store_true',
                       help='Update a single property')
    parser.add_argument('--bulk-update', action='store_true',
                       help='Update multiple properties')

    parser.add_argument('--atom-id', type=str,
                       help='Atom/Runtime ID')
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
    if not any([args.get, args.update, args.bulk_update]):
        parser.print_help()
        return 1

    # Use default IDs if not provided (for testing)
    if not args.atom_id:
        print(f"ℹ️ No --atom-id provided, using default: {DEFAULT_ATOM_ID}")
        print("⚠️ WARNING: Replace DEFAULT_ATOM_ID in the script with your actual Atom/Runtime ID")
        args.atom_id = DEFAULT_ATOM_ID

    if (args.update or args.bulk_update) and not args.process_id:
        print(f"ℹ️ No --process-id provided, using default: {DEFAULT_PROCESS_ID}")
        print("⚠️ WARNING: Replace DEFAULT_PROCESS_ID in the script with your actual Process ID")
        args.process_id = DEFAULT_PROCESS_ID

    try:
        manager = PersistedPropertiesManager(verbose=args.verbose)

        if args.get:
            print(f"🔍 Getting persisted properties for atom {args.atom_id}")
            properties = manager.get_persisted_properties(args.atom_id)

            if properties:
                print(f"\n{'='*60}")
                print(f"Persisted Properties for Atom: {args.atom_id}")
                print(f"{'='*60}")

                # Display metadata
                metadata = properties.get('metadata', {})
                if metadata:
                    print("📋 Metadata:")
                    for key, value in metadata.items():
                        print(f"  {key}: {value}")
                    print()

                # Display property values
                values = properties.get('values', {})
                if values:
                    print(f"🔧 Properties ({len(values)}):")
                    for name, value in values.items():
                        print(f"  {name}: {value}")
                else:
                    print("No properties configured")

                # Display raw data if verbose
                if args.verbose and properties.get('raw_data'):
                    print("\n📊 Raw Data:")
                    print(json.dumps(properties['raw_data'], indent=2, default=str))

                print(f"{'='*60}")
            else:
                print("❌ Failed to retrieve persisted properties")

        elif args.update:
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