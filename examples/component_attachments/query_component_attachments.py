#!/usr/bin/env python3
"""
Boomi SDK Example: Query Component Attachments

This example demonstrates how to query component attachments using both
ComponentEnvironmentAttachment and ComponentAtomAttachment APIs. This helps you
understand which components are deployed where.

Features:
- Query component attachments by component ID, environment ID, or atom ID
- Shows all attachment details including IDs and types
- Supports filtering by attachment type (environment or atom)
- Provides comprehensive deployment overview

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- Or create a .env file with these variables

Usage:
    python query_component_attachments.py [--component COMPONENT_ID] [--environment ENV_ID] [--atom ATOM_ID] [--type TYPE]
    
    Options:
    --component COMPONENT_ID    Filter by component ID
    --environment ENV_ID        Filter by environment ID  
    --atom ATOM_ID             Filter by atom ID
    --type TYPE                Filter by attachment type (environment, atom, all)
    
    Examples:
    python query_component_attachments.py --component 112b4efe-b173-4258-9492-613ead7d52ce
    python query_component_attachments.py --environment afeeb4ea-3bb9-4640-b41e-f6aba08d3c41
    python query_component_attachments.py --atom 81e9dbc8-4684-4814-897c-0a1af0a6fe51
    python query_component_attachments.py --type environment
"""

import os
import sys
sys.path.insert(0, '../../src')
from boomi import Boomi
from boomi.models import (
    ComponentEnvironmentAttachmentQueryConfig,
    ComponentEnvironmentAttachmentQueryConfigQueryFilter,
    ComponentEnvironmentAttachmentSimpleExpression,
    ComponentEnvironmentAttachmentSimpleExpressionOperator,
    ComponentEnvironmentAttachmentSimpleExpressionProperty,
    ComponentAtomAttachmentQueryConfig,
    ComponentAtomAttachmentQueryConfigQueryFilter,
    ComponentAtomAttachmentSimpleExpression,
    ComponentAtomAttachmentSimpleExpressionOperator,
    ComponentAtomAttachmentSimpleExpressionProperty
)

# Load environment variables
try:
    from dotenv import load_dotenv
    load_dotenv('../../.env')
except ImportError:
    pass

def format_date(date_str):
    """Format ISO date string to readable format"""
    if date_str and 'T' in date_str:
        return date_str.split('T')[0] + ' ' + date_str.split('T')[1].split('.')[0]
    return date_str or 'N/A'

def print_environment_attachment(attachment, index):
    """Print environment attachment details"""
    print(f"   {index:2d}. Environment Attachment:")
    print(f"       Attachment ID: {getattr(attachment, 'id_', 'N/A')}")
    print(f"       Component ID: {getattr(attachment, 'component_id', 'N/A')}")
    print(f"       Environment ID: {getattr(attachment, 'environment_id', 'N/A')}")
    print(f"       Component Type: {getattr(attachment, 'component_type', 'N/A')}")
    print()

def print_atom_attachment(attachment, index):
    """Print atom attachment details"""
    print(f"   {index:2d}. Atom Attachment:")
    print(f"       Attachment ID: {getattr(attachment, 'id_', 'N/A')}")
    print(f"       Component ID: {getattr(attachment, 'component_id', 'N/A')}")
    print(f"       Atom ID: {getattr(attachment, 'atom_id', 'N/A')}")
    print(f"       Component Type: {getattr(attachment, 'component_type', 'N/A')}")
    print()

