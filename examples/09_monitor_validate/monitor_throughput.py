#!/usr/bin/env python3
"""
Throughput Monitoring

This example demonstrates how to monitor integration throughput including:
- Account-level throughput metrics
- Document processing rates
- Data volume analysis
- Peak load identification
- Capacity planning insights

The Throughput APIs provide visibility into data processing volumes
to help with capacity planning and performance optimization.
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
    ThroughputAccountQueryConfig,
    ThroughputAccountSimpleExpression,
    ThroughputAccountSimpleExpressionOperator,
    ThroughputAccountSimpleExpressionProperty,
    ThroughputAccountQueryConfigQueryFilter
)


class ThroughputMonitor:
    """Monitors integration throughput and data processing volumes"""
    
    def __init__(self, verbose: bool = False):
        """Initialize the Throughput Monitor
        
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
    
    def get_throughput_metrics(self, start_date: datetime, end_date: datetime,
                               limit: int = 1000) -> List[Dict[str, Any]]:
        """Get throughput metrics for a time period
        
        Args:
            start_date: Start date for metrics
            end_date: End date for metrics
            limit: Maximum number of results
            
        Returns:
            List of throughput metrics
        """
        try:
            self._log(f"Querying throughput metrics from {start_date} to {end_date}")
            
            # Build query expression
            date_expression = ThroughputAccountSimpleExpression(
                operator=ThroughputAccountSimpleExpressionOperator.BETWEEN,
                property=ThroughputAccountSimpleExpressionProperty.PROCESSDATE,
                argument=[start_date.isoformat(), end_date.isoformat()]
            )
            
            query_filter = ThroughputAccountQueryConfigQueryFilter(
                expression=date_expression
            )
            query_config = ThroughputAccountQueryConfig(query_filter=query_filter)
            
            result = self.sdk.throughput_account.query_throughput_account(
                request_body=query_config
            )
            
            metrics = []
            if hasattr(result, 'result') and result.result:
                for throughput in result.result[:limit]:
                    metric = {
                        'date': getattr(throughput, 'date', 'N/A'),
                        'hour': getattr(throughput, 'hour', 0),
                        'documents_processed': getattr(throughput, 'documents_processed', 0),
                        'bytes_processed': getattr(throughput, 'bytes_processed', 0),
                        'executions': getattr(throughput, 'executions', 0),
                        'successful_executions': getattr(throughput, 'successful_executions', 0),
                        'failed_executions': getattr(throughput, 'failed_executions', 0),
                        'atom_id': getattr(throughput, 'atom_id', 'N/A'),
                        'process_id': getattr(throughput, 'process_id', 'N/A'),
                        'environment_id': getattr(throughput, 'environment_id', 'N/A')
                    }
                    
                    # Calculate derived metrics
                    if metric['executions'] > 0:
                        metric['success_rate'] = (
                            metric['successful_executions'] / metric['executions']
                        ) * 100
                    else:
                        metric['success_rate'] = 0
                    
                    # Calculate throughput rates
                    metric['docs_per_hour'] = metric['documents_processed']
                    metric['mb_per_hour'] = metric['bytes_processed'] / (1024 * 1024)
                    
                    metrics.append(metric)
                
                self._log(f"Retrieved {len(metrics)} throughput metrics")
            else:
                self._log("No throughput metrics found for the specified period")
            
            return metrics
            
        except Exception as e:
            self._log(f"Error getting throughput metrics: {e}", "ERROR")
            if self.verbose:
                import traceback
                traceback.print_exc()
            return []
    
    def analyze_throughput(self, metrics: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyze throughput patterns and performance
        
        Args:
            metrics: List of throughput metrics
            
        Returns:
            Throughput analysis results
        """
        analysis = {
            'summary': {
                'total_documents': 0,
                'total_bytes': 0,
                'total_executions': 0,
                'avg_docs_per_hour': 0,
                'avg_mb_per_hour': 0,
                'peak_docs_per_hour': 0,
                'peak_mb_per_hour': 0,
                'peak_time': None,
                'overall_success_rate': 0
            },
            'daily_patterns': defaultdict(lambda: {
                'documents': 0,
                'bytes': 0,
                'executions': 0
            }),
            'hourly_patterns': defaultdict(lambda: {
                'documents': 0,
                'bytes': 0,
                'count': 0
            }),
            'capacity_insights': [],
            'recommendations': []
        }
        
        if not metrics:
            return analysis
        
        try:
            # Calculate summary statistics
            total_successful = 0
            peak_docs = 0
            peak_mb = 0
            peak_time = None
            
            for metric in metrics:
                # Update totals
                docs = metric['documents_processed']
                bytes_proc = metric['bytes_processed']
                execs = metric['executions']
                
                analysis['summary']['total_documents'] += docs
                analysis['summary']['total_bytes'] += bytes_proc
                analysis['summary']['total_executions'] += execs
                total_successful += metric['successful_executions']
                
                # Track peak throughput
                if docs > peak_docs:
                    peak_docs = docs
                    peak_time = f"{metric['date']} {metric['hour']}:00"
                
                mb_per_hour = bytes_proc / (1024 * 1024)
                if mb_per_hour > peak_mb:
                    peak_mb = mb_per_hour
                
                # Analyze daily patterns
                date_key = metric['date']
                analysis['daily_patterns'][date_key]['documents'] += docs
                analysis['daily_patterns'][date_key]['bytes'] += bytes_proc
                analysis['daily_patterns'][date_key]['executions'] += execs
                
                # Analyze hourly patterns
                hour_key = metric['hour']
                analysis['hourly_patterns'][hour_key]['documents'] += docs
                analysis['hourly_patterns'][hour_key]['bytes'] += bytes_proc
                analysis['hourly_patterns'][hour_key]['count'] += 1
            
            # Calculate averages
            num_hours = len(metrics)
            if num_hours > 0:
                analysis['summary']['avg_docs_per_hour'] = (
                    analysis['summary']['total_documents'] / num_hours
                )
                analysis['summary']['avg_mb_per_hour'] = (
                    analysis['summary']['total_bytes'] / (1024 * 1024 * num_hours)
                )
                
                if analysis['summary']['total_executions'] > 0:
                    analysis['summary']['overall_success_rate'] = (
                        total_successful / analysis['summary']['total_executions']
                    ) * 100
            
            analysis['summary']['peak_docs_per_hour'] = peak_docs
            analysis['summary']['peak_mb_per_hour'] = peak_mb
            analysis['summary']['peak_time'] = peak_time
            
            # Identify peak hours
            peak_hours = sorted(
                analysis['hourly_patterns'].items(),
                key=lambda x: x[1]['documents'],
                reverse=True
            )[:3]
            
            analysis['capacity_insights'].append(
                f"Peak processing hours: {', '.join([f'{h[0]}:00' for h in peak_hours])}"
            )
            
            # Capacity planning insights
            if peak_docs > analysis['summary']['avg_docs_per_hour'] * 2:
                analysis['capacity_insights'].append(
                    f"Peak load is {peak_docs / analysis['summary']['avg_docs_per_hour']:.1f}x average"
                )
                analysis['recommendations'].append(
                    "Consider auto-scaling during peak hours"
                )
            
            # Check for processing bottlenecks
            if analysis['summary']['overall_success_rate'] < 95:
                analysis['recommendations'].append(
                    f"Success rate is {analysis['summary']['overall_success_rate']:.1f}%. "
                    "Review error logs and processing capacity."
                )
            
            # Analyze growth trends
            daily_data = sorted(analysis['daily_patterns'].items())
            if len(daily_data) >= 7:
                first_week_avg = sum(
                    d[1]['documents'] for d in daily_data[:7]
                ) / 7
                last_week_avg = sum(
                    d[1]['documents'] for d in daily_data[-7:]
                ) / 7
                
                if last_week_avg > first_week_avg * 1.2:
                    growth = ((last_week_avg - first_week_avg) / first_week_avg) * 100
                    analysis['capacity_insights'].append(
                        f"Document volume growing at {growth:.1f}% per week"
                    )
                    analysis['recommendations'].append(
                        "Plan for capacity expansion based on growth trend"
                    )
            
            self._log("Throughput analysis completed")
            
        except Exception as e:
            self._log(f"Error analyzing throughput: {e}", "ERROR")
            analysis['error'] = str(e)
        
        return analysis
    
    def calculate_capacity_metrics(self, metrics: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Calculate capacity utilization metrics
        
        Args:
            metrics: List of throughput metrics
            
        Returns:
            Capacity metrics and recommendations
        """
        capacity = {
            'utilization_by_hour': {},
            'avg_utilization': 0,
            'peak_utilization': 0,
            'capacity_thresholds': {
                'documents_per_hour': 10000,  # Example threshold
                'mb_per_hour': 1000  # Example threshold
            },
            'warnings': [],
            'recommendations': []
        }
        
        try:
            # Calculate utilization for each hour
            for metric in metrics:
                hour_key = f"{metric['date']} {metric['hour']}:00"
                
                doc_utilization = (
                    metric['documents_processed'] / 
                    capacity['capacity_thresholds']['documents_per_hour']
                ) * 100
                
                mb_utilization = (
                    (metric['bytes_processed'] / (1024 * 1024)) /
                    capacity['capacity_thresholds']['mb_per_hour']
                ) * 100
                
                utilization = max(doc_utilization, mb_utilization)
                capacity['utilization_by_hour'][hour_key] = utilization
                
                if utilization > capacity['peak_utilization']:
                    capacity['peak_utilization'] = utilization
                
                # Check for capacity warnings
                if utilization > 90:
                    capacity['warnings'].append(
                        f"Critical capacity at {hour_key}: {utilization:.1f}%"
                    )
                elif utilization > 75:
                    capacity['warnings'].append(
                        f"High capacity at {hour_key}: {utilization:.1f}%"
                    )
            
            # Calculate average utilization
            if capacity['utilization_by_hour']:
                capacity['avg_utilization'] = sum(
                    capacity['utilization_by_hour'].values()
                ) / len(capacity['utilization_by_hour'])
            
            # Generate recommendations
            if capacity['peak_utilization'] > 90:
                capacity['recommendations'].append(
                    "Peak utilization exceeds 90%. Immediate capacity expansion recommended."
                )
            elif capacity['peak_utilization'] > 75:
                capacity['recommendations'].append(
                    "Peak utilization exceeds 75%. Plan for capacity expansion."
                )
            
            if capacity['avg_utilization'] > 60:
                capacity['recommendations'].append(
                    f"Average utilization is {capacity['avg_utilization']:.1f}%. "
                    "Consider load balancing or additional resources."
                )
            
            self._log(f"Capacity analysis: avg={capacity['avg_utilization']:.1f}%, "
                     f"peak={capacity['peak_utilization']:.1f}%")
            
        except Exception as e:
            self._log(f"Error calculating capacity metrics: {e}", "ERROR")
            capacity['error'] = str(e)
        
        return capacity
    
    def display_throughput_summary(self, analysis: Dict[str, Any]):
        """Display throughput analysis summary
        
        Args:
            analysis: Throughput analysis results
        """
        print(f"\n{'='*80}")
        print("Throughput Analysis Summary")
        print(f"{'='*80}\n")
        
        summary = analysis['summary']
        
        print("📊 Overall Statistics:")
        print(f"  Total Documents: {summary['total_documents']:,}")
        print(f"  Total Data: {summary['total_bytes'] / (1024**3):.2f} GB")
        print(f"  Total Executions: {summary['total_executions']:,}")
        print(f"  Success Rate: {summary['overall_success_rate']:.1f}%")
        
        print("\n📈 Throughput Rates:")
        print(f"  Average: {summary['avg_docs_per_hour']:.0f} docs/hour, "
              f"{summary['avg_mb_per_hour']:.1f} MB/hour")
        print(f"  Peak: {summary['peak_docs_per_hour']} docs/hour, "
              f"{summary['peak_mb_per_hour']:.1f} MB/hour")
        if summary['peak_time']:
            print(f"  Peak Time: {summary['peak_time']}")
        
        if analysis['capacity_insights']:
            print("\n🔍 Capacity Insights:")
            for insight in analysis['capacity_insights']:
                print(f"  • {insight}")
        
        if analysis['recommendations']:
            print("\n💡 Recommendations:")
            for rec in analysis['recommendations']:
                print(f"  • {rec}")
    
    def display_patterns(self, analysis: Dict[str, Any], pattern_type: str = "daily"):
        """Display throughput patterns
        
        Args:
            analysis: Throughput analysis results
            pattern_type: Type of pattern to display (daily, hourly)
        """
        if pattern_type == "daily":
            patterns = analysis['daily_patterns']
            if not patterns:
                print("No daily patterns available")
                return
            
            print(f"\n{'='*80}")
            print("Daily Throughput Patterns")
            print(f"{'='*80}")
            print(f"{'Date':<15} {'Documents':<15} {'Data (GB)':<15} {'Executions':<15}")
            print("-" * 60)
            
            for date, stats in sorted(patterns.items()):
                gb = stats['bytes'] / (1024**3)
                print(f"{date:<15} {stats['documents']:<15,} "
                      f"{gb:<15.2f} {stats['executions']:<15,}")
        
        elif pattern_type == "hourly":
            patterns = analysis['hourly_patterns']
            if not patterns:
                print("No hourly patterns available")
                return
            
            print(f"\n{'='*80}")
            print("Hourly Throughput Patterns (Averages)")
            print(f"{'='*80}")
            print(f"{'Hour':<10} {'Avg Documents':<20} {'Avg Data (MB)':<20}")
            print("-" * 50)
            
            for hour in range(24):
                if hour in patterns:
                    stats = patterns[hour]
                    count = stats['count']
                    avg_docs = stats['documents'] / count if count > 0 else 0
                    avg_mb = (stats['bytes'] / (1024**2)) / count if count > 0 else 0
                    
                    # Create visual bar
                    bar_length = int(avg_docs / 100)
                    bar = '█' * min(bar_length, 30)
                    
                    print(f"{hour:02d}:00     {avg_docs:<20.0f} {avg_mb:<20.1f} {bar}")


def main():
    """Main function to handle command-line arguments"""
    parser = argparse.ArgumentParser(
        description="Monitor integration throughput",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Get throughput metrics for last 7 days
  %(prog)s --get-metrics --days 7
  
  # Analyze throughput patterns
  %(prog)s --analyze --days 30
  
  # Calculate capacity utilization
  %(prog)s --capacity --days 7
  
  # Display daily patterns
  %(prog)s --patterns daily --days 30
  
  # Display hourly patterns
  %(prog)s --patterns hourly --days 7
  
  # Full throughput report
  %(prog)s --full-report --days 30
  
  # Output metrics in JSON format
  %(prog)s --get-metrics --days 1 --format json
        """
    )
    
    parser.add_argument('--get-metrics', action='store_true',
                       help='Get raw throughput metrics')
    parser.add_argument('--analyze', action='store_true',
                       help='Analyze throughput patterns')
    parser.add_argument('--capacity', action='store_true',
                       help='Calculate capacity utilization')
    parser.add_argument('--patterns', type=str, choices=['daily', 'hourly'],
                       help='Display throughput patterns')
    parser.add_argument('--full-report', action='store_true',
                       help='Generate full throughput report')
    
    parser.add_argument('--days', type=int, default=7,
                       help='Number of days to analyze')
    
    parser.add_argument('--format', type=str, choices=['table', 'json'],
                       default='table', help='Output format')
    parser.add_argument('--limit', type=int, default=1000,
                       help='Maximum number of metrics')
    parser.add_argument('--verbose', action='store_true',
                       help='Enable verbose output')
    
    args = parser.parse_args()
    
    # Validate arguments - use default operation if none specified
    if not any([args.get_metrics, args.analyze, args.capacity, 
                args.patterns, args.full_report]):
        args.get_metrics = True
        print("ℹ️ No operation specified, using default: --get-metrics")
        print("💡 Available operations: --get-metrics, --analyze, --capacity, --patterns, --full-report")
    
    try:
        monitor = ThroughputMonitor(verbose=args.verbose)
        
        # Calculate date range
        end_date = datetime.now()
        start_date = end_date - timedelta(days=args.days)
        
        # Get metrics
        metrics = monitor.get_throughput_metrics(
            start_date=start_date,
            end_date=end_date,
            limit=args.limit
        )
        
        if not metrics:
            print("No throughput metrics found for the specified period")
            return 0
        
        if args.get_metrics:
            if args.format == 'json':
                print(json.dumps(metrics, indent=2, default=str))
            else:
                print(f"\n{'='*100}")
                print(f"{'Date':<12} {'Hour':<6} {'Documents':<12} {'MB':<10} "
                      f"{'Executions':<12} {'Success %':<10}")
                print(f"{'='*100}")
                
                for metric in metrics[:50]:  # Limit table output
                    date = str(metric['date'])[:10]
                    hour = f"{metric['hour']:02d}:00"
                    docs = metric['documents_processed']
                    mb = metric['bytes_processed'] / (1024**2)
                    execs = metric['executions']
                    success = metric['success_rate']
                    
                    print(f"{date:<12} {hour:<6} {docs:<12,} {mb:<10.1f} "
                          f"{execs:<12} {success:<10.1f}")
                
                print(f"{'='*100}")
                print(f"Showing {min(50, len(metrics))} of {len(metrics)} metrics")
        
        # Analyze throughput
        analysis = None
        if args.analyze or args.full_report:
            analysis = monitor.analyze_throughput(metrics)
            monitor.display_throughput_summary(analysis)
        
        if args.capacity or args.full_report:
            capacity = monitor.calculate_capacity_metrics(metrics)
            
            print(f"\n{'='*60}")
            print("Capacity Utilization")
            print(f"{'='*60}\n")
            
            print(f"Average Utilization: {capacity['avg_utilization']:.1f}%")
            print(f"Peak Utilization: {capacity['peak_utilization']:.1f}%")
            
            if capacity['warnings']:
                print("\n⚠️ Capacity Warnings:")
                for warning in capacity['warnings'][:10]:  # Limit warnings
                    print(f"  • {warning}")
            
            if capacity['recommendations']:
                print("\n💡 Recommendations:")
                for rec in capacity['recommendations']:
                    print(f"  • {rec}")
        
        if args.patterns:
            if not analysis:
                analysis = monitor.analyze_throughput(metrics)
            monitor.display_patterns(analysis, args.patterns)
        
        if args.full_report:
            # Display both pattern types
            if analysis:
                monitor.display_patterns(analysis, "daily")
                monitor.display_patterns(analysis, "hourly")
        
        return 0
        
    except Exception as e:
        print(f"❌ Error: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())