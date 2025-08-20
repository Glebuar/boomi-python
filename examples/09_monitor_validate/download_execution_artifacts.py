#!/usr/bin/env python3
"""
Boomi SDK Example: Download Execution Artifacts
===============================================

This example demonstrates how to download and extract execution artifacts from
completed Boomi process runs. Execution artifacts contain detailed logs, data,
and output documents from process executions.

Features:
- Download execution artifacts by execution ID
- Extract ZIP archives with proper file handling
- Validate artifact content and structure
- Support for different output formats (JSON, XML, CSV, logs)
- Organize artifacts by execution ID and timestamp
- Detailed content analysis and reporting
- Batch downloading of multiple executions

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- RUNTIME MANAGEMENT privilege required for artifact access
- Account must have "Enable Download of Execution Artifacts" enabled

Usage:
    # Download artifacts for single execution
    python download_execution_artifacts.py --execution-id "execution-id" --output-dir "./artifacts"
    
    # Download artifacts for recent executions of a process
    python download_execution_artifacts.py --process-id "process-id" --limit 5 --output-dir "./artifacts"
    
    # Extract and analyze artifact contents
    python download_execution_artifacts.py --execution-id "execution-id" --extract --analyze
    
    # Batch download with filtering
    python download_execution_artifacts.py --process-id "process-id" --status COMPLETE --since 2025-01-01

Examples:
    python download_execution_artifacts.py --execution-id "execution-abc123-2025.01.01" --output-dir "./test_artifacts"
    python download_execution_artifacts.py --process-id "186bc687-95b9-43f2-b64a-c86355ac8cf2" --limit 3 --extract
    python download_execution_artifacts.py --execution-id "execution-abc123-2025.01.01" --analyze --summary
"""

import os
import sys
import argparse
import json
import zipfile
import tempfile
import shutil
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Dict, Optional, Any, Tuple

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.boomi import Boomi


