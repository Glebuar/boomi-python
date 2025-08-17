#!/usr/bin/env python3
"""
Boomi Component Update Examples
==============================
Update examples for all main Boomi component types.
"""

import os
from dotenv import load_dotenv
import sys
sys.path.insert(0, '../src')
from boomi import Boomi

load_dotenv()

def get_sdk():
    return Boomi(
        account_id=os.getenv("BOOMI_ACCOUNT"),
        username=os.getenv("BOOMI_USER"), 
        password=os.getenv("BOOMI_SECRET")
    )

def find_component_by_type(sdk, component_type):
    """Find first current version, non-deleted component of given type"""
    from boomi.models import (
        ComponentMetadataQueryConfig,
        ComponentMetadataQueryConfigQueryFilter,
        ComponentMetadataSimpleExpression,
        ComponentMetadataSimpleExpressionOperator,
        ComponentMetadataSimpleExpressionProperty
    )
    
    expression = ComponentMetadataSimpleExpression(
        operator=ComponentMetadataSimpleExpressionOperator.EQUALS,
        property=ComponentMetadataSimpleExpressionProperty.TYPE,
        argument=[component_type]
    )
    
    query_filter = ComponentMetadataQueryConfigQueryFilter(expression=expression)
    query_config = ComponentMetadataQueryConfig(query_filter=query_filter)
    
    components = sdk.component_metadata.query_component_metadata(request_body=query_config)
    if hasattr(components, 'result') and components.result:
        # Find first current version, non-deleted component
        for comp in components.result:
            if comp.deleted == 'false' and comp.current_version == 'true':
                return comp.component_id, comp.name, comp.folder_id
    return None, None, None

# 1. Process Component
def update_process():
    sdk = get_sdk()
    component_id, original_name, folder_id = find_component_by_type(sdk, "process")
    if not component_id:
        print("❌ No suitable process component found")
        return
    
    xml = f'''<Component xmlns="http://api.platform.boomi.com/"
           componentId="{component_id}"
           name="Updated {original_name}"
           type="process"
           folderId="{folder_id}">
      <description>Updated process with enhanced logging via Python SDK</description>
      <object>
        <process xmlns="" allowSimultaneous="false" enableUserLog="true">
          <shapes>
            <shape image="start" name="start" shapetype="start" userlabel="Updated Start" x="100" y="100">
              <configuration><noaction/></configuration>
              <dragpoints><dragpoint name="start.drag" toShape="stop" x="250" y="126"/></dragpoints>
            </shape>
            <shape image="stop_icon" name="stop" shapetype="stop" userlabel="Updated Stop" x="300" y="100">
              <configuration><stop continue="true"/></configuration>
              <dragpoints/>
            </shape>
          </shapes>
        </process>
      </object>
    </Component>'''
    
    result = sdk.component.update_component(component_id=component_id, request_body=xml)
    print(f"✅ Process updated: {getattr(result, 'name', 'Success')} (v{getattr(result, 'version', '?')})")
    print(f"📁 Folder preserved: {getattr(result, 'folder_name', 'Unknown')}")

# 2. Map Transform Component  
def update_map():
    xml = '''<Component xmlns="http://api.platform.boomi.com/" name="Updated Data Map" type="transform.map">
      <description>Updated data mapping transformation</description>
      <object>
        <map xmlns="">
          <mappings>
            <mapping sourceElement="input/name" targetElement="output/fullName"/>
            <mapping sourceElement="input/status" targetElement="output/currentStatus"/>
          </mappings>
        </map>
      </object>
    </Component>'''
    
    sdk = get_sdk()
    component_id = find_component_by_type(sdk, "transform.map")
    if component_id:
        result = sdk.component.update_component(component_id=component_id, request_body=xml)
        print(f"✅ Map updated: {getattr(result, 'name', 'Success')}")

# 3. Database Profile
def update_db_profile():
    xml = '''<Component xmlns="http://api.platform.boomi.com/" name="Updated DB Profile" type="profile.db">
      <description>Updated database connection profile</description>
      <object>
        <profile xmlns="" type="database">
          <connection>
            <driver>postgresql</driver>
            <url>jdbc:postgresql://updated-host:5432/mydb</url>
            <username>dbuser</username>
          </connection>
        </profile>
      </object>
    </Component>'''
    
    sdk = get_sdk()
    component_id = find_component_by_type(sdk, "profile.db")
    if component_id:
        result = sdk.component.update_component(component_id=component_id, request_body=xml)
        print(f"✅ DB Profile updated: {getattr(result, 'name', 'Success')}")

