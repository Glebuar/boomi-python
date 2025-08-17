#!/usr/bin/env python3
"""
Boomi SDK Example: Comprehensive Process Execution Records Viewer

This example demonstrates how to query execution records (process execution logs)
from the Boomi Platform API using the Python SDK. It includes advanced filtering,
complex queries, and downloading detailed execution artifacts.

Available Filter Properties:
- executionId, originalExecutionId, account, executionTime
- status, executionType, processName, processId  
- runtimeName, runtimeId, inboundDocumentCount, outboundDocumentCount
- executionDuration, message, reportKey, launcherId, nodeId, recordedDate

Available Operators:
- EQUALS, NOT_EQUALS, LIKE, IS_NULL, IS_NOT_NULL
- BETWEEN, GREATER_THAN, GREATER_THAN_OR_EQUAL
- LESS_THAN, LESS_THAN_OR_EQUAL, CONTAINS, NOT_CONTAINS

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- Or create a .env file with these variables

Usage:
    python execution_records.py
"""

import os
import requests
import time
from datetime import datetime, timedelta
from boomi import Boomi
from boomi.models import ExecutionRecordQueryConfig, ExecutionArtifacts

# Load environment variables from .env file if dotenv is available
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv is optional

def download_execution_artifacts(sdk, execution_id, download_dir="./logs"):
    """Download detailed execution artifacts/logs for a specific execution"""
    
    print(f"  📥 Downloading artifacts for execution: {execution_id}")
    
    try:
        # Request the download URL
        artifacts_request = ExecutionArtifacts(execution_id=execution_id)
        result = sdk.execution_artifacts.create_execution_artifacts(artifacts_request)
        
        if hasattr(result, 'url') and result.url:
            print(f"    ✅ Download URL obtained")
            
            # Create download directory if it doesn't exist
            os.makedirs(download_dir, exist_ok=True)
            
            # Download using session with Basic Auth (same credentials as SDK)
            session = requests.Session()
            session.auth = (os.getenv("BOOMI_USER"), os.getenv("BOOMI_SECRET"))
            
            filename = f"{download_dir}/execution_{execution_id}.zip"
            
            # The download URL might return 202 (Accepted) initially while preparing the file
            # Try a few times with delays
            max_attempts = 3
            for attempt in range(max_attempts):
                response = session.get(result.url, timeout=30)
                
                if response.status_code == 200:
                    with open(filename, 'wb') as f:
                        f.write(response.content)
                    print(f"    ✅ Downloaded to: {filename}")
                    print(f"    📊 File size: {len(response.content)} bytes")
                    
                    # Show what's in the zip file
                    try:
                        import zipfile
                        with zipfile.ZipFile(filename, 'r') as zf:
                            files = zf.namelist()
                            print(f"    📁 Contents: {', '.join(files)}")
                    except:
                        pass
                        
                    return filename
                elif response.status_code == 202:
                    if attempt < max_attempts - 1:
                        print(f"    ⏳ File being prepared, waiting...")
                        time.sleep(3)  # Wait 3 seconds before retry
                else:
                    print(f"    ❌ Download failed with status: {response.status_code}")
                    break
                    
            if response.status_code == 202:
                print(f"    ❌ File still being prepared after {max_attempts} attempts")
        else:
            print("    ❌ No download URL in response")
            
    except Exception as e:
        print(f"    ❌ Error downloading artifacts: {e}")
    
    return None

