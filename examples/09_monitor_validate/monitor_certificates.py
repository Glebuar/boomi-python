#!/usr/bin/env python3
"""
Certificate Monitoring

This example demonstrates how to monitor SSL/TLS certificates including:
- Checking certificate expiration dates
- Finding expired or soon-to-expire certificates
- Certificate validation and compliance checks
- Alert generation for certificate issues
- Certificate renewal tracking

The Certificate Monitoring APIs help you maintain security by tracking
certificate status across your Boomi infrastructure.
"""

import os
import sys
import json
import argparse
from typing import Dict, Any, List, Optional, Tuple
from datetime import datetime, timedelta
from pathlib import Path

# Add the src directory to the path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from boomi import Boomi
from boomi.models import (
    DeployedExpiredCertificateQueryConfig,
    DeployedExpiredCertificateSimpleExpression,
    DeployedExpiredCertificateSimpleExpressionOperator,
    DeployedExpiredCertificateSimpleExpressionProperty,
    DeployedExpiredCertificateQueryConfigQueryFilter
)


class CertificateMonitor:
    """Monitors SSL/TLS certificates for expiration and compliance"""
    
    def __init__(self, verbose: bool = False):
        """Initialize the Certificate Monitor
        
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
    
    def get_expired_certificates(self, days_ahead: int = 0) -> List[Dict[str, Any]]:
        """Get expired or soon-to-expire certificates
        
        Args:
            days_ahead: Number of days to look ahead for expiration
            
        Returns:
            List of expired/expiring certificates
        """
        try:
            self._log(f"Querying for certificates expiring within {days_ahead} days")
            
            # Calculate expiry date threshold
            expiry_threshold = datetime.now() + timedelta(days=days_ahead)
            
            # Query for expired certificates
            simple_expression = DeployedExpiredCertificateSimpleExpression(
                operator=DeployedExpiredCertificateSimpleExpressionOperator.LESS_THAN_OR_EQUAL,
                property=DeployedExpiredCertificateSimpleExpressionProperty.EXPIRY_DATE,
                argument=[expiry_threshold.isoformat()]
            )
            
            query_filter = DeployedExpiredCertificateQueryConfigQueryFilter(
                expression=simple_expression
            )
            query_config = DeployedExpiredCertificateQueryConfig(
                query_filter=query_filter
            )
            
            result = self.sdk.deployed_expired_certificate.query_deployed_expired_certificate(
                request_body=query_config
            )
            
            certificates = []
            if hasattr(result, 'result') and result.result:
                for cert in result.result:
                    cert_info = {
                        'id': getattr(cert, 'id_', 'N/A'),
                        'name': getattr(cert, 'name', 'N/A'),
                        'subject': getattr(cert, 'subject', 'N/A'),
                        'issuer': getattr(cert, 'issuer', 'N/A'),
                        'expiry_date': getattr(cert, 'expiry_date', 'N/A'),
                        'days_until_expiry': self._calculate_days_until_expiry(
                            getattr(cert, 'expiry_date', None)
                        ),
                        'environment': getattr(cert, 'environment_id', 'N/A'),
                        'atom': getattr(cert, 'atom_id', 'N/A')
                    }
                    certificates.append(cert_info)
                
                self._log(f"Found {len(certificates)} certificate(s)")
            else:
                self._log("No expired/expiring certificates found")
            
            return certificates
            
        except Exception as e:
            self._log(f"Error getting expired certificates: {e}", "ERROR")
            if self.verbose:
                import traceback
                traceback.print_exc()
            return []
    
    def _calculate_days_until_expiry(self, expiry_date: Optional[str]) -> int:
        """Calculate days until certificate expiry
        
        Args:
            expiry_date: Certificate expiry date string
            
        Returns:
            Number of days until expiry (negative if already expired)
        """
        if not expiry_date:
            return -999
        
        try:
            expiry = datetime.fromisoformat(expiry_date.replace('Z', '+00:00'))
            delta = expiry - datetime.now()
            return delta.days
        except:
            return -999
    
    def get_all_certificates(self, limit: int = 100) -> List[Dict[str, Any]]:
        """Get all deployed certificates
        
        Args:
            limit: Maximum number of certificates to return
            
        Returns:
            List of all certificates
        """
        try:
            self._log("Querying all deployed certificates")
            
            # Query without filter to get all
            simple_expression = DeployedExpiredCertificateSimpleExpression(
                operator=DeployedExpiredCertificateSimpleExpressionOperator.ISNOTNULL,
                property=DeployedExpiredCertificateSimpleExpressionProperty.ID,
                argument=[]
            )
            
            query_filter = DeployedExpiredCertificateQueryConfigQueryFilter(
                expression=simple_expression
            )
            query_config = DeployedExpiredCertificateQueryConfig(
                query_filter=query_filter
            )
            
            result = self.sdk.deployed_expired_certificate.query_deployed_expired_certificate(
                request_body=query_config
            )
            
            certificates = []
            if hasattr(result, 'result') and result.result:
                for cert in result.result[:limit]:
                    cert_info = {
                        'id': getattr(cert, 'id_', 'N/A'),
                        'name': getattr(cert, 'name', 'N/A'),
                        'subject': getattr(cert, 'subject', 'N/A'),
                        'issuer': getattr(cert, 'issuer', 'N/A'),
                        'expiry_date': getattr(cert, 'expiry_date', 'N/A'),
                        'days_until_expiry': self._calculate_days_until_expiry(
                            getattr(cert, 'expiry_date', None)
                        ),
                        'environment': getattr(cert, 'environment_id', 'N/A'),
                        'atom': getattr(cert, 'atom_id', 'N/A'),
                        'type': getattr(cert, 'type', 'N/A'),
                        'thumbprint': getattr(cert, 'thumbprint', 'N/A')
                    }
                    certificates.append(cert_info)
                
                self._log(f"Found {len(certificates)} certificate(s)")
            
            return certificates
            
        except Exception as e:
            self._log(f"Error getting certificates: {e}", "ERROR")
            return []
    
    def analyze_certificate_health(self, warning_days: int = 30, 
                                  critical_days: int = 7) -> Dict[str, Any]:
        """Analyze overall certificate health
        
        Args:
            warning_days: Days threshold for warning status
            critical_days: Days threshold for critical status
            
        Returns:
            Certificate health analysis
        """
        analysis = {
            'total_certificates': 0,
            'expired': [],
            'critical': [],
            'warning': [],
            'healthy': [],
            'health_score': 100,
            'recommendations': []
        }
        
        try:
            # Get all certificates
            certificates = self.get_all_certificates()
            analysis['total_certificates'] = len(certificates)
            
            if not certificates:
                analysis['recommendations'].append("No certificates found to monitor")
                return analysis
            
            # Categorize certificates by health status
            for cert in certificates:
                days_until_expiry = cert['days_until_expiry']
                
                if days_until_expiry < 0:
                    analysis['expired'].append(cert)
                elif days_until_expiry <= critical_days:
                    analysis['critical'].append(cert)
                elif days_until_expiry <= warning_days:
                    analysis['warning'].append(cert)
                else:
                    analysis['healthy'].append(cert)
            
            # Calculate health score
            expired_weight = 30
            critical_weight = 20
            warning_weight = 10
            
            penalties = (
                len(analysis['expired']) * expired_weight +
                len(analysis['critical']) * critical_weight +
                len(analysis['warning']) * warning_weight
            )
            
            analysis['health_score'] = max(0, 100 - penalties)
            
            # Generate recommendations
            if analysis['expired']:
                analysis['recommendations'].append(
                    f"URGENT: {len(analysis['expired'])} certificate(s) have expired and need immediate renewal"
                )
            
            if analysis['critical']:
                analysis['recommendations'].append(
                    f"CRITICAL: {len(analysis['critical'])} certificate(s) expiring within {critical_days} days"
                )
            
            if analysis['warning']:
                analysis['recommendations'].append(
                    f"WARNING: {len(analysis['warning'])} certificate(s) expiring within {warning_days} days"
                )
            
            # General recommendations
            if analysis['health_score'] < 50:
                analysis['recommendations'].append(
                    "Certificate health is poor. Implement automated renewal process."
                )
            elif analysis['health_score'] < 80:
                analysis['recommendations'].append(
                    "Consider setting up automated alerts for certificate expiration"
                )
            
            self._log(f"Certificate health score: {analysis['health_score']}")
            
        except Exception as e:
            analysis['error'] = str(e)
            self._log(f"Error analyzing certificate health: {e}", "ERROR")
        
        return analysis
    
    def generate_renewal_report(self, days_ahead: int = 90) -> Dict[str, Any]:
        """Generate certificate renewal report
        
        Args:
            days_ahead: Days to look ahead for renewals
            
        Returns:
            Renewal report dictionary
        """
        report = {
            'report_date': datetime.now().isoformat(),
            'days_ahead': days_ahead,
            'certificates_needing_renewal': [],
            'renewal_timeline': {},
            'summary': {}
        }
        
        try:
            # Get certificates expiring within the period
            certificates = self.get_expired_certificates(days_ahead=days_ahead)
            
            # Sort by expiry date
            certificates.sort(key=lambda x: x['days_until_expiry'])
            
            report['certificates_needing_renewal'] = certificates
            
            # Group by renewal timeline
            for cert in certificates:
                days = cert['days_until_expiry']
                
                if days < 0:
                    timeline = 'Expired'
                elif days <= 7:
                    timeline = 'This Week'
                elif days <= 30:
                    timeline = 'This Month'
                elif days <= 90:
                    timeline = 'Next 3 Months'
                else:
                    timeline = 'Future'
                
                if timeline not in report['renewal_timeline']:
                    report['renewal_timeline'][timeline] = []
                
                report['renewal_timeline'][timeline].append(cert['name'])
            
            # Generate summary
            report['summary'] = {
                'total_renewals_needed': len(certificates),
                'expired': len([c for c in certificates if c['days_until_expiry'] < 0]),
                'urgent': len([c for c in certificates if 0 <= c['days_until_expiry'] <= 7]),
                'upcoming': len([c for c in certificates if 7 < c['days_until_expiry'] <= 30])
            }
            
            self._log(f"Generated renewal report for {len(certificates)} certificate(s)")
            
        except Exception as e:
            report['error'] = str(e)
            self._log(f"Error generating renewal report: {e}", "ERROR")
        
        return report
    
    def display_certificates(self, certificates: List[Dict[str, Any]], 
                            format_output: str = "table"):
        """Display certificates
        
        Args:
            certificates: List of certificates to display
            format_output: Output format (table, json, detailed)
        """
        if not certificates:
            print("No certificates found")
            return
        
        if format_output == "json":
            print(json.dumps(certificates, indent=2, default=str))
            
        elif format_output == "detailed":
            for i, cert in enumerate(certificates, 1):
                status_icon = self._get_status_icon(cert['days_until_expiry'])
                
                print(f"\n{'='*60}")
                print(f"Certificate {i}: {status_icon}")
                print(f"{'='*60}")
                for key, value in cert.items():
                    if key == 'days_until_expiry':
                        if value < 0:
                            print(f"{key}: {abs(value)} days EXPIRED ❌")
                        else:
                            print(f"{key}: {value} days")
                    else:
                        print(f"{key}: {value}")
                        
        else:  # table format
            print(f"\n{'='*100}")
            print(f"{'Status':<8} {'Name':<30} {'Days':<10} {'Expiry Date':<20} {'Environment':<20}")
            print(f"{'='*100}")
            
            for cert in certificates:
                status = self._get_status_icon(cert['days_until_expiry'])
                name = str(cert['name'])[:28]
                days = cert['days_until_expiry']
                days_str = f"{days}d" if days >= 0 else f"EXP {abs(days)}d"
                expiry = str(cert['expiry_date'])[:18]
                env = str(cert['environment'])[:18]
                
                print(f"{status:<8} {name:<30} {days_str:<10} {expiry:<20} {env:<20}")
            
            print(f"{'='*100}")
            print(f"Total: {len(certificates)} certificate(s)")
    
    def _get_status_icon(self, days_until_expiry: int) -> str:
        """Get status icon based on days until expiry
        
        Args:
            days_until_expiry: Days until certificate expires
            
        Returns:
            Status icon string
        """
        if days_until_expiry < 0:
            return "❌ EXP"
        elif days_until_expiry <= 7:
            return "🔴 CRIT"
        elif days_until_expiry <= 30:
            return "🟡 WARN"
        else:
            return "🟢 OK"


def main():
    """Main function to handle command-line arguments"""
    parser = argparse.ArgumentParser(
        description="Monitor SSL/TLS certificates",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # List all certificates
  %(prog)s --list
  
  # Check for expired certificates
  %(prog)s --expired
  
  # Check certificates expiring in next 30 days
  %(prog)s --expiring --days 30
  
  # Analyze certificate health
  %(prog)s --analyze
  
  # Generate renewal report
  %(prog)s --renewal-report --days 90
  
  # Output in JSON format
  %(prog)s --list --format json
  
  # Detailed certificate information
  %(prog)s --expiring --days 7 --format detailed
        """
    )
    
    parser.add_argument('--list', action='store_true',
                       help='List all certificates')
    parser.add_argument('--expired', action='store_true',
                       help='Show only expired certificates')
    parser.add_argument('--expiring', action='store_true',
                       help='Show expiring certificates')
    parser.add_argument('--analyze', action='store_true',
                       help='Analyze certificate health')
    parser.add_argument('--renewal-report', action='store_true',
                       help='Generate renewal report')
    
    parser.add_argument('--days', type=int, default=30,
                       help='Days ahead to check for expiration')
    parser.add_argument('--warning-days', type=int, default=30,
                       help='Days threshold for warning status')
    parser.add_argument('--critical-days', type=int, default=7,
                       help='Days threshold for critical status')
    
    parser.add_argument('--format', type=str, choices=['table', 'json', 'detailed'],
                       default='table', help='Output format')
    parser.add_argument('--limit', type=int, default=100,
                       help='Maximum number of results')
    parser.add_argument('--verbose', action='store_true',
                       help='Enable verbose output')
    
    args = parser.parse_args()
    
    # Validate arguments
    if not any([args.list, args.expired, args.expiring, args.analyze, args.renewal_report]):
        parser.print_help()
        return 1
    
    try:
        monitor = CertificateMonitor(verbose=args.verbose)
        
        if args.list:
            certificates = monitor.get_all_certificates(limit=args.limit)
            monitor.display_certificates(certificates, args.format)
        
        elif args.expired:
            certificates = monitor.get_expired_certificates(days_ahead=0)
            expired_only = [c for c in certificates if c['days_until_expiry'] < 0]
            
            print(f"\n{'='*60}")
            print("Expired Certificates")
            print(f"{'='*60}")
            
            if expired_only:
                monitor.display_certificates(expired_only, args.format)
            else:
                print("✅ No expired certificates found")
        
        elif args.expiring:
            certificates = monitor.get_expired_certificates(days_ahead=args.days)
            
            print(f"\n{'='*60}")
            print(f"Certificates Expiring Within {args.days} Days")
            print(f"{'='*60}")
            
            monitor.display_certificates(certificates, args.format)
        
        elif args.analyze:
            analysis = monitor.analyze_certificate_health(
                warning_days=args.warning_days,
                critical_days=args.critical_days
            )
            
            print(f"\n{'='*60}")
            print("Certificate Health Analysis")
            print(f"{'='*60}\n")
            
            # Display health score with color
            score = analysis['health_score']
            if score >= 80:
                score_icon = "🟢"
            elif score >= 50:
                score_icon = "🟡"
            else:
                score_icon = "🔴"
            
            print(f"Health Score: {score_icon} {score}/100")
            print(f"Total Certificates: {analysis['total_certificates']}")
            
            print("\n📊 Status Distribution:")
            print(f"  ❌ Expired: {len(analysis['expired'])}")
            print(f"  🔴 Critical: {len(analysis['critical'])}")
            print(f"  🟡 Warning: {len(analysis['warning'])}")
            print(f"  🟢 Healthy: {len(analysis['healthy'])}")
            
            if analysis['recommendations']:
                print("\n💡 Recommendations:")
                for rec in analysis['recommendations']:
                    print(f"  • {rec}")
        
        elif args.renewal_report:
            report = monitor.generate_renewal_report(days_ahead=args.days)
            
            print(f"\n{'='*60}")
            print("Certificate Renewal Report")
            print(f"{'='*60}")
            print(f"Report Date: {report['report_date']}")
            print(f"Looking Ahead: {report['days_ahead']} days\n")
            
            summary = report['summary']
            print("📊 Summary:")
            print(f"  Total Renewals Needed: {summary['total_renewals_needed']}")
            print(f"  Expired: {summary['expired']}")
            print(f"  Urgent (≤7 days): {summary['urgent']}")
            print(f"  Upcoming (≤30 days): {summary['upcoming']}")
            
            if report['renewal_timeline']:
                print("\n📅 Renewal Timeline:")
                for timeline, certs in report['renewal_timeline'].items():
                    print(f"\n  {timeline}:")
                    for cert_name in certs:
                        print(f"    • {cert_name}")
        
        return 0
        
    except Exception as e:
        print(f"❌ Error: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())