# 4. XML Profile
def update_xml_profile():
    xml = '''<Component xmlns="http://api.platform.boomi.com/" name="Updated XML Profile" type="profile.xml">
      <description>Updated XML document profile</description>
      <object>
        <profile xmlns="" type="xml">
          <schema>
            <element name="UpdatedRoot">
              <element name="name" type="string"/>
              <element name="updatedField" type="string"/>
            </element>
          </schema>
        </profile>
      </object>
    </Component>'''
    
    sdk = get_sdk()
    component_id = find_component_by_type(sdk, "profile.xml")
    if component_id:
        result = sdk.component.update_component(component_id=component_id, request_body=xml)
        print(f"✅ XML Profile updated: {getattr(result, 'name', 'Success')}")

# 5. JSON Profile
def update_json_profile():
    xml = '''<Component xmlns="http://api.platform.boomi.com/" name="Updated JSON Profile" type="profile.json">
      <description>Updated JSON document profile</description>
      <object>
        <profile xmlns="" type="json">
          <schema>
            {"type": "object", "properties": {"name": {"type": "string"}, "updatedStatus": {"type": "string"}}}
          </schema>
        </profile>
      </object>
    </Component>'''
    
    sdk = get_sdk()
    component_id = find_component_by_type(sdk, "profile.json")
    if component_id:
        result = sdk.component.update_component(component_id=component_id, request_body=xml)
        print(f"✅ JSON Profile updated: {getattr(result, 'name', 'Success')}")

# 6. Flat File Profile
def update_flatfile_profile():
    xml = '''<Component xmlns="http://api.platform.boomi.com/" name="Updated Flat File Profile" type="profile.flatfile">
      <description>Updated flat file document profile</description>
      <object>
        <profile xmlns="" type="flatfile">
          <delimiter>,</delimiter>
          <fields>
            <field name="name" length="50"/>
            <field name="updatedStatus" length="20"/>
          </fields>
        </profile>
      </object>
    </Component>'''
    
    sdk = get_sdk()
    component_id = find_component_by_type(sdk, "profile.flatfile")
    if component_id:
        result = sdk.component.update_component(component_id=component_id, request_body=xml)
        print(f"✅ Flat File Profile updated: {getattr(result, 'name', 'Success')}")

# 7. EDI Profile
def update_edi_profile():
    xml = '''<Component xmlns="http://api.platform.boomi.com/" name="Updated EDI Profile" type="profile.edi">
      <description>Updated EDI document profile</description>
      <object>
        <profile xmlns="" type="edi">
          <standard>X12</standard>
          <version>004010</version>
          <transactionSet>850</transactionSet>
        </profile>
      </object>
    </Component>'''
    
    sdk = get_sdk()
    component_id = find_component_by_type(sdk, "profile.edi")
    if component_id:
        result = sdk.component.update_component(component_id=component_id, request_body=xml)
        print(f"✅ EDI Profile updated: {getattr(result, 'name', 'Success')}")

# 8. Web Service Component
def update_webservice():
    xml = '''<Component xmlns="http://api.platform.boomi.com/" name="Updated Web Service" type="webservice">
      <description>Updated web service definition</description>
      <object>
        <webservice xmlns="">
          <endpoint>https://api.updated-service.com/v2</endpoint>
          <method>POST</method>
          <contentType>application/json</contentType>
        </webservice>
      </object>
    </Component>'''
    
    sdk = get_sdk()
    component_id = find_component_by_type(sdk, "webservice")
    if component_id:
        result = sdk.component.update_component(component_id=component_id, request_body=xml)
        print(f"✅ Web Service updated: {getattr(result, 'name', 'Success')}")

# 9. Connector Settings
def update_connector_settings():
    xml = '''<Component xmlns="http://api.platform.boomi.com/" name="Updated Connector Settings" type="connector-settings">
      <description>Updated connector configuration</description>
      <object>
        <connector xmlns="">
          <setting name="timeout">30000</setting>
          <setting name="retryCount">5</setting>
          <setting name="updatedProperty">newValue</setting>
        </connector>
      </object>
    </Component>'''
    
    sdk = get_sdk()
    component_id = find_component_by_type(sdk, "connector-settings")
    if component_id:
        result = sdk.component.update_component(component_id=component_id, request_body=xml)
        print(f"✅ Connector Settings updated: {getattr(result, 'name', 'Success')}")

