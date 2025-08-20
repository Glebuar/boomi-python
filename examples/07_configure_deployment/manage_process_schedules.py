#!/usr/bin/env python3
"""
Boomi SDK Example: Manage Process Schedules
===========================================

This example demonstrates how to create and manage process execution schedules
in Boomi. It provides comprehensive schedule management with cron-like syntax.

Features:
- List all process schedules across atoms and processes
- Create new schedules with cron-like expressions
- Update existing schedule configurations
- Clear/disable schedules for processes
- Show schedule status and retry configurations
- Convert common schedule patterns to Boomi format

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- Appropriate permissions to manage process schedules
- SCHEDULING privilege required for updates

Usage:
    # List all schedules
    python manage_process_schedules.py --list
    
    # Show schedule for specific process and atom
    python manage_process_schedules.py --get --process-id "process-id" --atom-id "atom-id"
    
    # Create a simple daily schedule
    python manage_process_schedules.py --update --process-id "process-id" --atom-id "atom-id" --schedule "0 9 * * *"
    
    # Create weekday business hours schedule
    python manage_process_schedules.py --update --process-id "process-id" --atom-id "atom-id" --schedule "*/15 9-17 * * 1-5"
    
    # Clear schedule (disable)
    python manage_process_schedules.py --clear --process-id "process-id" --atom-id "atom-id"

Examples:
    python manage_process_schedules.py --list
    python manage_process_schedules.py --get --process-id "186bc687-95b9-43f2-b64a-c86355ac8cf2" --atom-id "2d4d5da4-0dfe-41f8-914b-f5f5120ad90a"
    python manage_process_schedules.py --update --process-id "186bc687-95b9-43f2-b64a-c86355ac8cf2" --atom-id "2d4d5da4-0dfe-41f8-914b-f5f5120ad90a" --schedule "0 */6 * * *"
"""

import os
import sys
import argparse
import json
from datetime import datetime
from typing import List, Dict, Optional, Any

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.boomi import Boomi


