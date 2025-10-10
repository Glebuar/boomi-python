#!/usr/bin/env python3
"""
Get Execution Summary - Retrieve execution performance metrics and generate reports

This example demonstrates how to retrieve execution summary and metrics using
the ExecutionRecord API endpoint to analyze performance and generate reports.

Features:
- Get execution performance metrics for specific executions or processes
- Show success/failure statistics with detailed breakdowns
- Calculate processing times and throughput metrics
- Generate comprehensive execution reports with visual formatting
- Support multiple output formats (table, JSON, CSV)
- Process-level and execution-level analysis

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET

Usage:
    python get_execution_summary.py [options]
    
Examples:
    # Get summary for specific execution
    python get_execution_summary.py --execution execution-abc123-def456-2025.08.17
    
    # Get summary for all executions of a process
    python get_execution_summary.py --process 186bc687-95b9-43f2-b64a-c86355ac8cf2
    
    # Get summary for recent executions (last N days)
    python get_execution_summary.py --days 7 --limit 50
    
    # JSON output for automation
    python get_execution_summary.py --process 186bc687-95b9-43f2-b64a-c86355ac8cf2 --json
    
    # CSV export
    python get_execution_summary.py --days 30 --csv summary.csv

Required Endpoints:
- ExecutionRecord/query - Get detailed execution records
"""

import os
import sys
import argparse
# Add parent directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

from boomi import Boomi
import json
import csv
from datetime import datetime, timedelta, timezone
from typing import Optional, Dict, Any, List
from collections import Counter, defaultdict
import statistics