# 10. Connector Action
def update_connector_action():
    xml = '''<Component xmlns="http://api.platform.boomi.com/" name="Updated Connector Action" type="connector-action">
      <description>Updated connector operation</description>
      <object>
        <action xmlns="">
          <operation>UPDATED_OPERATION</operation>
          <parameters>
            <parameter name="action">update</parameter>
            <parameter name="enhancedMode">true</parameter>
          </parameters>
        </action>
      </object>
    </Component>'''
    
    sdk = get_sdk()
    component_id = find_component_by_type(sdk, "connector-action")
    if component_id:
        result = sdk.component.update_component(component_id=component_id, request_body=xml)
        print(f"✅ Connector Action updated: {getattr(result, 'name', 'Success')}")

# 11. Cross Reference
def update_crossref():
    xml = '''<Component xmlns="http://api.platform.boomi.com/" name="Updated Cross Reference" type="crossref">
      <description>Updated cross reference table</description>
      <object>
        <crossreference xmlns="">
          <entries>
            <entry sourceValue="OLD_VALUE" targetValue="UPDATED_VALUE"/>
            <entry sourceValue="STATUS_ACTIVE" targetValue="ENHANCED_ACTIVE"/>
          </entries>
        </crossreference>
      </object>
    </Component>'''
    
    sdk = get_sdk()
    component_id = find_component_by_type(sdk, "crossref")
    if component_id:
        result = sdk.component.update_component(component_id=component_id, request_body=xml)
        print(f"✅ Cross Reference updated: {getattr(result, 'name', 'Success')}")

# 12. Document Cache
def update_document_cache():
    xml = '''<Component xmlns="http://api.platform.boomi.com/" name="Updated Document Cache" type="documentcache">
      <description>Updated document cache configuration</description>
      <object>
        <cache xmlns="">
          <maxSize>2048</maxSize>
          <ttl>7200</ttl>
          <cacheKey>updatedKey</cacheKey>
        </cache>
      </object>
    </Component>'''
    
    sdk = get_sdk()
    component_id = find_component_by_type(sdk, "documentcache")
    if component_id:
        result = sdk.component.update_component(component_id=component_id, request_body=xml)
        print(f"✅ Document Cache updated: {getattr(result, 'name', 'Success')}")

# 13. Function Transform
def update_function_transform():
    xml = '''<Component xmlns="http://api.platform.boomi.com/" name="Updated Function Transform" type="transform.function">
      <description>Updated function-based transformation</description>
      <object>
        <function xmlns="">
          <script>
            // Updated transformation function
            function transform(input) {
              return input.toUpperCase() + "_UPDATED";
            }
          </script>
        </function>
      </object>
    </Component>'''
    
    sdk = get_sdk()
    component_id = find_component_by_type(sdk, "transform.function")
    if component_id:
        result = sdk.component.update_component(component_id=component_id, request_body=xml)
        print(f"✅ Function Transform updated: {getattr(result, 'name', 'Success')}")

# 14. Process Property
def update_process_property():
    xml = '''<Component xmlns="http://api.platform.boomi.com/" name="Updated Process Property" type="processproperty">
      <description>Updated process property configuration</description>
      <object>
        <property xmlns="">
          <name>UPDATED_PROPERTY</name>
          <value>enhanced_value</value>
          <type>STRING</type>
        </property>
      </object>
    </Component>'''
    
    sdk = get_sdk()
    component_id = find_component_by_type(sdk, "processproperty")
    if component_id:
        result = sdk.component.update_component(component_id=component_id, request_body=xml)
        print(f"✅ Process Property updated: {getattr(result, 'name', 'Success')}")

# 15. Certificate
def update_certificate():
    xml = '''<Component xmlns="http://api.platform.boomi.com/" name="Updated Certificate" type="certificate">
      <description>Updated certificate configuration</description>
      <object>
        <certificate xmlns="">
          <alias>updated_cert_alias</alias>
          <description>Enhanced certificate for secure communication</description>
        </certificate>
      </object>
    </Component>'''
    
    sdk = get_sdk()
    component_id = find_component_by_type(sdk, "certificate")
    if component_id:
        result = sdk.component.update_component(component_id=component_id, request_body=xml)
        print(f"✅ Certificate updated: {getattr(result, 'name', 'Success')}")

