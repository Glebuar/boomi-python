#!/usr/bin/env python3
"""
Secrets Rotation Management

This example demonstrates how to manage secrets rotation including:
- Refreshing secrets from secrets manager
- Rotating API keys and credentials
- Updating connection credentials
- Auditing secret usage
- Implementing rotation schedules

The Secrets Manager APIs help maintain security by automating
credential rotation and secrets management.
"""

import os
import sys
import json
import argparse
import hashlib
from typing import Dict, Any, List, Optional, Tuple
from datetime import datetime, timedelta
from pathlib import Path

# Add the src directory to the path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from boomi import Boomi
from boomi.models import (
    SecretsManagerRefreshRequest,
    SecretsManagerRefreshResponse,
    Provider
)


class SecretsRotationManager:
    """Manages secrets rotation and credential management"""
    
    def __init__(self, verbose: bool = False):
        """Initialize the Secrets Rotation Manager
        
        Args:
            verbose: Enable verbose output
        """
        self.verbose = verbose
        self.sdk = self._initialize_sdk()
        self.rotation_policies = {
            'api_keys': {'days': 90, 'critical': 7},
            'passwords': {'days': 60, 'critical': 5},
            'certificates': {'days': 365, 'critical': 30},
            'tokens': {'days': 30, 'critical': 3}
        }
        
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
    
    def refresh_secrets(self, secret_type: Optional[str] = None,
                       force: bool = False,
                       provider: str = "AWS") -> Dict[str, Any]:
        """Refresh secrets from secrets manager

        Args:
            secret_type: Optional type of secrets to refresh (not used by API)
            force: Force refresh even if not due (not used by API)
            provider: Secrets manager provider - "AWS" or "AZURE" (required by API)

        Returns:
            Refresh operation result
        """
        result = {
            'success': False,
            'message': '',
            'refreshed_secrets': [],
            'failed_secrets': [],
            'timestamp': datetime.now().isoformat()
        }
        
        try:
            self._log(f"Initiating secrets refresh{' for ' + secret_type if secret_type else ''}")
            
            # Create refresh request with provider
            # The API requires 'provider' parameter (AWS or AZURE) to succeed
            # The secret_type and force parameters are not supported by the API
            provider_enum = Provider.AWS if provider.upper() == "AWS" else Provider.AZURE
            refresh_request = SecretsManagerRefreshRequest(provider=provider_enum)

            self._log(f"Using {provider.upper()} Secrets Manager")

            if force:
                self._log("Note: Force refresh flag not supported by API, all secrets will be refreshed")
            
            # Execute refresh
            response = self.sdk.refresh_secrets_manager.refresh_secrets_manager(
                request_body=refresh_request
            )
            
            # Process response
            if response:
                result['success'] = True

                # Extract message from response
                if hasattr(response, 'message'):
                    result['message'] = response.message
                    self._log(f"API response: {response.message}")
                else:
                    result['message'] = "Secrets refreshed successfully"

                # Extract refreshed secrets info if available
                if hasattr(response, 'refreshed_secrets'):
                    result['refreshed_secrets'] = response.refreshed_secrets

                self._log(f"Successfully refreshed {len(result['refreshed_secrets'])} secret(s)")
            else:
                result['message'] = "No response from secrets manager"
                self._log(result['message'], "WARNING")
            
        except Exception as e:
            result['message'] = f"Failed to refresh secrets: {str(e)}"
            result['error'] = str(e)
            self._log(result['message'], "ERROR")
            if self.verbose:
                import traceback
                traceback.print_exc()
        
        return result
    
    def check_rotation_status(self, secret_name: str, 
                             secret_type: str = "api_keys") -> Dict[str, Any]:
        """Check if a secret needs rotation
        
        Args:
            secret_name: Name of the secret
            secret_type: Type of secret
            
        Returns:
            Rotation status information
        """
        status = {
            'secret_name': secret_name,
            'secret_type': secret_type,
            'needs_rotation': False,
            'days_until_rotation': 0,
            'status': 'CURRENT',
            'last_rotated': None,
            'next_rotation': None,
            'recommendation': ''
        }
        
        try:
            # Get rotation policy
            policy = self.rotation_policies.get(secret_type, {'days': 90, 'critical': 7})
            
            # Simulate checking last rotation date (would query actual system)
            # For demo purposes, we'll use a hash-based simulation
            hash_value = int(hashlib.md5(secret_name.encode()).hexdigest()[:8], 16)
            days_since_rotation = hash_value % policy['days']
            
            last_rotated = datetime.now() - timedelta(days=days_since_rotation)
            next_rotation = last_rotated + timedelta(days=policy['days'])
            days_until = (next_rotation - datetime.now()).days
            
            status['last_rotated'] = last_rotated.isoformat()
            status['next_rotation'] = next_rotation.isoformat()
            status['days_until_rotation'] = days_until
            
            # Determine status
            if days_until <= 0:
                status['needs_rotation'] = True
                status['status'] = 'EXPIRED'
                status['recommendation'] = "Immediate rotation required"
            elif days_until <= policy['critical']:
                status['needs_rotation'] = True
                status['status'] = 'CRITICAL'
                status['recommendation'] = f"Rotate within {days_until} days"
            elif days_until <= policy['days'] * 0.2:  # Within 20% of expiry
                status['status'] = 'WARNING'
                status['recommendation'] = "Schedule rotation soon"
            else:
                status['status'] = 'CURRENT'
                status['recommendation'] = "No action needed"
            
            self._log(f"Secret {secret_name}: {status['status']} "
                     f"(expires in {days_until} days)")
            
        except Exception as e:
            status['error'] = str(e)
            self._log(f"Error checking rotation status: {e}", "ERROR")
        
        return status
    
    def rotate_secret(self, secret_name: str, secret_type: str = "api_keys",
                     dry_run: bool = False) -> Dict[str, Any]:
        """Rotate a specific secret
        
        Args:
            secret_name: Name of the secret to rotate
            secret_type: Type of secret
            dry_run: Simulate rotation without making changes
            
        Returns:
            Rotation result
        """
        result = {
            'secret_name': secret_name,
            'secret_type': secret_type,
            'success': False,
            'message': '',
            'old_version': None,
            'new_version': None,
            'rotation_time': datetime.now().isoformat()
        }
        
        try:
            self._log(f"Initiating rotation for {secret_name} ({secret_type})")
            
            # Check current status
            status = self.check_rotation_status(secret_name, secret_type)
            
            if not status['needs_rotation'] and not dry_run:
                result['message'] = f"Secret does not need rotation (expires in {status['days_until_rotation']} days)"
                self._log(result['message'])
                return result
            
            if dry_run:
                result['success'] = True
                result['message'] = f"Dry run: Would rotate {secret_name}"
                result['old_version'] = "v1.0.0"
                result['new_version'] = "v2.0.0"
                self._log(result['message'])
                return result
            
            # Perform actual rotation (simplified)
            self._log(f"Rotating {secret_name}...")
            
            # Step 1: Generate new secret
            new_secret = self._generate_new_secret(secret_type)
            
            # Step 2: Update in secrets manager
            refresh_result = self.refresh_secrets(secret_type=secret_type, force=True)
            
            if refresh_result['success']:
                result['success'] = True
                result['message'] = f"Successfully rotated {secret_name}"
                result['old_version'] = "previous"
                result['new_version'] = "current"
                self._log(result['message'])
            else:
                result['message'] = f"Rotation failed: {refresh_result['message']}"
                self._log(result['message'], "ERROR")
            
        except Exception as e:
            result['message'] = f"Rotation failed: {str(e)}"
            result['error'] = str(e)
            self._log(result['message'], "ERROR")
        
        return result
    
    def _generate_new_secret(self, secret_type: str) -> str:
        """Generate a new secret value
        
        Args:
            secret_type: Type of secret to generate
            
        Returns:
            New secret value
        """
        import secrets
        import string
        
        if secret_type == "api_keys":
            # Generate API key format
            return f"sk_{secrets.token_hex(32)}"
        elif secret_type == "passwords":
            # Generate strong password
            alphabet = string.ascii_letters + string.digits + string.punctuation
            return ''.join(secrets.choice(alphabet) for _ in range(24))
        elif secret_type == "tokens":
            # Generate bearer token
            return secrets.token_urlsafe(32)
        else:
            # Default to hex token
            return secrets.token_hex(32)
    
    def audit_secrets(self) -> Dict[str, Any]:
        """Audit all secrets and generate compliance report
        
        Returns:
            Audit results
        """
        audit = {
            'audit_time': datetime.now().isoformat(),
            'total_secrets': 0,
            'expired': [],
            'critical': [],
            'warning': [],
            'current': [],
            'compliance_score': 100,
            'recommendations': []
        }
        
        try:
            self._log("Starting secrets audit")
            
            # Simulate auditing different secret types
            secret_inventory = [
                ('api_key_prod', 'api_keys'),
                ('api_key_dev', 'api_keys'),
                ('db_password_main', 'passwords'),
                ('db_password_replica', 'passwords'),
                ('auth_token_service', 'tokens'),
                ('ssl_cert_main', 'certificates')
            ]
            
            audit['total_secrets'] = len(secret_inventory)
            
            for secret_name, secret_type in secret_inventory:
                status = self.check_rotation_status(secret_name, secret_type)
                
                if status['status'] == 'EXPIRED':
                    audit['expired'].append({
                        'name': secret_name,
                        'type': secret_type,
                        'days_expired': abs(status['days_until_rotation'])
                    })
                elif status['status'] == 'CRITICAL':
                    audit['critical'].append({
                        'name': secret_name,
                        'type': secret_type,
                        'days_remaining': status['days_until_rotation']
                    })
                elif status['status'] == 'WARNING':
                    audit['warning'].append({
                        'name': secret_name,
                        'type': secret_type,
                        'days_remaining': status['days_until_rotation']
                    })
                else:
                    audit['current'].append({
                        'name': secret_name,
                        'type': secret_type,
                        'days_remaining': status['days_until_rotation']
                    })
            
            # Calculate compliance score
            expired_penalty = len(audit['expired']) * 30
            critical_penalty = len(audit['critical']) * 15
            warning_penalty = len(audit['warning']) * 5
            
            audit['compliance_score'] = max(
                0, 100 - expired_penalty - critical_penalty - warning_penalty
            )
            
            # Generate recommendations
            if audit['expired']:
                audit['recommendations'].append(
                    f"URGENT: {len(audit['expired'])} secret(s) have expired and need immediate rotation"
                )
            
            if audit['critical']:
                audit['recommendations'].append(
                    f"CRITICAL: {len(audit['critical'])} secret(s) expiring soon"
                )
            
            if audit['compliance_score'] < 70:
                audit['recommendations'].append(
                    "Implement automated secret rotation to improve compliance"
                )
            
            self._log(f"Audit complete: compliance score {audit['compliance_score']}")
            
        except Exception as e:
            audit['error'] = str(e)
            self._log(f"Error during audit: {e}", "ERROR")
        
        return audit
    
    def create_rotation_schedule(self) -> List[Dict[str, Any]]:
        """Create a rotation schedule for all secrets
        
        Returns:
            Rotation schedule
        """
        schedule = []
        
        try:
            # Get all secrets and their rotation dates
            secret_inventory = [
                ('api_key_prod', 'api_keys'),
                ('api_key_dev', 'api_keys'),
                ('db_password_main', 'passwords'),
                ('db_password_replica', 'passwords'),
                ('auth_token_service', 'tokens'),
                ('ssl_cert_main', 'certificates')
            ]
            
            for secret_name, secret_type in secret_inventory:
                status = self.check_rotation_status(secret_name, secret_type)
                
                schedule_entry = {
                    'secret_name': secret_name,
                    'secret_type': secret_type,
                    'rotation_date': status['next_rotation'],
                    'days_until': status['days_until_rotation'],
                    'priority': 'LOW'
                }
                
                # Set priority
                if status['status'] == 'EXPIRED':
                    schedule_entry['priority'] = 'IMMEDIATE'
                elif status['status'] == 'CRITICAL':
                    schedule_entry['priority'] = 'HIGH'
                elif status['status'] == 'WARNING':
                    schedule_entry['priority'] = 'MEDIUM'
                
                schedule.append(schedule_entry)
            
            # Sort by priority and date
            priority_order = {'IMMEDIATE': 0, 'HIGH': 1, 'MEDIUM': 2, 'LOW': 3}
            schedule.sort(key=lambda x: (priority_order[x['priority']], x['days_until']))
            
            self._log(f"Created rotation schedule for {len(schedule)} secret(s)")
            
        except Exception as e:
            self._log(f"Error creating schedule: {e}", "ERROR")
        
        return schedule


