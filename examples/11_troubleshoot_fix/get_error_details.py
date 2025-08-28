#!/usr/bin/env python3
"""
Boomi SDK Example: Get Error Details
====================================

This example demonstrates how to retrieve and analyze detailed error information
from failed Boomi process executions.

Features:
- Get error details from failed execution records
- Download and parse process logs
- Extract error messages and stack traces
- Provide troubleshooting suggestions
- Analyze error patterns and frequencies
- Support for different error severity levels
- Format error information for easy analysis

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- RUNTIME MANAGEMENT privilege required for log access
- Valid execution ID or process ID

Usage:
    # Get error details for specific execution
    python get_error_details.py --execution-id "execution-id"
    
    # Get recent errors for a process
    python get_error_details.py --process-id "process-id" --limit 3
    
    # Get all recent errors
    python get_error_details.py --recent-errors --days 7
    
    # Download full logs for analysis
    python get_error_details.py --execution-id "execution-id" --download-logs

Examples:
    python get_error_details.py --execution-id "execution-3fff4492-3735-45a5-9d64-dd7af8160374-2025.08.20"
    python get_error_details.py --process-id "186bc687-95b9-43f2-b64a-c86355ac8cf2" --recent-errors
    python get_error_details.py --recent-errors --days 3 --limit 10
"""

import os
import sys
import argparse
import json
import re
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Any, Tuple

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.boomi import Boomi
from src.boomi.models import (
    ExecutionRecordQueryConfig,
    ExecutionRecordQueryConfigQueryFilter,
    ExecutionRecordSimpleExpression,
    ExecutionRecordSimpleExpressionOperator,
    ExecutionRecordSimpleExpressionProperty,
    ExecutionRecordGroupingExpression,
    ProcessLog,
    QuerySort,
    SortField
)