# 16. Queue
def update_queue():
    xml = '''<Component xmlns="http://api.platform.boomi.com/" name="Updated Queue" type="queue">
      <description>Updated message queue configuration</description>
      <object>
        <queue xmlns="">
          <maxSize>2000</maxSize>
          <timeout>60000</timeout>
          <persistence>true</persistence>
        </queue>
      </object>
    </Component>'''
    
    sdk = get_sdk()
    component_id = find_component_by_type(sdk, "queue")
    if component_id:
        result = sdk.component.update_component(component_id=component_id, request_body=xml)
        print(f"✅ Queue updated: {getattr(result, 'name', 'Success')}")

# 17. Trading Partner
def update_trading_partner():
    xml = '''<Component xmlns="http://api.platform.boomi.com/" name="Updated Trading Partner" type="tradingpartner">
      <description>Updated trading partner configuration</description>
      <object>
        <tradingpartner xmlns="">
          <name>Enhanced Trading Partner</name>
          <identifier>TP_UPDATED_001</identifier>
          <protocol>AS2</protocol>
        </tradingpartner>
      </object>
    </Component>'''
    
    sdk = get_sdk()
    component_id = find_component_by_type(sdk, "tradingpartner")
    if component_id:
        result = sdk.component.update_component(component_id=component_id, request_body=xml)
        print(f"✅ Trading Partner updated: {getattr(result, 'name', 'Success')}")

# 18. Custom Library
def update_custom_library():
    xml = '''<Component xmlns="http://api.platform.boomi.com/" name="Updated Custom Library" type="customlibrary">
      <description>Updated custom library with enhanced functions</description>
      <object>
        <library xmlns="">
          <version>2.0</version>
          <functions>
            <function name="enhancedProcessor">
              // Updated custom processing logic
              return processData(input) + "_enhanced";
            </function>
          </functions>
        </library>
      </object>
    </Component>'''
    
    sdk = get_sdk()
    component_id = find_component_by_type(sdk, "customlibrary")
    if component_id:
        result = sdk.component.update_component(component_id=component_id, request_body=xml)
        print(f"✅ Custom Library updated: {getattr(result, 'name', 'Success')}")

# 19. XSLT Transform
def update_xslt():
    xml = '''<Component xmlns="http://api.platform.boomi.com/" name="Updated XSLT Transform" type="xslt">
      <description>Updated XSLT transformation</description>
      <object>
        <xslt xmlns="">
          <stylesheet>
            &lt;xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;
              &lt;xsl:template match="/"&gt;
                &lt;updatedOutput&gt;
                  &lt;xsl:value-of select="//name"/&gt; - Enhanced
                &lt;/updatedOutput&gt;
              &lt;/xsl:template&gt;
            &lt;/xsl:stylesheet&gt;
          </stylesheet>
        </xslt>
      </object>
    </Component>'''
    
    sdk = get_sdk()
    component_id = find_component_by_type(sdk, "xslt")
    if component_id:
        result = sdk.component.update_component(component_id=component_id, request_body=xml)
        print(f"✅ XSLT Transform updated: {getattr(result, 'name', 'Success')}")

# 20. Flow Service
def update_flow_service():
    xml = '''<Component xmlns="http://api.platform.boomi.com/" name="Updated Flow Service" type="flowservice">
      <description>Updated flow service with enhanced routing</description>
      <object>
        <flowservice xmlns="">
          <flow>
            <step name="enhanced_step">
              <operation>ENHANCED_ROUTING</operation>
            </step>
          </flow>
        </flowservice>
      </object>
    </Component>'''
    
    sdk = get_sdk()
    component_id = find_component_by_type(sdk, "flowservice")
    if component_id:
        result = sdk.component.update_component(component_id=component_id, request_body=xml)
        print(f"✅ Flow Service updated: {getattr(result, 'name', 'Success')}")

def main():
    """Run all component update examples"""
    print("🔄 Boomi Component Update Examples")
    print("=" * 50)
    
    updates = [
        update_process, update_map, update_db_profile, update_xml_profile,
        update_json_profile, update_flatfile_profile, update_edi_profile,
        update_webservice, update_connector_settings, update_connector_action,
        update_crossref, update_document_cache, update_function_transform,
        update_process_property, update_certificate, update_queue,
        update_trading_partner, update_custom_library, update_xslt, update_flow_service
    ]
    
    for update_func in updates:
        try:
            update_func()
        except Exception as e:
            print(f"❌ {update_func.__name__}: {e}")
    
    print("\n🎉 Component update examples completed!")

if __name__ == "__main__":
    main()