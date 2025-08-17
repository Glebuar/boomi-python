#!/usr/bin/env python3
"""
Query Atoms/Runtimes

This example demonstrates how to query available atoms/runtimes using the Boomi SDK.

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET

Usage:
    python query_atoms.py

Endpoint:
- atom.query_atom
"""

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

from boomi import Boomi
from boomi.models import (
    AtomQueryConfig,
    AtomQueryConfigQueryFilter,
    AtomSimpleExpression,
    AtomSimpleExpressionOperator,
    AtomSimpleExpressionProperty
)

def main():
    # Initialize SDK
    sdk = Boomi(
        account_id=os.getenv("BOOMI_ACCOUNT"),
        username=os.getenv("BOOMI_USER"),
        password=os.getenv("BOOMI_SECRET"),
        timeout=30000,
    )
    
    print("🔍 Querying available atoms/runtimes...")
    
    # Query atoms containing "ATOM" in type
    simple_expression = AtomSimpleExpression(
        operator=AtomSimpleExpressionOperator.CONTAINS,
        property=AtomSimpleExpressionProperty.TYPE,
        argument=["ATOM"]
    )
    
    query_filter = AtomQueryConfigQueryFilter(expression=simple_expression)
    query_config = AtomQueryConfig(query_filter=query_filter)
    query_response = sdk.atom.query_atom(query_config)
    
    # Process results
    atoms = []
    if hasattr(query_response, 'result') and query_response.result:
        atoms = query_response.result if isinstance(query_response.result, list) else [query_response.result]
    
    if atoms:
        print(f"✅ Found {len(atoms)} atom(s):")
        for i, atom in enumerate(atoms, 1):
            atom_id = atom.get('@id', 'N/A')
            atom_name = atom.get('@name', 'N/A')
            atom_type = atom.get('@type', 'N/A')
            atom_status = atom.get('@status', 'N/A')
            
            print(f"{i:2}. {atom_name}")
            print(f"    ID: {atom_id}")
            print(f"    Type: {atom_type}")
            print(f"    Status: {atom_status}")
    else:
        print("❌ No atoms found")

if __name__ == "__main__":
    main()