class ProcessScheduleManager:
    """Manages process schedule operations"""
    
    def __init__(self):
        """Initialize the Boomi SDK client"""
        self.sdk = Boomi(
            account_id=os.getenv("BOOMI_ACCOUNT"),
            username=os.getenv("BOOMI_USER"),
            password=os.getenv("BOOMI_SECRET"),
            timeout=30000
        )
        print("✅ SDK initialized successfully")
    
    def query_all_schedules(self) -> List[Dict[str, Any]]:
        """Query all process schedules using SDK"""
        print("\n🔍 Querying all process schedules...")
        
        try:
            # Due to SDK model issues, fall back to direct API call for now
            # TODO: Fix ProcessSchedulesQueryConfig model requirements
            import requests
            from requests.auth import HTTPBasicAuth
            
            url = f"https://api.boomi.com/api/rest/v1/{os.getenv('BOOMI_ACCOUNT')}/ProcessSchedules/query"
            auth = HTTPBasicAuth(os.getenv('BOOMI_USER'), os.getenv('BOOMI_SECRET'))
            headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
            
            # Empty query body to get all schedules
            response = requests.post(url, json={}, auth=auth, headers=headers)
            
            if response.status_code == 200:
                result_data = response.json()
                schedules = result_data.get('result', [])
                total_count = result_data.get('numberOfResults', len(schedules))
                
                print(f"✅ Found {total_count} process schedule(s)")
                return schedules
            else:
                print(f"❌ Failed to query schedules: HTTP {response.status_code}")
                return []
                
        except Exception as e:
            print(f"❌ Failed to query process schedules: {e}")
            return []
    
    def get_schedule(self, process_id: str, atom_id: str) -> Optional[Dict[str, Any]]:
        """Get specific process schedule using SDK"""
        print(f"\n🔍 Getting schedule for process {process_id} on atom {atom_id}")
        
        try:
            # The schedule ID is encoded as base64 of "CPS{atom_id}:{process_id}"
            import base64
            schedule_id = base64.b64encode(f"CPS{atom_id}:{process_id}".encode()).decode()
            
            # Use SDK to get schedule
            result = self.sdk.process_schedules.get_process_schedules(id_=schedule_id)
            
            if result and hasattr(result, 'id_'):
                # Convert SDK model to dict for backward compatibility
                schedule_data = {
                    'id': result.id_,
                    'processId': result.process_id,
                    'atomId': result.atom_id,
                    'Schedule': [{
                        'minutes': s.minutes,
                        'hours': s.hours,
                        'daysOfMonth': s.days_of_month,
                        'months': s.months,
                        'daysOfWeek': s.days_of_week
                    } for s in result.schedule] if result.schedule else [],
                    'Retry': {
                        'maxRetry': result.retry.max_retry if result.retry else 5
                    }
                }
                print("✅ Schedule retrieved successfully")
                return schedule_data
            else:
                print("❌ Schedule not found")
                return None
                
        except Exception as e:
            error_msg = str(e)
            if "404" in error_msg or "Not Found" in error_msg:
                print("❌ Schedule not found")
                return None
            else:
                print(f"❌ Failed to get schedule: {e}")
                return None
    
    def update_schedule(self, process_id: str, atom_id: str, cron_expression: str, 
                       max_retry: int = 5) -> bool:
        """Update/create process schedule with cron expression using SDK"""
        print(f"\n🔧 Updating schedule for process {process_id} on atom {atom_id}")
        print(f"   Schedule: {cron_expression}")
        
        try:
            # Parse cron expression (minute hour day_of_month month day_of_week)
            schedule_parts = self._parse_cron_expression(cron_expression)
            if not schedule_parts:
                print("❌ Invalid cron expression format")
                return False
            
            # The schedule ID is encoded
            import base64
            schedule_id = base64.b64encode(f"CPS{atom_id}:{process_id}".encode()).decode()
            
            # Import SDK models
            from src.boomi.models import ProcessSchedules, Schedule, ScheduleRetry
            
            # Create schedule object
            schedule = Schedule(
                minutes=schedule_parts['minutes'],
                hours=schedule_parts['hours'],
                days_of_month=schedule_parts['day_of_month'],
                months=schedule_parts['month'],
                days_of_week=schedule_parts['day_of_week']
            )
            
            # Create retry object
            retry = ScheduleRetry(
                max_retry=max_retry
            )
            
            # Create process schedule object
            process_schedule = ProcessSchedules(
                id_=schedule_id,
                process_id=process_id,
                atom_id=atom_id,
                schedule=[schedule],
                retry=retry
            )
            
            # Update schedule using SDK
            result = self.sdk.process_schedules.update_process_schedules(
                id_=schedule_id, 
                request_body=process_schedule
            )
            
            if result:
                print("✅ Schedule updated successfully")
                
                # Display the created schedule
                schedule_data = {
                    'processId': process_id,
                    'atomId': atom_id,
                    'Schedule': [{
                        'minutes': schedule_parts['minutes'],
                        'hours': schedule_parts['hours'],
                        'daysOfMonth': schedule_parts['day_of_month'],
                        'months': schedule_parts['month'],
                        'daysOfWeek': schedule_parts['day_of_week']
                    }]
                }
                self._display_schedule_details(schedule_data)
                return True
            else:
                print("❌ Failed to update schedule: No result returned")
                return False
                
        except Exception as e:
            print(f"❌ Failed to update schedule: {e}")
            return False
    
    def clear_schedule(self, process_id: str, atom_id: str) -> bool:
        """Clear/disable process schedule using SDK"""
        print(f"\n🗑️ Clearing schedule for process {process_id} on atom {atom_id}")
        
        try:
            # The schedule ID is encoded
            import base64
            schedule_id = base64.b64encode(f"CPS{atom_id}:{process_id}".encode()).decode()
            
            # Import SDK models
            from src.boomi.models import ProcessSchedules, ScheduleRetry
            
            # Create retry object
            retry = ScheduleRetry(
                max_retry=5
            )
            
            # Create empty process schedule object (empty schedule array disables scheduling)
            process_schedule = ProcessSchedules(
                id_=schedule_id,
                process_id=process_id,
                atom_id=atom_id,
                schedule=[],  # Empty schedule array disables scheduling
                retry=retry
            )
            
            # Update schedule using SDK
            result = self.sdk.process_schedules.update_process_schedules(
                id_=schedule_id, 
                request_body=process_schedule
            )
            
            if result:
                print("✅ Schedule cleared successfully")
                return True
            else:
                print("❌ Failed to clear schedule: No result returned")
                return False
                
        except Exception as e:
            print(f"❌ Failed to clear schedule: {e}")
            return False
    
    def _parse_cron_expression(self, cron_expr: str) -> Optional[Dict[str, str]]:
        """Parse cron expression into Boomi schedule format"""
        # Standard cron: minute hour day_of_month month day_of_week
        parts = cron_expr.strip().split()
        
        if len(parts) != 5:
            print(f"❌ Cron expression must have 5 parts: minute hour day_of_month month day_of_week")
            print(f"   Got: {cron_expr}")
            return None
        
        return {
            'minutes': parts[0],
            'hours': parts[1], 
            'day_of_month': parts[2],
            'month': parts[3],
            'day_of_week': parts[4]
        }
    
    def display_schedules_summary(self, schedules: List[Dict[str, Any]]) -> None:
        """Display summary of all schedules"""
        if not schedules:
            print("📊 No schedules to display")
            return
        
        print("\n📊 Process Schedules Summary:")
        print("=" * 60)
        
        # Count schedules by status
        active_count = 0
        inactive_count = 0
        process_counts = {}
        atom_counts = {}
        
        for schedule in schedules:
            has_schedules = schedule.get('Schedule', [])
            if has_schedules:
                active_count += 1
            else:
                inactive_count += 1
            
            # Count by process
            process_id = schedule.get('processId', 'Unknown')
            process_counts[process_id] = process_counts.get(process_id, 0) + 1
            
            # Count by atom
            atom_id = schedule.get('atomId', 'Unknown')
            atom_counts[atom_id] = atom_counts.get(atom_id, 0) + 1
        
        print(f"📦 Total Schedule Objects: {len(schedules)}")
        print(f"✅ Active (with schedules): {active_count}")
        print(f"⏸️ Inactive (empty): {inactive_count}")
        
        print(f"\n🤖 Top Atoms:")
        sorted_atoms = sorted(atom_counts.items(), key=lambda x: x[1], reverse=True)
        for atom_id, count in sorted_atoms[:5]:
            # Truncate long atom IDs for display
            display_atom = atom_id[:20] + "..." if len(atom_id) > 23 else atom_id
            print(f"   • {display_atom}: {count}")
        
        print(f"\n🔧 Top Processes:")
        sorted_processes = sorted(process_counts.items(), key=lambda x: x[1], reverse=True)
        for process_id, count in sorted_processes[:5]:
            # Truncate long process IDs for display
            display_process = process_id[:20] + "..." if len(process_id) > 23 else process_id
            print(f"   • {display_process}: {count}")
    
    def display_schedules_detailed(self, schedules: List[Dict[str, Any]], limit: int = 20) -> None:
        """Display detailed schedule information"""
        if not schedules:
            print("📋 No schedules to display")
            return
        
        print(f"\n📋 Detailed Schedule List (showing {min(limit, len(schedules))} of {len(schedules)}):")
        print("=" * 120)
        
        for i, schedule in enumerate(schedules[:limit], 1):
            schedule_id = schedule.get('id', 'N/A')
            process_id = schedule.get('processId', 'N/A')
            atom_id = schedule.get('atomId', 'N/A')
            schedules_list = schedule.get('Schedule', [])
            retry_config = schedule.get('Retry', {})
            max_retry = retry_config.get('maxRetry', 'N/A')
            
            # Status
            status = "ACTIVE" if schedules_list else "INACTIVE"
            status_icon = "✅" if schedules_list else "⏸️"
            
            print(f"{i:2}. {status_icon} Schedule: {status}")
            print(f"     🆔 Schedule ID: {schedule_id}")
            print(f"     🔧 Process ID: {process_id}")
            print(f"     🤖 Atom ID: {atom_id}")
            print(f"     🔄 Max Retry: {max_retry}")
            
            if schedules_list:
                print(f"     📅 Active Schedules ({len(schedules_list)}):")
                for j, sched in enumerate(schedules_list, 1):
                    minutes = sched.get('minutes', '*')
                    hours = sched.get('hours', '*')
                    days_month = sched.get('daysOfMonth', '*')
                    months = sched.get('months', '*')
                    days_week = sched.get('daysOfWeek', '*')
                    
                    cron_expr = f"{minutes} {hours} {days_month} {months} {days_week}"
                    description = self._describe_schedule(sched)
                    
                    print(f"        {j}. {cron_expr}")
                    print(f"           📝 {description}")
            else:
                print(f"     📅 No active schedules")
            
            print()
        
        if len(schedules) > limit:
            print(f"... and {len(schedules) - limit} more schedules")
            print(f"💡 Use --limit {len(schedules)} to see all results")
    
    def _display_schedule_details(self, schedule: Dict[str, Any]) -> None:
        """Display details of a single schedule"""
        print("\n📋 Schedule Details:")
        print("=" * 50)
        
        process_id = schedule.get('processId', 'N/A')
        atom_id = schedule.get('atomId', 'N/A')
        schedules_list = schedule.get('Schedule', [])
        
        print(f"🔧 Process ID: {process_id}")
        print(f"🤖 Atom ID: {atom_id}")
        
        if schedules_list:
            print(f"📅 Active Schedules:")
            for i, sched in enumerate(schedules_list, 1):
                minutes = sched.get('minutes', '*')
                hours = sched.get('hours', '*')
                days_month = sched.get('daysOfMonth', '*')
                months = sched.get('months', '*')
                days_week = sched.get('daysOfWeek', '*')
                
                cron_expr = f"{minutes} {hours} {days_month} {months} {days_week}"
                description = self._describe_schedule(sched)
                
                print(f"   {i}. {cron_expr}")
                print(f"      📝 {description}")
        else:
            print("📅 No active schedules")
    
    def _describe_schedule(self, schedule: Dict[str, Any]) -> str:
        """Generate human-readable description of schedule"""
        minutes = schedule.get('minutes', '*')
        hours = schedule.get('hours', '*')
        days_month = schedule.get('daysOfMonth', '*')
        months = schedule.get('months', '*')
        days_week = schedule.get('daysOfWeek', '*')
        
        descriptions = []
        
        # Frequency descriptions
        if minutes == '0':
            descriptions.append("At the top of the hour")
        elif '/' in minutes:
            interval = minutes.split('/')[-1]
            descriptions.append(f"Every {interval} minutes")
        elif minutes == '*':
            descriptions.append("Every minute")
        else:
            descriptions.append(f"At minute {minutes}")
        
        # Hour descriptions
        if hours != '*':
            if '-' in hours:
                start, end = hours.split('-')
                descriptions.append(f"between {start}:00 and {end}:00")
            elif '/' in hours:
                interval = hours.split('/')[-1]
                descriptions.append(f"every {interval} hours")
            else:
                descriptions.append(f"at {hours}:00")
        
        # Day descriptions
        if days_week != '*':
            if days_week == '1-5':
                descriptions.append("on weekdays")
            elif days_week == '6,7' or days_week == '0,6':
                descriptions.append("on weekends")
            else:
                descriptions.append(f"on days {days_week}")
        
        if not descriptions:
            return "Complex schedule pattern"
        
        return ", ".join(descriptions)
    
    def show_schedule_examples(self) -> None:
        """Show common schedule examples"""
        print("\n📋 Common Schedule Examples:")
        print("=" * 60)
        
        examples = [
            ("0 9 * * *", "Daily at 9:00 AM"),
            ("*/15 * * * *", "Every 15 minutes"),
            ("0 */6 * * *", "Every 6 hours"),
            ("0 9 * * 1-5", "Weekdays at 9:00 AM"),
            ("*/30 9-17 * * 1-5", "Every 30 minutes during business hours (9-5, weekdays)"),
            ("0 2 * * 0", "Sundays at 2:00 AM"),
            ("0 0 1 * *", "First day of every month at midnight"),
            ("0 9,13,17 * * 1-5", "Weekdays at 9 AM, 1 PM, and 5 PM")
        ]
        
        print("Cron Expression Format: minute hour day_of_month month day_of_week")
        print()
        
        for cron_expr, description in examples:
            print(f"📅 {cron_expr:20} - {description}")
        
        print(f"\n💡 Special Characters:")
        print(f"   *     - Any value")
        print(f"   */n   - Every n units") 
        print(f"   n-m   - Range from n to m")
        print(f"   n,m   - List of values n and m")
        
        print(f"\n🗓️ Day of Week Values:")
        print(f"   1 = Monday, 2 = Tuesday, ..., 7 = Sunday")
        print(f"   (Some systems use 0 = Sunday, 1 = Monday)")


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='Manage Boomi process execution schedules',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  %(prog)s --list                                     # List all schedules
  %(prog)s --get --process-id "proc-123" --atom-id "atom-456"  # Get specific schedule
  %(prog)s --update --process-id "proc-123" --atom-id "atom-456" --schedule "0 9 * * *"  # Daily at 9 AM
  %(prog)s --update --process-id "proc-123" --atom-id "atom-456" --schedule "*/15 9-17 * * 1-5"  # Business hours
  %(prog)s --clear --process-id "proc-123" --atom-id "atom-456"  # Disable schedule

