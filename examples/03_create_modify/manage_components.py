#!/usr/bin/env python3
"""
Boomi SDK Example: Comprehensive Component Management
===================================================

This example provides comprehensive component management capabilities using the Boomi SDK.
It combines component CRUD operations, querying, analysis, and metadata management into a single tool.

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- Account must have appropriate permissions for component operations
- Python 3.7+

Usage:
    # List all components
    PYTHONPATH=../../src python3 manage_components.py --list
    
    # List with filtering
    PYTHONPATH=../../src python3 manage_components.py --list --type process --limit 10
    PYTHONPATH=../../src python3 manage_components.py --list --folder "MyFolder" --current-only
    PYTHONPATH=../../src python3 manage_components.py --list --name-pattern "*API*"
    
    # Get specific component details  
    PYTHONPATH=../../src python3 manage_components.py --get COMPONENT_ID
    PYTHONPATH=../../src python3 manage_components.py --get COMPONENT_ID --version 2 --detailed
    
    # Clone component
    PYTHONPATH=../../src python3 manage_components.py --clone COMPONENT_ID --name "New Component Name"
    
    # Update component (description/name only - XML requires separate handling)
    PYTHONPATH=../../src python3 manage_components.py --update COMPONENT_ID --name "Updated Name" --description "New description"
    
    # Query components with custom filters
    PYTHONPATH=../../src python3 manage_components.py --query --property type --operator EQUALS --value "process"
    
    # Show component statistics
    PYTHONPATH=../../src python3 manage_components.py --stats
    
    # Analyze component structure (detailed XML analysis)
    PYTHONPATH=../../src python3 manage_components.py --analyze COMPONENT_ID
    
    # Help and examples
    PYTHONPATH=../../src python3 manage_components.py --help-examples

Features:
- Complete component CRUD operations
- Advanced filtering and querying capabilities
- Component statistics and analysis
- XML structure analysis and validation
- Component cloning functionality
- Detailed metadata display
- Version management
- Folder organization analysis

Endpoints Used:
- component.get_component
- component.create_component
- component.update_component
- component_metadata.query_component_metadata
"""

import os
import sys
import argparse
import time
import xml.etree.ElementTree as ET
from datetime import datetime
from typing import List, Optional, Dict, Any

# Add the src directory to the path to import the SDK
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

from boomi import Boomi
from boomi.models import (
    ComponentMetadataQueryConfig,
    ComponentMetadataQueryConfigQueryFilter,
    ComponentMetadataSimpleExpression,
    ComponentMetadataSimpleExpressionOperator,
    ComponentMetadataSimpleExpressionProperty
)


