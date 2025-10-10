#!/usr/bin/env python3
"""
Query Environment Runtime Attachments

This example demonstrates how to query environment-runtime attachments.

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET

Usage:
    python query_environment_runtime_attachments_clean.py

Endpoint:
- environment_atom_attachment.query_environment_atom_attachment
"""

import os
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

# Load environment variables from .env file if available
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv is optional

from boomi import Boomi
from boomi.models import (
    EnvironmentAtomAttachmentQueryConfig,
    EnvironmentAtomAttachmentQueryConfigQueryFilter,
    EnvironmentAtomAttachmentSimpleExpression,
    EnvironmentAtomAttachmentSimpleExpressionOperator,
    EnvironmentAtomAttachmentSimpleExpressionProperty
)

def main():
    # Initialize SDK
    sdk = Boomi(
        account_id=os.getenv("BOOMI_ACCOUNT"),
        username=os.getenv("BOOMI_USER"),
        password=os.getenv("BOOMI_SECRET"),
        timeout=30000,
    )
    
    print("🔗 Querying environment-runtime attachments...")
    
    try:
        # Query all attachments - filter by environment ID contains any character
        simple_expression = EnvironmentAtomAttachmentSimpleExpression(
            operator=EnvironmentAtomAttachmentSimpleExpressionOperator.CONTAINS,
            property=EnvironmentAtomAttachmentSimpleExpressionProperty.ENVIRONMENTID,
            argument=[""]
        )
        
        query_filter = EnvironmentAtomAttachmentQueryConfigQueryFilter(expression=simple_expression)
        query_config = EnvironmentAtomAttachmentQueryConfig(query_filter=query_filter)
        query_response = sdk.environment_atom_attachment.query_environment_atom_attachment(query_config)
        
        # Process results
        attachments = []
        if hasattr(query_response, 'result') and query_response.result:
            attachments = query_response.result if isinstance(query_response.result, list) else [query_response.result]
        
        if attachments:
            print(f"✅ Found {len(attachments)} attachment(s):")
            for i, attachment in enumerate(attachments, 1):
                att_id = getattr(attachment, 'id_', 'N/A')
                att_atom_id = getattr(attachment, 'atom_id', 'N/A')
                att_env_id = getattr(attachment, 'environment_id', 'N/A')
                
                print(f"{i:2}. Attachment ID: {att_id}")
                print(f"    Runtime ID: {att_atom_id}")
                print(f"    Environment ID: {att_env_id}")
        else:
            print("❌ No attachments found")
            
    except Exception as e:
        print(f"❌ Error querying attachments: {str(e)}")

if __name__ == "__main__":
    main()