Schedule Format (Cron):
  minute hour day_of_month month day_of_week
  
Common Patterns:
  • "0 9 * * *"        - Daily at 9:00 AM
  • "*/15 * * * *"     - Every 15 minutes  
  • "0 */6 * * *"      - Every 6 hours
  • "0 9 * * 1-5"      - Weekdays at 9:00 AM
  • "*/30 9-17 * * 1-5" - Every 30 min during business hours
        '''
    )
    
    # Action flags
    parser.add_argument('--list', action='store_true',
                       help='List all process schedules')
    parser.add_argument('--get', action='store_true',
                       help='Get specific process schedule')
    parser.add_argument('--update', action='store_true',
                       help='Update/create process schedule')
    parser.add_argument('--clear', action='store_true',
                       help='Clear/disable process schedule')
    parser.add_argument('--examples', action='store_true',
                       help='Show common schedule examples')
    
    # Parameters
    parser.add_argument('--process-id', metavar='ID',
                       help='Process ID for schedule operations')
    parser.add_argument('--atom-id', metavar='ID', 
                       help='Atom ID for schedule operations')
    parser.add_argument('--schedule', metavar='CRON',
                       help='Cron expression for schedule (e.g., "0 9 * * *")')
    parser.add_argument('--max-retry', type=int, default=5, metavar='N',
                       help='Maximum retry attempts (default: 5)')
    
    # Display options
    parser.add_argument('--summary', action='store_true',
                       help='Show summary statistics only')
    parser.add_argument('--limit', type=int, default=20, metavar='N',
                       help='Maximum number of schedules to display (default: 20)')
    
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
        manager = ProcessScheduleManager()
        
        # Show examples
        if args.examples:
            manager.show_schedule_examples()
            return
        
        # Operations requiring process and atom IDs
        if args.get or args.update or args.clear:
            if not args.process_id or not args.atom_id:
                print("❌ --process-id and --atom-id are required for this operation")
                sys.exit(1)
        
        # Update operation
        if args.update:
            if not args.schedule:
                print("❌ --schedule is required for update operation")
                print("💡 Example: --schedule '0 9 * * *'")
                sys.exit(1)
            
            success = manager.update_schedule(
                args.process_id, 
                args.atom_id, 
                args.schedule,
                args.max_retry
            )
            
            if success:
                print(f"\n✅ Schedule updated successfully")
            else:
                sys.exit(1)
            return
        
        # Clear operation
        if args.clear:
            success = manager.clear_schedule(args.process_id, args.atom_id)
            
            if success:
                print(f"\n✅ Schedule cleared successfully")
            else:
                sys.exit(1)
            return
        
        # Get operation
        if args.get:
            schedule = manager.get_schedule(args.process_id, args.atom_id)
            
            if schedule:
                manager._display_schedule_details(schedule)
            else:
                print("❌ Schedule not found")
                sys.exit(1)
            return
        
        # List operation (default)
        print(f"\n🚀 Boomi Process Schedules Manager")
        print("=" * 50)
        
        schedules = manager.query_all_schedules()
        
        if not schedules:
            print("❌ No process schedules found")
            return
        
        # Display results
        if args.summary:
            manager.display_schedules_summary(schedules)
        else:
            manager.display_schedules_detailed(schedules, args.limit)
            if not args.summary:
                print(f"\n💡 Use --examples to see common schedule patterns")
                print(f"💡 Use --summary to see statistics only")
        
        print(f"\n✅ Query completed successfully")
        print(f"📊 Total schedules: {len(schedules)}")
        
    except KeyboardInterrupt:
        print("\n❌ Operation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()