class ComponentManager:
    """Comprehensive component management using Boomi SDK."""
    
    def __init__(self, account_id: str, username: str, password: str, timeout: int = 30000):
        """Initialize the Component Manager with Boomi SDK."""
        self.sdk = Boomi(
            account_id=account_id,
            username=username,
            password=password,
            timeout=timeout
        )
    
    def list_components(self, component_type: Optional[str] = None,
                       folder: Optional[str] = None,
                       name_pattern: Optional[str] = None,
                       current_only: bool = True,
                       limit: Optional[int] = None) -> List[Any]:
        """
        List components with optional filtering.
        
        Args:
            component_type: Filter by type (process, connector, profile, etc.)
            folder: Filter by folder name/path
            name_pattern: Filter by name pattern (supports wildcards)
            current_only: Show only current versions (default: True)
            limit: Limit number of results
        
        Returns:
            List of component metadata objects
        """
        try:
            print("🔍 Querying components...")
            
            # Build query expression
            if component_type:
                expression = ComponentMetadataSimpleExpression(
                    operator=ComponentMetadataSimpleExpressionOperator.EQUALS,
                    property=ComponentMetadataSimpleExpressionProperty.TYPE,
                    argument=[component_type]
                )
            elif name_pattern:
                # Convert wildcards to LIKE pattern
                like_pattern = name_pattern.replace('*', '%')
                expression = ComponentMetadataSimpleExpression(
                    operator=ComponentMetadataSimpleExpressionOperator.LIKE,
                    property=ComponentMetadataSimpleExpressionProperty.NAME,
                    argument=[like_pattern]
                )
            else:
                # Query all components
                expression = ComponentMetadataSimpleExpression(
                    operator=ComponentMetadataSimpleExpressionOperator.LIKE,
                    property=ComponentMetadataSimpleExpressionProperty.NAME,
                    argument=["%"]  # Wildcard that matches all names
                )
            
            query_filter = ComponentMetadataQueryConfigQueryFilter(expression=expression)
            query_config = ComponentMetadataQueryConfig(query_filter=query_filter)
            
            response = self.sdk.component_metadata.query_component_metadata(request_body=query_config)
            
            components = []
            if hasattr(response, 'result') and response.result:
                all_components = response.result
                
                # Apply filters
                filtered_components = all_components
                
                # Filter by folder if specified
                if folder:
                    filtered_components = [c for c in filtered_components
                                         if (getattr(c, 'folder_full_path', '') or 
                                             getattr(c, 'folder_name', '')).lower().find(folder.lower()) >= 0]
                
                # Filter to current versions only if requested
                if current_only:
                    filtered_components = [c for c in filtered_components
                                         if str(getattr(c, 'current_version', 'false')).lower() == 'true'
                                         and str(getattr(c, 'deleted', 'true')).lower() == 'false']
                
                components = filtered_components
            
            if limit and len(components) > limit:
                components = components[:limit]
            
            return components
            
        except Exception as e:
            print(f"❌ Error listing components: {e}")
            return []
    
    def get_component(self, component_id: str, version: Optional[str] = None) -> Optional[Any]:
        """
        Get detailed information about a specific component.
        
        Args:
            component_id: The component ID
            version: Specific version (optional, defaults to latest)
            
        Returns:
            Component object or None if not found
        """
        try:
            # Construct component identifier
            if version:
                component_identifier = f"{component_id}~{version}"
            else:
                component_identifier = component_id
            
            print(f"🔍 Getting component: {component_identifier}")
            component = self.sdk.component.get_component(component_id=component_identifier)
            return component
            
        except Exception as e:
            print(f"❌ Error getting component {component_id}: {e}")
            if hasattr(e, 'status') and e.status == 404:
                print("   Component not found")
            return None
    
    def clone_component(self, source_component_id: str, new_name: str, 
                       description: Optional[str] = None) -> Optional[Any]:
        """
        Clone an existing component with a new name.
        
        Args:
            source_component_id: ID of component to clone
            new_name: Name for the new component
            description: Optional description for the new component
            
        Returns:
            Created component object or None if failed
        """
        try:
            print(f"🔄 Cloning component: {source_component_id}")
            print(f"   New name: {new_name}")
            
            # Get source component
            source_component = self.get_component(source_component_id)
            if not source_component:
                print("❌ Source component not found")
                return None
            
            # Generate XML for cloning
            if hasattr(source_component, 'to_xml') and callable(source_component.to_xml):
                xml_str = source_component.to_xml()
            else:
                print("❌ Cannot extract XML from source component")
                return None
            
            # Parse and modify XML
            root = ET.fromstring(xml_str)
            
            # Update name and remove unique identifiers
            root.set('name', new_name)
            if description:
                # Try to set description if the element exists
                desc_elem = root.find('.//description') or root.find('.//{*}description')
                if desc_elem is not None:
                    desc_elem.text = description
                else:
                    # Add description as attribute if no element found
                    root.set('description', description)
            
            # Remove unique identifiers for creation
            for attr in ['componentId', 'version', 'currentVersion', 'createdDate', 
                        'createdBy', 'modifiedDate', 'modifiedBy']:
                if attr in root.attrib:
                    del root.attrib[attr]
            
            new_xml = ET.tostring(root, encoding='unicode')
            
            # Create new component
            print("   Creating cloned component...")
            result = self.sdk.component.create_component(request_body=new_xml)
            print("✅ Component cloned successfully!")
            
            return result
            
        except Exception as e:
            print(f"❌ Error cloning component: {e}")
            return None
    
    def update_component_metadata(self, component_id: str, 
                                 new_name: Optional[str] = None,
                                 new_description: Optional[str] = None) -> Optional[Any]:
        """
        Update component metadata (name, description).
        Note: For XML changes, use separate XML-specific tools.
        
        Args:
            component_id: Component ID to update
            new_name: New component name
            new_description: New component description
            
        Returns:
            Updated component object or None if failed
        """
        try:
            print(f"🔄 Updating component metadata: {component_id}")
            
            if not any([new_name, new_description]):
                print("❌ No updates specified")
                return None
            
            # Get current component
            component = self.get_component(component_id)
            if not component:
                return None
            
            # Generate updated XML
            if hasattr(component, 'to_xml') and callable(component.to_xml):
                xml_str = component.to_xml()
            else:
                print("❌ Cannot extract XML from component")
                return None
            
            # Parse and modify XML
            root = ET.fromstring(xml_str)
            
            if new_name:
                root.set('name', new_name)
                print(f"   Updated name to: {new_name}")
            
            if new_description:
                # Try to set description
                desc_elem = root.find('.//description') or root.find('.//{*}description')
                if desc_elem is not None:
                    desc_elem.text = new_description
                else:
                    root.set('description', new_description)
                print(f"   Updated description to: {new_description}")
            
            modified_xml = ET.tostring(root, encoding='unicode')
            
            # Update component
            result = self.sdk.component.update_component(
                component_id=component_id,
                request_body=modified_xml
            )
            
            print("✅ Component updated successfully!")
            return result
            
        except Exception as e:
            print(f"❌ Error updating component: {e}")
            return None
    
    def query_components(self, property_name: str, operator: str, value: str) -> List[Any]:
        """
        Query components with custom filters.
        
        Args:
            property_name: Property to filter on (name, type, etc.)
            operator: Comparison operator (EQUALS, LIKE, etc.)
            value: Value to compare against
            
        Returns:
            List of matching components
        """
        try:
            print(f"🔍 Querying components: {property_name} {operator} {value}")
            
            # Map property names
            property_map = {
                'name': ComponentMetadataSimpleExpressionProperty.NAME,
                'type': ComponentMetadataSimpleExpressionProperty.TYPE,
                'id': ComponentMetadataSimpleExpressionProperty.COMPONENTID,
                'folder': ComponentMetadataSimpleExpressionProperty.FOLDERNAME
            }
            
            # Map operators
            operator_map = {
                'EQUALS': ComponentMetadataSimpleExpressionOperator.EQUALS,
                'LIKE': ComponentMetadataSimpleExpressionOperator.LIKE,
                'CONTAINS': ComponentMetadataSimpleExpressionOperator.CONTAINS
            }
            
            if property_name not in property_map:
                print(f"❌ Invalid property: {property_name}")
                print(f"   Valid options: {', '.join(property_map.keys())}")
                return []
            
            if operator not in operator_map:
                print(f"❌ Invalid operator: {operator}")
                print(f"   Valid options: {', '.join(operator_map.keys())}")
                return []
            
            expression = ComponentMetadataSimpleExpression(
                operator=operator_map[operator],
                property=property_map[property_name],
                argument=[value]
            )
            
            query_filter = ComponentMetadataQueryConfigQueryFilter(expression=expression)
            query_config = ComponentMetadataQueryConfig(query_filter=query_filter)
            
            response = self.sdk.component_metadata.query_component_metadata(request_body=query_config)
            
            components = []
            if hasattr(response, 'result') and response.result:
                components = response.result if isinstance(response.result, list) else [response.result]
            
            return components
            
        except Exception as e:
            print(f"❌ Error querying components: {e}")
            return []
    
    def analyze_component_xml(self, component_id: str, version: Optional[str] = None) -> Dict[str, Any]:
        """
        Perform detailed XML analysis of a component.
        
        Args:
            component_id: Component ID to analyze
            version: Specific version (optional)
            
        Returns:
            Dictionary with analysis results
        """
        try:
            component = self.get_component(component_id, version)
            if not component:
                return {"error": "Component not found"}
            
            analysis = {
                "basic_info": {
                    "name": getattr(component, 'name', 'N/A'),
                    "type": getattr(component, 'type_', 'N/A'),
                    "version": getattr(component, 'version', 'N/A'),
                    "deleted": getattr(component, 'deleted', 'false'),
                    "current": getattr(component, 'current_version', 'false')
                },
                "xml_structure": {},
                "complexity_metrics": {}
            }
            
            # Analyze XML structure
            xml_obj = getattr(component, 'object', None)
            if xml_obj:
                analysis["xml_structure"]["has_config"] = True
                
                # Try to analyze structure if it's a dict-like object
                if hasattr(xml_obj, '__dict__'):
                    obj_dict = xml_obj.__dict__
                    analysis["xml_structure"]["top_level_elements"] = len([k for k in obj_dict.keys() if not k.startswith('_')])
                    analysis["xml_structure"]["element_names"] = [k for k in obj_dict.keys() if not k.startswith('_')][:10]  # First 10
                
                # Complexity metrics
                xml_str = ""
                if hasattr(component, 'to_xml') and callable(component.to_xml):
                    xml_str = component.to_xml()
                    analysis["complexity_metrics"]["xml_length"] = len(xml_str)
                    analysis["complexity_metrics"]["xml_lines"] = xml_str.count('\n') + 1
                    
                    # Count XML elements
                    try:
                        root = ET.fromstring(xml_str)
                        analysis["complexity_metrics"]["xml_elements"] = len(list(root.iter()))
                        analysis["complexity_metrics"]["xml_depth"] = self._calculate_xml_depth(root)
                    except ET.ParseError:
                        analysis["complexity_metrics"]["parse_error"] = True
            else:
                analysis["xml_structure"]["has_config"] = False
            
            return analysis
            
        except Exception as e:
            return {"error": str(e)}
    
    def _calculate_xml_depth(self, element, depth=0):
        """Calculate maximum depth of XML tree."""
        if not list(element):
            return depth
        return max(self._calculate_xml_depth(child, depth + 1) for child in element)
    
    def get_component_stats(self) -> Dict[str, Any]:
        """
        Get comprehensive component statistics.
        
        Returns:
            Dictionary with component statistics
        """
        try:
            print("📊 Gathering component statistics...")
            
            # Get all components
            all_components = self.list_components(current_only=False)  # Get all versions
            current_components = [c for c in all_components 
                                if str(getattr(c, 'current_version', 'false')).lower() == 'true'
                                and str(getattr(c, 'deleted', 'true')).lower() == 'false']
            
            if not all_components:
                return {"total": 0}
            
            stats = {
                "total_versions": len(all_components),
                "current_active": len(current_components),
                "by_type": {},
                "by_folder": {},
                "by_status": {"current": 0, "historical": 0, "deleted": 0},
                "creation_summary": {}
            }
            
            # Analyze all components
            for comp in all_components:
                comp_type = getattr(comp, 'type_', 'Unknown')
                folder = getattr(comp, 'folder_full_path', None) or getattr(comp, 'folder_name', None) or 'Root'
                current = str(getattr(comp, 'current_version', 'false')).lower() == 'true'
                deleted = str(getattr(comp, 'deleted', 'false')).lower() == 'true'
                created_by = getattr(comp, 'created_by', 'Unknown')
                
                # Count by type
                stats["by_type"][comp_type] = stats["by_type"].get(comp_type, 0) + 1
                
                # Count by folder
                stats["by_folder"][folder] = stats["by_folder"].get(folder, 0) + 1
                
                # Count by status
                if deleted:
                    stats["by_status"]["deleted"] += 1
                elif current:
                    stats["by_status"]["current"] += 1
                else:
                    stats["by_status"]["historical"] += 1
                
                # Count by creator
                stats["creation_summary"][created_by] = stats["creation_summary"].get(created_by, 0) + 1
            
            return stats
            
        except Exception as e:
            print(f"❌ Error getting component statistics: {e}")
            return {"error": str(e)}


