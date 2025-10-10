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
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/src")

from boomi import Boomi
from boomi.models import ProcessSchedulesQueryConfig


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
            # Create empty query config to get all schedules
            query_config = ProcessSchedulesQueryConfig()
            
            # Query using SDK
            result = self.sdk.process_schedules.query_process_schedules(
                request_body=query_config
            )
            
            if hasattr(result, 'result') and result.result:
                schedules = result.result
                total_count = result.number_of_results if hasattr(result, 'number_of_results') else len(schedules)
                
                print(f"✅ Found {total_count} process schedule(s)")
                # Return the schedule objects directly
                return schedules
            else:
                print("✅ No process schedules found")
                return []
                
        except Exception as e:
            error_msg = str(e)
            if "403" in error_msg:
                print("❌ Access denied (403). This may occur if:")
                print("   - Your account lacks permission for query operations")
                print("   - The API endpoint is restricted for your account type")
            else:
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
                        'minutes': getattr(s, 'minutes', '*'),
                        'hours': getattr(s, 'hours', '*'),
                        'daysOfMonth': getattr(s, 'days_of_month', '*'),
                        'months': getattr(s, 'months', '*'),
                        'daysOfWeek': getattr(s, 'days_of_week', '*')
                    } for s in result.schedule] if hasattr(result, 'schedule') and result.schedule else [],
                    'Retry': {
                        'maxRetry': result.retry.max_retry if hasattr(result, 'retry') and result.retry else 5
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
            elif "403" in error_msg:
                print("❌ Access denied (403). This may occur if:")
                print("   - The Process ID or Atom ID doesn't exist")
                print("   - Your account lacks permission for schedule operations")
                print("   - The atom is not properly configured")
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
            from boomi.models import ProcessSchedules, Schedule, ScheduleRetry
            
            # Create schedule object
            schedule = Schedule(
                minutes=schedule_parts['minutes'],
                hours=schedule_parts['hours'],
                days_of_month=schedule_parts['day_of_month'],
                months=schedule_parts['month'],
                days_of_week=schedule_parts['day_of_week'],
                years='*'  # Years field is required by the API
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
            error_msg = str(e)
            if "403" in error_msg:
                print("❌ Access denied (403). This may occur if:")
                print("   - The Process ID or Atom ID doesn't exist")
                print("   - Your account lacks permission for schedule operations")
                print("   - The atom is not properly configured")
            else:
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
            from boomi.models import ProcessSchedules, ScheduleRetry
            
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
            error_msg = str(e)
            if "403" in error_msg:
                print("❌ Access denied (403). This may occur if:")
                print("   - The Process ID or Atom ID doesn't exist")
                print("   - Your account lacks permission for schedule operations")
                print("   - The atom is not properly configured")
            else:
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
            has_schedules = getattr(schedule, 'schedule', [])
            if has_schedules:
                active_count += 1
            else:
                inactive_count += 1
            
            # Count by process
            process_id = getattr(schedule, 'process_id', 'Unknown')
            process_counts[process_id] = process_counts.get(process_id, 0) + 1
            
            # Count by atom
            atom_id = getattr(schedule, 'atom_id', 'Unknown')
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
            # Handle SDK model objects
            if hasattr(schedule, 'id_'):
                # It's an SDK model object
                schedule_id = getattr(schedule, 'id_', 'N/A')
                process_id = getattr(schedule, 'process_id', 'N/A')
                atom_id = getattr(schedule, 'atom_id', 'N/A')
                schedules_list = getattr(schedule, 'schedule', [])
                retry_obj = getattr(schedule, 'retry', None)
                max_retry = retry_obj.max_retry if retry_obj else 'N/A'
            else:
                # It's a dictionary
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
                    # Handle SDK model objects for schedule items
                    if hasattr(sched, 'minutes'):
                        minutes = getattr(sched, 'minutes', '*')
                        hours = getattr(sched, 'hours', '*')
                        days_month = getattr(sched, 'days_of_month', '*')
                        months = getattr(sched, 'months', '*')
                        days_week = getattr(sched, 'days_of_week', '*')
                    else:
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
    
    def _describe_schedule(self, schedule) -> str:
        """Generate human-readable description of schedule"""
        # Handle both SDK model objects and dictionaries
        if hasattr(schedule, 'minutes'):
            # SDK model object
            minutes = getattr(schedule, 'minutes', '*')
            hours = getattr(schedule, 'hours', '*')
            days_month = getattr(schedule, 'days_of_month', '*')
            months = getattr(schedule, 'months', '*')
            days_week = getattr(schedule, 'days_of_week', '*')
        else:
            # Dictionary
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

    # DEFAULT IDs FOR TESTING - REPLACE WITH YOUR ACTUAL IDs
    # These are example IDs that may work in a test environment
    # You MUST replace these with your actual Process and Atom IDs
    # To find your IDs: Use the Boomi UI or query APIs to get real Process and Atom IDs
    DEFAULT_PROCESS_ID = "11111111-1111-1111-1111-111111111111"  # Replace with your Process ID
    DEFAULT_ATOM_ID = "22222222-2222-2222-2222-222222222222"  # Replace with your Atom/Runtime ID

    # IMPORTANT: ProcessSchedules API Requirements (from OpenAPI spec):
    #
    # PRIVILEGES REQUIRED:
    # - "Runtime Management" privilege (not just "Runtime Management Read Access")
    # - "Scheduling" privilege
    #
    # PROCESS REQUIREMENTS:
    # - Process must be deployed to an Atom/Runtime
    # - Process CANNOT be a listener process (returns 400 Bad Request)
    # - Process and Atom IDs must exist in your account
    #
    # COMMON 403 FORBIDDEN CAUSES:
    # - Insufficient API privileges (especially common in sandbox accounts)
    # - Process or Atom IDs don't exist
    # - Account type restrictions (trial/sandbox accounts often have limited API access)
    #
    # HOW TO GET REAL IDs:
    # 1. Log into Boomi Platform UI
    # 2. Navigate to "Manage > Atom Management" for Atom IDs
    # 3. Navigate to "Design > Processes" for Process IDs
    # 4. Check "Deploy > Deployed Processes" to see active deployments
    # 5. IDs are visible in URL or properties panel

    parser = argparse.ArgumentParser(
        description='Manage Boomi process execution schedules',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  %(prog)s --list                                     # List all schedules
  %(prog)s --get --process-id "proc-123" --atom-id "atom-456"  # Get specific schedule
  %(prog)s --get  # Uses default IDs
  %(prog)s --update --process-id "proc-123" --atom-id "atom-456" --schedule "0 9 * * *"  # Daily at 9 AM
  %(prog)s --update --schedule "0 9 * * *"  # Uses default IDs
  %(prog)s --update --process-id "proc-123" --atom-id "atom-456" --schedule "*/15 9-17 * * 1-5"  # Business hours
  %(prog)s --clear --process-id "proc-123" --atom-id "atom-456"  # Disable schedule
  %(prog)s --clear  # Uses default IDs

OpenAPI Example IDs (for reference):
  Process ID: 789abcde-f012-3456-789a-bcdef0123456
  Atom ID:    3456789a-bcde-f0123-4567-89abcdef012

Note:
- Default IDs are provided for testing but MUST be replaced with your actual IDs
- Get real IDs from Boomi Platform UI (see comments above for instructions)

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
            if not args.process_id:
                print(f"ℹ️ No --process-id provided, using default: {DEFAULT_PROCESS_ID}")
                print("⚠️ WARNING: Replace DEFAULT_PROCESS_ID in the script with your actual Process ID")
                args.process_id = DEFAULT_PROCESS_ID

            if not args.atom_id:
                print(f"ℹ️ No --atom-id provided, using default: {DEFAULT_ATOM_ID}")
                print("⚠️ WARNING: Replace DEFAULT_ATOM_ID in the script with your actual Atom ID")
                args.atom_id = DEFAULT_ATOM_ID
        
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