class ArtifactDownloader:
    """Manages execution artifact downloading and processing operations"""
    
    def __init__(self):
        """Initialize the Boomi SDK client"""
        self.sdk = Boomi(
            account_id=os.getenv("BOOMI_ACCOUNT"),
            username=os.getenv("BOOMI_USER"),
            password=os.getenv("BOOMI_SECRET"),
            timeout=30000
        )
        print("✅ SDK initialized successfully")
    
    def get_execution_details(self, execution_id: str) -> Optional[Dict[str, Any]]:
        """Get details about a specific execution"""
        try:
            import requests
            from requests.auth import HTTPBasicAuth
            
            url = f"https://api.boomi.com/api/rest/v1/{os.getenv('BOOMI_ACCOUNT')}/ExecutionRecord/query"
            auth = HTTPBasicAuth(os.getenv('BOOMI_USER'), os.getenv('BOOMI_SECRET'))
            headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
            
            query_payload = {
                "QueryFilter": {
                    "expression": {
                        "argument": [execution_id],
                        "operator": "EQUALS",
                        "property": "executionId"
                    }
                }
            }
            
            response = requests.post(url, json=query_payload, auth=auth, headers=headers)
            
            if response.status_code == 200:
                result = response.json()
                executions = result.get('result', [])
                return executions[0] if executions else None
            else:
                print(f"❌ Failed to get execution details: HTTP {response.status_code}")
                return None
                
        except Exception as e:
            print(f"❌ Failed to get execution details: {e}")
            return None
    
    def get_process_executions(self, process_id: str, limit: int = 10, 
                             status_filter: Optional[str] = None,
                             since_date: Optional[str] = None) -> List[Dict[str, Any]]:
        """Get recent executions for a specific process"""
        print(f"\n🔍 Querying executions for process {process_id}")
        
        try:
            import requests
            from requests.auth import HTTPBasicAuth
            
            url = f"https://api.boomi.com/api/rest/v1/{os.getenv('BOOMI_ACCOUNT')}/ExecutionRecord/query"
            auth = HTTPBasicAuth(os.getenv('BOOMI_USER'), os.getenv('BOOMI_SECRET'))
            headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
            
            # Build query expressions
            expressions = [
                {
                    "argument": [process_id],
                    "operator": "EQUALS",
                    "property": "processId"
                }
            ]
            
            # Add status filter if specified
            if status_filter:
                expressions.append({
                    "argument": [status_filter],
                    "operator": "EQUALS",
                    "property": "status"
                })
            
            # Add date filter if specified
            if since_date:
                expressions.append({
                    "argument": [since_date],
                    "operator": "GREATER_THAN_OR_EQUAL",
                    "property": "executionTime"
                })
            
            # Build query payload
            if len(expressions) == 1:
                query_filter = {"expression": expressions[0]}
            else:
                query_filter = {
                    "expression": {
                        "operator": "and",
                        "nestedExpression": expressions
                    }
                }
            
            query_payload = {
                "QueryFilter": query_filter,
                "QuerySort": {
                    "sortField": [
                        {
                            "fieldName": "executionTime",
                            "sortOrder": "DESC"
                        }
                    ]
                }
            }
            
            response = requests.post(url, json=query_payload, auth=auth, headers=headers)
            
            if response.status_code == 200:
                result = response.json()
                executions = result.get('result', [])
                total_count = result.get('numberOfResults', len(executions))
                
                print(f"✅ Found {total_count} execution(s) for this process")
                return executions[:limit]
            else:
                print(f"❌ Failed to query executions: HTTP {response.status_code}")
                return []
                
        except Exception as e:
            print(f"❌ Failed to query executions: {e}")
            return []
    
    def request_artifact_download(self, execution_id: str) -> Optional[str]:
        """Request download URL for execution artifacts"""
        print(f"🔄 Requesting artifacts for execution {execution_id[:30]}...")
        
        try:
            import requests
            from requests.auth import HTTPBasicAuth
            
            url = f"https://api.boomi.com/api/rest/v1/{os.getenv('BOOMI_ACCOUNT')}/ExecutionArtifacts"
            auth = HTTPBasicAuth(os.getenv('BOOMI_USER'), os.getenv('BOOMI_SECRET'))
            headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
            
            payload = {"executionId": execution_id}
            
            response = requests.post(url, json=payload, auth=auth, headers=headers)
            
            if response.status_code in [200, 202]:
                result = response.json()
                download_url = result.get('url')
                status_code = result.get('statusCode')
                message = result.get('message', '')
                
                print(f"✅ Artifact request successful (status: {status_code})")
                if message:
                    print(f"   Message: {message}")
                
                return download_url
            else:
                print(f"❌ Failed to request artifacts: HTTP {response.status_code}")
                if response.text:
                    print(f"   Error: {response.text}")
                return None
                
        except Exception as e:
            print(f"❌ Failed to request artifacts: {e}")
            return None
    
    def download_artifacts(self, download_url: str, output_path: str, max_retries: int = 3, retry_delay: int = 3) -> bool:
        """Download artifacts from the provided URL with retry logic"""
        print(f"⬇️ Downloading artifacts to {output_path}")
        
        try:
            import requests
            from requests.auth import HTTPBasicAuth
            import time
            
            auth = HTTPBasicAuth(os.getenv('BOOMI_USER'), os.getenv('BOOMI_SECRET'))
            
            # Create output directory if it doesn't exist
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            
            # Retry download with delays (artifacts may need time to be prepared)
            for attempt in range(max_retries):
                if attempt > 0:
                    print(f"   Retry {attempt}/{max_retries-1} in {retry_delay} seconds...")
                    time.sleep(retry_delay)
                
                response = requests.get(download_url, auth=auth, stream=True)
                
                if response.status_code == 200:
                    total_size = int(response.headers.get('content-length', 0))
                    
                    with open(output_path, 'wb') as f:
                        downloaded = 0
                        for chunk in response.iter_content(chunk_size=8192):
                            if chunk:
                                f.write(chunk)
                                downloaded += len(chunk)
                                if total_size > 0:
                                    percent = (downloaded / total_size) * 100
                                    print(f"   Progress: {percent:.1f}% ({downloaded}/{total_size} bytes)", end='\r')
                    
                    print(f"\n✅ Downloaded {downloaded} bytes successfully")
                    return True
                    
                elif response.status_code == 202:
                    print(f"   Artifacts still being prepared... (attempt {attempt+1})")
                    continue
                    
                elif response.status_code == 404:
                    print("❌ Download URL expired or not found")
                    return False
                    
                else:
                    print(f"❌ Download failed: HTTP {response.status_code}")
                    if attempt == max_retries - 1:  # Last attempt
                        return False
            
            print("❌ Download failed after all retries")
            return False
                
        except Exception as e:
            print(f"❌ Download failed: {e}")
            return False
    
    def extract_artifacts(self, zip_path: str, extract_dir: str) -> bool:
        """Extract artifacts ZIP file"""
        print(f"📦 Extracting artifacts to {extract_dir}")
        
        try:
            os.makedirs(extract_dir, exist_ok=True)
            
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                file_list = zip_ref.namelist()
                print(f"   Found {len(file_list)} files in archive")
                
                for file_name in file_list:
                    print(f"   Extracting: {file_name}")
                    zip_ref.extract(file_name, extract_dir)
                
                print(f"✅ Extracted {len(file_list)} files successfully")
                return True
                
        except zipfile.BadZipFile:
            print("❌ Invalid or corrupted ZIP file")
            return False
        except Exception as e:
            print(f"❌ Extraction failed: {e}")
            return False
    
    def analyze_artifacts(self, extract_dir: str) -> Dict[str, Any]:
        """Analyze extracted artifact contents"""
        print(f"\n🔍 Analyzing artifacts in {extract_dir}")
        
        analysis = {
            "total_files": 0,
            "file_types": {},
            "log_files": [],
            "data_files": [],
            "error_files": [],
            "total_size": 0,
            "summary": {}
        }
        
        try:
            extract_path = Path(extract_dir)
            
            if not extract_path.exists():
                print("❌ Extract directory does not exist")
                return analysis
            
            for file_path in extract_path.rglob('*'):
                if file_path.is_file():
                    analysis["total_files"] += 1
                    file_size = file_path.stat().st_size
                    analysis["total_size"] += file_size
                    
                    # Categorize by extension
                    extension = file_path.suffix.lower() or 'no_extension'
                    analysis["file_types"][extension] = analysis["file_types"].get(extension, 0) + 1
                    
                    # Categorize by content type
                    relative_path = str(file_path.relative_to(extract_path))
                    
                    if any(keyword in file_path.name.lower() for keyword in ['log', 'trace', 'debug']):
                        analysis["log_files"].append({
                            "name": relative_path,
                            "size": file_size,
                            "type": self._detect_content_type(file_path)
                        })
                    elif any(keyword in file_path.name.lower() for keyword in ['error', 'exception', 'fail']):
                        analysis["error_files"].append({
                            "name": relative_path,
                            "size": file_size,
                            "type": self._detect_content_type(file_path)
                        })
                    else:
                        analysis["data_files"].append({
                            "name": relative_path,
                            "size": file_size,
                            "type": self._detect_content_type(file_path)
                        })
            
            # Generate summary
            analysis["summary"] = {
                "total_files": analysis["total_files"],
                "total_size_mb": round(analysis["total_size"] / (1024 * 1024), 2),
                "most_common_type": max(analysis["file_types"].items(), key=lambda x: x[1])[0] if analysis["file_types"] else None,
                "has_logs": len(analysis["log_files"]) > 0,
                "has_errors": len(analysis["error_files"]) > 0,
                "has_data": len(analysis["data_files"]) > 0
            }
            
            print(f"✅ Analysis complete:")
            print(f"   📁 Total files: {analysis['total_files']}")
            print(f"   💾 Total size: {analysis['summary']['total_size_mb']} MB")
            print(f"   📝 Log files: {len(analysis['log_files'])}")
            print(f"   📄 Data files: {len(analysis['data_files'])}")
            print(f"   ❌ Error files: {len(analysis['error_files'])}")
            
            return analysis
            
        except Exception as e:
            print(f"❌ Analysis failed: {e}")
            return analysis
    
    def _detect_content_type(self, file_path: Path) -> str:
        """Detect content type of a file"""
        try:
            extension = file_path.suffix.lower()
            
            # Known extensions
            type_map = {
                '.xml': 'XML',
                '.json': 'JSON',
                '.csv': 'CSV',
                '.txt': 'Text',
                '.log': 'Log',
                '.html': 'HTML',
                '.zip': 'Archive'
            }
            
            if extension in type_map:
                return type_map[extension]
            
            # Try to detect by content for small files
            if file_path.stat().st_size < 10000:  # Only check files smaller than 10KB
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read(100).strip()
                        
                    if content.startswith('<?xml') or content.startswith('<'):
                        return 'XML'
                    elif content.startswith('{') or content.startswith('['):
                        return 'JSON'
                    elif ',' in content and '\n' in content:
                        return 'CSV'
                    else:
                        return 'Text'
                except:
                    pass
            
            return 'Binary'
            
        except Exception:
            return 'Unknown'
    
    def display_execution_summary(self, execution_data: Dict[str, Any], artifacts_info: Optional[Dict[str, Any]] = None) -> None:
        """Display summary of execution and artifacts"""
        print(f"\n📋 Execution Summary:")
        print("=" * 60)
        
        execution_id = execution_data.get('executionId', 'N/A')
        status = execution_data.get('status', 'N/A')
        process_name = execution_data.get('processName', 'N/A')
        atom_name = execution_data.get('atomName', 'N/A')
        execution_time = execution_data.get('executionTime', 'N/A')
        
        # Duration handling
        duration = execution_data.get('executionDuration', 'N/A')
        if isinstance(duration, list) and len(duration) > 1:
            duration_ms = duration[1]
            duration_display = f"{duration_ms}ms ({duration_ms/1000:.2f}s)"
        else:
            duration_display = str(duration)
        
        # Document counts
        inbound_docs = execution_data.get('inboundDocumentCount', 0)
        outbound_docs = execution_data.get('outboundDocumentCount', 0)
        error_docs = execution_data.get('inboundErrorDocumentCount', 0)
        
        # Status icon
        status_icon = {
            'COMPLETE': '✅',
            'ERROR': '❌', 
            'ABORTED': '⏹️',
            'INPROCESS': '⏳'
        }.get(status, '❓')
        
        print(f"{status_icon} Status: {status}")
        print(f"🆔 Execution ID: {execution_id}")
        print(f"🔧 Process: {process_name}")
        print(f"🤖 Atom: {atom_name}")
        print(f"📅 Execution Time: {self._format_datetime(execution_time)}")
        print(f"⏱️ Duration: {duration_display}")
        print(f"📊 Documents: {inbound_docs} in → {outbound_docs} out")
        if error_docs > 0:
            print(f"❌ Errors: {error_docs} documents")
        
        # Artifacts info
        if artifacts_info:
            print(f"\n📦 Artifacts Summary:")
            summary = artifacts_info.get('summary', {})
            print(f"   📁 Files: {summary.get('total_files', 0)}")
            print(f"   💾 Size: {summary.get('total_size_mb', 0)} MB")
            if summary.get('has_logs'):
                print(f"   📝 Contains logs: Yes")
            if summary.get('has_errors'):
                print(f"   ❌ Contains errors: Yes")
            if summary.get('most_common_type'):
                print(f"   📄 Primary type: {summary['most_common_type']}")
    
    def _format_datetime(self, datetime_string: str) -> str:
        """Format ISO datetime string to readable format"""
        try:
            if datetime_string and datetime_string != 'N/A':
                dt = datetime.fromisoformat(datetime_string.replace('Z', '+00:00'))
                return dt.strftime('%Y-%m-%d %H:%M:%S UTC')
        except:
            pass
        return datetime_string or 'N/A'
    
    def save_analysis_report(self, analysis: Dict[str, Any], output_file: str) -> bool:
        """Save analysis results to JSON file"""
        try:
            with open(output_file, 'w') as f:
                json.dump({
                    'analysis_date': datetime.now().isoformat(),
                    'analysis': analysis
                }, f, indent=2)
            
            print(f"📄 Analysis report saved to {output_file}")
            return True
        except Exception as e:
            print(f"❌ Failed to save analysis report: {e}")
            return False


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='Download and analyze Boomi execution artifacts',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  %(prog)s --execution-id "execution-abc123-2025.01.01"               # Download single execution
  %(prog)s --process-id "process-id" --limit 3 --extract              # Download recent executions
  %(prog)s --execution-id "execution-id" --analyze --summary          # Download and analyze
  %(prog)s --process-id "process-id" --status COMPLETE --since 2025-01-01  # Filtered download