def format_date(date_str: str) -> str:
    """Format ISO date string to readable format."""
    if date_str and 'T' in date_str:
        return date_str.split('T')[0] + ' ' + date_str.split('T')[1].split('.')[0]
    return date_str or 'N/A'


def display_component(comp: Any, detailed: bool = False) -> None:
    """Display component information in a formatted way."""
    
    name = getattr(comp, 'name', 'N/A')
    comp_id = getattr(comp, 'component_id', 'N/A')
    comp_type = getattr(comp, 'type_', 'N/A')
    version = getattr(comp, 'version', 'N/A')
    
    # Type-specific icons
    type_icons = {
        'process': '⚙️',
        'connector': '🔌',
        'profile': '📋',
        'document': '📄',
        'tradingpartner': '🤝'
    }
    
    icon = type_icons.get(comp_type.lower(), '📦')
    
    # Status indicators
    current_version = str(getattr(comp, 'current_version', 'false')).lower() == 'true'
    deleted = str(getattr(comp, 'deleted', 'false')).lower() == 'true'
    
    status_parts = []
    if current_version:
        status_parts.append("CURRENT")
    if deleted:
        status_parts.append("DELETED")
    
    status_str = f" [{' | '.join(status_parts)}]" if status_parts else ""
    
    print(f"{icon} {name}{status_str}")
    print(f"   🆔 ID: {comp_id}")
    print(f"   📋 Type: {comp_type}")
    print(f"   📌 Version: {version}")
    
    if detailed:
        # Additional details
        folder = getattr(comp, 'folder_full_path', None) or getattr(comp, 'folder_name', None)
        if folder:
            print(f"   📁 Folder: {folder}")
        
        created_by = getattr(comp, 'created_by', 'N/A')
        created_date = getattr(comp, 'created_date', 'N/A')
        modified_by = getattr(comp, 'modified_by', 'N/A')
        modified_date = getattr(comp, 'modified_date', 'N/A')
        
        print(f"   👤 Created: {format_date(created_date)} by {created_by}")
        print(f"   ✏️ Modified: {format_date(modified_date)} by {modified_by}")
        
        branch = getattr(comp, 'branch_name', None)
        if branch and branch != 'main':
            print(f"   🌿 Branch: {branch}")
    
    print()


