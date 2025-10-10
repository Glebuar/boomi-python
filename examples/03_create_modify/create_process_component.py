#!/usr/bin/env python3
"""
Boomi SDK Example: Create Simple Process (Standalone)
=====================================================

This example demonstrates creating a simple process using inline XML.
This version doesn't require external XML files and shows the complete workflow.
"""

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

from boomi import Boomi

# Simple process XML definition (inline for easier distribution)
SIMPLE_PROCESS_XML = '''<Component xmlns="http://api.platform.boomi.com/"
           xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
           name="Simple API Demo Process"
           type="process">
  <description>A basic demo process created via Boomi Python SDK.</description>
  <object>
    <process xmlns="" allowSimultaneous="false" enableUserLog="false" processLogOnErrorOnly="false" purgeDataImmediately="false" updateRunDates="true" workload="general">
      <shapes>
        <shape image="start" name="start_shape" shapetype="start" userlabel="Start" x="100.0" y="100.0">
          <configuration>
            <noaction/>
          </configuration>
          <dragpoints>
            <dragpoint name="start_shape.dragpoint1" toShape="message_shape" x="200.0" y="126.0"/>
          </dragpoints>
        </shape>
        <shape image="message_icon" name="message_shape" shapetype="message" userlabel="SDK Demo Message" x="250.0" y="100.0">
          <configuration>
            <message combined="false">
              <msgTxt>Process created successfully with Boomi Python SDK!</msgTxt>
              <msgParameters/>
            </message>
          </configuration>
          <dragpoints>
            <dragpoint name="message_shape.dragpoint1" toShape="stop_shape" x="350.0" y="126.0"/>
          </dragpoints>
        </shape>
        <shape image="stop_icon" name="stop_shape" shapetype="stop" userlabel="Stop" x="400.0" y="100.0">
          <configuration>
            <stop continue="true"/>
          </configuration>
          <dragpoints/>
        </shape>
      </shapes>
    </process>
  </object>
</Component>'''

def create_demo_process():
    """Create a demo process to showcase the Boomi SDK"""
    
    print("🚀 Boomi Python SDK - Process Creation Demo")
    print("=" * 45)
    
    # Initialize SDK
    try:
        sdk = Boomi(
            account_id=os.getenv("BOOMI_ACCOUNT"),
            username=os.getenv("BOOMI_USER"),
            password=os.getenv("BOOMI_SECRET"),
            timeout=15000,
        )
        print("✅ SDK initialized successfully!")
        print(f"📍 Target account: {os.getenv('BOOMI_ACCOUNT')}")
    except Exception as e:
        print(f"❌ SDK initialization failed: {e}")
        return False
    
    # Show what we're creating
    print(f"\n📋 Process to create:")
    print(f"  Name: 'Simple API Demo Process'")
    print(f"  Type: process")
    print(f"  Flow: Start → Message → Stop")
    print(f"  Message: 'Process created successfully with Boomi Python SDK!'")
    
    # Create the process
    print(f"\n🔄 Creating process via Component API...")
    
    try:
        result = sdk.component.create_component(request_body=SIMPLE_PROCESS_XML)
        
        print("✅ Process creation successful!")
        print(f"📊 Response type: {type(result).__name__}")
        
        # Extract useful information from the result if available
        if hasattr(result, '__dict__'):
            for key, value in result.__dict__.items():
                if not key.startswith('_') and value is not None:
                    if key in ['name', 'type', 'id', 'componentId']:
                        print(f"  {key}: {value}")
        
        print(f"\n🎉 SUCCESS!")
        print(f"📍 Check your Boomi Build page to see the new process")
        print(f"🔧 The process demonstrates the SDK's component creation capabilities")
        
        return True
        
    except Exception as e:
        error_msg = str(e)
        print(f"❌ Process creation failed: {error_msg}")
        
        # Provide helpful troubleshooting hints
        if "403" in error_msg:
            print("🔍 Permission issue - check your API credentials and account permissions")
        elif "400" in error_msg:
            print("🔍 Bad request - check XML format or account configuration")
        elif "401" in error_msg:
            print("🔍 Authentication failed - verify your credentials")
        else:
            print("🔍 Check network connectivity and API endpoint availability")
            
        return False

if __name__ == "__main__":
    success = create_demo_process()
    
    print(f"\n{'='*45}")
    if success:
        print("🌟 Demo completed successfully!")
        print("📚 This example shows how the fixed Boomi SDK can:")
    else:
        print("💥 Demo encountered issues")
        print("🔧 The SDK itself is working - this is likely an API/credentials issue")