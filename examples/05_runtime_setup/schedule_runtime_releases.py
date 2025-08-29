#!/usr/bin/env python3
"""
Runtime Release Schedule Management

This example demonstrates how to manage runtime release schedules including:
- Viewing scheduled releases
- Creating new release schedules
- Updating release windows
- Managing maintenance windows
- Coordinating multi-atom releases

The Runtime Release Schedule API helps you plan and coordinate runtime updates
across your Atom infrastructure with minimal disruption.
"""

import os
import sys
import json
import argparse
from typing import Dict, Any, List, Optional
from datetime import datetime, timedelta
from pathlib import Path

# Add the src directory to the path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from boomi import Boomi
from boomi.models import (
    RuntimeReleaseSchedule,
    RuntimeReleaseScheduleQueryConfig,
    RuntimeReleaseScheduleSimpleExpression,
    RuntimeReleaseScheduleSimpleExpressionOperator,
    RuntimeReleaseScheduleQueryConfigQueryFilter
)


class RuntimeReleaseManager:
    """Manages runtime release schedules"""
    
    def __init__(self, verbose: bool = False):
        """Initialize the Runtime Release Manager
        
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
    
    def list_schedules(self, atom_id: Optional[str] = None, limit: int = 100) -> List[RuntimeReleaseSchedule]:
        """List runtime release schedules
        
        Args:
            atom_id: Optional Atom ID to filter schedules
            limit: Maximum number of schedules to return
            
        Returns:
            List of runtime release schedules
        """
        try:
            self._log("Querying runtime release schedules")
            
            # Build query filter if atom_id provided
            if atom_id:
                self._log(f"Filtering by Atom ID: {atom_id}")
                simple_expression = RuntimeReleaseScheduleSimpleExpression(
                    operator=RuntimeReleaseScheduleSimpleExpressionOperator.EQUALS,
                    property="atomId",
                    argument=[atom_id]
                )
                query_filter = RuntimeReleaseScheduleQueryConfigQueryFilter(
                    expression=simple_expression
                )
                query_config = RuntimeReleaseScheduleQueryConfig(query_filter=query_filter)
            else:
                # Query all schedules
                simple_expression = RuntimeReleaseScheduleSimpleExpression(
                    operator=RuntimeReleaseScheduleSimpleExpressionOperator.ISNOTNULL,
                    property="id",
                    argument=[]
                )
                query_filter = RuntimeReleaseScheduleQueryConfigQueryFilter(
                    expression=simple_expression
                )
                query_config = RuntimeReleaseScheduleQueryConfig(query_filter=query_filter)
            
            result = self.sdk.runtime_release_schedule.query_runtime_release_schedule(
                request_body=query_config
            )
            
            if hasattr(result, 'result') and result.result:
                schedules = result.result[:limit]
                self._log(f"Found {len(schedules)} release schedule(s)")
                return schedules
            else:
                self._log("No release schedules found")
                return []
                
        except Exception as e:
            self._log(f"Error listing release schedules: {e}", "ERROR")
            if self.verbose:
                import traceback
                traceback.print_exc()
            return []
    
    def get_schedule(self, schedule_id: str) -> Optional[RuntimeReleaseSchedule]:
        """Get a specific runtime release schedule
        
        Args:
            schedule_id: Schedule ID
            
        Returns:
            RuntimeReleaseSchedule object or None if not found
        """
        try:
            self._log(f"Getting release schedule: {schedule_id}")
            schedule = self.sdk.runtime_release_schedule.get_runtime_release_schedule(id_=schedule_id)
            self._log("Successfully retrieved release schedule")
            return schedule
        except Exception as e:
            self._log(f"Error getting release schedule: {e}", "ERROR")
            return None
    
    def create_schedule(self, atom_id: str, release_version: str, 
                       scheduled_time: datetime, maintenance_window: int = 60,
                       description: str = "") -> Optional[RuntimeReleaseSchedule]:
        """Create a new runtime release schedule
        
        Args:
            atom_id: Atom ID for the release
            release_version: Target release version
            scheduled_time: Scheduled release time
            maintenance_window: Maintenance window in minutes
            description: Optional description
            
        Returns:
            Created RuntimeReleaseSchedule or None if failed
        """
        try:
            self._log(f"Creating release schedule for Atom {atom_id}")
            
            # Create schedule object
            schedule = RuntimeReleaseSchedule(
                atom_id=atom_id,
                release_version=release_version,
                scheduled_date_time=scheduled_time.isoformat(),
                maintenance_window_minutes=maintenance_window,
                description=description or f"Release {release_version} for Atom {atom_id}"
            )
            
            # Create the schedule
            created = self.sdk.runtime_release_schedule.create_runtime_release_schedule(
                request_body=schedule
            )
            
            self._log(f"Successfully created release schedule: {created.id_}")
            return created
            
        except Exception as e:
            self._log(f"Error creating release schedule: {e}", "ERROR")
            if self.verbose:
                import traceback
                traceback.print_exc()
            return None
    
    def update_schedule(self, schedule_id: str, new_time: Optional[datetime] = None,
                       new_window: Optional[int] = None, 
                       new_description: Optional[str] = None) -> bool:
        """Update an existing release schedule
        
        Args:
            schedule_id: Schedule ID to update
            new_time: New scheduled time
            new_window: New maintenance window in minutes
            new_description: New description
            
        Returns:
            True if updated successfully, False otherwise
        """
        try:
            self._log(f"Updating release schedule: {schedule_id}")
            
            # Get existing schedule
            schedule = self.get_schedule(schedule_id)
            if not schedule:
                self._log("Schedule not found", "ERROR")
                return False
            
            # Update fields
            if new_time:
                schedule.scheduled_date_time = new_time.isoformat()
                self._log(f"Updated scheduled time to: {new_time}")
            
            if new_window:
                schedule.maintenance_window_minutes = new_window
                self._log(f"Updated maintenance window to: {new_window} minutes")
            
            if new_description:
                schedule.description = new_description
                self._log("Updated description")
            
            # Update the schedule
            updated = self.sdk.runtime_release_schedule.update_runtime_release_schedule(
                id_=schedule_id,
                request_body=schedule
            )
            
            self._log("Successfully updated release schedule")
            return True
            
        except Exception as e:
            self._log(f"Error updating release schedule: {e}", "ERROR")
            return False
    
    def delete_schedule(self, schedule_id: str) -> bool:
        """Delete a release schedule
        
        Args:
            schedule_id: Schedule ID to delete
            
        Returns:
            True if deleted successfully, False otherwise
        """
        try:
            self._log(f"Deleting release schedule: {schedule_id}")
            self.sdk.runtime_release_schedule.delete_runtime_release_schedule(id_=schedule_id)
            self._log("Successfully deleted release schedule")
            return True
        except Exception as e:
            self._log(f"Error deleting release schedule: {e}", "ERROR")
            return False
    
    def display_schedules(self, schedules: List[RuntimeReleaseSchedule], 
                         format_output: str = "table"):
        """Display release schedules
        
        Args:
            schedules: List of schedules to display
            format_output: Output format (table, json, detailed)
        """
        if not schedules:
            print("No release schedules found")
            return
        
        if format_output == "json":
            schedules_data = []
            for schedule in schedules:
                schedule_dict = {
                    'id': getattr(schedule, 'id_', 'N/A'),
                    'atom_id': getattr(schedule, 'atom_id', 'N/A'),
                    'release_version': getattr(schedule, 'release_version', 'N/A'),
                    'scheduled_time': getattr(schedule, 'scheduled_date_time', 'N/A'),
                    'maintenance_window': getattr(schedule, 'maintenance_window_minutes', 'N/A'),
                    'status': getattr(schedule, 'status', 'N/A'),
                    'description': getattr(schedule, 'description', '')
                }
                schedules_data.append(schedule_dict)
            print(json.dumps(schedules_data, indent=2, default=str))
            
        elif format_output == "detailed":
            for i, schedule in enumerate(schedules, 1):
                print(f"\n{'='*60}")
                print(f"Release Schedule {i}:")
                print(f"{'='*60}")
                print(f"ID: {getattr(schedule, 'id_', 'N/A')}")
                print(f"Atom ID: {getattr(schedule, 'atom_id', 'N/A')}")
                print(f"Release Version: {getattr(schedule, 'release_version', 'N/A')}")
                print(f"Scheduled Time: {getattr(schedule, 'scheduled_date_time', 'N/A')}")
                print(f"Maintenance Window: {getattr(schedule, 'maintenance_window_minutes', 'N/A')} minutes")
                print(f"Status: {getattr(schedule, 'status', 'N/A')}")
                print(f"Description: {getattr(schedule, 'description', '')}")
                
        else:  # table format
            print(f"\n{'='*100}")
            print(f"{'Schedule ID':<20} {'Atom ID':<20} {'Version':<15} {'Scheduled Time':<25} {'Status':<10}")
            print(f"{'='*100}")
            
            for schedule in schedules:
                schedule_id = str(getattr(schedule, 'id_', 'N/A'))[:18]
                atom_id = str(getattr(schedule, 'atom_id', 'N/A'))[:18]
                version = str(getattr(schedule, 'release_version', 'N/A'))[:13]
                scheduled_time = str(getattr(schedule, 'scheduled_date_time', 'N/A'))[:23]
                status = str(getattr(schedule, 'status', 'N/A'))[:8]
                
                print(f"{schedule_id:<20} {atom_id:<20} {version:<15} {scheduled_time:<25} {status:<10}")
            
            print(f"{'='*100}")
            print(f"Total: {len(schedules)} schedule(s)")
    
    def analyze_schedule_conflicts(self, atom_ids: List[str] = None) -> Dict[str, Any]:
        """Analyze potential conflicts in release schedules
        
        Args:
            atom_ids: Optional list of Atom IDs to analyze
            
        Returns:
            Analysis results with conflicts and recommendations
        """
        analysis = {
            'conflicts': [],
            'overlapping_windows': [],
            'recommendations': [],
            'statistics': {}
        }
        
        # Get all schedules
        all_schedules = []
        if atom_ids:
            for atom_id in atom_ids:
                schedules = self.list_schedules(atom_id=atom_id)
                all_schedules.extend(schedules)
        else:
            all_schedules = self.list_schedules()
        
        if not all_schedules:
            analysis['statistics']['total_schedules'] = 0
            return analysis
        
        # Analyze schedules
        analysis['statistics']['total_schedules'] = len(all_schedules)
        analysis['statistics']['unique_atoms'] = len(set(
            getattr(s, 'atom_id', '') for s in all_schedules
        ))
        
        # Check for overlapping maintenance windows
        for i, schedule1 in enumerate(all_schedules):
            try:
                time1 = datetime.fromisoformat(
                    getattr(schedule1, 'scheduled_date_time', '').replace('Z', '+00:00')
                )
                window1 = getattr(schedule1, 'maintenance_window_minutes', 60)
                end1 = time1 + timedelta(minutes=window1)
                
                for schedule2 in all_schedules[i+1:]:
                    time2 = datetime.fromisoformat(
                        getattr(schedule2, 'scheduled_date_time', '').replace('Z', '+00:00')
                    )
                    window2 = getattr(schedule2, 'maintenance_window_minutes', 60)
                    end2 = time2 + timedelta(minutes=window2)
                    
                    # Check for overlap
                    if (time1 <= time2 < end1) or (time2 <= time1 < end2):
                        overlap = {
                            'schedule1_id': getattr(schedule1, 'id_', 'N/A'),
                            'schedule2_id': getattr(schedule2, 'id_', 'N/A'),
                            'atom1': getattr(schedule1, 'atom_id', 'N/A'),
                            'atom2': getattr(schedule2, 'atom_id', 'N/A'),
                            'time1': time1.isoformat(),
                            'time2': time2.isoformat()
                        }
                        analysis['overlapping_windows'].append(overlap)
                        
            except Exception as e:
                self._log(f"Error analyzing schedule: {e}", "WARNING")
        
        # Generate recommendations
        if analysis['overlapping_windows']:
            analysis['recommendations'].append(
                f"Found {len(analysis['overlapping_windows'])} overlapping maintenance windows"
            )
            analysis['recommendations'].append(
                "Consider spacing out releases to avoid resource conflicts"
            )
        
        # Check for releases scheduled too close together
        sorted_schedules = sorted(
            all_schedules,
            key=lambda s: getattr(s, 'scheduled_date_time', '')
        )
        
        for i in range(len(sorted_schedules) - 1):
            try:
                time1 = datetime.fromisoformat(
                    getattr(sorted_schedules[i], 'scheduled_date_time', '').replace('Z', '+00:00')
                )
                time2 = datetime.fromisoformat(
                    getattr(sorted_schedules[i+1], 'scheduled_date_time', '').replace('Z', '+00:00')
                )
                
                time_diff = (time2 - time1).total_seconds() / 3600  # Hours
                
                if time_diff < 2:  # Less than 2 hours apart
                    analysis['conflicts'].append({
                        'type': 'too_close',
                        'schedule1': getattr(sorted_schedules[i], 'id_', 'N/A'),
                        'schedule2': getattr(sorted_schedules[i+1], 'id_', 'N/A'),
                        'time_difference_hours': round(time_diff, 2)
                    })
                    
            except Exception as e:
                self._log(f"Error comparing schedules: {e}", "WARNING")
        
        if analysis['conflicts']:
            analysis['recommendations'].append(
                "Some releases are scheduled very close together"
            )
            analysis['recommendations'].append(
                "Allow at least 2 hours between releases for proper monitoring"
            )
        
        return analysis


def main():
    """Main function to handle command-line arguments"""
    parser = argparse.ArgumentParser(
        description="Manage runtime release schedules",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # List all release schedules
  %(prog)s --list
  
  # List schedules for a specific Atom
  %(prog)s --list --atom-id YOUR_ATOM_ID
  
  # Get specific schedule details
  %(prog)s --get --schedule-id SCHEDULE_ID
  
  # Create a new release schedule
  %(prog)s --create --atom-id ATOM_ID --version 22.4.1 --time "2024-01-15 02:00:00" --window 120
  
  # Update a schedule
  %(prog)s --update --schedule-id SCHEDULE_ID --time "2024-01-16 03:00:00"
  
  # Delete a schedule
  %(prog)s --delete --schedule-id SCHEDULE_ID
  
  # Analyze schedule conflicts
  %(prog)s --analyze
  
  # Output in JSON format
  %(prog)s --list --format json
        """
    )
    
    parser.add_argument('--list', action='store_true',
                       help='List runtime release schedules')
    parser.add_argument('--get', action='store_true',
                       help='Get specific schedule details')
    parser.add_argument('--create', action='store_true',
                       help='Create a new release schedule')
    parser.add_argument('--update', action='store_true',
                       help='Update an existing schedule')
    parser.add_argument('--delete', action='store_true',
                       help='Delete a release schedule')
    parser.add_argument('--analyze', action='store_true',
                       help='Analyze schedule conflicts')
    
    parser.add_argument('--schedule-id', type=str,
                       help='Schedule ID')
    parser.add_argument('--atom-id', type=str,
                       help='Atom ID')
    parser.add_argument('--version', type=str,
                       help='Release version')
    parser.add_argument('--time', type=str,
                       help='Scheduled time (YYYY-MM-DD HH:MM:SS)')
    parser.add_argument('--window', type=int, default=60,
                       help='Maintenance window in minutes (default: 60)')
    parser.add_argument('--description', type=str,
                       help='Schedule description')
    
    parser.add_argument('--format', type=str, choices=['table', 'json', 'detailed'],
                       default='table', help='Output format')
    parser.add_argument('--limit', type=int, default=100,
                       help='Maximum number of results')
    parser.add_argument('--verbose', action='store_true',
                       help='Enable verbose output')
    
    args = parser.parse_args()
    
    # Validate arguments
    if not any([args.list, args.get, args.create, args.update, args.delete, args.analyze]):
        parser.print_help()
        return 1
    
    try:
        manager = RuntimeReleaseManager(verbose=args.verbose)
        
        if args.list:
            schedules = manager.list_schedules(
                atom_id=args.atom_id,
                limit=args.limit
            )
            manager.display_schedules(schedules, args.format)
        
        elif args.get:
            if not args.schedule_id:
                print("Error: --schedule-id is required for --get")
                return 1
            
            schedule = manager.get_schedule(args.schedule_id)
            if schedule:
                manager.display_schedules([schedule], 'detailed')
            else:
                print(f"Schedule not found: {args.schedule_id}")
        
        elif args.create:
            if not all([args.atom_id, args.version, args.time]):
                print("Error: --atom-id, --version, and --time are required for --create")
                return 1
            
            try:
                scheduled_time = datetime.strptime(args.time, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                print("Error: Invalid time format. Use YYYY-MM-DD HH:MM:SS")
                return 1
            
            schedule = manager.create_schedule(
                atom_id=args.atom_id,
                release_version=args.version,
                scheduled_time=scheduled_time,
                maintenance_window=args.window,
                description=args.description or ""
            )
            
            if schedule:
                print(f"✅ Created release schedule: {schedule.id_}")
                manager.display_schedules([schedule], 'detailed')
            else:
                print("❌ Failed to create release schedule")
        
        elif args.update:
            if not args.schedule_id:
                print("Error: --schedule-id is required for --update")
                return 1
            
            new_time = None
            if args.time:
                try:
                    new_time = datetime.strptime(args.time, "%Y-%m-%d %H:%M:%S")
                except ValueError:
                    print("Error: Invalid time format. Use YYYY-MM-DD HH:MM:SS")
                    return 1
            
            success = manager.update_schedule(
                schedule_id=args.schedule_id,
                new_time=new_time,
                new_window=args.window if args.window != 60 else None,
                new_description=args.description
            )
            
            if success:
                print(f"✅ Updated release schedule: {args.schedule_id}")
            else:
                print("❌ Failed to update release schedule")
        
        elif args.delete:
            if not args.schedule_id:
                print("Error: --schedule-id is required for --delete")
                return 1
            
            success = manager.delete_schedule(args.schedule_id)
            if success:
                print(f"✅ Deleted release schedule: {args.schedule_id}")
            else:
                print("❌ Failed to delete release schedule")
        
        elif args.analyze:
            analysis = manager.analyze_schedule_conflicts()
            
            print(f"\n{'='*60}")
            print("Release Schedule Analysis")
            print(f"{'='*60}\n")
            
            print(f"Total Schedules: {analysis['statistics'].get('total_schedules', 0)}")
            print(f"Unique Atoms: {analysis['statistics'].get('unique_atoms', 0)}")
            
            if analysis['overlapping_windows']:
                print(f"\n⚠️ Found {len(analysis['overlapping_windows'])} overlapping maintenance windows:")
                for overlap in analysis['overlapping_windows']:
                    print(f"  - {overlap['atom1']} and {overlap['atom2']} overlap")
            
            if analysis['conflicts']:
                print(f"\n⚠️ Found {len(analysis['conflicts'])} potential conflicts:")
                for conflict in analysis['conflicts']:
                    if conflict['type'] == 'too_close':
                        print(f"  - Schedules {conflict['schedule1']} and {conflict['schedule2']} are only {conflict['time_difference_hours']:.1f} hours apart")
            
            if analysis['recommendations']:
                print("\n📋 Recommendations:")
                for rec in analysis['recommendations']:
                    print(f"  • {rec}")
        
        return 0
        
    except Exception as e:
        print(f"❌ Error: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())