def display_components_list(components: List[Any], title: str = "Components", detailed: bool = False) -> None:
    """Display a list of components in a formatted way."""
    
    if not components:
        print(f"   No {title.lower()} found")
        return
    
    print(f"\n✅ Found {len(components)} {title.lower()}:")
    print("=" * 70)
    
    # Group by folder for better organization
    by_folder = {}
    for comp in components:
        folder = getattr(comp, 'folder_full_path', None) or getattr(comp, 'folder_name', None) or 'Root'
        if folder not in by_folder:
            by_folder[folder] = []
        by_folder[folder].append(comp)
    
    # Display by folder
    for folder, folder_components in sorted(by_folder.items()):
        print(f"\n📁 Folder: {folder}")
        print("   " + "-" * 60)
        
        for i, comp in enumerate(folder_components, 1):
            print(f"   {i:2}. ", end="")
            display_component(comp, detailed)


def display_analysis(analysis: Dict[str, Any], component_id: str) -> None:
    """Display component analysis results."""
    
    if "error" in analysis:
        print(f"❌ Analysis failed: {analysis['error']}")
        return
    
    print(f"\n🔍 Component Analysis for {component_id}")
    print("=" * 60)
    
    # Basic info
    basic = analysis.get("basic_info", {})
    print(f"📋 Basic Information:")
    print(f"   Name: {basic.get('name', 'N/A')}")
    print(f"   Type: {basic.get('type', 'N/A')}")
    print(f"   Version: {basic.get('version', 'N/A')}")
    print(f"   Status: Current={basic.get('current', 'N/A')}, Deleted={basic.get('deleted', 'N/A')}")
    
    # XML structure
    xml_struct = analysis.get("xml_structure", {})
    print(f"\n🔧 XML Configuration:")
    if xml_struct.get("has_config", False):
        print(f"   ✅ Has XML configuration")
        if "top_level_elements" in xml_struct:
            print(f"   📊 Top-level elements: {xml_struct['top_level_elements']}")
        if "element_names" in xml_struct:
            element_names = xml_struct["element_names"]
            print(f"   🔑 Elements: {', '.join(element_names[:5])}")
            if len(element_names) > 5:
                print(f"        ... and {len(element_names) - 5} more")
    else:
        print(f"   ❌ No XML configuration found")
    
    # Complexity metrics
    complexity = analysis.get("complexity_metrics", {})
    if complexity:
        print(f"\n📊 Complexity Metrics:")
        if "xml_length" in complexity:
            print(f"   📏 XML length: {complexity['xml_length']:,} characters")
        if "xml_lines" in complexity:
            print(f"   📝 XML lines: {complexity['xml_lines']:,}")
        if "xml_elements" in complexity:
            print(f"   🏗️ XML elements: {complexity['xml_elements']:,}")
        if "xml_depth" in complexity:
            print(f"   🌳 XML depth: {complexity['xml_depth']} levels")
        if complexity.get("parse_error", False):
            print(f"   ⚠️ XML parse error detected")


