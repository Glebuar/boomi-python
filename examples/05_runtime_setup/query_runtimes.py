#!/usr/bin/env python3
"""
Query Runtimes

This example demonstrates how to query available runtimes (Atoms, Molecules, Clouds) using the Boomi SDK.

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET

Usage:
    python query_runtimes.py

Endpoint:
- atom.query_atom
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

    print("🔍 Querying available runtimes...")

    # Query all runtimes (no filter needed for all types)
    # Or you can query specific types: ATOM, MOLECULE, CLOUD, GATEWAY
    query_config = AtomQueryConfig()  # Empty query gets all runtimes
    query_response = sdk.atom.query_atom(query_config)

    # Process results
    runtimes = []
    if hasattr(query_response, 'result') and query_response.result:
        runtimes = query_response.result if isinstance(query_response.result, list) else [query_response.result]

    if runtimes:
        print(f"✅ Found {len(runtimes)} runtime(s):")

        # Group by type
        by_type = {}
        for runtime in runtimes:
            runtime_type = getattr(runtime, 'type_', 'UNKNOWN')
            if runtime_type not in by_type:
                by_type[runtime_type] = []
            by_type[runtime_type].append(runtime)

        # Display grouped by type
        for runtime_type, type_runtimes in sorted(by_type.items()):
            print(f"\n📦 {runtime_type} ({len(type_runtimes)})")
            print("-" * 40)
            for runtime in type_runtimes:
                runtime_id = getattr(runtime, 'id_', 'N/A')
                runtime_name = getattr(runtime, 'name', 'N/A')
                runtime_status = getattr(runtime, 'status', 'N/A')
                runtime_host = getattr(runtime, 'host_name', 'N/A')

                status_icon = "🟢" if runtime_status == "ONLINE" else "🔴"
                print(f"  {status_icon} {runtime_name}")
                print(f"     ID: {runtime_id}")
                print(f"     Host: {runtime_host}")
                print()
    else:
        print("❌ No runtimes found")

if __name__ == "__main__":
    main()