#!/usr/bin/env python3
"""
Get the original XML for a complex component to understand its structure
"""

import os
import requests
import base64

# Get credentials
account_id = "psrisksand-U7OGUC"
username = "BOOMI_TOKEN.hlib.bochkarov@intapp.com"
password = "08bc1505-c54d-407e-9c25-9a7472b1e898"

# Complex component
component_id = "f7f52a40-21fa-4850-a415-c88d69c8f5a2"

# Create auth header
auth_string = f"{username}:{password}"
auth_bytes = auth_string.encode('ascii')
auth_b64 = base64.b64encode(auth_bytes).decode('ascii')

headers = {
    "Authorization": f"Basic {auth_b64}",
    "Content-Type": "application/xml",
    "Accept": "application/xml"
}

# GET the component
get_url = f"https://api.boomi.com/api/rest/v1/{account_id}/Component/{component_id}"
print(f"📥 Getting complex component: {component_id}")
get_response = requests.get(get_url, headers=headers)

if get_response.status_code == 200:
    print("✅ GET successful")
    
    # Save the XML
    with open("complex_original.xml", "w") as f:
        f.write(get_response.text)
    print("📝 Saved to: complex_original.xml")
    
    # Show first 2000 chars to see the structure
    print("\nFirst 2000 characters of XML:")
    print("=" * 60)
    print(get_response.text[:2000])
else:
    print(f"❌ GET failed: {get_response.status_code}")