def display_stats(stats: Dict[str, Any]) -> None:
    """Display component statistics."""
    
    if "error" in stats:
        print(f"❌ Error in statistics: {stats['error']}")
        return
    
    if stats.get("total_versions", 0) == 0:
        print("📊 No components found")
        return
    
    print(f"\n📊 Component Statistics:")
    print("=" * 50)
    print(f"   Total component versions: {stats['total_versions']}")
    print(f"   Current active components: {stats['current_active']}")
    
    # Status breakdown
    status_info = stats.get("by_status", {})
    print(f"\n   📈 By Status:")
    print(f"     🟢 Current: {status_info.get('current', 0)}")
    print(f"     🟡 Historical: {status_info.get('historical', 0)}")
    print(f"     🔴 Deleted: {status_info.get('deleted', 0)}")
    
    # Type breakdown
    type_info = stats.get("by_type", {})
    if type_info:
        print(f"\n   📋 By Type:")
        for comp_type, count in sorted(type_info.items()):
            icon = {'process': '⚙️', 'connector': '🔌', 'profile': '📋'}.get(comp_type.lower(), '📦')
            print(f"     {icon} {comp_type}: {count}")
    
    # Top folders
    folder_info = stats.get("by_folder", {})
    if folder_info:
        print(f"\n   📁 Top Folders:")
        sorted_folders = sorted(folder_info.items(), key=lambda x: x[1], reverse=True)
        for folder, count in sorted_folders[:5]:
            print(f"     📂 {folder}: {count}")
        if len(sorted_folders) > 5:
            print(f"     ... and {len(sorted_folders) - 5} more")
    
    print(f"\n💡 Tips:")
    print(f"   • Use --list --current-only to see only active components")
    print(f"   • Use --get COMPONENT_ID to analyze specific components")
    print(f"   • Use --clone to duplicate components for development")


