#!/usr/bin/env python3
"""
Download Process Log - Download and analyze process execution logs

This example demonstrates how to download process execution logs using the Boomi SDK.
Process logs contain detailed information about execution steps, errors, warnings,
and performance metrics that are essential for debugging and monitoring.

Features:
- Download logs by execution ID with configurable log levels
- Parse log content for errors, warnings, and key metrics
- Save logs to files with proper naming conventions
- Extract and analyze execution statistics from logs
- Support for different log levels (ALL, SEVERE, WARNING, INFO, etc.)
- Automatic retry logic for log availability
- Log content analysis and summary generation

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET

Usage:
    python download_process_log.py EXECUTION_ID [options]
    
Examples:
    # Download all logs for specific execution
    python download_process_log.py execution-abc123-def456-2025.08.17
    
    # Download only error/warning logs
    python download_process_log.py execution-abc123-def456-2025.08.17 --level SEVERE
    
    # Specify output directory
    python download_process_log.py execution-abc123-def456-2025.08.17 --output-dir ./logs/
    
    # Analyze logs and show summary
    python download_process_log.py execution-abc123-def456-2025.08.17 --analyze
    
    # Download with custom filename
    python download_process_log.py execution-abc123-def456-2025.08.17 --filename my_execution.log
    
    # Show examples and test
    python download_process_log.py --examples

Required SDK Components:
- ProcessLogService.create_process_log() - Initiate log download
- ExecutionRecordService.query_execution_record() - Get execution details
"""

import os
import sys
import argparse
import urllib.request
import urllib.error
import base64
import time
from datetime import datetime
from pathlib import Path
from typing import Optional, Tuple, Dict, Any
import re
from urllib.parse import urlparse
import zipfile
import io

# Import Boomi SDK
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))
from boomi import Boomi
from boomi.models import ProcessLog, LogLevel