def query_environment_attachments(sdk, component_id=None, environment_id=None):
    """Query component environment attachments"""
    print("🌍 Querying environment attachments...")
    
    try:
        if component_id:
            expression = ComponentEnvironmentAttachmentSimpleExpression(
                operator=ComponentEnvironmentAttachmentSimpleExpressionOperator.EQUALS,
                property=ComponentEnvironmentAttachmentSimpleExpressionProperty.COMPONENTID,
                argument=[component_id]
            )
        elif environment_id:
            expression = ComponentEnvironmentAttachmentSimpleExpression(
                operator=ComponentEnvironmentAttachmentSimpleExpressionOperator.EQUALS,
                property=ComponentEnvironmentAttachmentSimpleExpressionProperty.ENVIRONMENTID,
                argument=[environment_id]
            )
        else:
            # Query all if no filter provided
            expression = ComponentEnvironmentAttachmentSimpleExpression(
                operator=ComponentEnvironmentAttachmentSimpleExpressionOperator.ISNOTNULL,
                property=ComponentEnvironmentAttachmentSimpleExpressionProperty.COMPONENTID,
                argument=[]
            )
        
        query_filter = ComponentEnvironmentAttachmentQueryConfigQueryFilter(expression=expression)
        query_config = ComponentEnvironmentAttachmentQueryConfig(query_filter=query_filter)
        
        result = sdk.component_environment_attachment.query_component_environment_attachment(
            request_body=query_config
        )
        
        # Handle response
        attachments = []
        if hasattr(result, '_kwargs') and result._kwargs:
            if 'ComponentEnvironmentAttachment' in result._kwargs:
                att_data = result._kwargs['ComponentEnvironmentAttachment']
                attachments = att_data if isinstance(att_data, list) else [att_data]
        elif hasattr(result, 'result'):
            attachments = result.result if isinstance(result.result, list) else [result.result]
        elif isinstance(result, list):
            attachments = result
        
        return attachments
        
    except Exception as e:
        print(f"❌ Environment attachment query failed: {e}")
        return []

def query_atom_attachments(sdk, component_id=None, atom_id=None):
    """Query component atom attachments"""
    print("⚛️ Querying atom attachments...")
    
    try:
        if component_id:
            expression = ComponentAtomAttachmentSimpleExpression(
                operator=ComponentAtomAttachmentSimpleExpressionOperator.EQUALS,
                property=ComponentAtomAttachmentSimpleExpressionProperty.COMPONENTID,
                argument=[component_id]
            )
        elif atom_id:
            expression = ComponentAtomAttachmentSimpleExpression(
                operator=ComponentAtomAttachmentSimpleExpressionOperator.EQUALS,
                property=ComponentAtomAttachmentSimpleExpressionProperty.ATOMID,
                argument=[atom_id]
            )
        else:
            # Query all if no filter provided
            expression = ComponentAtomAttachmentSimpleExpression(
                operator=ComponentAtomAttachmentSimpleExpressionOperator.ISNOTNULL,
                property=ComponentAtomAttachmentSimpleExpressionProperty.COMPONENTID,
                argument=[]
            )
        
        query_filter = ComponentAtomAttachmentQueryConfigQueryFilter(expression=expression)
        query_config = ComponentAtomAttachmentQueryConfig(query_filter=query_filter)
        
        result = sdk.component_atom_attachment.query_component_atom_attachment(
            request_body=query_config
        )
        
        # Handle response
        attachments = []
        if hasattr(result, '_kwargs') and result._kwargs:
            if 'ComponentAtomAttachment' in result._kwargs:
                att_data = result._kwargs['ComponentAtomAttachment']
                attachments = att_data if isinstance(att_data, list) else [att_data]
        elif hasattr(result, 'result'):
            attachments = result.result if isinstance(result.result, list) else [result.result]
        elif isinstance(result, list):
            attachments = result
        
        return attachments
        
    except Exception as e:
        print(f"❌ Atom attachment query failed: {e}")
        return []

