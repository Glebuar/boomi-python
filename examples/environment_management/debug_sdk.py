#!/usr/bin/env python3
"""Debug SDK connection issue"""

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

from boomi import Boomi
from boomi.models import Environment, EnvironmentClassification

# Test credentials
account_id = "psrisksand-U7OGUC"
username = "BOOMI_TOKEN.hlib.bochkarov@intapp.com"
password = "08bc1505-c54d-407e-9c25-9a7472b1e898"

print(f"Account ID: '{account_id}'")
print(f"Account ID repr: {repr(account_id)}")
print(f"Username: '{username}'")

# Initialize SDK
sdk = Boomi(
    account_id=account_id,
    username=username,
    password=password,
    timeout=30000,
)

print("\n✅ SDK initialized")

# Try to create environment
try:
    new_env = Environment(
        name="SDK_Debug_Test_Env",
        classification=EnvironmentClassification.TEST
    )
    
    result = sdk.environment.create_environment(new_env)
    print(f"\n✅ Environment created: {result.id_}")
    
    # Clean up
    sdk.environment.delete_environment(id_=result.id_)
    print("✅ Environment deleted")
    
except Exception as e:
    print(f"\n❌ Error: {repr(e)}")
    if hasattr(e, 'message'):
        print(f"Message: {repr(e.message)}")