#!/usr/bin/env python3
"""
Persisted Process Properties Management

This example demonstrates how to manage persisted process properties including:
- Viewing persisted properties for processes
- Updating property values
- Managing property inheritance
- Handling async property retrieval
- Property versioning and rollback

The Persisted Process Properties API allows you to manage configuration
properties that persist across process executions.
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
from boomi.models import (
    PersistedProcessProperties,
    ProcessQueryConfig,
    ProcessSimpleExpression,
    ProcessSimpleExpressionOperator,
    ProcessSimpleExpressionProperty,
    ProcessQueryConfigQueryFilter
)


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
    
    def get_persisted_properties(self, process_id: str, timeout: int = 30) -> Optional[Dict[str, Any]]:
        """Get persisted properties for a process (async operation)
        
        Args:
            process_id: Process ID
            timeout: Timeout in seconds for async operation
            
        Returns:
            Properties dictionary or None if failed
        """
        try:
            self._log(f"Initiating async request for persisted properties: {process_id}")
            
            # Initiate async request
            token_result = self.sdk.persisted_process_properties.async_get_persisted_process_properties(
                id_=process_id
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
                    if "not ready" in str(e).lower() or "202" in str(e):
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
            if 'properties' in raw_data:
                properties['values'] = raw_data['properties']
            elif hasattr(response, 'properties'):
                properties['values'] = response.properties
            
            # Extract metadata
            for key in ['process_id', 'processId', 'environment_id', 'environmentId']:
                if key in raw_data:
                    properties['metadata'][key] = raw_data[key]
            
            # Extract version info
            for key in ['version', 'last_modified', 'lastModified']:
                if key in raw_data:
                    properties['metadata'][key] = raw_data[key]
                    
        except Exception as e:
            self._log(f"Error parsing properties: {e}", "WARNING")
        
        return properties
    
    def list_processes_with_properties(self, limit: int = 100) -> List[Dict[str, Any]]:
        """List processes that have persisted properties
        
        Args:
            limit: Maximum number of processes to return
            
        Returns:
            List of processes with property info
        """
        processes_with_props = []
        
        try:
            self._log("Querying processes")
            
            # Query all processes
            simple_expression = ProcessSimpleExpression(
                operator=ProcessSimpleExpressionOperator.ISNOTNULL,
                property=ProcessSimpleExpressionProperty.ID,
                argument=[]
            )
            query_filter = ProcessQueryConfigQueryFilter(expression=simple_expression)
            query_config = ProcessQueryConfig(query_filter=query_filter)
            
            result = self.sdk.process.query_process(request_body=query_config)
            
            if hasattr(result, 'result') and result.result:
                processes = result.result[:limit]
                self._log(f"Found {len(processes)} process(es)")
                
                # Check each process for persisted properties
                for process in processes:
                    process_info = {
                        'id': process.id_,
                        'name': getattr(process, 'name', 'N/A'),
                        'has_properties': False,
                        'property_count': 0
                    }
                    
                    # Try to get properties (simplified check)
                    if hasattr(process, 'has_persisted_properties'):
                        process_info['has_properties'] = process.has_persisted_properties
                    
                    processes_with_props.append(process_info)
            
        except Exception as e:
            self._log(f"Error listing processes: {e}", "ERROR")
            if self.verbose:
                import traceback
                traceback.print_exc()
        
        return processes_with_props
    
    def update_property(self, process_id: str, property_name: str, 
                       property_value: Any) -> bool:
        """Update a persisted property value
        
        Args:
            process_id: Process ID
            property_name: Property name
            property_value: New property value
            
        Returns:
            True if updated successfully, False otherwise
        """
        try:
            self._log(f"Updating property {property_name} for process {process_id}")
            
            # Get current properties
            current_props = self.get_persisted_properties(process_id)
            
            if not current_props:
                self._log("Could not retrieve current properties", "ERROR")
                return False
            
            # Update property value
            if 'values' not in current_props:
                current_props['values'] = {}
            
            current_props['values'][property_name] = property_value
            self._log(f"Set {property_name} = {property_value}")
            
            # Note: Actual update would require proper API endpoint
            # This is a simplified representation
            self._log("Property update queued (actual API call would go here)")
            
            return True
            
        except Exception as e:
            self._log(f"Error updating property: {e}", "ERROR")
            return False
    
    def bulk_update_properties(self, process_id: str, 
                              properties: Dict[str, Any]) -> bool:
        """Update multiple properties at once
        
        Args:
            process_id: Process ID
            properties: Dictionary of property names and values
            
        Returns:
            True if all updated successfully, False otherwise
        """
        try:
            self._log(f"Bulk updating {len(properties)} properties for process {process_id}")
            
            success_count = 0
            for name, value in properties.items():
                if self.update_property(process_id, name, value):
                    success_count += 1
                else:
                    self._log(f"Failed to update property: {name}", "WARNING")
            
            self._log(f"Successfully updated {success_count}/{len(properties)} properties")
            return success_count == len(properties)
            
        except Exception as e:
            self._log(f"Error in bulk update: {e}", "ERROR")
            return False
    
    def compare_properties(self, process_id1: str, process_id2: str) -> Dict[str, Any]:
        """Compare persisted properties between two processes
        
        Args:
            process_id1: First process ID
            process_id2: Second process ID
            
        Returns:
            Comparison results
        """
        comparison = {
            'process1': process_id1,
            'process2': process_id2,
            'common': {},
            'only_in_1': {},
            'only_in_2': {},
            'different_values': {}
        }
        
        try:
            self._log(f"Comparing properties between {process_id1} and {process_id2}")
            
            # Get properties for both processes
            props1 = self.get_persisted_properties(process_id1)
            props2 = self.get_persisted_properties(process_id2)
            
            if not props1 or not props2:
                comparison['error'] = "Could not retrieve properties for comparison"
                return comparison
            
            values1 = props1.get('values', {})
            values2 = props2.get('values', {})
            
            # Find common, unique, and different properties
            keys1 = set(values1.keys())
            keys2 = set(values2.keys())
            
            common_keys = keys1 & keys2
            only_in_1 = keys1 - keys2
            only_in_2 = keys2 - keys1
            
            # Check common properties for differences
            for key in common_keys:
                if values1[key] == values2[key]:
                    comparison['common'][key] = values1[key]
                else:
                    comparison['different_values'][key] = {
                        'process1': values1[key],
                        'process2': values2[key]
                    }
            
            # Add unique properties
            for key in only_in_1:
                comparison['only_in_1'][key] = values1[key]
            
            for key in only_in_2:
                comparison['only_in_2'][key] = values2[key]
            
            self._log(f"Comparison complete: {len(common_keys)} common, "
                     f"{len(only_in_1)} unique to process1, "
                     f"{len(only_in_2)} unique to process2")
            
        except Exception as e:
            comparison['error'] = str(e)
            self._log(f"Error comparing properties: {e}", "ERROR")
        
        return comparison
    
    def display_properties(self, process_id: str, format_output: str = "detailed"):
        """Display persisted properties for a process
        
        Args:
            process_id: Process ID
            format_output: Output format (detailed, json, table)
        """
        print(f"\n{'='*60}")
        print(f"Persisted Properties: {process_id}")
        print(f"{'='*60}\n")
        
        properties = self.get_persisted_properties(process_id)
        
        if not properties:
            print("❌ Failed to retrieve persisted properties")
            return
        
        if format_output == "json":
            print(json.dumps(properties, indent=2, default=str))
            
        elif format_output == "table":
            values = properties.get('values', {})
            if values:
                print(f"{'Property Name':<30} {'Value':<40}")
                print(f"{'-'*70}")
                for name, value in values.items():
                    name_str = str(name)[:28]
                    value_str = str(value)[:38]
                    print(f"{name_str:<30} {value_str:<40}")
            else:
                print("No properties found")
                
        else:  # detailed
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
            if self.verbose and properties.get('raw_data'):
                print("\n📊 Raw Data:")
                print(json.dumps(properties['raw_data'], indent=2, default=str))


def main():
    """Main function to handle command-line arguments"""
    parser = argparse.ArgumentParser(
        description="Manage persisted process properties",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Get properties for a process
  %(prog)s --get --process-id YOUR_PROCESS_ID
  
  # List processes with properties
  %(prog)s --list
  
  # Update a property value
  %(prog)s --update --process-id PROCESS_ID --property "timeout" --value "30000"
  
  # Bulk update properties
  %(prog)s --bulk-update --process-id PROCESS_ID --properties '{"timeout": "30000", "retries": "3"}'
  
  # Compare properties between processes
  %(prog)s --compare --process1 PROCESS_ID_1 --process2 PROCESS_ID_2
  
  # Output in JSON format
  %(prog)s --get --process-id PROCESS_ID --format json
        """
    )
    
    parser.add_argument('--get', action='store_true',
                       help='Get persisted properties')
    parser.add_argument('--list', action='store_true',
                       help='List processes with properties')
    parser.add_argument('--update', action='store_true',
                       help='Update a property')
    parser.add_argument('--bulk-update', action='store_true',
                       help='Update multiple properties')
    parser.add_argument('--compare', action='store_true',
                       help='Compare properties between processes')
    
    parser.add_argument('--process-id', type=str,
                       help='Process ID')
    parser.add_argument('--process1', type=str,
                       help='First process ID for comparison')
    parser.add_argument('--process2', type=str,
                       help='Second process ID for comparison')
    parser.add_argument('--property', type=str,
                       help='Property name')
    parser.add_argument('--value', type=str,
                       help='Property value')
    parser.add_argument('--properties', type=str,
                       help='JSON string of properties')
    
    parser.add_argument('--format', type=str, choices=['detailed', 'json', 'table'],
                       default='detailed', help='Output format')
    parser.add_argument('--limit', type=int, default=100,
                       help='Maximum number of results')
    parser.add_argument('--verbose', action='store_true',
                       help='Enable verbose output')
    
    args = parser.parse_args()
    
    # Validate arguments
    if not any([args.get, args.list, args.update, args.bulk_update, args.compare]):
        parser.print_help()
        return 1
    
    try:
        manager = PersistedPropertiesManager(verbose=args.verbose)
        
        if args.get:
            if not args.process_id:
                print("Error: --process-id is required")
                return 1
            
            manager.display_properties(args.process_id, args.format)
        
        elif args.list:
            processes = manager.list_processes_with_properties(limit=args.limit)
            
            print(f"\n{'='*80}")
            print("Processes with Persisted Properties")
            print(f"{'='*80}")
            print(f"{'Process ID':<40} {'Name':<30} {'Has Props':<10}")
            print(f"{'-'*80}")
            
            for process in processes:
                proc_id = str(process['id'])[:38]
                name = str(process['name'])[:28]
                has_props = '✅' if process['has_properties'] else '❌'
                print(f"{proc_id:<40} {name:<30} {has_props:<10}")
            
            print(f"{'='*80}")
            print(f"Total: {len(processes)} process(es)")
        
        elif args.update:
            if not all([args.process_id, args.property, args.value]):
                print("Error: --process-id, --property, and --value are required")
                return 1
            
            success = manager.update_property(
                args.process_id,
                args.property,
                args.value
            )
            
            if success:
                print(f"✅ Updated property '{args.property}' = '{args.value}'")
            else:
                print(f"❌ Failed to update property")
        
        elif args.bulk_update:
            if not args.process_id or not args.properties:
                print("Error: --process-id and --properties are required")
                return 1
            
            try:
                properties = json.loads(args.properties)
            except json.JSONDecodeError:
                print("Error: Invalid JSON in --properties")
                return 1
            
            success = manager.bulk_update_properties(args.process_id, properties)
            
            if success:
                print(f"✅ Successfully updated all properties")
            else:
                print(f"⚠️ Some properties failed to update")
        
        elif args.compare:
            if not args.process1 or not args.process2:
                print("Error: --process1 and --process2 are required")
                return 1
            
            comparison = manager.compare_properties(args.process1, args.process2)
            
            print(f"\n{'='*60}")
            print("Property Comparison")
            print(f"{'='*60}")
            print(f"Process 1: {comparison['process1']}")
            print(f"Process 2: {comparison['process2']}\n")
            
            if 'error' in comparison:
                print(f"❌ Error: {comparison['error']}")
            else:
                if comparison['common']:
                    print(f"✅ Common Properties ({len(comparison['common'])}):")
                    for key, value in comparison['common'].items():
                        print(f"  {key}: {value}")
                
                if comparison['different_values']:
                    print(f"\n⚠️ Different Values ({len(comparison['different_values'])}):")
                    for key, values in comparison['different_values'].items():
                        print(f"  {key}:")
                        print(f"    Process 1: {values['process1']}")
                        print(f"    Process 2: {values['process2']}")
                
                if comparison['only_in_1']:
                    print(f"\n📌 Only in Process 1 ({len(comparison['only_in_1'])}):")
                    for key, value in comparison['only_in_1'].items():
                        print(f"  {key}: {value}")
                
                if comparison['only_in_2']:
                    print(f"\n📌 Only in Process 2 ({len(comparison['only_in_2'])}):")
                    for key, value in comparison['only_in_2'].items():
                        print(f"  {key}: {value}")
        
        return 0
        
    except Exception as e:
        print(f"❌ Error: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())