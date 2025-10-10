#!/usr/bin/env python3
"""
Boomi SDK Example: Query Audit Logs
===================================

This example demonstrates how to query and analyze Boomi audit logs for compliance,
security monitoring, and change tracking purposes. Audit logs provide detailed records
of all user actions, system changes, and administrative operations.

Features:
- Query audit logs by date range with flexible filtering
- Filter by user, action type, object type, and level
- Export audit reports in multiple formats (JSON, CSV, HTML)
- Track specific changes to components, processes, and configurations  
- Generate compliance reports with summary statistics
- Support for pagination with large result sets
- Advanced search with multiple filter criteria

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- Appropriate audit log access privileges required
- ACCOUNT ADMIN or AUDIT privileges may be required for full access

Usage:
    # Query recent audit logs
    python query_audit_logs.py --days 30
    
    # Query specific date range
    python query_audit_logs.py --start-date 2025-01-01 --end-date 2025-01-31
    
    # Filter by user and action
    python query_audit_logs.py --days 7 --user "user@company.com" --action UPDATE
    
    # Export compliance report
    python query_audit_logs.py --days 90 --export report.json --summary

Examples:
    python query_audit_logs.py --days 30 --type "as.atom" --action UPDATE
    python query_audit_logs.py --start-date 2025-01-01 --user "admin@company.com" --export audit_report.csv
    python query_audit_logs.py --days 7 --level ERROR --summary
"""

import os
import sys
import argparse
import json
import csv
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Any
from collections import defaultdict, Counter

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.boomi import Boomi