def query_component_attachments(component_id=None, environment_id=None, atom_id=None, attachment_type="all"):
    """Query component attachments with various filters"""
    
    # Check for required environment variables
    account_id = os.getenv("BOOMI_ACCOUNT")
    username = os.getenv("BOOMI_USER") 
    password = os.getenv("BOOMI_SECRET")
    
    if not all([account_id, username, password]):
        print("❌ Error: Missing required environment variables")
        print("   Please set: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET")
        return False
    
    print(f"🏢 Account: {account_id}")
    print(f"👤 User: {username}")
    if component_id:
        print(f"🎯 Component ID: {component_id}")
    if environment_id:
        print(f"🌍 Environment ID: {environment_id}")
    if atom_id:
        print(f"⚛️ Atom ID: {atom_id}")
    print(f"🎭 Attachment Type: {attachment_type}")
    
    # Initialize the Boomi SDK
    sdk = Boomi(
        account_id=account_id,
        username=username, 
        password=password,
        timeout=30000
    )
    
    print(f"\n🔍 Querying component attachments...")
    
    environment_attachments = []
    atom_attachments = []
    
    # Query environment attachments
    if attachment_type in ["all", "environment"]:
        environment_attachments = query_environment_attachments(sdk, component_id, environment_id)
    
    # Query atom attachments  
    if attachment_type in ["all", "atom"]:
        atom_attachments = query_atom_attachments(sdk, component_id, atom_id)
    
    # Display results
    total_attachments = len(environment_attachments) + len(atom_attachments)
    
    if total_attachments > 0:
        print(f"✅ Found {total_attachments} attachment(s)")
        
        if environment_attachments:
            print(f"\n📋 Environment Attachments ({len(environment_attachments)}):")
            print("=" * 60)
            for i, attachment in enumerate(environment_attachments, 1):
                print_environment_attachment(attachment, i)
        
        if atom_attachments:
            print(f"\n📋 Atom Attachments ({len(atom_attachments)}):")
            print("=" * 60)
            for i, attachment in enumerate(atom_attachments, 1):
                print_atom_attachment(attachment, i)
        
        # Summary
        print(f"📊 Summary:")
        print("=" * 60)
        print(f"  • Total attachments: {total_attachments}")
        print(f"  • Environment attachments: {len(environment_attachments)}")
        print(f"  • Atom attachments: {len(atom_attachments)}")
        
        # Component type breakdown
        all_attachments = environment_attachments + atom_attachments
        component_types = {}
        for att in all_attachments:
            comp_type = getattr(att, 'component_type', 'Unknown')
            component_types[comp_type] = component_types.get(comp_type, 0) + 1
        
        if component_types:
            print(f"  • Component types:")
            for ctype, count in sorted(component_types.items()):
                print(f"     • {ctype}: {count}")
        
        print(f"\n💡 Deployment Overview:")
        print(f"  • Components are deployed across {len(set(getattr(att, 'environment_id', '') for att in environment_attachments if getattr(att, 'environment_id', '')))} environment(s)")
        print(f"  • Components are deployed across {len(set(getattr(att, 'atom_id', '') for att in atom_attachments if getattr(att, 'atom_id', '')))} atom(s)")
        
        return True
    else:
        print("📝 No attachments found")
        print("This could mean:")
        print("  • No components are attached with the given filters")
        print("  • The specified IDs don't exist")
        print("  • Insufficient permissions to view attachments")
        return True

def main():
    """Main entry point"""
    component_id = None
    environment_id = None
    atom_id = None
    attachment_type = "all"
    
    # Parse command line arguments
    i = 1
    while i < len(sys.argv):
        arg = sys.argv[i]
        
        if arg == "--component" and i + 1 < len(sys.argv):
            component_id = sys.argv[i + 1]
            i += 2
        elif arg == "--environment" and i + 1 < len(sys.argv):
            environment_id = sys.argv[i + 1]
            i += 2
        elif arg == "--atom" and i + 1 < len(sys.argv):
            atom_id = sys.argv[i + 1]
            i += 2
        elif arg == "--type" and i + 1 < len(sys.argv):
            attachment_type = sys.argv[i + 1]
            if attachment_type not in ["all", "environment", "atom"]:
                print("❌ Error: --type must be 'all', 'environment', or 'atom'")
                return
            i += 2
        else:
            print(f"❌ Error: Unknown argument '{arg}'")
            print("\nUsage:")
            print(f"  {sys.argv[0]} [--component COMPONENT_ID] [--environment ENV_ID] [--atom ATOM_ID] [--type TYPE]")
            print("\nOptions:")
            print("  --component COMPONENT_ID    Filter by component ID")
            print("  --environment ENV_ID        Filter by environment ID")
            print("  --atom ATOM_ID             Filter by atom ID")
            print("  --type TYPE                Filter by attachment type (environment, atom, all)")
            print("\nExamples:")
            print(f"  {sys.argv[0]} --component 112b4efe-b173-4258-9492-613ead7d52ce")
            print(f"  {sys.argv[0]} --type environment")
            return
            i += 1
    
    print("🚀 Boomi SDK Example: Query Component Attachments")
    print("=" * 55)
    print()
    
    success = query_component_attachments(component_id, environment_id, atom_id, attachment_type)
    
    print(f"\n{'='*55}")
    if success:
        print("🌟 Component attachment query completed successfully!")
    else:
        print("💥 Component attachment query encountered issues")

if __name__ == "__main__":
    main()