class ProcessLogDownloader:
    """Download and analyze process execution logs using Boomi SDK"""
    
    def __init__(self):
        self.account_id = os.getenv('BOOMI_ACCOUNT')
        self.username = os.getenv('BOOMI_USER') 
        self.password = os.getenv('BOOMI_SECRET')
        
        if not all([self.account_id, self.username, self.password]):
            raise ValueError("Environment variables BOOMI_ACCOUNT, BOOMI_USER, and BOOMI_SECRET must be set")
        
        # Initialize Boomi SDK
        self.sdk = Boomi(
            account_id=self.account_id,
            username=self.username,
            password=self.password,
            timeout=60000
        )

    def get_execution_details(self, execution_id: str) -> Optional[Dict[str, Any]]:
        """Get execution details using SDK"""
        try:
            # Query for execution record
            from boomi.models import ExecutionRecordQueryConfig, ExecutionRecordQueryConfigQueryFilter, ExecutionRecordSimpleExpression, ExecutionRecordSimpleExpressionOperator, ExecutionRecordSimpleExpressionProperty
            
            query_expression = ExecutionRecordSimpleExpression(
                operator=ExecutionRecordSimpleExpressionOperator.EQUALS,
                property=ExecutionRecordSimpleExpressionProperty.EXECUTIONID,
                argument=[execution_id]
            )
            
            query_filter = ExecutionRecordQueryConfigQueryFilter(expression=query_expression)
            query_config = ExecutionRecordQueryConfig(query_filter=query_filter)
            
            result = self.sdk.execution_record.query_execution_record(request_body=query_config)
            
            if hasattr(result, 'result') and result.result:
                return result.result[0]
            return None
            
        except Exception as e:
            print(f"⚠️ Could not retrieve execution details: {str(e)}")
            return None

    def request_log_download(self, execution_id: str, log_level: LogLevel = LogLevel.ALL) -> Tuple[bool, Optional[str], Optional[str]]:
        """Request log download using SDK"""
        try:
            print(f"📋 Requesting log download for execution: {execution_id}")
            print(f"🔧 Log Level: {log_level.value}")
            
            # Create ProcessLog request
            process_log = ProcessLog(
                execution_id=execution_id,
                log_level=log_level
            )
            
            # Request log download via SDK
            log_download = self.sdk.process_log.create_process_log(request_body=process_log)
            
            if hasattr(log_download, 'status_code'):
                status_code = int(log_download.status_code)
                message = getattr(log_download, 'message', 'No message')
                download_url = getattr(log_download, 'url', None)
                
                if status_code == 202:
                    print(f"✅ Log download initiated: {message}")
                    return True, download_url, message
                elif status_code == 504:
                    print(f"❌ Runtime unavailable: {message}")
                    return False, None, message
                else:
                    print(f"⚠️ Unexpected status code {status_code}: {message}")
                    return False, None, message
            else:
                print(f"⚠️ Unexpected response format: {log_download}")
                return False, None, "Unexpected response format"
                
        except Exception as e:
            print(f"❌ Error requesting log download: {str(e)}")
            return False, None, str(e)

    def download_log_content(self, download_url: str, max_retries: int = 5, retry_delay: int = 5) -> Tuple[bool, Optional[str]]:
        """Download log content from the provided URL (handles ZIP archives)"""
        if not download_url:
            return False, "No download URL provided"

        print(f"📥 Downloading log content from: {download_url}")

        # Create basic auth header
        credentials = base64.b64encode(f"{self.username}:{self.password}".encode()).decode()

        for attempt in range(max_retries):
            if attempt > 0:
                print(f"   ⏳ Retry {attempt}/{max_retries-1} in {retry_delay} seconds...")
                time.sleep(retry_delay)

            try:
                # Create request with authentication
                request = urllib.request.Request(download_url)
                request.add_header('Authorization', f'Basic {credentials}')

                with urllib.request.urlopen(request, timeout=30) as response:
                    content = response.read()

                    # Check if content is empty (still being prepared)
                    if len(content) == 0:
                        print(f"   ⏳ Log still being prepared (0 bytes)... (attempt {attempt+1})")
                        continue

                    # Check if it's a ZIP file (ProcessLog returns ZIP archives)
                    if content[:2] == b'PK':
                        print(f"   📦 Detected ZIP archive ({len(content)} bytes)")
                        log_content = self._extract_log_from_zip(content)
                        if log_content is not None:  # Empty string is valid (no logs at this level)
                            print(f"✅ Log download successful ({len(log_content)} characters)")
                            return True, log_content
                        else:
                            print("   ⚠️ Could not extract log from ZIP")
                            if attempt < max_retries - 1:
                                continue
                            return False, "Could not extract log from ZIP archive"
                    else:
                        # Try to decode as UTF-8
                        try:
                            log_content = content.decode('utf-8')
                            print(f"✅ Log download successful ({len(log_content)} characters)")
                            return True, log_content
                        except UnicodeDecodeError:
                            # Try latin-1 as fallback
                            log_content = content.decode('latin-1', errors='ignore')
                            print(f"✅ Log download successful ({len(log_content)} characters, decoded with latin-1)")
                            return True, log_content
                    
            except urllib.error.HTTPError as e:
                if e.code == 202:
                    print(f"   ⏳ Log still being prepared... (attempt {attempt+1})")
                    continue
                else:
                    error_content = e.read().decode('utf-8', errors='ignore')[:200] if e.fp else ""
                    print(f"❌ Download failed with status {e.code}: {error_content}")
                    if attempt == max_retries - 1:
                        return False, f"HTTP {e.code}: {error_content}"
                    
            except Exception as e:
                print(f"❌ Request failed on attempt {attempt+1}: {str(e)}")
                if attempt == max_retries - 1:
                    return False, f"All attempts failed. Last error: {str(e)}"
        
        return False, "Max retries exceeded"

    def _extract_log_from_zip(self, zip_content: bytes) -> Optional[str]:
        """Extract log file from ZIP archive"""
        try:
            with zipfile.ZipFile(io.BytesIO(zip_content)) as zf:
                # Get list of files in ZIP
                file_list = zf.namelist()

                if not file_list:
                    print("   ⚠️ ZIP archive is empty")
                    return None

                # Look for .log file or use first file
                log_file = None
                for filename in file_list:
                    if filename.endswith('.log'):
                        log_file = filename
                        break

                if not log_file:
                    log_file = file_list[0]

                print(f"   📄 Extracting: {log_file}")

                # Extract and decode the log file
                with zf.open(log_file) as f:
                    log_bytes = f.read()

                    # Check if log is empty
                    if len(log_bytes) == 0:
                        print("   ℹ️ Log file is empty (no matching log entries for this level)")
                        return ""  # Return empty string instead of None

                    try:
                        return log_bytes.decode('utf-8')
                    except UnicodeDecodeError:
                        return log_bytes.decode('latin-1', errors='ignore')

        except zipfile.BadZipFile:
            print("   ❌ Invalid ZIP file")
            return None
        except Exception as e:
            print(f"   ❌ Error extracting ZIP: {e}")
            return None

    def save_log_to_file(self, log_content: str, execution_id: str, output_dir: str = "./logs/", filename: Optional[str] = None) -> str:
        """Save log content to file with proper naming"""
        # Create output directory if it doesn't exist
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        
        if filename:
            log_filename = filename
        else:
            # Generate filename with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            log_filename = f"{execution_id}_{timestamp}.log"
        
        filepath = Path(output_dir) / log_filename
        
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(log_content)
            
            print(f"💾 Log saved to: {filepath}")
            print(f"📏 File size: {len(log_content)} characters ({len(log_content.splitlines())} lines)")
            return str(filepath)
            
        except Exception as e:
            print(f"❌ Error saving log file: {str(e)}")
            raise

    def analyze_log_content(self, log_content: str) -> Dict[str, Any]:
        """Analyze log content and extract key metrics"""
        if not log_content:
            return {"error": "No log content to analyze"}
        
        lines = log_content.splitlines()
        
        analysis = {
            "total_lines": len(lines),
            "errors": [],
            "warnings": [],
            "info_messages": [],
            "timestamps": [],
            "execution_steps": [],
            "performance_metrics": {},
            "summary": {}
        }
        
        # Regular expressions for different log patterns
        timestamp_pattern = r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}'
        error_patterns = [
            r'ERROR',
            r'Exception',
            r'Failed',
            r'Error:',
            r'SEVERE'
        ]
        warning_patterns = [
            r'WARNING',
            r'WARN',
            r'deprecated'
        ]
        
        # Analyze each line
        for i, line in enumerate(lines):
            line_num = i + 1
            
            # Extract timestamps
            timestamp_match = re.search(timestamp_pattern, line)
            if timestamp_match:
                analysis["timestamps"].append(timestamp_match.group())
            
            # Check for errors
            for pattern in error_patterns:
                if re.search(pattern, line, re.IGNORECASE):
                    analysis["errors"].append({
                        "line": line_num,
                        "content": line.strip(),
                        "type": pattern
                    })
                    break
            
            # Check for warnings
            for pattern in warning_patterns:
                if re.search(pattern, line, re.IGNORECASE):
                    analysis["warnings"].append({
                        "line": line_num,
                        "content": line.strip(),
                        "type": pattern
                    })
                    break
            
            # Extract execution steps/processes
            if "Processing" in line or "Executing" in line or "Starting" in line:
                analysis["execution_steps"].append({
                    "line": line_num,
                    "content": line.strip()
                })
            
            # Extract performance metrics
            duration_match = re.search(r'(\d+)\s*(ms|milliseconds|seconds|sec)', line, re.IGNORECASE)
            if duration_match:
                value = int(duration_match.group(1))
                unit = duration_match.group(2).lower()
                if unit in ['ms', 'milliseconds']:
                    analysis["performance_metrics"].setdefault("durations_ms", []).append(value)
                elif unit in ['seconds', 'sec']:
                    analysis["performance_metrics"].setdefault("durations_ms", []).append(value * 1000)
        
        # Generate summary
        analysis["summary"] = {
            "has_errors": len(analysis["errors"]) > 0,
            "has_warnings": len(analysis["warnings"]) > 0,
            "error_count": len(analysis["errors"]),
            "warning_count": len(analysis["warnings"]),
            "execution_steps_count": len(analysis["execution_steps"]),
            "timespan": self._calculate_timespan(analysis["timestamps"]),
            "avg_duration_ms": self._calculate_average_duration(analysis["performance_metrics"].get("durations_ms", []))
        }
        
        return analysis

    def _calculate_timespan(self, timestamps: list) -> Optional[str]:
        """Calculate timespan from first to last timestamp"""
        if len(timestamps) < 2:
            return None
        
        try:
            # Parse timestamps and calculate difference
            first = datetime.fromisoformat(timestamps[0].replace('Z', '+00:00'))
            last = datetime.fromisoformat(timestamps[-1].replace('Z', '+00:00'))
            diff = last - first
            return str(diff)
        except:
            return None

    def _calculate_average_duration(self, durations: list) -> Optional[float]:
        """Calculate average duration from list of durations in ms"""
        if not durations:
            return None
        return sum(durations) / len(durations)

    def display_analysis(self, analysis: Dict[str, Any]) -> None:
        """Display log analysis in formatted output"""
        if "error" in analysis:
            print(f"❌ {analysis['error']}")
            return
        
        summary = analysis["summary"]
        
        print("📊 LOG ANALYSIS SUMMARY")
        print("=" * 50)
        print(f"📏 Total Lines: {analysis['total_lines']}")
        
        if summary["has_errors"]:
            print(f"❌ Errors Found: {summary['error_count']}")
        else:
            print("✅ No Errors Detected")
        
        if summary["has_warnings"]:
            print(f"⚠️ Warnings Found: {summary['warning_count']}")
        else:
            print("✅ No Warnings Detected")
        
        if summary["execution_steps_count"] > 0:
            print(f"🔄 Execution Steps: {summary['execution_steps_count']}")
        
        if summary["timespan"]:
            print(f"⏱️ Execution Timespan: {summary['timespan']}")
        
        if summary["avg_duration_ms"]:
            print(f"📊 Average Duration: {summary['avg_duration_ms']:.1f}ms")
        
        # Show first few errors and warnings
        if analysis["errors"]:
            print(f"\n❌ First {min(3, len(analysis['errors']))} Error(s):")
            for error in analysis["errors"][:3]:
                print(f"   Line {error['line']}: {error['content'][:100]}...")
        
        if analysis["warnings"]:
            print(f"\n⚠️ First {min(3, len(analysis['warnings']))} Warning(s):")
            for warning in analysis["warnings"][:3]:
                print(f"   Line {warning['line']}: {warning['content'][:100]}...")

    def run_examples(self) -> None:
        """Show example usage and test with available executions"""
        print("📥 ProcessLogDownloader - Examples and Testing")
        print("=" * 60)
        
        # Try to get recent executions to use as examples
        try:
            from boomi.models import ExecutionRecordQueryConfig, QuerySort
            from boomi.models.execution_record_query_config import SortField
            
            # Query recent executions
            sort_field = SortField(
                field_name="executionTime",
                sort_order="DESC"
            )
            query_sort = QuerySort(sort_field=[sort_field])
            
            # Create query config with only sort (no filter for getting all recent executions)
            # Create a dummy filter since query_filter appears to be required
            from boomi.models import ExecutionRecordQueryConfigQueryFilter, ExecutionRecordSimpleExpression, ExecutionRecordSimpleExpressionOperator, ExecutionRecordSimpleExpressionProperty
            
            # Create a simple filter that gets all records (executionId is not null)
            dummy_expression = ExecutionRecordSimpleExpression(
                operator=ExecutionRecordSimpleExpressionOperator.ISNOTNULL,
                property=ExecutionRecordSimpleExpressionProperty.EXECUTIONID,
                argument=[]
            )
            query_filter = ExecutionRecordQueryConfigQueryFilter(expression=dummy_expression)
            
            query_config = ExecutionRecordQueryConfig(
                query_filter=query_filter,
                query_sort=query_sort
            )
            
            result = self.sdk.execution_record.query_execution_record(request_body=query_config)
            
            if hasattr(result, 'result') and result.result:
                executions = result.result[:5]  # Get first 5 executions
                
                print("🔍 Recent Executions Available for Log Download:")
                print("-" * 50)
                
                for i, execution in enumerate(executions):
                    execution_id = getattr(execution, 'execution_id', 'Unknown')
                    process_name = getattr(execution, 'process_name', 'Unknown Process')
                    status = getattr(execution, 'status', 'Unknown')
                    execution_time = getattr(execution, 'execution_time', 'Unknown')
                    
                    print(f"  {i+1}. {execution_id}")
                    print(f"     Process: {process_name}")
                    print(f"     Status: {status}")  
                    print(f"     Time: {execution_time}")
                    print()
                
                # Test log download with the most recent execution
                if executions:
                    latest_execution_id = getattr(executions[0], 'execution_id', None)
                    if latest_execution_id:
                        print(f"🧪 Testing log download with: {latest_execution_id}")
                        print("-" * 50)
                        
                        success, download_url, message = self.request_log_download(
                            latest_execution_id, 
                            LogLevel.ALL
                        )
                        
                        if success and download_url:
                            print("✅ Log download request successful!")
                            print(f"📥 Download URL received: {download_url}")
                            print("💡 To complete the download, run:")
                            print(f"   python download_process_log.py {latest_execution_id}")
                        else:
                            print(f"❌ Log download request failed: {message}")
            else:
                print("❌ No recent executions found for testing")
                
        except Exception as e:
            print(f"❌ Error during examples: {str(e)}")


