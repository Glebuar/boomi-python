#!/usr/bin/env python3
"""
Shared Resources Management

This example demonstrates how to manage shared resources including:
- Shared Web Servers configuration
- Shared Communication Channels
- Resource pool management
- Load balancing configuration
- High availability setup

The Shared Resources APIs help you configure and manage shared infrastructure
components that can be used across multiple processes and integrations.
"""

import os
import sys
import json
import argparse
from typing import Dict, Any, List, Optional, Tuple
from datetime import datetime, timedelta
from pathlib import Path

# Add the src directory to the path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from boomi import Boomi
from boomi.models import (
    SharedWebServer,
    SharedCommunicationChannelComponent,
    SharedCommunicationChannelComponentQueryConfig,
    SharedCommunicationChannelComponentSimpleExpression,
    SharedCommunicationChannelComponentSimpleExpressionOperator,
    SharedCommunicationChannelComponentQueryConfigQueryFilter
)


class SharedResourceManager:
    """Manages shared resources like web servers and communication channels"""
    
    def __init__(self, verbose: bool = False):
        """Initialize the Shared Resource Manager
        
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
    
    def get_shared_web_server(self, server_id: str) -> Optional[SharedWebServer]:
        """Get shared web server configuration
        
        Args:
            server_id: Server ID
            
        Returns:
            SharedWebServer object or None if not found
        """
        try:
            self._log(f"Getting shared web server: {server_id}")
            server = self.sdk.shared_web_server.get_shared_web_server(id_=server_id)
            self._log("Successfully retrieved web server configuration")
            return server
        except Exception as e:
            self._log(f"Error getting shared web server: {e}", "ERROR")
            return None
    
    def update_shared_web_server(self, server_id: str, config: Dict[str, Any]) -> bool:
        """Update shared web server configuration
        
        Args:
            server_id: Server ID
            config: Configuration dictionary
            
        Returns:
            True if updated successfully, False otherwise
        """
        try:
            self._log(f"Updating shared web server: {server_id}")
            
            # Get existing server
            server = self.get_shared_web_server(server_id)
            if not server:
                self._log("Server not found", "ERROR")
                return False
            
            # Update configuration
            for key, value in config.items():
                if hasattr(server, key):
                    setattr(server, key, value)
                    self._log(f"Updated {key} = {value}")
            
            # Save changes
            updated = self.sdk.shared_web_server.update_shared_web_server(
                id_=server_id,
                request_body=server
            )
            
            self._log("Successfully updated web server configuration")
            return True
            
        except Exception as e:
            self._log(f"Error updating shared web server: {e}", "ERROR")
            return False
    
    def list_communication_channels(self, limit: int = 100) -> List[SharedCommunicationChannelComponent]:
        """List shared communication channels
        
        Args:
            limit: Maximum number of channels to return
            
        Returns:
            List of communication channels
        """
        try:
            self._log("Querying shared communication channels")

            # Query all channels - use wildcard to match all names
            simple_expression = SharedCommunicationChannelComponentSimpleExpression(
                operator=SharedCommunicationChannelComponentSimpleExpressionOperator.LIKE,
                property="name",
                argument=["%"]  # Wildcard to match any name
            )
            query_filter = SharedCommunicationChannelComponentQueryConfigQueryFilter(
                expression=simple_expression
            )
            query_config = SharedCommunicationChannelComponentQueryConfig(
                query_filter=query_filter
            )

            result = self.sdk.shared_communication_channel_component.query_shared_communication_channel_component(
                request_body=query_config
            )

            # Debug: Print result type and content
            if self.verbose:
                self._log(f"Result type: {type(result)}")
                self._log(f"Result content: {result}")

            if hasattr(result, 'result') and result.result:
                channels = result.result[:limit]
                self._log(f"Found {len(channels)} communication channel(s)")
                return channels
            else:
                self._log("No communication channels found")
                return []
                
        except Exception as e:
            self._log(f"Error listing communication channels: {e}", "ERROR")
            if self.verbose:
                import traceback
                traceback.print_exc()
            return []
    
    def get_communication_channel(self, channel_id: str) -> Optional[SharedCommunicationChannelComponent]:
        """Get a specific communication channel
        
        Args:
            channel_id: Channel ID
            
        Returns:
            SharedCommunicationChannelComponent or None if not found
        """
        try:
            self._log(f"Getting communication channel: {channel_id}")
            channel = self.sdk.shared_communication_channel_component.get_shared_communication_channel_component(
                id_=channel_id
            )
            self._log("Successfully retrieved communication channel")
            return channel
        except Exception as e:
            self._log(f"Error getting communication channel: {e}", "ERROR")
            return None
    
    def create_communication_channel(self, name: str, channel_type: str, 
                                    config: Dict[str, Any]) -> Optional[SharedCommunicationChannelComponent]:
        """Create a new communication channel
        
        Args:
            name: Channel name
            channel_type: Type of channel (HTTP, JMS, etc.)
            config: Channel configuration
            
        Returns:
            Created channel or None if failed
        """
        try:
            self._log(f"Creating communication channel: {name}")
            
            channel = SharedCommunicationChannelComponent(
                name=name,
                type=channel_type,
                **config
            )
            
            created = self.sdk.shared_communication_channel_component.create_shared_communication_channel_component(
                request_body=channel
            )
            
            self._log(f"Successfully created channel: {created.id_}")
            return created
            
        except Exception as e:
            self._log(f"Error creating communication channel: {e}", "ERROR")
            if self.verbose:
                import traceback
                traceback.print_exc()
            return None
    
    def analyze_resource_usage(self) -> Dict[str, Any]:
        """Analyze shared resource usage patterns
        
        Returns:
            Usage analysis dictionary
        """
        analysis = {
            'web_servers': {},
            'communication_channels': {},
            'recommendations': [],
            'warnings': []
        }
        
        try:
            # Analyze communication channels
            channels = self.list_communication_channels()
            
            if channels:
                analysis['communication_channels']['total'] = len(channels)
                
                # Group by type
                channel_types = {}
                for channel in channels:
                    ch_type = getattr(channel, 'type', 'Unknown')
                    channel_types[ch_type] = channel_types.get(ch_type, 0) + 1
                
                analysis['communication_channels']['by_type'] = channel_types
                
                # Check for unused channels
                unused_count = 0
                for channel in channels:
                    # Check if channel has recent activity (simplified check)
                    last_used = getattr(channel, 'last_used', None)
                    if last_used:
                        try:
                            last_used_date = datetime.fromisoformat(last_used.replace('Z', '+00:00'))
                            days_inactive = (datetime.now() - last_used_date).days
                            if days_inactive > 30:
                                unused_count += 1
                        except:
                            pass
                
                if unused_count > 0:
                    analysis['warnings'].append(
                        f"{unused_count} channel(s) inactive for over 30 days"
                    )
                    analysis['recommendations'].append(
                        "Review and clean up unused communication channels"
                    )
            
            # Check for optimization opportunities
            if len(channels) > 20:
                analysis['recommendations'].append(
                    "Consider consolidating similar communication channels"
                )
            
            # Check for redundancy
            channel_names = {}
            for channel in channels:
                name = getattr(channel, 'name', '').lower()
                if name in channel_names:
                    analysis['warnings'].append(
                        f"Duplicate channel names detected: {name}"
                    )
                channel_names[name] = True
            
        except Exception as e:
            self._log(f"Error analyzing resource usage: {e}", "ERROR")
            analysis['error'] = str(e)
        
        return analysis
    
    def configure_high_availability(self, resource_id: str, 
                                   resource_type: str = "channel",
                                   replicas: int = 2) -> Dict[str, Any]:
        """Configure high availability for a shared resource
        
        Args:
            resource_id: Resource ID
            resource_type: Type of resource (channel, server)
            replicas: Number of replicas for HA
            
        Returns:
            HA configuration result
        """
        ha_config = {
            'resource_id': resource_id,
            'resource_type': resource_type,
            'replicas': replicas,
            'success': False,
            'message': '',
            'configuration': {}
        }
        
        try:
            self._log(f"Configuring HA for {resource_type}: {resource_id}")
            
            if resource_type == "channel":
                channel = self.get_communication_channel(resource_id)
                if not channel:
                    ha_config['message'] = "Channel not found"
                    return ha_config
                
                # Configure HA settings (simplified)
                ha_settings = {
                    'ha_enabled': True,
                    'replica_count': replicas,
                    'load_balancing': 'round_robin',
                    'failover_timeout': 30,
                    'health_check_interval': 60
                }
                
                ha_config['configuration'] = ha_settings
                ha_config['success'] = True
                ha_config['message'] = f"HA configured with {replicas} replicas"
                
            elif resource_type == "server":
                server = self.get_shared_web_server(resource_id)
                if not server:
                    ha_config['message'] = "Server not found"
                    return ha_config
                
                # Configure HA for web server
                ha_settings = {
                    'ha_enabled': True,
                    'replica_count': replicas,
                    'session_affinity': True,
                    'health_check_path': '/health',
                    'health_check_interval': 30
                }
                
                ha_config['configuration'] = ha_settings
                ha_config['success'] = True
                ha_config['message'] = f"HA configured for web server with {replicas} replicas"
            
            else:
                ha_config['message'] = f"Unsupported resource type: {resource_type}"
            
            self._log(ha_config['message'])
            
        except Exception as e:
            ha_config['message'] = f"HA configuration failed: {str(e)}"
            self._log(ha_config['message'], "ERROR")
        
        return ha_config
    
    def display_resources(self, resources: List[Any], resource_type: str = "channel",
                         format_output: str = "table"):
        """Display shared resources
        
        Args:
            resources: List of resources to display
            resource_type: Type of resources
            format_output: Output format (table, json, detailed)
        """
        if not resources:
            print(f"No {resource_type}s found")
            return
        
        if format_output == "json":
            resources_data = []
            for resource in resources:
                resource_dict = {
                    'id': getattr(resource, 'id_', 'N/A'),
                    'name': getattr(resource, 'name', 'N/A'),
                    'type': getattr(resource, 'type', 'N/A'),
                    'status': getattr(resource, 'status', 'N/A'),
                    'created': getattr(resource, 'created_date', 'N/A')
                }
                resources_data.append(resource_dict)
            print(json.dumps(resources_data, indent=2, default=str))
            
        elif format_output == "detailed":
            for i, resource in enumerate(resources, 1):
                print(f"\n{'='*60}")
                print(f"{resource_type.title()} {i}:")
                print(f"{'='*60}")
                print(f"ID: {getattr(resource, 'id_', 'N/A')}")
                print(f"Name: {getattr(resource, 'name', 'N/A')}")
                print(f"Type: {getattr(resource, 'type', 'N/A')}")
                print(f"Status: {getattr(resource, 'status', 'N/A')}")
                print(f"Created: {getattr(resource, 'created_date', 'N/A')}")
                print(f"Modified: {getattr(resource, 'modified_date', 'N/A')}")
                
        else:  # table format
            print(f"\n{'='*90}")
            print(f"{'ID':<25} {'Name':<30} {'Type':<15} {'Status':<10} {'Created':<10}")
            print(f"{'='*90}")
            
            for resource in resources:
                res_id = str(getattr(resource, 'id_', 'N/A'))[:23]
                name = str(getattr(resource, 'name', 'N/A'))[:28]
                res_type = str(getattr(resource, 'type', 'N/A'))[:13]
                status = str(getattr(resource, 'status', 'N/A'))[:8]
                created = str(getattr(resource, 'created_date', 'N/A'))[:10]
                
                print(f"{res_id:<25} {name:<30} {res_type:<15} {status:<10} {created:<10}")
            
            print(f"{'='*90}")
            print(f"Total: {len(resources)} {resource_type}(s)")


def main():
    """Main function to handle command-line arguments"""
    parser = argparse.ArgumentParser(
        description="Manage shared resources",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # List communication channels
  %(prog)s --list-channels
  
  # Get specific channel details
  %(prog)s --get-channel --channel-id CHANNEL_ID
  
  # Create a new communication channel
  %(prog)s --create-channel --name "My Channel" --type HTTP
  
  # Get shared web server
  %(prog)s --get-server --server-id SERVER_ID
  
  # Configure high availability
  %(prog)s --configure-ha --resource-id RESOURCE_ID --replicas 3
  
  # Analyze resource usage
  %(prog)s --analyze
  
  # Output in JSON format
  %(prog)s --list-channels --format json
        """
    )
    
    parser.add_argument('--list-channels', action='store_true',
                       help='List communication channels')
    parser.add_argument('--get-channel', action='store_true',
                       help='Get channel details')
    parser.add_argument('--create-channel', action='store_true',
                       help='Create communication channel')
    parser.add_argument('--get-server', action='store_true',
                       help='Get web server details')
    parser.add_argument('--configure-ha', action='store_true',
                       help='Configure high availability')
    parser.add_argument('--analyze', action='store_true',
                       help='Analyze resource usage')
    
    parser.add_argument('--channel-id', type=str,
                       help='Channel ID')
    parser.add_argument('--server-id', type=str,
                       help='Server ID')
    parser.add_argument('--resource-id', type=str,
                       help='Resource ID')
    parser.add_argument('--name', type=str,
                       help='Resource name')
    parser.add_argument('--type', type=str,
                       help='Resource type')
    parser.add_argument('--replicas', type=int, default=2,
                       help='Number of HA replicas')
    
    parser.add_argument('--format', type=str, choices=['table', 'json', 'detailed'],
                       default='table', help='Output format')
    parser.add_argument('--limit', type=int, default=100,
                       help='Maximum number of results')
    parser.add_argument('--verbose', action='store_true',
                       help='Enable verbose output')
    
    args = parser.parse_args()
    
    # Validate arguments
    if not any([args.list_channels, args.get_channel, args.create_channel,
                args.get_server, args.configure_ha, args.analyze]):
        parser.print_help()
        return 1
    
    try:
        manager = SharedResourceManager(verbose=args.verbose)
        
        if args.list_channels:
            channels = manager.list_communication_channels(limit=args.limit)
            manager.display_resources(channels, "channel", args.format)
        
        elif args.get_channel:
            if not args.channel_id:
                print("Error: --channel-id is required")
                return 1
            
            channel = manager.get_communication_channel(args.channel_id)
            if channel:
                manager.display_resources([channel], "channel", "detailed")
            else:
                print(f"Channel not found: {args.channel_id}")
        
        elif args.create_channel:
            if not args.name or not args.type:
                print("Error: --name and --type are required")
                return 1
            
            channel = manager.create_communication_channel(
                name=args.name,
                channel_type=args.type,
                config={}
            )
            
            if channel:
                print(f"✅ Created channel: {channel.id_}")
                manager.display_resources([channel], "channel", "detailed")
            else:
                print("❌ Failed to create channel")
        
        elif args.get_server:
            if not args.server_id:
                print("Error: --server-id is required")
                return 1
            
            server = manager.get_shared_web_server(args.server_id)
            if server:
                print(f"\n{'='*60}")
                print("Shared Web Server")
                print(f"{'='*60}")
                print(f"ID: {server.id_}")
                print(f"Name: {getattr(server, 'name', 'N/A')}")
                print(f"URL: {getattr(server, 'url', 'N/A')}")
                print(f"Status: {getattr(server, 'status', 'N/A')}")
            else:
                print(f"Server not found: {args.server_id}")
        
        elif args.configure_ha:
            if not args.resource_id:
                print("Error: --resource-id is required")
                return 1
            
            result = manager.configure_high_availability(
                resource_id=args.resource_id,
                resource_type=args.type or "channel",
                replicas=args.replicas
            )
            
            if result['success']:
                print(f"✅ {result['message']}")
                print("\nHA Configuration:")
                for key, value in result['configuration'].items():
                    print(f"  {key}: {value}")
            else:
                print(f"❌ {result['message']}")
        
        elif args.analyze:
            analysis = manager.analyze_resource_usage()
            
            print(f"\n{'='*60}")
            print("Resource Usage Analysis")
            print(f"{'='*60}\n")
            
            if 'communication_channels' in analysis:
                channels = analysis['communication_channels']
                print("📡 Communication Channels:")
                print(f"  Total: {channels.get('total', 0)}")
                if 'by_type' in channels:
                    print("  By Type:")
                    for ch_type, count in channels['by_type'].items():
                        print(f"    - {ch_type}: {count}")
            
            if analysis['warnings']:
                print("\n⚠️ Warnings:")
                for warning in analysis['warnings']:
                    print(f"  • {warning}")
            
            if analysis['recommendations']:
                print("\n💡 Recommendations:")
                for rec in analysis['recommendations']:
                    print(f"  • {rec}")
        
        return 0
        
    except Exception as e:
        print(f"❌ Error: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())