class ErrorAnalyzer:
    """Analyzes execution errors and provides troubleshooting insights"""
    
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
        print(f"\n🔍 Getting details for execution {execution_id[:40]}...")
        
        try:
            # Create query expression for the specific execution ID
            query_expression = ExecutionRecordSimpleExpression(
                operator=ExecutionRecordSimpleExpressionOperator.EQUALS,
                property=ExecutionRecordSimpleExpressionProperty.EXECUTIONID,
                argument=[execution_id]
            )
            
            # Create query filter
            query_filter = ExecutionRecordQueryConfigQueryFilter(expression=query_expression)
            query_config = ExecutionRecordQueryConfig(query_filter=query_filter)
            
            # Execute query using SDK
            result = self.sdk.execution_record.query_execution_record(request_body=query_config)
            
            if result and hasattr(result, 'result') and result.result:
                execution = result.result[0]
                execution_dict = self._execution_to_dict(execution)
                print(f"✅ Execution found: {execution_dict.get('process_name', 'Unknown Process')}")
                return execution_dict
            else:
                print("❌ Execution not found")
                return None
                
        except Exception as e:
            print(f"❌ Failed to get execution details: {e}")
            return None
    
    def get_error_executions(self, process_id: Optional[str] = None, 
                           days: int = 7, limit: int = 10) -> List[Dict[str, Any]]:
        """Get recent error executions with optional process filtering"""
        print(f"\n🔍 Querying error executions from last {days} days")
        if process_id:
            print(f"   📎 Process filter: {process_id}")
        
        try:
            # Build query expressions
            expressions = []
            
            # Add error status filter
            error_expression = ExecutionRecordSimpleExpression(
                operator=ExecutionRecordSimpleExpressionOperator.EQUALS,
                property=ExecutionRecordSimpleExpressionProperty.STATUS,
                argument=["ERROR"]
            )
            expressions.append(error_expression)
            
            # Add process ID filter if specified
            if process_id:
                process_expression = ExecutionRecordSimpleExpression(
                    operator=ExecutionRecordSimpleExpressionOperator.EQUALS,
                    property=ExecutionRecordSimpleExpressionProperty.PROCESSID,
                    argument=[process_id]
                )
                expressions.append(process_expression)
            
            # Add date filter for recent executions
            since_date = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%dT%H:%M:%SZ')
            date_expression = ExecutionRecordSimpleExpression(
                operator=ExecutionRecordSimpleExpressionOperator.GREATERTHANOREQUAL,
                property=ExecutionRecordSimpleExpressionProperty.EXECUTIONTIME,
                argument=[since_date]
            )
            expressions.append(date_expression)
            
            # Create query filter
            if len(expressions) == 1:
                query_filter = ExecutionRecordQueryConfigQueryFilter(expression=expressions[0])
            else:
                grouping_expression = ExecutionRecordGroupingExpression(
                    operator="and",
                    nested_expression=expressions
                )
                query_filter = ExecutionRecordQueryConfigQueryFilter(expression=grouping_expression)
            
            # Create query config
            query_config = ExecutionRecordQueryConfig(query_filter=query_filter)
            
            # Execute query
            result = self.sdk.execution_record.query_execution_record(request_body=query_config)
            
            if result and hasattr(result, 'result') and result.result:
                executions = []
                for execution in result.result[:limit]:
                    execution_dict = self._execution_to_dict(execution)
                    executions.append(execution_dict)
                
                total_count = getattr(result, 'number_of_results', len(executions))
                print(f"✅ Found {total_count} error execution(s)")
                
                return executions
            else:
                print("✅ No error executions found")
                return []
                
        except Exception as e:
            print(f"❌ Failed to query error executions: {e}")
            return []
    
    def analyze_execution_error(self, execution: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze execution error and extract key information"""
        print(f"\n🔬 Analyzing error for execution {execution.get('execution_id', 'Unknown')[:40]}...")
        
        analysis = {
            'execution_id': execution.get('execution_id'),
            'process_name': execution.get('process_name'),
            'error_type': 'Unknown',
            'error_message': 'No specific error message available',
            'error_category': 'General Error',
            'troubleshooting_tips': [],
            'severity': 'Medium',
            'execution_info': execution
        }
        
        try:
            # Analyze based on available execution record data
            status = execution.get('status', '').upper()
            
            # Extract error information from execution record
            if status == 'ERROR':
                analysis['error_type'] = 'Execution Error'
                analysis['error_category'] = 'Runtime Error'
                
                # Check document counts for analysis (convert to int)
                inbound_count = self._safe_int(execution.get('inbound_document_count', 0))
                outbound_count = self._safe_int(execution.get('outbound_document_count', 0))
                error_count = self._safe_int(execution.get('inbound_error_document_count', 0))
                
                if error_count > 0:
                    analysis['error_message'] = f"Process failed with {error_count} error document(s)"
                    analysis['error_category'] = 'Document Processing Error'
                    analysis['troubleshooting_tips'].extend([
                        "Check input document format and structure",
                        "Verify data mapping and transformation logic",
                        "Review connector configuration and endpoints"
                    ])
                elif inbound_count == 0:
                    analysis['error_message'] = "No input documents processed"
                    analysis['error_category'] = 'Input Error'
                    analysis['troubleshooting_tips'].extend([
                        "Check source connector configuration",
                        "Verify trigger conditions and scheduling",
                        "Ensure data source availability"
                    ])
                elif outbound_count == 0 and inbound_count > 0:
                    analysis['error_message'] = f"Processed {inbound_count} input(s) but no output generated"
                    analysis['error_category'] = 'Processing Error'
                    analysis['troubleshooting_tips'].extend([
                        "Check process logic and data transformation",
                        "Review decision shapes and routing conditions",
                        "Verify output connector configuration"
                    ])
                
                # Analyze execution duration
                duration = execution.get('execution_duration')
                if isinstance(duration, list) and len(duration) > 1:
                    duration_ms = duration[1]
                    if duration_ms > 300000:  # 5 minutes
                        analysis['troubleshooting_tips'].append("Long execution time - check for performance bottlenecks")
                    elif duration_ms < 1000:  # 1 second
                        analysis['troubleshooting_tips'].append("Very short execution - may indicate early failure")
                
                # Analyze process name for common patterns
                process_name = execution.get('process_name', '').lower()
                if 'connector' in process_name:
                    analysis['troubleshooting_tips'].extend([
                        "Check connector endpoint connectivity",
                        "Verify authentication credentials",
                        "Review firewall and network settings"
                    ])
                elif 'database' in process_name or 'sql' in process_name:
                    analysis['troubleshooting_tips'].extend([
                        "Check database connection and credentials",
                        "Verify SQL query syntax and permissions",
                        "Review database availability and performance"
                    ])
                elif 'api' in process_name or 'rest' in process_name:
                    analysis['troubleshooting_tips'].extend([
                        "Check API endpoint availability",
                        "Verify authentication and authorization",
                        "Review API rate limits and quotas"
                    ])
                
                # Set severity based on error patterns
                if error_count > 10 or (inbound_count == 0 and 'scheduled' in process_name):
                    analysis['severity'] = 'High'
                elif error_count == 0 and outbound_count > 0:
                    analysis['severity'] = 'Low'
                    
            print(f"✅ Error analysis complete: {analysis['error_category']}")
            return analysis
            
        except Exception as e:
            print(f"❌ Error analysis failed: {e}")
            analysis['error_message'] = f"Analysis failed: {str(e)}"
            return analysis
    
    def download_process_logs(self, execution_id: str, log_level: str = "SEVERE") -> Optional[str]:
        """Download process logs for detailed error analysis"""
        print(f"\n📥 Downloading process logs for execution {execution_id[:40]}...")
        print(f"   📊 Log level: {log_level}")
        
        try:
            # Create process log request
            process_log = ProcessLog(
                execution_id=execution_id,
                log_level=log_level
            )
            
            # Request log download
            result = self.sdk.process_log.create_process_log(request_body=process_log)
            
            if result and hasattr(result, 'url'):
                download_url = result.url
                print(f"✅ Log download URL obtained")
                
                # Download the actual log content using built-in urllib
                import urllib.request
                import base64
                
                # Create basic auth header
                username = os.getenv('BOOMI_USER')
                password = os.getenv('BOOMI_SECRET')
                credentials = base64.b64encode(f"{username}:{password}".encode()).decode()
                
                # Create request with authentication
                request = urllib.request.Request(download_url)
                request.add_header('Authorization', f'Basic {credentials}')
                
                try:
                    with urllib.request.urlopen(request) as response:
                        log_content = response.read().decode('utf-8')
                        print(f"✅ Downloaded {len(log_content)} characters of log data")
                        return log_content
                except urllib.error.HTTPError as e:
                    print(f"❌ Failed to download logs: HTTP {e.code}")
                    return None
                except Exception as e:
                    print(f"❌ Failed to download logs: {e}")
                    return None
            else:
                print("❌ Failed to get log download URL")
                return None
                
        except Exception as e:
            print(f"❌ Log download failed: {e}")
            return None
    
    def parse_log_content(self, log_content: str) -> Dict[str, Any]:
        """Parse log content to extract error details"""
        print(f"\n🔍 Parsing log content ({len(log_content)} characters)...")
        
        parsed = {
            'total_lines': 0,
            'error_lines': [],
            'stack_traces': [],
            'exceptions': [],
            'common_errors': {},
            'timestamps': [],
            'components': set()
        }
        
        try:
            lines = log_content.split('\n')
            parsed['total_lines'] = len(lines)
            
            current_stack_trace = []
            in_stack_trace = False
            
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                
                # Extract timestamp
                timestamp_match = re.search(r'\d{4}-\d{2}-\d{2}[T\s]\d{2}:\d{2}:\d{2}', line)
                if timestamp_match:
                    parsed['timestamps'].append(timestamp_match.group())
                
                # Extract component names
                component_match = re.search(r'\[([^]]+)\]', line)
                if component_match:
                    parsed['components'].add(component_match.group(1))
                
                # Detect error severity levels
                if any(level in line.upper() for level in ['SEVERE', 'ERROR', 'EXCEPTION', 'FAILED']):
                    parsed['error_lines'].append(line)
                    
                    # Extract exception types
                    exception_match = re.search(r'(\w+Exception|\w+Error):', line)
                    if exception_match:
                        exception_type = exception_match.group(1)
                        parsed['exceptions'].append(exception_type)
                        parsed['common_errors'][exception_type] = parsed['common_errors'].get(exception_type, 0) + 1
                    
                    # Start stack trace detection
                    if 'Exception' in line or 'Error' in line:
                        in_stack_trace = True
                        current_stack_trace = [line]
                    
                elif in_stack_trace:
                    # Continue collecting stack trace lines
                    if line.startswith('\tat ') or line.startswith('    at ') or 'Caused by:' in line:
                        current_stack_trace.append(line)
                    else:
                        # End of stack trace
                        if current_stack_trace:
                            parsed['stack_traces'].append('\n'.join(current_stack_trace))
                            current_stack_trace = []
                        in_stack_trace = False
            
            # Add final stack trace if we ended while collecting one
            if current_stack_trace:
                parsed['stack_traces'].append('\n'.join(current_stack_trace))
            
            print(f"✅ Log parsing complete:")
            print(f"   📝 Total lines: {parsed['total_lines']}")
            print(f"   ❌ Error lines: {len(parsed['error_lines'])}")
            print(f"   📚 Stack traces: {len(parsed['stack_traces'])}")
            print(f"   🚨 Exception types: {len(parsed['exceptions'])}")
            print(f"   🔧 Components: {len(parsed['components'])}")
            
            return parsed
            
        except Exception as e:
            print(f"❌ Log parsing failed: {e}")
            return parsed
    
    def _execution_to_dict(self, execution) -> Dict[str, Any]:
        """Convert execution record to standardized dict"""
        execution_dict = {
            'execution_id': getattr(execution, 'execution_id', 'N/A'),
            'status': getattr(execution, 'status', 'N/A'),
            'process_name': getattr(execution, 'process_name', 'Unknown'),
            'process_id': getattr(execution, 'process_id', 'N/A'),
            'atom_name': getattr(execution, 'atom_name', 'Unknown'),
            'atom_id': getattr(execution, 'atom_id', 'N/A'),
            'execution_time': getattr(execution, 'execution_time', 'N/A'),
            'execution_duration': getattr(execution, 'execution_duration', None),
            'inbound_document_count': getattr(execution, 'inbound_document_count', 0),
            'outbound_document_count': getattr(execution, 'outbound_document_count', 0),
            'inbound_error_document_count': getattr(execution, 'inbound_error_document_count', 0)
        }
        return execution_dict
    
    def display_error_summary(self, execution: Dict[str, Any], analysis: Dict[str, Any], 
                            log_analysis: Optional[Dict[str, Any]] = None) -> None:
        """Display comprehensive error summary"""
        print(f"\n📋 Error Analysis Summary:")
        print("=" * 70)
        
        # Execution details
        exec_id = execution.get('execution_id', 'N/A')
        process_name = execution.get('process_name', 'N/A')
        execution_time = execution.get('execution_time', 'N/A')
        atom_name = execution.get('atom_name', 'N/A')
        
        print(f"🆔 Execution ID: {exec_id}")
        print(f"🔧 Process: {process_name}")
        print(f"🤖 Atom: {atom_name}")
        print(f"📅 Execution Time: {self._format_datetime(execution_time)}")
        
        # Error analysis
        severity_icon = {'High': '🔴', 'Medium': '🟡', 'Low': '🟢'}.get(analysis['severity'], '⚪')
        print(f"\n{severity_icon} Error Details:")
        print(f"   📂 Category: {analysis['error_category']}")
        print(f"   🎯 Type: {analysis['error_type']}")
        print(f"   💬 Message: {analysis['error_message']}")
        print(f"   ⚠️ Severity: {analysis['severity']}")
        
        # Document counts (convert to int)
        inbound = self._safe_int(execution.get('inbound_document_count', 0))
        outbound = self._safe_int(execution.get('outbound_document_count', 0))
        errors = self._safe_int(execution.get('inbound_error_document_count', 0))
        
        print(f"\n📊 Document Processing:")
        print(f"   📥 Inbound: {inbound}")
        print(f"   📤 Outbound: {outbound}")
        if errors > 0:
            print(f"   ❌ Errors: {errors}")
        
        # Duration
        duration = execution.get('execution_duration')
        if isinstance(duration, list) and len(duration) > 1:
            duration_ms = duration[1]
            duration_display = f"{duration_ms}ms ({duration_ms/1000:.2f}s)"
            print(f"   ⏱️ Duration: {duration_display}")
        
        # Log analysis if available
        if log_analysis:
            print(f"\n📝 Log Analysis:")
            print(f"   📄 Total log lines: {log_analysis.get('total_lines', 0)}")
            print(f"   ❌ Error lines: {len(log_analysis.get('error_lines', []))}")
            print(f"   📚 Stack traces: {len(log_analysis.get('stack_traces', []))}")
            
            # Most common exceptions
            common_errors = log_analysis.get('common_errors', {})
            if common_errors:
                print(f"   🚨 Top exceptions:")
                for exception, count in sorted(common_errors.items(), key=lambda x: x[1], reverse=True)[:3]:
                    print(f"      • {exception}: {count} occurrences")
            
            # Components involved
            components = log_analysis.get('components', set())
            if components:
                print(f"   🔧 Components: {', '.join(sorted(components)[:5])}")
        
        # Troubleshooting tips
        if analysis['troubleshooting_tips']:
            print(f"\n💡 Troubleshooting Suggestions:")
            for i, tip in enumerate(analysis['troubleshooting_tips'][:5], 1):
                print(f"   {i}. {tip}")
        
        # Stack traces (first one only)
        if log_analysis and log_analysis.get('stack_traces'):
            print(f"\n📚 Stack Trace (first occurrence):")
            stack_trace = log_analysis['stack_traces'][0]
            # Show first 10 lines of stack trace
            lines = stack_trace.split('\n')[:10]
            for line in lines:
                print(f"   {line}")
            if len(log_analysis['stack_traces'][0].split('\n')) > 10:
                print("   ... (truncated)")
    
    def _format_datetime(self, datetime_string: str) -> str:
        """Format ISO datetime string to readable format"""
        try:
            if datetime_string and datetime_string != 'N/A':
                dt = datetime.fromisoformat(datetime_string.replace('Z', '+00:00'))
                return dt.strftime('%Y-%m-%d %H:%M:%S UTC')
        except:
            pass
        return datetime_string or 'N/A'
    
    def _safe_int(self, value) -> int:
        """Safely convert value to int"""
        try:
            if isinstance(value, (int, float)):
                return int(value)
            elif isinstance(value, str):
                return int(value) if value.isdigit() else 0
            else:
                return 0
        except (ValueError, TypeError):
            return 0


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='Analyze Boomi execution errors and get troubleshooting details',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  %(prog)s --execution-id "execution-abc123-2025.01.01"               # Analyze specific execution
  %(prog)s --process-id "process-id" --recent-errors --limit 5       # Recent errors for process
  %(prog)s --recent-errors --days 3                                  # All recent errors
  %(prog)s --execution-id "execution-id" --download-logs --log-level SEVERE  # With log analysis

Error Categories:
  • Runtime Error: Process execution failures
  • Document Processing Error: Data transformation issues
  • Input Error: Source connector/trigger problems
  • Processing Error: Internal logic failures
  
Troubleshooting Features:
  • Automatic error categorization
  • Pattern-based suggestions
  • Log parsing and stack trace analysis
  • Common exception identification
        '''
    )
    
    # Target selection (mutually exclusive)
    target_group = parser.add_mutually_exclusive_group(required=True)
    target_group.add_argument('--execution-id', metavar='ID',
                             help='Specific execution ID to analyze')
    target_group.add_argument('--process-id', metavar='ID',
                             help='Process ID to analyze recent errors for')
    target_group.add_argument('--recent-errors', action='store_true',
                             help='Get all recent error executions')
    
    # Filtering options
    parser.add_argument('--days', type=int, default=7, metavar='N',
                       help='Number of days to look back for errors (default: 7)')
    parser.add_argument('--limit', type=int, default=10, metavar='N',
                       help='Maximum number of executions to analyze (default: 10)')
    
    # Log analysis options
    parser.add_argument('--download-logs', action='store_true',
                       help='Download and analyze process logs')
    parser.add_argument('--log-level', choices=['SEVERE', 'WARNING', 'INFO', 'ALL'],
                       default='SEVERE', metavar='LEVEL',
                       help='Log level for download (default: SEVERE)')
    
    # Output options
    parser.add_argument('--summary', action='store_true',
                       help='Show detailed summary for each error')
    parser.add_argument('--save-report', metavar='FILE',
                       help='Save error analysis report to JSON file')
    
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
    
    # Execute operation
    try:
        analyzer = ErrorAnalyzer()
        
        print(f"\n🔍 Boomi Error Analysis Tool")
        print("=" * 40)
        
        executions_to_analyze = []
        
        if args.execution_id:
            # Single execution analysis
            execution = analyzer.get_execution_details(args.execution_id)
            if execution:
                executions_to_analyze.append(execution)
            else:
                print(f"❌ Execution {args.execution_id} not found or not accessible")
                sys.exit(1)
        
        elif args.process_id:
            # Process-specific error analysis
            executions_to_analyze = analyzer.get_error_executions(
                process_id=args.process_id,
                days=args.days,
                limit=args.limit
            )
        
        elif args.recent_errors:
            # Recent error analysis
            executions_to_analyze = analyzer.get_error_executions(
                days=args.days,
                limit=args.limit
            )
        
        if not executions_to_analyze:
            print("🎉 No error executions found!")
            sys.exit(0)
        
        print(f"\n📊 Analyzing {len(executions_to_analyze)} error execution(s)")
        
        all_analyses = []
        
        # Analyze each execution
        for i, execution in enumerate(executions_to_analyze, 1):
            print(f"\n{'='*70}")
            print(f"🔍 Analysis {i}/{len(executions_to_analyze)}")
            print(f"{'='*70}")
            
            # Perform error analysis
            analysis = analyzer.analyze_execution_error(execution)
            
            # Download and analyze logs if requested
            log_analysis = None
            if args.download_logs:
                execution_id = execution.get('execution_id')
                log_content = analyzer.download_process_logs(execution_id, args.log_level)
                if log_content:
                    log_analysis = analyzer.parse_log_content(log_content)
            
            # Display results
            if args.summary or len(executions_to_analyze) == 1:
                analyzer.display_error_summary(execution, analysis, log_analysis)
            else:
                # Brief summary
                exec_id = execution.get('execution_id', 'Unknown')
                process_name = execution.get('process_name', 'Unknown')
                error_category = analysis.get('error_category', 'Unknown')
                severity = analysis.get('severity', 'Unknown')
                
                severity_icon = {'High': '🔴', 'Medium': '🟡', 'Low': '🟢'}.get(severity, '⚪')
                print(f"{i}. {exec_id[:50]}")
                print(f"   🔧 Process: {process_name}")
                print(f"   {severity_icon} {error_category} - {severity} severity")
                print(f"   💬 {analysis.get('error_message', 'No message')}")
            
            # Collect for report
            analysis_record = {
                'execution': execution,
                'analysis': analysis,
                'log_analysis': log_analysis
            }
            all_analyses.append(analysis_record)
        
        # Save report if requested
        if args.save_report:
            report = {
                'generated_at': datetime.now().isoformat(),
                'total_executions': len(all_analyses),
                'analysis_criteria': {
                    'days_back': args.days,
                    'process_id': getattr(args, 'process_id', None),
                    'execution_id': getattr(args, 'execution_id', None),
                    'log_level': args.log_level if args.download_logs else None
                },
                'analyses': all_analyses
            }
            
            with open(args.save_report, 'w') as f:
                json.dump(report, f, indent=2, default=str)
            
            print(f"\n📄 Error analysis report saved to {args.save_report}")
        
        print(f"\n🎉 Error analysis completed!")
        print(f"📊 Analyzed {len(all_analyses)} execution(s)")
        
        # Summary statistics
        severity_counts = {}
        category_counts = {}
        for record in all_analyses:
            analysis = record['analysis']
            severity = analysis.get('severity', 'Unknown')
            category = analysis.get('error_category', 'Unknown')
            
            severity_counts[severity] = severity_counts.get(severity, 0) + 1
            category_counts[category] = category_counts.get(category, 0) + 1
        
        if len(all_analyses) > 1:
            print(f"\n📈 Summary Statistics:")
            print(f"   Severity breakdown: {dict(severity_counts)}")
            print(f"   Category breakdown: {dict(category_counts)}")
        
    except KeyboardInterrupt:
        print("\n❌ Analysis cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()