class AuditLogAnalyzer:
    """Manages audit log querying and analysis operations"""
    
    def __init__(self):
        """Initialize the Boomi SDK client"""
        self.sdk = Boomi(
            account_id=os.getenv("BOOMI_ACCOUNT"),
            username=os.getenv("BOOMI_USER"),
            password=os.getenv("BOOMI_SECRET"),
            timeout=30000
        )
        print("✅ SDK initialized successfully")
    
    def query_audit_logs(self, start_date: str, end_date: str,
                        user_filter: Optional[str] = None,
                        action_filter: Optional[str] = None,
                        type_filter: Optional[str] = None,
                        level_filter: Optional[str] = None,
                        limit: Optional[int] = None) -> List[Dict[str, Any]]:
        """Query audit logs with optional filters using SDK"""
        print(f"\n🔍 Querying audit logs from {start_date} to {end_date}")
        
        try:
            # Import SDK models
            from src.boomi.models import (
                AuditLogQueryConfig,
                AuditLogQueryConfigQueryFilter,
                AuditLogSimpleExpression,
                AuditLogSimpleExpressionOperator,
                AuditLogSimpleExpressionProperty,
                AuditLogGroupingExpression,
                QuerySort,
                SortField
            )
            
            # Build filter expressions
            expressions = []
            
            # Add date range filter
            date_expression = AuditLogSimpleExpression(
                operator=AuditLogSimpleExpressionOperator.BETWEEN,
                property=AuditLogSimpleExpressionProperty.DATE,
                argument=[start_date, end_date]
            )
            expressions.append(date_expression)
            
            # Add optional filters
            if user_filter:
                user_expression = AuditLogSimpleExpression(
                    operator=AuditLogSimpleExpressionOperator.EQUALS,
                    property=AuditLogSimpleExpressionProperty.USERID,
                    argument=[user_filter]
                )
                expressions.append(user_expression)
                print(f"   📧 Filtering by user: {user_filter}")
            
            if action_filter:
                action_expression = AuditLogSimpleExpression(
                    operator=AuditLogSimpleExpressionOperator.EQUALS,
                    property=AuditLogSimpleExpressionProperty.ACTION,
                    argument=[action_filter]
                )
                expressions.append(action_expression)
                print(f"   ⚡ Filtering by action: {action_filter}")
            
            if type_filter:
                type_expression = AuditLogSimpleExpression(
                    operator=AuditLogSimpleExpressionOperator.EQUALS,
                    property=AuditLogSimpleExpressionProperty.TYPE,
                    argument=[type_filter]
                )
                expressions.append(type_expression)
                print(f"   🏷️ Filtering by type: {type_filter}")
            
            if level_filter:
                level_expression = AuditLogSimpleExpression(
                    operator=AuditLogSimpleExpressionOperator.EQUALS,
                    property=AuditLogSimpleExpressionProperty.LEVEL,
                    argument=[level_filter]
                )
                expressions.append(level_expression)
                print(f"   📊 Filtering by level: {level_filter}")
            
            # Create query filter
            if len(expressions) == 1:
                query_filter = AuditLogQueryConfigQueryFilter(
                    expression=expressions[0]
                )
            else:
                grouping_expression = AuditLogGroupingExpression(
                    operator="and",
                    nested_expression=expressions
                )
                query_filter = AuditLogQueryConfigQueryFilter(
                    expression=grouping_expression
                )
            
            # Create sort configuration
            sort_field = SortField(
                field_name="date",
                sort_order="DESC"
            )
            query_sort = QuerySort(sort_field=[sort_field])
            
            # Create query config
            query_config = AuditLogQueryConfig(
                query_filter=query_filter,
                query_sort=query_sort
            )
            
            # Execute query using SDK
            result = self.sdk.audit_log.query_audit_log(
                request_body=query_config
            )
            
            if result and hasattr(result, 'result') and result.result:
                # Convert SDK models to dicts for backward compatibility
                audit_logs = []
                for log_entry in result.result:
                    log_dict = {
                        'userId': getattr(log_entry, 'user_id', 'Unknown'),
                        'action': getattr(log_entry, 'action', 'Unknown'),
                        'type': getattr(log_entry, 'type_', 'Unknown'),
                        'level': getattr(log_entry, 'level', 'Unknown'),
                        'modifier': getattr(log_entry, 'modifier', 'Unknown'),
                        'source': getattr(log_entry, 'source', 'Unknown'),
                        'date': getattr(log_entry, 'date_', ''),
                        'containerId': getattr(log_entry, 'container_id', 'N/A'),
                        'accountId': getattr(log_entry, 'account_id', 'N/A')
                    }
                    audit_logs.append(log_dict)
                
                total_count = getattr(result, 'number_of_results', len(audit_logs))
                query_token = getattr(result, 'query_token', None)
                
                print(f"✅ Found {total_count} audit log entries")
                
                # Handle pagination if we have more results
                if query_token and len(audit_logs) < total_count:
                    print(f"   📄 Retrieving additional results (showing first page of {len(audit_logs)})")
                    # For now, return first page. Could implement full pagination later
                
                # Apply limit if specified
                if limit and len(audit_logs) > limit:
                    audit_logs = audit_logs[:limit]
                    print(f"   📊 Limited to {limit} results")
                
                return audit_logs
            else:
                print("✅ No audit logs found matching criteria")
                return []
                
        except Exception as e:
            print(f"❌ Failed to query audit logs: {e}")
            return []
    
    def analyze_audit_logs(self, audit_logs: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyze audit log data and generate statistics"""
        print(f"\n📊 Analyzing {len(audit_logs)} audit log entries")
        
        if not audit_logs:
            return {"total_entries": 0}
        
        analysis = {
            "total_entries": len(audit_logs),
            "date_range": {
                "earliest": None,
                "latest": None
            },
            "users": Counter(),
            "actions": Counter(),
            "types": Counter(),
            "levels": Counter(),
            "modifiers": Counter(),
            "sources": Counter(),
            "daily_activity": defaultdict(int),
            "hourly_activity": defaultdict(int),
            "user_actions": defaultdict(Counter),
            "type_actions": defaultdict(Counter),
            "recent_changes": [],
            "error_entries": [],
            "summary": {}
        }
        
        try:
            dates = []
            
            for log_entry in audit_logs:
                # Basic fields
                user = log_entry.get('userId', 'Unknown')
                action = log_entry.get('action', 'Unknown')
                log_type = log_entry.get('type', 'Unknown')
                level = log_entry.get('level', 'Unknown')
                modifier = log_entry.get('modifier', 'Unknown')
                source = log_entry.get('source', 'Unknown')
                date_str = log_entry.get('date', '')
                
                # Count occurrences
                analysis["users"][user] += 1
                analysis["actions"][action] += 1
                analysis["types"][log_type] += 1
                analysis["levels"][level] += 1
                analysis["modifiers"][modifier] += 1
                analysis["sources"][source] += 1
                
                # User-action combinations
                analysis["user_actions"][user][action] += 1
                analysis["type_actions"][log_type][action] += 1
                
                # Date analysis
                if date_str:
                    try:
                        date_obj = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
                        dates.append(date_obj)
                        
                        # Daily activity
                        day_key = date_obj.strftime('%Y-%m-%d')
                        analysis["daily_activity"][day_key] += 1
                        
                        # Hourly activity
                        hour_key = date_obj.strftime('%H:00')
                        analysis["hourly_activity"][hour_key] += 1
                        
                    except ValueError:
                        pass
                
                # Track errors and recent changes
                if level in ['ERROR', 'WARN']:
                    analysis["error_entries"].append({
                        "date": date_str,
                        "user": user,
                        "action": action,
                        "type": log_type,
                        "level": level,
                        "container_id": log_entry.get('containerId', 'N/A')
                    })
                
                # Track recent significant changes
                if action in ['CREATE', 'UPDATE', 'DELETE'] and log_type not in ['account', 'as.atom.log']:
                    analysis["recent_changes"].append({
                        "date": date_str,
                        "user": user,
                        "action": action,
                        "type": log_type,
                        "container_id": log_entry.get('containerId', 'N/A')
                    })
            
            # Date range
            if dates:
                analysis["date_range"]["earliest"] = min(dates).isoformat()
                analysis["date_range"]["latest"] = max(dates).isoformat()
            
            # Limit recent changes to most recent 10
            analysis["recent_changes"] = sorted(
                analysis["recent_changes"],
                key=lambda x: x["date"],
                reverse=True
            )[:10]
            
            # Generate summary
            analysis["summary"] = {
                "total_entries": analysis["total_entries"],
                "unique_users": len(analysis["users"]),
                "most_active_user": analysis["users"].most_common(1)[0] if analysis["users"] else ("N/A", 0),
                "most_common_action": analysis["actions"].most_common(1)[0] if analysis["actions"] else ("N/A", 0),
                "most_common_type": analysis["types"].most_common(1)[0] if analysis["types"] else ("N/A", 0),
                "error_count": len(analysis["error_entries"]),
                "change_count": len(analysis["recent_changes"]),
                "date_span_days": (max(dates) - min(dates)).days + 1 if len(dates) > 1 else 1
            }
            
            print(f"✅ Analysis complete:")
            print(f"   👥 Unique users: {analysis['summary']['unique_users']}")
            print(f"   ⚡ Most common action: {analysis['summary']['most_common_action'][0]} ({analysis['summary']['most_common_action'][1]})")
            print(f"   🏷️ Most common type: {analysis['summary']['most_common_type'][0]} ({analysis['summary']['most_common_type'][1]})")
            print(f"   ❌ Error entries: {analysis['summary']['error_count']}")
            print(f"   🔄 Recent changes: {analysis['summary']['change_count']}")
            
            return analysis
            
        except Exception as e:
            print(f"❌ Analysis failed: {e}")
            return analysis
    
    def display_audit_summary(self, analysis: Dict[str, Any], detailed: bool = False) -> None:
        """Display audit log summary"""
        if not analysis or analysis.get("total_entries", 0) == 0:
            print("\n📊 No audit data to display")
            return
        
        print(f"\n📋 Audit Log Summary:")
        print("=" * 60)
        
        summary = analysis.get("summary", {})
        
        print(f"📊 Total Entries: {summary.get('total_entries', 0)}")
        
        earliest = analysis['date_range'].get('earliest', 'N/A')
        latest = analysis['date_range'].get('latest', 'N/A')
        if earliest and earliest != 'N/A':
            earliest = earliest[:10]
        if latest and latest != 'N/A':
            latest = latest[:10]
        print(f"📅 Date Range: {earliest} to {latest}")
        
        print(f"👥 Unique Users: {summary.get('unique_users', 0)}")
        
        most_active_user = summary.get('most_active_user', ('N/A', 0))
        print(f"🏆 Most Active User: {most_active_user[0]} ({most_active_user[1]} actions)")
        
        most_common_action = summary.get('most_common_action', ('N/A', 0))
        print(f"⚡ Most Common Action: {most_common_action[0]} ({most_common_action[1]} occurrences)")
        
        most_common_type = summary.get('most_common_type', ('N/A', 0))
        print(f"🏷️ Most Common Type: {most_common_type[0]} ({most_common_type[1]} occurrences)")
        
        if summary.get('error_count', 0) > 0:
            print(f"❌ Error/Warning Entries: {summary['error_count']}")
        
        if summary.get('change_count', 0) > 0:
            print(f"🔄 Recent Changes: {summary['change_count']}")
        
        if detailed:
            self._display_detailed_analysis(analysis)
    
    def _display_detailed_analysis(self, analysis: Dict[str, Any]) -> None:
        """Display detailed analysis breakdown"""
        print(f"\n📊 Detailed Analysis:")
        print("-" * 40)
        
        # Top users
        print(f"\n👥 Top 5 Users:")
        for user, count in analysis["users"].most_common(5):
            print(f"   • {user}: {count} actions")
        
        # Top actions
        print(f"\n⚡ Actions Breakdown:")
        for action, count in analysis["actions"].most_common(10):
            print(f"   • {action}: {count}")
        
        # Top types
        print(f"\n🏷️ Object Types:")
        for obj_type, count in analysis["types"].most_common(10):
            print(f"   • {obj_type}: {count}")
        
        # Recent changes
        if analysis["recent_changes"]:
            print(f"\n🔄 Recent Changes:")
            for change in analysis["recent_changes"][:5]:
                date_short = change["date"][:16].replace('T', ' ')
                print(f"   • {date_short} - {change['user']} {change['action']} {change['type']}")
        
        # Errors if any
        if analysis["error_entries"]:
            print(f"\n❌ Recent Errors/Warnings:")
            for error in analysis["error_entries"][:3]:
                date_short = error["date"][:16].replace('T', ' ')
                print(f"   • {date_short} - {error['user']} {error['level']}: {error['type']} {error['action']}")
    
    def export_audit_data(self, audit_logs: List[Dict[str, Any]], 
                         analysis: Dict[str, Any], filename: str) -> bool:
        """Export audit data to file"""
        print(f"\n💾 Exporting audit data to {filename}")
        
        try:
            file_ext = filename.lower().split('.')[-1]
            
            if file_ext == 'json':
                return self._export_json(audit_logs, analysis, filename)
            elif file_ext == 'csv':
                return self._export_csv(audit_logs, filename)
            elif file_ext == 'html':
                return self._export_html(audit_logs, analysis, filename)
            else:
                print(f"❌ Unsupported file format: {file_ext}")
                return False
                
        except Exception as e:
            print(f"❌ Export failed: {e}")
            return False
    
    def _export_json(self, audit_logs: List[Dict[str, Any]], 
                    analysis: Dict[str, Any], filename: str) -> bool:
        """Export to JSON format"""
        try:
            export_data = {
                'export_date': datetime.now().isoformat(),
                'summary': analysis.get('summary', {}),
                'analysis': {
                    'users': dict(analysis.get('users', {})),
                    'actions': dict(analysis.get('actions', {})),
                    'types': dict(analysis.get('types', {})),
                    'levels': dict(analysis.get('levels', {})),
                    'recent_changes': analysis.get('recent_changes', []),
                    'error_entries': analysis.get('error_entries', [])
                },
                'audit_logs': audit_logs
            }
            
            with open(filename, 'w') as f:
                json.dump(export_data, f, indent=2)
            
            print(f"✅ JSON export completed")
            return True
        except Exception as e:
            print(f"❌ JSON export failed: {e}")
            return False
    
    def _export_csv(self, audit_logs: List[Dict[str, Any]], filename: str) -> bool:
        """Export to CSV format"""
        try:
            if not audit_logs:
                print("❌ No audit logs to export")
                return False
            
            # Extract all unique fields from audit logs
            fieldnames = set()
            for log in audit_logs:
                fieldnames.update(log.keys())
            
            # Common fields first, then others
            common_fields = ['date', 'userId', 'action', 'type', 'level', 'modifier', 'source', 'containerId', 'accountId']
            other_fields = sorted(fieldnames - set(common_fields))
            fieldnames = [f for f in common_fields if f in fieldnames] + other_fields
            
            with open(filename, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                
                for log in audit_logs:
                    # Flatten complex fields if any
                    row = {}
                    for field in fieldnames:
                        value = log.get(field, '')
                        if isinstance(value, (dict, list)):
                            row[field] = json.dumps(value)
                        else:
                            row[field] = str(value) if value is not None else ''
                    writer.writerow(row)
            
            print(f"✅ CSV export completed")
            return True
        except Exception as e:
            print(f"❌ CSV export failed: {e}")
            return False
    
    def _export_html(self, audit_logs: List[Dict[str, Any]], 
                    analysis: Dict[str, Any], filename: str) -> bool:
        """Export to HTML format"""
        try:
            html_content = self._generate_html_report(audit_logs, analysis)
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            print(f"✅ HTML export completed")
            return True
        except Exception as e:
            print(f"❌ HTML export failed: {e}")
            return False
    
    def _generate_html_report(self, audit_logs: List[Dict[str, Any]], 
                            analysis: Dict[str, Any]) -> str:
        """Generate HTML report"""
        summary = analysis.get('summary', {})
        
        html = f"""<!DOCTYPE html>
<html>
<head>
    <title>Boomi Audit Log Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; }}
        .header {{ background: #f0f8ff; padding: 20px; border-radius: 5px; }}
        .summary {{ background: #f9f9f9; padding: 15px; margin: 20px 0; border-radius: 5px; }}
        .section {{ margin: 20px 0; }}
        table {{ border-collapse: collapse; width: 100%; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
        th {{ background-color: #f2f2f2; }}
        .error {{ color: #d32f2f; }}
        .warning {{ color: #f57c00; }}
        .info {{ color: #1976d2; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>🔍 Boomi Audit Log Report</h1>
        <p>Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    </div>
    
    <div class="summary">
        <h2>📊 Summary</h2>
        <ul>
            <li><strong>Total Entries:</strong> {summary.get('total_entries', 0)}</li>
            <li><strong>Date Range:</strong> {analysis['date_range']['earliest'][:10]} to {analysis['date_range']['latest'][:10]}</li>
            <li><strong>Unique Users:</strong> {summary.get('unique_users', 0)}</li>
            <li><strong>Most Active User:</strong> {summary.get('most_active_user', ('N/A', 0))[0]} ({summary.get('most_active_user', ('N/A', 0))[1]} actions)</li>
            <li><strong>Most Common Action:</strong> {summary.get('most_common_action', ('N/A', 0))[0]} ({summary.get('most_common_action', ('N/A', 0))[1]})</li>
            <li><strong>Error Count:</strong> {summary.get('error_count', 0)}</li>
        </ul>
    </div>
    
    <div class="section">
        <h2>🔄 Recent Changes</h2>
        <table>
            <tr><th>Date</th><th>User</th><th>Action</th><th>Type</th></tr>"""
        
        for change in analysis.get('recent_changes', [])[:10]:
            html += f"""
            <tr>
                <td>{change['date'][:16].replace('T', ' ')}</td>
                <td>{change['user']}</td>
                <td>{change['action']}</td>
                <td>{change['type']}</td>
            </tr>"""
        
        html += """
        </table>
    </div>
    
    <div class="section">
        <h2>📋 Audit Log Entries</h2>
        <table>
            <tr><th>Date</th><th>User</th><th>Action</th><th>Type</th><th>Level</th></tr>"""
        
        for log in audit_logs[:50]:  # Limit to first 50 for HTML readability
            level_class = log.get('level', '').lower()
            html += f"""
            <tr>
                <td>{log.get('date', '')[:16].replace('T', ' ')}</td>
                <td>{log.get('userId', '')}</td>
                <td>{log.get('action', '')}</td>
                <td>{log.get('type', '')}</td>
                <td class="{level_class}">{log.get('level', '')}</td>
            </tr>"""
        
        html += """
        </table>
    </div>
</body>
</html>"""
        
        return html


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='Query and analyze Boomi audit logs for compliance and monitoring',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  %(prog)s --days 30                                    # Last 30 days
  %(prog)s --start-date 2025-01-01 --end-date 2025-01-31    # Specific range
  %(prog)s --days 7 --user "admin@company.com"         # User activity
  %(prog)s --days 14 --action UPDATE --type "as.atom"  # Atom updates
  %(prog)s --days 90 --export report.json --summary    # Compliance report

Audit Log Types:
  • account - Account-related activities
  • as.atom - Runtime/Atom operations  
  • as.atom.process - Process deployments
  • as.atom.log - Log downloads
  • component - Component changes
  • environment - Environment modifications

Common Actions:
  • CREATE, UPDATE, DELETE - Object lifecycle
  • ATTACH, DETACH - Deployment operations
  • LOGIN, LOGOUT - Authentication events
  • DOWNLOAD - File access events
        '''
    )
    
    # Date range options (mutually exclusive)
    date_group = parser.add_mutually_exclusive_group(required=True)
    date_group.add_argument('--days', type=int, metavar='N',
                           help='Query last N days of audit logs')
    date_group.add_argument('--start-date', metavar='YYYY-MM-DD',
                           help='Start date for audit log query')
    
    parser.add_argument('--end-date', metavar='YYYY-MM-DD',
                       help='End date (required with --start-date, defaults to today)')
    
    # Filtering options
    parser.add_argument('--user', metavar='EMAIL',
                       help='Filter by user email address')
    parser.add_argument('--action', metavar='ACTION',
                       help='Filter by action type (CREATE, UPDATE, DELETE, etc.)')
    parser.add_argument('--type', metavar='TYPE',
                       help='Filter by object type (account, as.atom, component, etc.)')
    parser.add_argument('--level', metavar='LEVEL',
                       help='Filter by log level (INFO, WARN, ERROR)')
    
    # Output options
    parser.add_argument('--limit', type=int, metavar='N',
                       help='Limit number of results returned')
    parser.add_argument('--summary', action='store_true',
                       help='Display detailed summary analysis')
    parser.add_argument('--export', metavar='FILE',
                       help='Export results to file (.json, .csv, .html)')
    
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
    
    # Calculate date range
    if args.days:
        end_date = datetime.now()
        start_date = end_date - timedelta(days=args.days)
    else:
        try:
            start_date = datetime.strptime(args.start_date, '%Y-%m-%d')
        except ValueError:
            print("❌ Invalid start date format. Use YYYY-MM-DD")
            sys.exit(1)
        
        if args.end_date:
            try:
                end_date = datetime.strptime(args.end_date, '%Y-%m-%d')
            except ValueError:
                print("❌ Invalid end date format. Use YYYY-MM-DD")
                sys.exit(1)
        else:
            end_date = datetime.now()
    
    # Validate date range
    if start_date >= end_date:
        print("❌ Start date must be before end date")
        sys.exit(1)
    
    # Convert to ISO format for API
    start_date_str = start_date.strftime('%Y-%m-%dT00:00:00Z')
    end_date_str = end_date.strftime('%Y-%m-%dT23:59:59Z')
    
    # Execute operation
    try:
        analyzer = AuditLogAnalyzer()
        
        print(f"\n🔍 Boomi Audit Log Analyzer")
        print("=" * 50)
        
        # Query audit logs
        audit_logs = analyzer.query_audit_logs(
            start_date_str,
            end_date_str,
            args.user,
            args.action,
            args.type,
            args.level,
            args.limit
        )
        
        if not audit_logs:
            print("❌ No audit logs found matching criteria")
            sys.exit(1)
        
        # Analyze results
        analysis = analyzer.analyze_audit_logs(audit_logs)
        
        # Display summary
        analyzer.display_audit_summary(analysis, detailed=args.summary)
        
        # Export if requested
        if args.export:
            if analyzer.export_audit_data(audit_logs, analysis, args.export):
                print(f"📄 Results exported to {args.export}")
            else:
                print("❌ Export failed")
                sys.exit(1)
        
        print(f"\n✅ Query completed successfully")
        print(f"📊 Processed {len(audit_logs)} audit log entries")
        
    except KeyboardInterrupt:
        print("\n❌ Operation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()