def main():
    parser = argparse.ArgumentParser(
        description="Download and analyze process execution logs",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    # Download all logs
    python download_process_log.py execution-abc123-def456-2025.08.17
    
    # Download only severe/error logs  
    python download_process_log.py execution-abc123-def456-2025.08.17 --level SEVERE
    
    # Specify output directory
    python download_process_log.py execution-abc123-def456-2025.08.17 --output-dir ./logs/
    
    # Analyze logs and show summary
    python download_process_log.py execution-abc123-def456-2025.08.17 --analyze
    
    # Custom filename
    python download_process_log.py execution-abc123-def456-2025.08.17 --filename my_logs.log
    
    # Show examples and test
    python download_process_log.py --examples
        """
    )
    
    parser.add_argument('execution_id', nargs='?', help='Execution ID to download logs for')
    parser.add_argument('--level', choices=[level.value for level in LogLevel], 
                       default='ALL', help='Log level to download (default: ALL)')
    parser.add_argument('--output-dir', default='./logs/', help='Output directory for log files')
    parser.add_argument('--filename', help='Custom filename for the log file')
    parser.add_argument('--analyze', action='store_true', help='Analyze log content and show summary')
    parser.add_argument('--no-save', action='store_true', help='Don\'t save log to file (analyze only)')
    parser.add_argument('--examples', action='store_true', help='Show examples and test with recent executions')
    
    args = parser.parse_args()
    
    try:
        downloader = ProcessLogDownloader()
        
        if args.examples:
            downloader.run_examples()
            return
        
        if not args.execution_id:
            parser.print_help()
            print("\n❌ Error: execution_id is required (use --examples to see available executions)")
            sys.exit(1)
        
        # Convert log level string to enum
        log_level = LogLevel(args.level)
        
        # Get execution details first
        execution_details = downloader.get_execution_details(args.execution_id)
        if execution_details:
            process_name = getattr(execution_details, 'process_name', 'Unknown Process')
            status = getattr(execution_details, 'status', 'Unknown')
            print(f"📋 Process: {process_name}")
            print(f"📊 Status: {status}")
            print()
        
        # Request log download
        success, download_url, message = downloader.request_log_download(args.execution_id, log_level)
        
        if not success:
            print(f"❌ Failed to request log download: {message}")
            sys.exit(1)
        
        if not download_url:
            print(f"❌ No download URL received: {message}")
            sys.exit(1)
        
        # Download log content
        success, log_content = downloader.download_log_content(download_url)
        
        if not success:
            print(f"❌ Failed to download log content: {log_content}")
            sys.exit(1)
        
        # Save to file unless --no-save specified
        if not args.no_save:
            filepath = downloader.save_log_to_file(
                log_content, 
                args.execution_id, 
                args.output_dir, 
                args.filename
            )
        
        # Analyze log content if requested
        if args.analyze:
            print("\n" + "=" * 50)
            analysis = downloader.analyze_log_content(log_content)
            downloader.display_analysis(analysis)
        
        print("\n✅ Log download completed successfully!")
        
    except KeyboardInterrupt:
        print("\n⛔ Download interrupted by user")
        sys.exit(130)
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()