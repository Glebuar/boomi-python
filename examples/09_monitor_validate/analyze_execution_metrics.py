#!/usr/bin/env python3
"""
Execution Metrics Analysis

This example demonstrates how to analyze execution metrics including:
- Process execution statistics
- Performance metrics and bottleneck identification
- Error rate analysis
- Throughput calculations
- Trend analysis over time

The ExecutionRecord API provides detailed metrics about process executions
to help optimize integration performance.
"""

import os
import sys
import json
import argparse
from typing import Dict, Any, List, Optional, Tuple
from datetime import datetime, timedelta
from collections import defaultdict
from pathlib import Path

# Add the src directory to the path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from boomi import Boomi
from boomi.models import (
    ExecutionRecordQueryConfig,
    ExecutionRecordQueryConfigQueryFilter,
    ExecutionRecordSimpleExpression,
    ExecutionRecordSimpleExpressionOperator,
    ExecutionRecordSimpleExpressionProperty
)


class ExecutionMetricsAnalyzer:
    """Analyzes execution metrics for performance optimization"""
    
    def __init__(self, verbose: bool = False):
        """Initialize the Execution Metrics Analyzer
        
        Args:
            verbose: Enable verbose output
        """
        self.verbose = verbose
        self.sdk = self._initialize_sdk()
        
    def _initialize_sdk(self) -> Boomi:
        """Initialize Boomi SDK with credentials from environment"""
        account_id = os.getenv('BOOMI_ACCOUNT')
        username = os.getenv('BOOMI_USER')
        password = os.getenv('BOOMI_SECRET')
        
        if not all([account_id, username, password]):
            raise ValueError("Please set BOOMI_ACCOUNT, BOOMI_USER, and BOOMI_SECRET environment variables")
        
        return Boomi(
            account_id=account_id,
            username=username,
            password=password,
            timeout=30000
        )
    
    def _log(self, message: str, level: str = "INFO"):
        """Log message if verbose mode is enabled"""
        if self.verbose:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{timestamp}] [{level}] {message}")
    
    def get_connector_metrics(self, start_date: datetime, end_date: datetime,
                             connector_type: Optional[str] = None,
                             limit: int = 1000) -> List[Dict[str, Any]]:
        """Get execution metrics for a time period

        Args:
            start_date: Start date for metrics
            end_date: End date for metrics
            connector_type: Optional filter by connector type (not used - for future enhancement)
            limit: Maximum number of results

        Returns:
            List of execution metrics
        """
        try:
            self._log(f"Querying execution metrics from {start_date} to {end_date}")

            # Build query expression for execution time
            date_expression = ExecutionRecordSimpleExpression(
                operator=ExecutionRecordSimpleExpressionOperator.GREATERTHAN,
                property=ExecutionRecordSimpleExpressionProperty.EXECUTIONTIME,
                argument=[start_date.strftime("%Y-%m-%dT%H:%M:%SZ")]
            )

            query_filter = ExecutionRecordQueryConfigQueryFilter(
                expression=date_expression
            )

            query_config = ExecutionRecordQueryConfig(query_filter=query_filter)

            result = self.sdk.execution_record.query_execution_record(
                request_body=query_config
            )

            metrics = []
            if hasattr(result, 'result') and result.result:
                for execution in result.result[:limit]:
                    # Extract duration - handle string, int, float, and list formats
                    duration_raw = getattr(execution, 'execution_duration', 0)
                    if isinstance(duration_raw, str):
                        try:
                            duration_ms = int(duration_raw)
                        except (ValueError, TypeError):
                            duration_ms = 0
                    elif isinstance(duration_raw, list) and len(duration_raw) > 1:
                        duration_ms = duration_raw[1]
                    elif isinstance(duration_raw, (int, float)):
                        duration_ms = int(duration_raw)
                    else:
                        duration_ms = 0

                    # Extract document count - handle string and int formats
                    doc_count_raw = getattr(execution, 'inbound_document_count', 0)
                    if isinstance(doc_count_raw, str):
                        try:
                            doc_count = int(doc_count_raw)
                        except (ValueError, TypeError):
                            doc_count = 0
                    else:
                        doc_count = int(doc_count_raw) if doc_count_raw else 0

                    metric = {
                        'execution_id': getattr(execution, 'execution_id', 'N/A'),
                        'connector_type': getattr(execution, 'process_name', 'N/A'),  # Using process name as type
                        'connector_name': getattr(execution, 'process_name', 'N/A'),
                        'execution_time': getattr(execution, 'execution_time', 'N/A'),
                        'duration_ms': duration_ms,
                        'status': getattr(execution, 'status', 'N/A'),
                        'error_message': None,  # ExecutionRecord doesn't include error messages
                        'documents_processed': doc_count,
                        'bytes_processed': 0,  # Not available in ExecutionRecord
                        'atom_id': getattr(execution, 'atom_id', 'N/A'),
                        'atom_name': getattr(execution, 'atom_name', 'N/A'),
                        'process_id': getattr(execution, 'process_id', 'N/A'),
                        'process_name': getattr(execution, 'process_name', 'N/A')
                    }
                    metrics.append(metric)

                self._log(f"Retrieved {len(metrics)} execution metrics")
            else:
                self._log("No execution metrics found for the specified period")

            return metrics

        except Exception as e:
            self._log(f"Error getting execution metrics: {e}", "ERROR")
            if self.verbose:
                import traceback
                traceback.print_exc()
            return []
    
    def analyze_performance(self, metrics: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyze performance metrics
        
        Args:
            metrics: List of execution metrics
            
        Returns:
            Performance analysis results
        """
        analysis = {
            'total_executions': len(metrics),
            'connector_stats': defaultdict(lambda: {
                'count': 0,
                'total_duration': 0,
                'avg_duration': 0,
                'min_duration': float('inf'),
                'max_duration': 0,
                'errors': 0,
                'success_rate': 0,
                'total_documents': 0,
                'total_bytes': 0
            }),
            'overall_stats': {
                'avg_duration': 0,
                'total_errors': 0,
                'success_rate': 0,
                'total_documents': 0,
                'total_bytes': 0,
                'throughput_docs_per_sec': 0,
                'throughput_bytes_per_sec': 0
            },
            'bottlenecks': [],
            'recommendations': []
        }
        
        if not metrics:
            return analysis
        
        try:
            # Analyze by connector type
            total_duration = 0
            total_errors = 0
            total_documents = 0
            total_bytes = 0
            
            for metric in metrics:
                connector_type = metric['connector_type']
                duration = metric.get('duration_ms', 0)
                status = metric.get('status', 'UNKNOWN')
                docs = metric.get('documents_processed', 0)
                bytes_proc = metric.get('bytes_processed', 0)
                
                # Update connector-specific stats
                stats = analysis['connector_stats'][connector_type]
                stats['count'] += 1
                stats['total_duration'] += duration
                stats['min_duration'] = min(stats['min_duration'], duration)
                stats['max_duration'] = max(stats['max_duration'], duration)
                stats['total_documents'] += docs
                stats['total_bytes'] += bytes_proc
                
                if status == 'ERROR' or metric.get('error_message'):
                    stats['errors'] += 1
                    total_errors += 1
                
                # Update totals
                total_duration += duration
                total_documents += docs
                total_bytes += bytes_proc
            
            # Calculate averages and rates
            for connector_type, stats in analysis['connector_stats'].items():
                if stats['count'] > 0:
                    stats['avg_duration'] = stats['total_duration'] / stats['count']
                    stats['success_rate'] = ((stats['count'] - stats['errors']) / stats['count']) * 100
                    
                    # Identify bottlenecks
                    if stats['avg_duration'] > 5000:  # More than 5 seconds average
                        analysis['bottlenecks'].append({
                            'connector': connector_type,
                            'avg_duration_ms': stats['avg_duration'],
                            'recommendation': f"Optimize {connector_type} connector - average execution time is {stats['avg_duration']:.0f}ms"
                        })
            
            # Calculate overall statistics
            if len(metrics) > 0:
                analysis['overall_stats']['avg_duration'] = total_duration / len(metrics)
                analysis['overall_stats']['total_errors'] = total_errors
                analysis['overall_stats']['success_rate'] = ((len(metrics) - total_errors) / len(metrics)) * 100
                analysis['overall_stats']['total_documents'] = total_documents
                analysis['overall_stats']['total_bytes'] = total_bytes
                
                # Calculate throughput
                if total_duration > 0:
                    analysis['overall_stats']['throughput_docs_per_sec'] = (total_documents / total_duration) * 1000
                    analysis['overall_stats']['throughput_bytes_per_sec'] = (total_bytes / total_duration) * 1000
            
            # Generate recommendations
            if analysis['overall_stats']['success_rate'] < 95:
                analysis['recommendations'].append(
                    f"Success rate is {analysis['overall_stats']['success_rate']:.1f}%. Investigate error patterns."
                )
            
            if analysis['overall_stats']['avg_duration'] > 3000:
                analysis['recommendations'].append(
                    "Average execution time exceeds 3 seconds. Consider performance optimization."
                )
            
            # Find slowest connectors
            slowest = sorted(
                analysis['connector_stats'].items(),
                key=lambda x: x[1]['avg_duration'],
                reverse=True
            )[:3]
            
            for connector, stats in slowest:
                if stats['avg_duration'] > 2000:
                    analysis['recommendations'].append(
                        f"Optimize {connector}: avg execution time {stats['avg_duration']:.0f}ms"
                    )
            
            self._log("Performance analysis completed")
            
        except Exception as e:
            self._log(f"Error analyzing performance: {e}", "ERROR")
            analysis['error'] = str(e)
        
        return analysis
    
    def analyze_error_patterns(self, metrics: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyze error patterns in execution metrics
        
        Args:
            metrics: List of execution metrics
            
        Returns:
            Error pattern analysis
        """
        error_analysis = {
            'total_errors': 0,
            'error_rate': 0,
            'errors_by_connector': defaultdict(int),
            'errors_by_message': defaultdict(int),
            'error_timeline': defaultdict(int),
            'most_common_errors': [],
            'recommendations': []
        }
        
        try:
            error_metrics = [m for m in metrics if m.get('status') == 'ERROR' or m.get('error_message')]
            error_analysis['total_errors'] = len(error_metrics)
            
            if len(metrics) > 0:
                error_analysis['error_rate'] = (len(error_metrics) / len(metrics)) * 100
            
            # Analyze error patterns
            for metric in error_metrics:
                # By connector
                connector_type = metric.get('connector_type', 'Unknown')
                error_analysis['errors_by_connector'][connector_type] += 1
                
                # By error message
                error_msg = metric.get('error_message', 'Unknown error')
                if error_msg:
                    # Simplify error message for grouping
                    simplified = error_msg.split('\n')[0][:100]
                    error_analysis['errors_by_message'][simplified] += 1
                
                # By time (hourly buckets)
                try:
                    exec_time = datetime.fromisoformat(
                        metric.get('execution_time', '').replace('Z', '+00:00')
                    )
                    hour_bucket = exec_time.strftime('%Y-%m-%d %H:00')
                    error_analysis['error_timeline'][hour_bucket] += 1
                except:
                    pass
            
            # Identify most common errors
            if error_analysis['errors_by_message']:
                sorted_errors = sorted(
                    error_analysis['errors_by_message'].items(),
                    key=lambda x: x[1],
                    reverse=True
                )[:5]
                
                error_analysis['most_common_errors'] = [
                    {'message': msg, 'count': count}
                    for msg, count in sorted_errors
                ]
            
            # Generate recommendations
            if error_analysis['error_rate'] > 5:
                error_analysis['recommendations'].append(
                    f"High error rate ({error_analysis['error_rate']:.1f}%). Immediate investigation required."
                )
            
            # Check for connector-specific issues
            for connector, count in error_analysis['errors_by_connector'].items():
                error_rate = (count / len([m for m in metrics if m.get('connector_type') == connector])) * 100
                if error_rate > 10:
                    error_analysis['recommendations'].append(
                        f"{connector} has {error_rate:.1f}% error rate. Check connector configuration."
                    )
            
            self._log(f"Error pattern analysis completed: {error_analysis['total_errors']} errors found")
            
        except Exception as e:
            self._log(f"Error analyzing error patterns: {e}", "ERROR")
            error_analysis['error'] = str(e)
        
        return error_analysis
    
    def calculate_trends(self, metrics: List[Dict[str, Any]], 
                        bucket_hours: int = 24) -> Dict[str, Any]:
        """Calculate performance trends over time
        
        Args:
            metrics: List of execution metrics
            bucket_hours: Hours per time bucket for trending
            
        Returns:
            Trend analysis results
        """
        trends = {
            'time_buckets': [],
            'execution_count': [],
            'avg_duration': [],
            'error_rate': [],
            'throughput': [],
            'trend_direction': {},
            'insights': []
        }
        
        if not metrics:
            return trends
        
        try:
            # Group metrics by time buckets
            time_buckets = defaultdict(list)
            
            for metric in metrics:
                try:
                    exec_time = datetime.fromisoformat(
                        metric.get('execution_time', '').replace('Z', '+00:00')
                    )
                    
                    # Create bucket key
                    bucket_time = exec_time.replace(
                        hour=(exec_time.hour // bucket_hours) * bucket_hours,
                        minute=0,
                        second=0,
                        microsecond=0
                    )
                    
                    time_buckets[bucket_time].append(metric)
                except:
                    continue
            
            # Sort buckets by time
            sorted_buckets = sorted(time_buckets.items())
            
            # Calculate metrics for each bucket
            for bucket_time, bucket_metrics in sorted_buckets:
                trends['time_buckets'].append(bucket_time.isoformat())
                trends['execution_count'].append(len(bucket_metrics))
                
                # Average duration
                durations = [m.get('duration_ms', 0) for m in bucket_metrics]
                avg_duration = sum(durations) / len(durations) if durations else 0
                trends['avg_duration'].append(avg_duration)
                
                # Error rate
                errors = len([m for m in bucket_metrics if m.get('status') == 'ERROR'])
                error_rate = (errors / len(bucket_metrics)) * 100 if bucket_metrics else 0
                trends['error_rate'].append(error_rate)
                
                # Throughput (docs per second)
                total_docs = sum(m.get('documents_processed', 0) for m in bucket_metrics)
                total_duration_sec = sum(m.get('duration_ms', 0) for m in bucket_metrics) / 1000
                throughput = total_docs / total_duration_sec if total_duration_sec > 0 else 0
                trends['throughput'].append(throughput)
            
            # Calculate trend directions
            if len(trends['execution_count']) >= 2:
                # Execution count trend
                if trends['execution_count'][-1] > trends['execution_count'][0]:
                    trends['trend_direction']['execution_count'] = 'increasing'
                    trends['insights'].append("Execution volume is increasing")
                elif trends['execution_count'][-1] < trends['execution_count'][0]:
                    trends['trend_direction']['execution_count'] = 'decreasing'
                    trends['insights'].append("Execution volume is decreasing")
                else:
                    trends['trend_direction']['execution_count'] = 'stable'
                
                # Performance trend
                if trends['avg_duration'][-1] > trends['avg_duration'][0] * 1.1:
                    trends['trend_direction']['performance'] = 'degrading'
                    trends['insights'].append("Performance is degrading over time")
                elif trends['avg_duration'][-1] < trends['avg_duration'][0] * 0.9:
                    trends['trend_direction']['performance'] = 'improving'
                    trends['insights'].append("Performance is improving")
                else:
                    trends['trend_direction']['performance'] = 'stable'
                
                # Error trend
                if trends['error_rate'][-1] > trends['error_rate'][0]:
                    trends['trend_direction']['errors'] = 'increasing'
                    trends['insights'].append("Error rate is increasing - investigation needed")
                elif trends['error_rate'][-1] < trends['error_rate'][0]:
                    trends['trend_direction']['errors'] = 'decreasing'
                    trends['insights'].append("Error rate is improving")
            
            self._log("Trend analysis completed")
            
        except Exception as e:
            self._log(f"Error calculating trends: {e}", "ERROR")
            trends['error'] = str(e)
        
        return trends
    
    def display_analysis(self, analysis: Dict[str, Any], analysis_type: str = "performance"):
        """Display analysis results
        
        Args:
            analysis: Analysis results dictionary
            analysis_type: Type of analysis (performance, errors, trends)
        """
        if analysis_type == "performance":
            print(f"\n{'='*80}")
            print("Performance Analysis")
            print(f"{'='*80}\n")
            
            overall = analysis['overall_stats']
            print("📊 Overall Statistics:")
            print(f"  Total Executions: {analysis['total_executions']}")
            print(f"  Average Duration: {overall['avg_duration']:.0f}ms")
            print(f"  Success Rate: {overall['success_rate']:.1f}%")
            print(f"  Total Documents: {overall['total_documents']:,}")
            print(f"  Total Bytes: {overall['total_bytes']:,}")
            print(f"  Throughput: {overall['throughput_docs_per_sec']:.1f} docs/sec")
            
            if analysis['connector_stats']:
                print("\n📈 Connector Performance:")
                print(f"{'Connector':<20} {'Count':<10} {'Avg (ms)':<12} {'Success %':<12} {'Documents':<12}")
                print("-" * 70)
                
                for connector, stats in sorted(analysis['connector_stats'].items()):
                    print(f"{connector:<20} {stats['count']:<10} "
                          f"{stats['avg_duration']:<12.0f} {stats['success_rate']:<12.1f} "
                          f"{stats['total_documents']:<12}")
            
            if analysis['bottlenecks']:
                print("\n⚠️ Performance Bottlenecks:")
                for bottleneck in analysis['bottlenecks']:
                    print(f"  • {bottleneck['recommendation']}")
            
            if analysis['recommendations']:
                print("\n💡 Recommendations:")
                for rec in analysis['recommendations']:
                    print(f"  • {rec}")
        
        elif analysis_type == "errors":
            print(f"\n{'='*80}")
            print("Error Pattern Analysis")
            print(f"{'='*80}\n")
            
            print(f"Total Errors: {analysis['total_errors']}")
            print(f"Error Rate: {analysis['error_rate']:.1f}%")
            
            if analysis['errors_by_connector']:
                print("\n❌ Errors by Connector:")
                for connector, count in sorted(
                    analysis['errors_by_connector'].items(),
                    key=lambda x: x[1],
                    reverse=True
                ):
                    print(f"  {connector}: {count}")
            
            if analysis['most_common_errors']:
                print("\n🔍 Most Common Errors:")
                for i, error in enumerate(analysis['most_common_errors'], 1):
                    print(f"  {i}. {error['message'][:80]}... ({error['count']} occurrences)")
            
            if analysis['recommendations']:
                print("\n💡 Recommendations:")
                for rec in analysis['recommendations']:
                    print(f"  • {rec}")
        
        elif analysis_type == "trends":
            print(f"\n{'='*80}")
            print("Trend Analysis")
            print(f"{'='*80}\n")
            
            if analysis['trend_direction']:
                print("📈 Trend Directions:")
                for metric, direction in analysis['trend_direction'].items():
                    icon = "↗️" if direction == "increasing" else "↘️" if direction == "decreasing" else "→"
                    print(f"  {metric}: {icon} {direction}")
            
            if analysis['insights']:
                print("\n🔍 Insights:")
                for insight in analysis['insights']:
                    print(f"  • {insight}")
            
            if analysis['time_buckets']:
                print("\n📊 Execution Count Over Time:")
                for i, (time, count) in enumerate(zip(
                    analysis['time_buckets'][-5:],
                    analysis['execution_count'][-5:]
                )):
                    print(f"  {time}: {count} executions")


def main():
    """Main function to handle command-line arguments"""
    parser = argparse.ArgumentParser(
        description="Analyze execution metrics",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Analyze performance for last 7 days
  %(prog)s --analyze-performance --days 7
  
  # Analyze error patterns
  %(prog)s --analyze-errors --days 1
  
  # Calculate trends over time
  %(prog)s --analyze-trends --days 30 --bucket-hours 24
  
  # Filter by connector type
  %(prog)s --analyze-performance --days 7 --connector-type HTTP
  
  # Get raw metrics
  %(prog)s --get-metrics --days 1 --format json
  
  # Full analysis suite
  %(prog)s --full-analysis --days 7
        """
    )
    
    parser.add_argument('--get-metrics', action='store_true',
                       help='Get raw execution metrics')
    parser.add_argument('--analyze-performance', action='store_true',
                       help='Analyze performance metrics')
    parser.add_argument('--analyze-errors', action='store_true',
                       help='Analyze error patterns')
    parser.add_argument('--analyze-trends', action='store_true',
                       help='Analyze trends over time')
    parser.add_argument('--full-analysis', action='store_true',
                       help='Run complete analysis suite')
    
    parser.add_argument('--days', type=int, default=7,
                       help='Number of days to analyze')
    parser.add_argument('--connector-type', type=str,
                       help='Filter by connector type')
    parser.add_argument('--bucket-hours', type=int, default=24,
                       help='Hours per time bucket for trends')
    
    parser.add_argument('--format', type=str, choices=['table', 'json'],
                       default='table', help='Output format')
    parser.add_argument('--limit', type=int, default=1000,
                       help='Maximum number of metrics to analyze')
    parser.add_argument('--verbose', action='store_true',
                       help='Enable verbose output')
    
    args = parser.parse_args()
    
    # Validate arguments
    if not any([args.get_metrics, args.analyze_performance, args.analyze_errors,
                args.analyze_trends, args.full_analysis]):
        parser.print_help()
        return 1
    
    try:
        analyzer = ExecutionMetricsAnalyzer(verbose=args.verbose)
        
        # Calculate date range
        end_date = datetime.now()
        start_date = end_date - timedelta(days=args.days)
        
        # Get metrics
        metrics = analyzer.get_connector_metrics(
            start_date=start_date,
            end_date=end_date,
            connector_type=args.connector_type,
            limit=args.limit
        )
        
        if not metrics:
            print("No metrics found for the specified period")
            return 0
        
        if args.get_metrics:
            if args.format == 'json':
                print(json.dumps(metrics, indent=2, default=str))
            else:
                print(f"\n{'='*100}")
                print(f"{'Connector':<20} {'Status':<10} {'Duration(ms)':<15} {'Docs':<10} {'Time':<25}")
                print(f"{'='*100}")
                
                for metric in metrics[:50]:  # Limit table output
                    connector = str(metric['connector_type'])[:18]
                    status = str(metric['status'])[:8]
                    duration = str(metric['duration_ms'])[:13]
                    docs = str(metric['documents_processed'])[:8]
                    exec_time = str(metric['execution_time'])[:23]
                    
                    print(f"{connector:<20} {status:<10} {duration:<15} {docs:<10} {exec_time:<25}")
                
                print(f"{'='*100}")
                print(f"Showing {min(50, len(metrics))} of {len(metrics)} metrics")
        
        if args.analyze_performance or args.full_analysis:
            analysis = analyzer.analyze_performance(metrics)
            analyzer.display_analysis(analysis, "performance")
        
        if args.analyze_errors or args.full_analysis:
            error_analysis = analyzer.analyze_error_patterns(metrics)
            analyzer.display_analysis(error_analysis, "errors")
        
        if args.analyze_trends or args.full_analysis:
            trends = analyzer.calculate_trends(metrics, args.bucket_hours)
            analyzer.display_analysis(trends, "trends")
        
        return 0
        
    except Exception as e:
        print(f"❌ Error: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())