class ExecutionSummaryAnalyzer:
    """Analyze execution records and generate performance summaries"""
    
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
            timeout=30000
        )

    def query_executions(
        self, 
        execution_id: Optional[str] = None,
        process_id: Optional[str] = None,
        days_back: Optional[int] = None,
        limit: Optional[int] = None
    ) -> List[Dict[str, Any]]:
        """Query execution records based on criteria using SDK"""
        try:
            # Import SDK models
            from boomi.models import (
                ExecutionRecordQueryConfig,
                ExecutionRecordQueryConfigQueryFilter,
                ExecutionRecordSimpleExpression,
                ExecutionRecordSimpleExpressionOperator,
                ExecutionRecordSimpleExpressionProperty,
                ExecutionRecordGroupingExpression
            )
            from boomi.models.execution_record_query_config import SortField, QuerySort
            
            expressions = []
            
            if execution_id:
                execution_expression = ExecutionRecordSimpleExpression(
                    operator=ExecutionRecordSimpleExpressionOperator.EQUALS,
                    property=ExecutionRecordSimpleExpressionProperty.EXECUTIONID,
                    argument=[execution_id]
                )
                expressions.append(execution_expression)
            
            if process_id:
                process_expression = ExecutionRecordSimpleExpression(
                    operator=ExecutionRecordSimpleExpressionOperator.EQUALS,
                    property=ExecutionRecordSimpleExpressionProperty.PROCESSID,
                    argument=[process_id]
                )
                expressions.append(process_expression)
            
            if days_back:
                end_date = datetime.now(timezone.utc)
                start_date = end_date - timedelta(days=days_back)
                date_expression = ExecutionRecordSimpleExpression(
                    operator=ExecutionRecordSimpleExpressionOperator.BETWEEN,
                    property=ExecutionRecordSimpleExpressionProperty.EXECUTIONTIME,
                    argument=[
                        start_date.strftime('%Y-%m-%dT%H:%M:%SZ'),
                        end_date.strftime('%Y-%m-%dT%H:%M:%SZ')
                    ]
                )
                expressions.append(date_expression)
            
            # Create query config
            query_config = None
            
            if expressions:
                # Create query filter
                if len(expressions) == 1:
                    query_filter = ExecutionRecordQueryConfigQueryFilter(
                        expression=expressions[0]
                    )
                else:
                    grouping_expression = ExecutionRecordGroupingExpression(
                        operator="and",
                        nested_expression=expressions
                    )
                    query_filter = ExecutionRecordQueryConfigQueryFilter(
                        expression=grouping_expression
                    )
                
                # Create sort configuration
                sort_field = SortField(
                    field_name="executionTime",
                    sort_order="DESC"
                )
                query_sort = QuerySort(sort_field=[sort_field])
                
                query_config = ExecutionRecordQueryConfig(
                    query_filter=query_filter,
                    query_sort=query_sort
                )
            else:
                # No filters, just sorting
                sort_field = SortField(
                    field_name="executionTime",
                    sort_order="DESC"
                )
                query_sort = QuerySort(sort_field=[sort_field])
                query_config = ExecutionRecordQueryConfig(
                    query_sort=query_sort
                )
            
            # Execute query using SDK
            result = self.sdk.execution_record.query_execution_record(
                request_body=query_config
            )
            
            if result and hasattr(result, 'result') and result.result:
                # Convert SDK models to dicts for backward compatibility
                executions = []
                for execution in result.result:
                    execution_dict = {
                        'executionId': execution.execution_id,
                        'status': execution.status,
                        'processName': getattr(execution, 'process_name', 'Unknown'),
                        'processId': getattr(execution, 'process_id', 'Unknown'),
                        'atomName': getattr(execution, 'atom_name', 'Unknown'),
                        'executionTime': getattr(execution, 'execution_time', 'Unknown'),
                        'executionDuration': getattr(execution, 'execution_duration', None),
                        'inboundDocumentCount': getattr(execution, 'inbound_document_count', 0),
                        'outboundDocumentCount': getattr(execution, 'outbound_document_count', 0),
                        'inboundErrorDocumentCount': getattr(execution, 'inbound_error_document_count', 0),
                        'error': getattr(execution, 'error', None)
                    }
                    executions.append(execution_dict)
                
                # Apply limit if specified
                if limit and len(executions) > limit:
                    executions = executions[:limit]
                
                return executions
            else:
                print("No execution records found matching criteria")
                return []
                
        except Exception as e:
            print(f"❌ Failed to query executions: {e}")
            return []

    def extract_duration_ms(self, duration: Any) -> int:
        """Extract duration in milliseconds from various formats"""
        if isinstance(duration, str):
            try:
                return int(duration)
            except (ValueError, TypeError):
                return 0
        elif isinstance(duration, list):
            # Handle ['Long', milliseconds] format
            if len(duration) >= 2:
                try:
                    return int(duration[1])
                except (ValueError, TypeError):
                    return 0
            return 0
        elif isinstance(duration, (int, float)):
            return int(duration)
        else:
            return 0

    def extract_size_bytes(self, size: Any) -> int:
        """Extract size in bytes from various formats"""
        if isinstance(size, str):
            try:
                return int(size)
            except (ValueError, TypeError):
                return 0
        elif isinstance(size, list):
            # Handle ['Long', bytes] format
            if len(size) >= 2:
                try:
                    return int(size[1])
                except (ValueError, TypeError):
                    return 0
            return 0
        elif isinstance(size, (int, float)):
            return int(size)
        else:
            return 0

    def format_duration(self, duration_ms: int) -> str:
        """Format duration for display"""
        if duration_ms < 1000:
            return f"{duration_ms}ms"
        elif duration_ms < 60000:
            return f"{duration_ms/1000:.1f}s"
        else:
            minutes = duration_ms // 60000
            seconds = (duration_ms % 60000) / 1000
            return f"{minutes}m {seconds:.1f}s"

    def format_size(self, size_bytes: int) -> str:
        """Format size for display"""
        if size_bytes == 0:
            return "0 B"
        elif size_bytes < 1024:
            return f"{size_bytes} B"
        elif size_bytes < 1024 * 1024:
            return f"{size_bytes/1024:.1f} KB"
        elif size_bytes < 1024 * 1024 * 1024:
            return f"{size_bytes/(1024*1024):.1f} MB"
        else:
            return f"{size_bytes/(1024*1024*1024):.1f} GB"

    def analyze_executions(self, executions: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyze execution records and generate comprehensive summary"""
        if not executions:
            return {
                "total_executions": 0,
                "summary": "No executions found"
            }
        
        # Basic counts
        total_executions = len(executions)
        status_counts = Counter()
        process_counts = Counter()
        atom_counts = Counter()
        
        # Performance metrics
        durations = []
        inbound_doc_counts = []
        outbound_doc_counts = []
        inbound_sizes = []
        outbound_sizes = []
        
        # Time analysis
        execution_times = []
        earliest_time = None
        latest_time = None
        
        # Error analysis
        error_executions = []
        
        for execution in executions:
            # Basic counts
            status = execution.get('status', 'Unknown').upper()
            process_name = execution.get('processName', 'Unknown')
            atom_name = execution.get('atomName', 'Unknown')
            
            status_counts[status] += 1
            process_counts[process_name] += 1
            atom_counts[atom_name] += 1
            
            # Performance metrics
            duration = self.extract_duration_ms(execution.get('executionDuration', 0))
            durations.append(duration)

            # Handle document counts as strings or ints
            inbound_docs_raw = execution.get('inboundDocumentCount', 0)
            outbound_docs_raw = execution.get('outboundDocumentCount', 0)
            inbound_docs = int(inbound_docs_raw) if isinstance(inbound_docs_raw, str) else (inbound_docs_raw if isinstance(inbound_docs_raw, int) else 0)
            outbound_docs = int(outbound_docs_raw) if isinstance(outbound_docs_raw, str) else (outbound_docs_raw if isinstance(outbound_docs_raw, int) else 0)
            inbound_doc_counts.append(inbound_docs)
            outbound_doc_counts.append(outbound_docs)
            
            inbound_size = self.extract_size_bytes(execution.get('inboundDocumentSize', 0))
            outbound_size = self.extract_size_bytes(execution.get('outboundDocumentSize', 0))
            inbound_sizes.append(inbound_size)
            outbound_sizes.append(outbound_size)
            
            # Time analysis
            exec_time = execution.get('executionTime')
            if exec_time:
                execution_times.append(exec_time)
                if not earliest_time or exec_time < earliest_time:
                    earliest_time = exec_time
                if not latest_time or exec_time > latest_time:
                    latest_time = exec_time
            
            # Error analysis
            if status in ['ERROR', 'ABORTED', 'FAILED']:
                error_executions.append(execution)
        
        # Calculate statistics
        success_rate = (status_counts.get('COMPLETE', 0) / total_executions) * 100 if total_executions > 0 else 0
        
        duration_stats = {}
        if durations:
            duration_stats = {
                'min': min(durations),
                'max': max(durations),
                'mean': statistics.mean(durations),
                'median': statistics.median(durations)
            }
            if len(durations) > 1:
                duration_stats['std_dev'] = statistics.stdev(durations)
        
        # Document processing stats
        total_inbound_docs = sum(inbound_doc_counts)
        total_outbound_docs = sum(outbound_doc_counts)
        total_inbound_size = sum(inbound_sizes)
        total_outbound_size = sum(outbound_sizes)
        
        # Calculate throughput (docs per minute)
        time_span_minutes = 0
        if earliest_time and latest_time:
            try:
                earliest_dt = datetime.fromisoformat(earliest_time.replace('Z', '+00:00'))
                latest_dt = datetime.fromisoformat(latest_time.replace('Z', '+00:00'))
                time_span_minutes = (latest_dt - earliest_dt).total_seconds() / 60
            except:
                pass
        
        throughput_docs_per_min = 0
        if time_span_minutes > 0:
            throughput_docs_per_min = total_inbound_docs / time_span_minutes
        
        return {
            "total_executions": total_executions,
            "time_period": {
                "earliest": earliest_time,
                "latest": latest_time,
                "span_minutes": time_span_minutes
            },
            "status_breakdown": dict(status_counts),
            "success_rate": success_rate,
            "process_breakdown": dict(process_counts),
            "atom_breakdown": dict(atom_counts),
            "performance": {
                "duration_stats": duration_stats,
                "total_processing_time_ms": sum(durations),
                "avg_docs_per_execution": statistics.mean(inbound_doc_counts) if inbound_doc_counts else 0
            },
            "throughput": {
                "total_inbound_docs": total_inbound_docs,
                "total_outbound_docs": total_outbound_docs,
                "total_inbound_size_bytes": total_inbound_size,
                "total_outbound_size_bytes": total_outbound_size,
                "docs_per_minute": throughput_docs_per_min,
                "bytes_per_minute": (total_inbound_size / time_span_minutes) if time_span_minutes > 0 else 0
            },
            "errors": {
                "error_count": len(error_executions),
                "error_rate": (len(error_executions) / total_executions) * 100 if total_executions > 0 else 0,
                "error_details": error_executions[:5]  # First 5 errors for analysis
            }
        }

    def display_summary(self, summary: Dict[str, Any], detailed: bool = False) -> None:
        """Display summary in formatted table format"""
        if summary["total_executions"] == 0:
            print("❌ No executions found matching criteria")
            return
        
        print("📊 EXECUTION SUMMARY REPORT")
        print("=" * 60)
        
        # Overview
        total = summary["total_executions"]
        success_rate = summary["success_rate"]
        print(f"📈 Total Executions: {total}")
        print(f"✅ Success Rate: {success_rate:.1f}%")
        
        # Time period
        time_period = summary["time_period"]
        if time_period["earliest"] and time_period["latest"]:
            print(f"📅 Time Period: {time_period['earliest']} to {time_period['latest']}")
            if time_period["span_minutes"] > 0:
                span_hours = time_period["span_minutes"] / 60
                print(f"⏱️ Time Span: {span_hours:.1f} hours")
        
        print()
        
        # Status breakdown
        print("📊 STATUS BREAKDOWN:")
        for status, count in summary["status_breakdown"].items():
            percentage = (count / total) * 100
            indicator = "✅" if status == "COMPLETE" else "❌" if status in ["ERROR", "ABORTED", "FAILED"] else "🟡"
            print(f"  {indicator} {status}: {count} ({percentage:.1f}%)")
        print()
        
        # Performance metrics
        perf = summary["performance"]
        if perf["duration_stats"]:
            stats = perf["duration_stats"]
            print("⏱️ PERFORMANCE METRICS:")
            print(f"  Fastest: {self.format_duration(stats['min'])}")
            print(f"  Slowest: {self.format_duration(stats['max'])}")
            print(f"  Average: {self.format_duration(int(stats['mean']))}")
            print(f"  Median: {self.format_duration(int(stats['median']))}")
            if 'std_dev' in stats:
                print(f"  Std Dev: {self.format_duration(int(stats['std_dev']))}")
            
            total_processing = perf["total_processing_time_ms"]
            print(f"  Total Processing Time: {self.format_duration(total_processing)}")
            print()
        
        # Throughput
        throughput = summary["throughput"]
        print("🚀 THROUGHPUT METRICS:")
        print(f"  Total Documents In: {throughput['total_inbound_docs']:,}")
        print(f"  Total Documents Out: {throughput['total_outbound_docs']:,}")
        print(f"  Total Data In: {self.format_size(throughput['total_inbound_size_bytes'])}")
        print(f"  Total Data Out: {self.format_size(throughput['total_outbound_size_bytes'])}")
        
        if throughput['docs_per_minute'] > 0:
            print(f"  Documents/Minute: {throughput['docs_per_minute']:.1f}")
            print(f"  Data/Minute: {self.format_size(int(throughput['bytes_per_minute']))}")
        print()
        
        # Top processes and atoms
        if len(summary["process_breakdown"]) > 1:
            print("🔄 TOP PROCESSES:")
            for process, count in list(summary["process_breakdown"].items())[:5]:
                percentage = (count / total) * 100
                print(f"  {process}: {count} ({percentage:.1f}%)")
            print()
        
        if len(summary["atom_breakdown"]) > 1:
            print("🚀 ATOMS USED:")
            for atom, count in list(summary["atom_breakdown"].items())[:5]:
                percentage = (count / total) * 100
                print(f"  {atom}: {count} ({percentage:.1f}%)")
            print()
        
        # Error analysis
        errors = summary["errors"]
        if errors["error_count"] > 0:
            print("💥 ERROR ANALYSIS:")
            print(f"  Error Count: {errors['error_count']}")
            print(f"  Error Rate: {errors['error_rate']:.1f}%")
            
            if detailed and errors["error_details"]:
                print("  Recent Errors:")
                for i, error_exec in enumerate(errors["error_details"]):
                    print(f"    {i+1}. {error_exec.get('executionId', 'Unknown')}")
                    print(f"       Status: {error_exec.get('status', 'Unknown')}")
                    print(f"       Process: {error_exec.get('processName', 'Unknown')}")
                    if error_exec.get('error'):
                        print(f"       Error: {error_exec.get('error')}")
            print()

    def export_csv(self, executions: List[Dict[str, Any]], filename: str) -> None:
        """Export execution data to CSV"""
        if not executions:
            print("❌ No data to export")
            return
        
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = [
                'execution_id', 'process_name', 'atom_name', 'status', 
                'execution_time', 'duration_ms', 'inbound_docs', 'outbound_docs',
                'inbound_size_bytes', 'outbound_size_bytes'
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for execution in executions:
                writer.writerow({
                    'execution_id': execution.get('executionId', ''),
                    'process_name': execution.get('processName', ''),
                    'atom_name': execution.get('atomName', ''),
                    'status': execution.get('status', ''),
                    'execution_time': execution.get('executionTime', ''),
                    'duration_ms': self.extract_duration_ms(execution.get('executionDuration', 0)),
                    'inbound_docs': execution.get('inboundDocumentCount', 0),
                    'outbound_docs': execution.get('outboundDocumentCount', 0),
                    'inbound_size_bytes': self.extract_size_bytes(execution.get('inboundDocumentSize', 0)),
                    'outbound_size_bytes': self.extract_size_bytes(execution.get('outboundDocumentSize', 0))
                })
        
        print(f"✅ Exported {len(executions)} execution records to {filename}")

    def run_examples(self) -> None:
        """Show example usage and test with recent executions"""
        print("📊 ExecutionSummaryAnalyzer - Examples and Testing")
        print("=" * 60)
        
        # Example 1: Recent executions summary
        print("🔍 Example 1: Recent Executions (Last 7 days)")
        print("-" * 40)
        
        recent_executions = self.query_executions(days_back=7, limit=50)
        if recent_executions:
            summary = self.analyze_executions(recent_executions)
            self.display_summary(summary, detailed=True)
        else:
            print("No recent executions found")
        
        print("\n" + "=" * 60)
        
        # Example 2: Process-specific summary  
        if recent_executions:
            # Find most common process
            process_counts = Counter()
            for exec in recent_executions:
                process_name = exec.get('processName', 'Unknown')
                process_counts[process_name] += 1
            
            if process_counts:
                top_process = process_counts.most_common(1)[0][0]
                process_id = None
                for exec in recent_executions:
                    if exec.get('processName') == top_process:
                        process_id = exec.get('processId')
                        break
                
                if process_id:
                    print(f"🔍 Example 2: Process-Specific Summary for '{top_process}'")
                    print("-" * 40)
                    
                    process_executions = self.query_executions(process_id=process_id, limit=20)
                    if process_executions:
                        process_summary = self.analyze_executions(process_executions)
                        self.display_summary(process_summary, detailed=True)


def main():
    parser = argparse.ArgumentParser(
        description="Get execution performance metrics and generate reports",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    # Get summary for specific execution
    python get_execution_summary.py --execution execution-abc123-def456-2025.08.17
    
    # Get summary for all executions of a process  
    python get_execution_summary.py --process 186bc687-95b9-43f2-b64a-c86355ac8cf2
    
    # Get summary for recent executions
    python get_execution_summary.py --days 7 --limit 50
    
    # JSON output for automation
    python get_execution_summary.py --process 186bc687-95b9-43f2-b64a-c86355ac8cf2 --json
    
    # CSV export
    python get_execution_summary.py --days 30 --csv summary.csv --limit 1000
    
    # Show examples and test
    python get_execution_summary.py --examples
        """
    )
    
    parser.add_argument('--execution', help='Specific execution ID to analyze')
    parser.add_argument('--process', help='Process ID to analyze')
    parser.add_argument('--days', type=int, help='Number of days back to analyze')
    parser.add_argument('--limit', type=int, help='Maximum number of executions to analyze')
    parser.add_argument('--json', action='store_true', help='Output JSON format')
    parser.add_argument('--csv', help='Export to CSV file')
    parser.add_argument('--detailed', '-d', action='store_true', help='Show detailed analysis')
    parser.add_argument('--examples', action='store_true', help='Show examples and test with recent data')
    
    args = parser.parse_args()
    
    try:
        analyzer = ExecutionSummaryAnalyzer()
        
        if args.examples:
            analyzer.run_examples()
            return
        
        # Validate arguments
        if not any([args.execution, args.process, args.days]):
            parser.print_help()
            print("\n❌ Error: Must specify --execution, --process, or --days")
            sys.exit(1)
        
        # Query executions
        print("🔍 Querying execution records...")
        executions = analyzer.query_executions(
            execution_id=args.execution,
            process_id=args.process,
            days_back=args.days,
            limit=args.limit
        )
        
        if not executions:
            print("❌ No executions found matching criteria")
            sys.exit(1)
        
        print(f"✅ Found {len(executions)} execution record(s)")
        print()
        
        # Analyze executions
        summary = analyzer.analyze_executions(executions)
        
        # Output results
        if args.json:
            print(json.dumps(summary, indent=2, default=str))
        else:
            analyzer.display_summary(summary, detailed=args.detailed)
        
        # Export to CSV if requested
        if args.csv:
            analyzer.export_csv(executions, args.csv)
        
    except KeyboardInterrupt:
        print("\n⛔ Analysis interrupted by user")
        sys.exit(130)
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()