def query_execution_records():
    """Comprehensive execution records query and review"""
    
    # Check for required environment variables
    account_id = os.getenv("BOOMI_ACCOUNT")
    username = os.getenv("BOOMI_USER") 
    password = os.getenv("BOOMI_SECRET")
    
    if not all([account_id, username, password]):
        print("❌ Error: Missing required environment variables")
        print("   Please set: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET")
        return
    
    print(f"🏢 Account: {account_id}")
    print(f"👤 User: {username}")
    
    # Initialize the Boomi SDK
    sdk = Boomi(
        account_id=account_id,
        username=username, 
        password=password,
        timeout=30000
    )
    
    print("\n🔍 Comprehensive Execution Records Analysis")
    print("=" * 60)
    
    # 1. Query by status
    print("\n1️⃣ Query by Status:")
    statuses_to_check = ['COMPLETE', 'ERROR', 'INPROCESS', 'ABORTED']
    all_records = []
    
    for status in statuses_to_check:
        try:
            query_config = ExecutionRecordQueryConfig(
                query_filter={
                    "expression": {
                        "argument": [status],
                        "operator": "EQUALS",
                        "property": "status"
                    }
                }
            )
            result = sdk.execution_record.query_execution_record(request_body=query_config)
            
            if hasattr(result, 'result') and result.result:
                print(f"  ✅ {status}: {len(result.result)} execution(s)")
                all_records.extend(result.result)
            else:
                print(f"  • {status}: 0 execution(s)")
                
        except Exception as e:
            print(f"  ❌ {status}: Error - {e}")
    
    # 2. Query by time range (last 24 hours)
    print("\n2️⃣ Query by Time Range (last 24 hours):")
    try:
        now = datetime.now().replace(tzinfo=None)
        yesterday = now - timedelta(days=1)
        
        query_config = ExecutionRecordQueryConfig(
            query_filter={
                "expression": {
                    "argument": [
                        yesterday.strftime("%Y-%m-%dT%H:%M:%SZ"),
                        now.strftime("%Y-%m-%dT%H:%M:%SZ")
                    ],
                    "operator": "BETWEEN",
                    "property": "executionTime"
                }
            }
        )
        result = sdk.execution_record.query_execution_record(request_body=query_config)
        if hasattr(result, 'result') and result.result:
            print(f"  ✅ Found {len(result.result)} executions in last 24 hours")
        else:
            print(f"  • No executions in last 24 hours")
    except Exception as e:
        print(f"  ❌ Error: {e}")
    
    # 3. Query long-running executions (>5 seconds)
    print("\n3️⃣ Query Long-Running Executions (>5 seconds):")
    try:
        query_config = ExecutionRecordQueryConfig(
            query_filter={
                "expression": {
                    "argument": ["5000"],
                    "operator": "GREATER_THAN",
                    "property": "executionDuration"
                }
            }
        )
        result = sdk.execution_record.query_execution_record(request_body=query_config)
        if hasattr(result, 'result') and result.result:
            print(f"  ✅ Found {len(result.result)} long-running executions")
            for record in result.result[:3]:  # Show first 3
                duration = getattr(record, 'execution_duration', 'N/A')
                print(f"    • {record.process_name}: {duration}ms")
        else:
            print(f"  • No long-running executions found")
    except Exception as e:
        print(f"  ❌ Error: {e}")
    
    # 4. Complex query (COMPLETE status AND >5 seconds)
    print("\n4️⃣ Complex Query (COMPLETE status AND >5 seconds):")
    try:
        query_config = ExecutionRecordQueryConfig(
            query_filter={
                "expression": {
                    "operator": "and",
                    "nestedExpression": [
                        {
                            "argument": ["COMPLETE"],
                            "operator": "EQUALS",
                            "property": "status"
                        },
                        {
                            "argument": ["5000"],
                            "operator": "GREATER_THAN",
                            "property": "executionDuration"
                        }
                    ]
                }
            }
        )
        result = sdk.execution_record.query_execution_record(request_body=query_config)
        if hasattr(result, 'result') and result.result:
            print(f"  ✅ Found {len(result.result)} completed executions >5 seconds")
            for record in result.result[:3]:
                duration = getattr(record, 'execution_duration', 'N/A')
                print(f"    • {record.process_name}: {duration}ms")
        else:
            print(f"  • No matching executions found")
    except Exception as e:
        print(f"  ❌ Error: {e}")
    
    # 5. Display detailed results
    if all_records:
        print(f"\n5️⃣ Detailed Execution Records ({len(all_records)} found):")
        print("=" * 80)
        
        for i, record in enumerate(all_records, 1):
            print(f"\n📋 Execution #{i}:")
            print(f"  🔍 ID: {record.execution_id}")
            print(f"  🔄 Process: {record.process_name}")
            print(f"  📊 Status: {record.status}")
            print(f"  ⏰ Time: {record.execution_time}")
            print(f"  ⚡ Type: {record.execution_type}")
            print(f"  🖥️  Runtime: {record.atom_name}")
            print(f"  📥 In Docs: {getattr(record, 'inbound_document_count', 'N/A')}")
            print(f"  📤 Out Docs: {getattr(record, 'outbound_document_count', 'N/A')}")
            print(f"  ⏱️  Duration: {getattr(record, 'execution_duration', 'N/A')} ms")
            
            if hasattr(record, 'message') and record.message:
                print(f"  💬 Message: {record.message}")
            
            if hasattr(record, 'inbound_error_document_count') and record.inbound_error_document_count and record.inbound_error_document_count != '0':
                print(f"  ❌ Error Docs: {record.inbound_error_document_count}")
        
        # 6. Show execution summary
        print(f"\n6️⃣ Execution Summary:")
        status_counts = {}
        error_records = []
        
        for record in all_records:
            status = record.status
            status_counts[status] = status_counts.get(status, 0) + 1
            if status == 'ERROR':
                error_records.append(record)
        
        for status, count in status_counts.items():
            print(f"  • {status}: {count} execution(s)")
        
        # 7. Download artifacts for errors or recent executions
        if error_records:
            print(f"\n7️⃣ Downloading Artifacts for Error Executions:")
            for record in error_records[:2]:  # Download first 2 errors
                download_execution_artifacts(sdk, record.execution_id)
        elif all_records:
            print(f"\n7️⃣ Downloading Artifacts for Recent Execution:")
            # Download for the most recent execution
            latest_record = max(all_records, key=lambda r: r.execution_time)
            download_execution_artifacts(sdk, latest_record.execution_id)
    
    else:
        print("\n❌ No execution records found")
        print("This could mean:")
        print("  • No processes have been executed recently")
        print("  • Execution records have been archived")
        print("  • Different query filters might be needed")
        
    print(f"\n📚 Available Query Options:")
    print("Filter Properties: executionId, status, processName, runtimeName, executionDuration, etc.")
    print("Operators: EQUALS, LIKE, GREATER_THAN, BETWEEN, IS_NOT_NULL, etc.")
    print("Complex queries: Use 'and'/'or' with nestedExpression arrays")

def main():
    """Main entry point"""
    print("🚀 Boomi SDK: Comprehensive Process Execution Log Reviewer")
    print("=" * 60)
    query_execution_records()

if __name__ == "__main__":
    main()