def main():
    """Main function to handle command-line arguments"""
    parser = argparse.ArgumentParser(
        description="Manage secrets rotation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Refresh all secrets from AWS Secrets Manager
  %(prog)s --refresh

  # Refresh from Azure Secrets Manager
  %(prog)s --refresh --provider AZURE

  # Force refresh (note: all secrets are always refreshed)
  %(prog)s --refresh --force
  
  # Check rotation status
  %(prog)s --check-status --name api_key_prod --type api_keys
  
  # Rotate a specific secret
  %(prog)s --rotate --name api_key_prod --type api_keys
  
  # Dry run rotation
  %(prog)s --rotate --name api_key_prod --dry-run
  
  # Audit all secrets
  %(prog)s --audit
  
  # Generate rotation schedule
  %(prog)s --schedule
        """
    )
    
    parser.add_argument('--refresh', action='store_true',
                       help='Refresh secrets from secrets manager')
    parser.add_argument('--check-status', action='store_true',
                       help='Check rotation status of a secret')
    parser.add_argument('--rotate', action='store_true',
                       help='Rotate a specific secret')
    parser.add_argument('--audit', action='store_true',
                       help='Audit all secrets')
    parser.add_argument('--schedule', action='store_true',
                       help='Generate rotation schedule')
    
    parser.add_argument('--name', type=str,
                       help='Secret name')
    parser.add_argument('--type', type=str,
                       choices=['api_keys', 'passwords', 'certificates', 'tokens'],
                       default='api_keys',
                       help='Secret type')
    parser.add_argument('--provider', type=str,
                       choices=['AWS', 'AZURE'],
                       default='AWS',
                       help='Secrets manager provider (required for --refresh, default: AWS)')

    parser.add_argument('--force', action='store_true',
                       help='Force operation')
    parser.add_argument('--dry-run', action='store_true',
                       help='Simulate operation without making changes')
    parser.add_argument('--verbose', action='store_true',
                       help='Enable verbose output')
    
    args = parser.parse_args()
    
    # Validate arguments
    if not any([args.refresh, args.check_status, args.rotate, args.audit, args.schedule]):
        parser.print_help()
        return 1
    
    try:
        manager = SecretsRotationManager(verbose=args.verbose)
        
        if args.refresh:
            result = manager.refresh_secrets(
                secret_type=args.type if args.type else None,
                force=args.force,
                provider=args.provider
            )
            
            if result['success']:
                print(f"✅ {result['message']}")
                if result['refreshed_secrets']:
                    print(f"   Refreshed: {len(result['refreshed_secrets'])} secret(s)")
            else:
                print(f"❌ {result['message']}")
        
        elif args.check_status:
            if not args.name:
                print("Error: --name is required for status check")
                return 1
            
            status = manager.check_rotation_status(args.name, args.type)
            
            print(f"\n{'='*60}")
            print(f"Secret Status: {args.name}")
            print(f"{'='*60}")
            
            status_icon = {
                'CURRENT': '🟢',
                'WARNING': '🟡',
                'CRITICAL': '🔴',
                'EXPIRED': '❌'
            }.get(status['status'], '⚫')
            
            print(f"Status: {status_icon} {status['status']}")
            print(f"Type: {status['secret_type']}")
            print(f"Last Rotated: {status['last_rotated']}")
            print(f"Next Rotation: {status['next_rotation']}")
            print(f"Days Until Rotation: {status['days_until_rotation']}")
            print(f"Recommendation: {status['recommendation']}")
        
        elif args.rotate:
            if not args.name:
                print("Error: --name is required for rotation")
                return 1
            
            result = manager.rotate_secret(
                secret_name=args.name,
                secret_type=args.type,
                dry_run=args.dry_run
            )
            
            if result['success']:
                print(f"✅ {result['message']}")
                if result['old_version'] and result['new_version']:
                    print(f"   Version: {result['old_version']} → {result['new_version']}")
            else:
                print(f"❌ {result['message']}")
        
        elif args.audit:
            audit = manager.audit_secrets()
            
            print(f"\n{'='*60}")
            print("Secrets Compliance Audit")
            print(f"{'='*60}\n")
            
            # Display compliance score with color
            score = audit['compliance_score']
            if score >= 80:
                score_icon = "🟢"
            elif score >= 60:
                score_icon = "🟡"
            else:
                score_icon = "🔴"
            
            print(f"Compliance Score: {score_icon} {score}/100")
            print(f"Total Secrets: {audit['total_secrets']}")
            
            print("\n📊 Status Distribution:")
            print(f"  ❌ Expired: {len(audit['expired'])}")
            print(f"  🔴 Critical: {len(audit['critical'])}")
            print(f"  🟡 Warning: {len(audit['warning'])}")
            print(f"  🟢 Current: {len(audit['current'])}")
            
            if audit['expired']:
                print("\n❌ Expired Secrets:")
                for secret in audit['expired']:
                    print(f"  • {secret['name']} ({secret['type']}) - "
                          f"expired {secret['days_expired']} days ago")
            
            if audit['critical']:
                print("\n🔴 Critical Secrets:")
                for secret in audit['critical']:
                    print(f"  • {secret['name']} ({secret['type']}) - "
                          f"expires in {secret['days_remaining']} days")
            
            if audit['recommendations']:
                print("\n💡 Recommendations:")
                for rec in audit['recommendations']:
                    print(f"  • {rec}")
        
        elif args.schedule:
            schedule = manager.create_rotation_schedule()
            
            print(f"\n{'='*60}")
            print("Secret Rotation Schedule")
            print(f"{'='*60}")
            print(f"{'Priority':<12} {'Secret':<25} {'Type':<15} {'Days':<8} {'Date':<12}")
            print("-" * 60)
            
            for entry in schedule:
                priority = entry['priority']
                name = entry['secret_name'][:23]
                secret_type = entry['secret_type'][:13]
                days = entry['days_until']
                date = entry['rotation_date'][:10]
                
                # Priority icon
                priority_icon = {
                    'IMMEDIATE': '🔴',
                    'HIGH': '🟡',
                    'MEDIUM': '🟠',
                    'LOW': '🟢'
                }.get(priority, '')
                
                print(f"{priority_icon} {priority:<10} {name:<25} {secret_type:<15} "
                      f"{days:<8} {date:<12}")
        
        return 0
        
    except Exception as e:
        print(f"❌ Error: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())