def show_help_examples():
    """Show comprehensive usage examples."""
    
    examples = """
🚀 Component Management Examples
===============================

LISTING COMPONENTS:
  # List all current active components
  python3 manage_components.py --list
  
  # List only process components
  python3 manage_components.py --list --type process
  
  # List components in specific folder
  python3 manage_components.py --list --folder "MyFolder"
  
  # List all versions (including deleted)
  python3 manage_components.py --list --include-deleted
  
  # List with name pattern and limit
  python3 manage_components.py --list --name-pattern "*API*" --limit 10

COMPONENT DETAILS:
  # Get specific component
  python3 manage_components.py --get 12345678-1234-1234-1234-123456789012
  
  # Get specific version with detailed info
  python3 manage_components.py --get 12345678-1234-1234-1234-123456789012 --version 2 --detailed

COMPONENT OPERATIONS:
  # Clone component
  python3 manage_components.py --clone 12345678-1234-1234-1234-123456789012 --name "My New Process"
  
  # Clone with description
  python3 manage_components.py --clone 12345678-1234-1234-1234-123456789012 --name "Cloned Process" --description "Test clone"
  
  # Update component metadata
  python3 manage_components.py --update 12345678-1234-1234-1234-123456789012 --name "Updated Name" --description "New description"

QUERYING WITH FILTERS:
  # Query by type
  python3 manage_components.py --query --property type --operator EQUALS --value "process"
  
  # Query by name pattern
  python3 manage_components.py --query --property name --operator LIKE --value "%integration%"
  
  # Query by folder
  python3 manage_components.py --query --property folder --operator CONTAINS --value "Production"

ANALYSIS:
  # Analyze component structure
  python3 manage_components.py --analyze 12345678-1234-1234-1234-123456789012
  
  # Analyze specific version
  python3 manage_components.py --analyze 12345678-1234-1234-1234-123456789012 --version 1

STATISTICS:
  # Show comprehensive statistics
  python3 manage_components.py --stats

COMMON WORKFLOWS:
  # Find all process components and show details
  python3 manage_components.py --list --type process --detailed
  
  # Clone a component and verify creation
  python3 manage_components.py --clone COMPONENT_ID --name "New Component"
  python3 manage_components.py --list --name-pattern "*New Component*"
  
  # Analyze complexity of all process components
  python3 manage_components.py --list --type process
  # Then use --analyze with specific component IDs

NOTES:
  • Component IDs are UUIDs (36 characters with hyphens)
  • Types include: process, connector, profile, document, tradingpartner
  • XML modification requires separate tools - this handles metadata only
  • Cloning preserves XML structure but creates new component IDs
  • Use quotes around names with spaces or special characters
"""
    
    print(examples)


