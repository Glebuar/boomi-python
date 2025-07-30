#!/usr/bin/env python3
"""Get detailed error information for component updates"""

import os
from dotenv import load_dotenv
import sys
sys.path.insert(0, '.')
from boomi import Boomi

load_dotenv()

def test_minimal_update():
    sdk = Boomi(account_id=os.getenv("BOOMI_ACCOUNT"), username=os.getenv("BOOMI_USER"), password=os.getenv("BOOMI_SECRET"))
    
    # Try updating a connector-action with minimal XML
    component_id = "6b1261db-342a-4970-bd19-51d928411191"
    
    minimal_xml = f"""<Component xmlns="http://api.platform.boomi.com/"
           componentId="{component_id}"
           name="Minimal Test Update"
           type="connector-action"
           folderId="Rjo3NTAwNzQ4">
      <description>Minimal test update</description>
    </Component>"""
    
    try:
        result = sdk.component.update_component(component_id=component_id, request_body=minimal_xml)
        print("✅ Success!")
        return result
    except Exception as e:
        print(f"❌ Error: {e}")
        
        # Get detailed error information
        if hasattr(e, 'response'):
            response = e.response
            print(f"Response type: {type(response)}")
            print(f"Response attributes: {dir(response)}")
            
            # Try different ways to get the response body
            if hasattr(response, 'text'):
                print(f"Response text: {response.text}")
            elif hasattr(response, 'body'):
                print(f"Response body: {response.body}")
            elif hasattr(response, 'content'):
                print(f"Response content: {response.content}")
            else:
                print("Could not extract error details")
        
        return None

if __name__ == "__main__":
    test_minimal_update()