Artifact Types:
  • Log files: Process execution logs and debug information
  • Data files: Input/output documents and transformed data
  • Error files: Exception details and error diagnostics
  
Output Organization:
  • artifacts/{execution_id}/
    ├── {execution_id}.zip     # Raw artifact archive
    ├── extracted/             # Extracted contents
    └── analysis.json          # Analysis report
        '''
    )
    
    # Target selection (mutually exclusive)
    target_group = parser.add_mutually_exclusive_group(required=True)
    target_group.add_argument('--execution-id', metavar='ID',
                             help='Specific execution ID to download artifacts for')
    target_group.add_argument('--process-id', metavar='ID',
                             help='Process ID to download recent execution artifacts for')
    
    # Process filtering (only with --process-id)
    parser.add_argument('--limit', type=int, default=5, metavar='N',
                       help='Maximum number of executions to process (default: 5)')
    parser.add_argument('--status', metavar='STATUS',
                       help='Filter by execution status (COMPLETE, ERROR, ABORTED, INPROCESS)')
    parser.add_argument('--since', metavar='DATE',
                       help='Filter executions since date (YYYY-MM-DD format)')
    
    # Output options
    parser.add_argument('--output-dir', default='./artifacts', metavar='DIR',
                       help='Output directory for artifacts (default: ./artifacts)')
    parser.add_argument('--extract', action='store_true',
                       help='Extract ZIP archives after download')
    parser.add_argument('--analyze', action='store_true',
                       help='Analyze extracted artifacts')
    parser.add_argument('--summary', action='store_true',
                       help='Display detailed summary')
    parser.add_argument('--keep-zip', action='store_true',
                       help='Keep ZIP files after extraction')
    
    args = parser.parse_args()
    
    # Validate environment variables
    required_env = ['BOOMI_ACCOUNT', 'BOOMI_USER', 'BOOMI_SECRET']
    missing = [var for var in required_env if not os.getenv(var)]
    
    if missing:
        print("❌ Missing environment variables:")
        for var in missing:
            print(f"  - {var}")
        print("\n💡 Set these in your .env file or export them")
        sys.exit(1)
    
    # Validate date format if provided
    if args.since:
        try:
            datetime.strptime(args.since, '%Y-%m-%d')
        except ValueError:
            print("❌ Invalid date format. Use YYYY-MM-DD (e.g., 2025-01-15)")
            sys.exit(1)
    
    # Execute operation
    try:
        downloader = ArtifactDownloader()
        
        print(f"\n📦 Boomi Execution Artifacts Downloader")
        print("=" * 50)
        
        # Get executions to process
        executions_to_process = []
        
        if args.execution_id:
            # Single execution mode
            execution_data = downloader.get_execution_details(args.execution_id)
            if execution_data:
                executions_to_process.append(execution_data)
            else:
                print(f"❌ Execution {args.execution_id} not found")
                sys.exit(1)
        
        elif args.process_id:
            # Multiple executions mode
            executions_to_process = downloader.get_process_executions(
                args.process_id,
                args.limit,
                args.status,
                args.since
            )
            
            if not executions_to_process:
                print(f"❌ No executions found for process {args.process_id}")
                sys.exit(1)
        
        print(f"\n🎯 Processing {len(executions_to_process)} execution(s)")
        
        # Process each execution
        for i, execution_data in enumerate(executions_to_process, 1):
            execution_id = execution_data.get('executionId')
            print(f"\n{'='*60}")
            print(f"📋 Processing execution {i}/{len(executions_to_process)}")
            print(f"🆔 Execution ID: {execution_id}")
            print(f"{'='*60}")
            
            # Create output directory for this execution
            exec_output_dir = os.path.join(args.output_dir, execution_id)
            os.makedirs(exec_output_dir, exist_ok=True)
            
            # Request artifact download
            download_url = downloader.request_artifact_download(execution_id)
            if not download_url:
                print(f"❌ Failed to get download URL for {execution_id}")
                continue
            
            # Download artifacts
            zip_path = os.path.join(exec_output_dir, f"{execution_id}.zip")
            if not downloader.download_artifacts(download_url, zip_path):
                print(f"❌ Failed to download artifacts for {execution_id}")
                continue
            
            artifacts_analysis = None
            
            # Extract if requested
            if args.extract:
                extract_dir = os.path.join(exec_output_dir, "extracted")
                if downloader.extract_artifacts(zip_path, extract_dir):
                    print(f"✅ Artifacts extracted to {extract_dir}")
                    
                    # Analyze if requested
                    if args.analyze:
                        artifacts_analysis = downloader.analyze_artifacts(extract_dir)
                        
                        # Save analysis report
                        analysis_file = os.path.join(exec_output_dir, "analysis.json")
                        downloader.save_analysis_report(artifacts_analysis, analysis_file)
                    
                    # Remove ZIP file if not keeping
                    if not args.keep_zip:
                        os.remove(zip_path)
                        print(f"🗑️ Removed ZIP file (use --keep-zip to retain)")
            
            # Display summary if requested
            if args.summary:
                downloader.display_execution_summary(execution_data, artifacts_analysis)
            
            print(f"✅ Completed processing {execution_id}")
        
        print(f"\n🎉 Successfully processed {len(executions_to_process)} execution(s)")
        print(f"📁 Artifacts saved to: {args.output_dir}")
        
    except KeyboardInterrupt:
        print("\n❌ Operation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()