def main():
    """Main function for component management CLI."""
    
    parser = argparse.ArgumentParser(
        description="Comprehensive Component Management using Boomi SDK",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Use --help-examples for detailed usage examples"
    )
    
    # Main actions (mutually exclusive)
    action_group = parser.add_mutually_exclusive_group(required=True)
    action_group.add_argument('--list', action='store_true',
                             help='List components')
    action_group.add_argument('--get', metavar='COMP_ID',
                             help='Get specific component details')
    action_group.add_argument('--clone', metavar='COMP_ID',
                             help='Clone existing component')
    action_group.add_argument('--update', metavar='COMP_ID',
                             help='Update component metadata')
    action_group.add_argument('--query', action='store_true',
                             help='Query components with custom filters')
    action_group.add_argument('--analyze', metavar='COMP_ID',
                             help='Analyze component XML structure')
    action_group.add_argument('--stats', action='store_true',
                             help='Show component statistics')
    action_group.add_argument('--help-examples', action='store_true',
                             help='Show detailed usage examples')
    
    # Options for list
    parser.add_argument('--type', choices=['process', 'connector', 'profile', 'document', 'tradingpartner'],
                       help='Filter by component type')
    parser.add_argument('--folder', help='Filter by folder name/path')
    parser.add_argument('--name-pattern', help='Filter by name pattern (supports wildcards)')
    parser.add_argument('--include-deleted', action='store_true',
                       help='Include deleted and historical versions')
    parser.add_argument('--limit', type=int, help='Limit number of results')
    
    # Options for get and analyze
    parser.add_argument('--version', help='Specific version number')
    parser.add_argument('--detailed', action='store_true',
                       help='Show detailed information')
    
    # Options for clone and update
    parser.add_argument('--name', help='Component name')
    parser.add_argument('--description', help='Component description')
    
    # Options for query
    parser.add_argument('--property', choices=['name', 'type', 'id', 'folder'],
                       help='Property to filter on')
    parser.add_argument('--operator', choices=['EQUALS', 'LIKE', 'CONTAINS'],
                       help='Comparison operator')
    parser.add_argument('--value', help='Value to compare against')
    
    args = parser.parse_args()
    
    # Show examples and exit
    if args.help_examples:
        show_help_examples()
        return
    
    print("🚀 Boomi SDK - Component Management Tool")
    print("=" * 50)
    
    # Check for required environment variables
    required_vars = ["BOOMI_ACCOUNT", "BOOMI_USER", "BOOMI_SECRET"]
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars:
        print("❌ Missing required environment variables:")
        for var in missing_vars:
            print(f"   - {var}")
        print("\nPlease set these variables in your environment")
        sys.exit(1)
    
    try:
        # Initialize Component Manager
        comp_manager = ComponentManager(
            account_id=os.getenv("BOOMI_ACCOUNT"),
            username=os.getenv("BOOMI_USER"),
            password=os.getenv("BOOMI_SECRET"),
            timeout=30000
        )
        
        print("✅ SDK initialized successfully!")
        print()
        
        # Execute requested action
        if args.list:
            print("📋 Listing Components")
            print("-" * 25)
            
            components = comp_manager.list_components(
                component_type=args.type,
                folder=args.folder,
                name_pattern=args.name_pattern,
                current_only=not args.include_deleted,
                limit=args.limit
            )
            
            display_components_list(components, "Components", args.detailed)
            
            if components:
                # Show summary
                total = len(components)
                by_type = {}
                for comp in components:
                    comp_type = getattr(comp, 'type_', 'Unknown')
                    by_type[comp_type] = by_type.get(comp_type, 0) + 1
                
                print("=" * 70)
                print(f"📊 Summary: {total} component(s)")
                for comp_type, count in by_type.items():
                    print(f"   {comp_type}: {count}")
        
        elif args.get:
            print(f"🔍 Component Details")
            print("-" * 25)
            
            component = comp_manager.get_component(args.get, args.version)
            if component:
                # Display basic metadata
                print(f"✅ Component retrieved successfully!")
                
                # Extract and display component info
                if hasattr(component, '_kwargs') and component._kwargs:
                    comp_data = component._kwargs.get('Component', component)
                else:
                    comp_data = component
                
                # Create pseudo-component for display
                class ComponentDisplay:
                    pass
                
                display_comp = ComponentDisplay()
                for attr in ['name', 'component_id', 'type_', 'version', 'current_version', 
                           'deleted', 'created_by', 'created_date', 'modified_by', 
                           'modified_date', 'folder_full_path', 'branch_name']:
                    setattr(display_comp, attr, getattr(comp_data, attr, 'N/A'))
                
                display_component(display_comp, detailed=True)
                
                # Show XML info if available
                if hasattr(component, 'object'):
                    print("🔧 XML Configuration: Available")
                else:
                    print("🔧 XML Configuration: Not available")
        
        elif args.clone:
            if not args.name:
                print("❌ --name is required for clone operation")
                sys.exit(1)
            
            print(f"🔄 Cloning Component")
            print("-" * 25)
            
            cloned = comp_manager.clone_component(
                source_component_id=args.clone,
                new_name=args.name,
                description=args.description
            )
            
            if cloned:
                print(f"\n💡 Tip: Use --list --name-pattern \"*{args.name}*\" to find the new component")
        
        elif args.update:
            if not any([args.name, args.description]):
                print("❌ --name or --description is required for update operation")
                sys.exit(1)
            
            print(f"🔄 Updating Component")
            print("-" * 25)
            
            updated = comp_manager.update_component_metadata(
                component_id=args.update,
                new_name=args.name,
                new_description=args.description
            )
            
            if updated:
                print(f"\n💡 Tip: Use --get {args.update} to verify the changes")
        
        elif args.query:
            if not all([args.property, args.operator, args.value]):
                print("❌ --property, --operator, and --value are all required for query")
                sys.exit(1)
            
            print(f"🔍 Querying Components")
            print("-" * 25)
            
            components = comp_manager.query_components(
                property_name=args.property,
                operator=args.operator,
                value=args.value
            )
            
            display_components_list(components, "Matching Components")
        
        elif args.analyze:
            print(f"🔍 Analyzing Component")
            print("-" * 25)
            
            analysis = comp_manager.analyze_component_xml(args.analyze, args.version)
            display_analysis(analysis, args.analyze)
        
        elif args.stats:
            print(f"📊 Component Statistics")
            print("-" * 25)
            
            stats = comp_manager.get_component_stats()
            display_stats(stats)
    
    except KeyboardInterrupt:
        print("\n⏸️  Operation interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()