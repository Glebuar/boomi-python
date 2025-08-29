#!/usr/bin/env python3
"""
Atom Security Policies Management

This example demonstrates how to manage Atom security policies including:
- Viewing current security policies
- Updating security configurations
- Managing TLS/SSL settings
- Configuring authentication methods
- Setting up security constraints

The Atom Security Policies API allows you to configure security settings
for Atom runtime environments to ensure secure communications and access control.
"""

import os
import sys
import json
import argparse
import time
from typing import Dict, Any, List, Optional, Tuple
from datetime import datetime, timedelta
from pathlib import Path

# Add the src directory to the path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from boomi import Boomi
from boomi.models import (
    AtomSecurityPolicies,
    AsyncToken
)


class SecurityPolicyManager:
    """Manages Atom security policies and configurations"""
    
    def __init__(self, verbose: bool = False):
        """Initialize the Security Policy Manager
        
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
    
    def get_security_policies(self, atom_id: str, timeout: int = 30) -> Optional[Dict[str, Any]]:
        """Get security policies for an Atom (async operation)
        
        Args:
            atom_id: Atom ID
            timeout: Timeout in seconds for async operation
            
        Returns:
            Security policies dictionary or None if failed
        """
        try:
            self._log(f"Initiating async request for Atom security policies: {atom_id}")
            
            # Initiate async request
            token_result = self.sdk.atom_security_policies.async_get_atom_security_policies(id_=atom_id)
            
            if not hasattr(token_result, 'async_token') or not token_result.async_token:
                self._log("Failed to get async token", "ERROR")
                return None
                
            token = token_result.async_token.token
            self._log(f"Got async token: {token}")
            
            # Poll for results
            start_time = time.time()
            poll_interval = 2
            
            while time.time() - start_time < timeout:
                time.sleep(poll_interval)
                
                try:
                    self._log(f"Polling for results (attempt {int((time.time() - start_time) / poll_interval)})")
                    response = self.sdk.atom_security_policies.async_token_atom_security_policies(token=token)
                    
                    if response:
                        self._log("Successfully retrieved security policies")
                        return self._parse_security_policies(response)
                    
                except Exception as e:
                    # Still waiting for results
                    if "not ready" in str(e).lower() or "202" in str(e):
                        self._log("Results not ready yet, continuing to poll...")
                        continue
                    else:
                        self._log(f"Error polling for results: {e}", "ERROR")
                        return None
            
            self._log(f"Timeout waiting for security policies after {timeout} seconds", "ERROR")
            return None
            
        except Exception as e:
            self._log(f"Error getting security policies: {e}", "ERROR")
            return None
    
    def _parse_security_policies(self, response: Any) -> Dict[str, Any]:
        """Parse security policies response
        
        Args:
            response: API response object
            
        Returns:
            Parsed security policies dictionary
        """
        policies = {
            'tls_settings': {},
            'authentication': {},
            'security_constraints': {},
            'certificate_info': {},
            'raw_data': {}
        }
        
        try:
            # Handle different response formats
            if hasattr(response, '__dict__'):
                raw_data = response.__dict__
            elif isinstance(response, dict):
                raw_data = response
            else:
                raw_data = {'response': str(response)}
            
            policies['raw_data'] = raw_data
            
            # Extract TLS/SSL settings
            for key in ['tls_version', 'tlsVersion', 'ssl_enabled', 'sslEnabled']:
                if key in raw_data:
                    policies['tls_settings']['version'] = raw_data[key]
                    break
            
            # Extract authentication settings
            for key in ['auth_type', 'authType', 'authentication_method', 'authenticationMethod']:
                if key in raw_data:
                    policies['authentication']['method'] = raw_data[key]
                    break
            
            # Extract certificate information
            for key in ['certificates', 'cert_info', 'certInfo']:
                if key in raw_data:
                    policies['certificate_info'] = raw_data[key]
                    break
            
            # Extract security constraints
            for key in ['security_constraints', 'securityConstraints', 'constraints']:
                if key in raw_data:
                    policies['security_constraints'] = raw_data[key]
                    break
                    
        except Exception as e:
            self._log(f"Error parsing security policies: {e}", "WARNING")
        
        return policies
    
    def display_security_policies(self, atom_id: str, format_output: str = "detailed"):
        """Display security policies for an Atom
        
        Args:
            atom_id: Atom ID
            format_output: Output format (detailed, json, summary)
        """
        print(f"\n{'='*60}")
        print(f"Atom Security Policies: {atom_id}")
        print(f"{'='*60}\n")
        
        policies = self.get_security_policies(atom_id)
        
        if not policies:
            print("❌ Failed to retrieve security policies")
            return
        
        if format_output == "json":
            print(json.dumps(policies, indent=2, default=str))
        elif format_output == "summary":
            self._display_summary(policies)
        else:
            self._display_detailed(policies)
    
    def _display_summary(self, policies: Dict[str, Any]):
        """Display summary of security policies"""
        print("📋 Security Policy Summary:")
        print("-" * 40)
        
        # TLS Settings
        if policies['tls_settings']:
            print(f"🔒 TLS: {policies['tls_settings'].get('version', 'Not configured')}")
        
        # Authentication
        if policies['authentication']:
            print(f"🔑 Auth: {policies['authentication'].get('method', 'Not configured')}")
        
        # Certificates
        if policies['certificate_info']:
            if isinstance(policies['certificate_info'], list):
                print(f"📜 Certificates: {len(policies['certificate_info'])} configured")
            else:
                print(f"📜 Certificates: Configured")
        
        # Constraints
        if policies['security_constraints']:
            if isinstance(policies['security_constraints'], list):
                print(f"🛡️ Constraints: {len(policies['security_constraints'])} rules")
            else:
                print(f"🛡️ Constraints: Configured")
    
    def _display_detailed(self, policies: Dict[str, Any]):
        """Display detailed security policies"""
        print("📋 Detailed Security Policies:")
        print("-" * 40)
        
        # TLS/SSL Settings
        print("\n🔒 TLS/SSL Settings:")
        if policies['tls_settings']:
            for key, value in policies['tls_settings'].items():
                print(f"  - {key}: {value}")
        else:
            print("  No TLS settings configured")
        
        # Authentication
        print("\n🔑 Authentication Settings:")
        if policies['authentication']:
            for key, value in policies['authentication'].items():
                print(f"  - {key}: {value}")
        else:
            print("  No authentication settings configured")
        
        # Certificate Information
        print("\n📜 Certificate Information:")
        if policies['certificate_info']:
            if isinstance(policies['certificate_info'], list):
                for i, cert in enumerate(policies['certificate_info'], 1):
                    print(f"  Certificate {i}:")
                    if isinstance(cert, dict):
                        for key, value in cert.items():
                            print(f"    - {key}: {value}")
                    else:
                        print(f"    {cert}")
            else:
                print(f"  {policies['certificate_info']}")
        else:
            print("  No certificates configured")
        
        # Security Constraints
        print("\n🛡️ Security Constraints:")
        if policies['security_constraints']:
            if isinstance(policies['security_constraints'], list):
                for i, constraint in enumerate(policies['security_constraints'], 1):
                    print(f"  Constraint {i}:")
                    if isinstance(constraint, dict):
                        for key, value in constraint.items():
                            print(f"    - {key}: {value}")
                    else:
                        print(f"    {constraint}")
            else:
                print(f"  {policies['security_constraints']}")
        else:
            print("  No security constraints configured")
        
        # Raw Data (if verbose)
        if self.verbose and policies['raw_data']:
            print("\n📊 Raw Response Data:")
            print(json.dumps(policies['raw_data'], indent=2, default=str))
    
    def analyze_security_posture(self, atom_id: str) -> Dict[str, Any]:
        """Analyze security posture and provide recommendations
        
        Args:
            atom_id: Atom ID
            
        Returns:
            Security analysis results
        """
        analysis = {
            'score': 0,
            'max_score': 100,
            'findings': [],
            'recommendations': [],
            'risk_level': 'UNKNOWN'
        }
        
        policies = self.get_security_policies(atom_id)
        
        if not policies:
            analysis['findings'].append("Unable to retrieve security policies")
            analysis['recommendations'].append("Verify Atom connectivity and permissions")
            return analysis
        
        # Check TLS configuration
        if policies['tls_settings']:
            tls_version = policies['tls_settings'].get('version', '')
            if 'TLS1.2' in str(tls_version) or 'TLS1.3' in str(tls_version):
                analysis['score'] += 25
                analysis['findings'].append(f"✅ Strong TLS version: {tls_version}")
            elif tls_version:
                analysis['score'] += 10
                analysis['findings'].append(f"⚠️ Outdated TLS version: {tls_version}")
                analysis['recommendations'].append("Upgrade to TLS 1.2 or higher")
            else:
                analysis['findings'].append("❌ No TLS configuration found")
                analysis['recommendations'].append("Enable TLS encryption for secure communications")
        
        # Check authentication
        if policies['authentication']:
            auth_method = policies['authentication'].get('method', '')
            if auth_method:
                analysis['score'] += 25
                analysis['findings'].append(f"✅ Authentication configured: {auth_method}")
            else:
                analysis['findings'].append("⚠️ No authentication method specified")
                analysis['recommendations'].append("Configure authentication method")
        else:
            analysis['findings'].append("❌ No authentication configuration found")
            analysis['recommendations'].append("Enable authentication for access control")
        
        # Check certificates
        if policies['certificate_info']:
            if isinstance(policies['certificate_info'], list):
                cert_count = len(policies['certificate_info'])
                if cert_count > 0:
                    analysis['score'] += 25
                    analysis['findings'].append(f"✅ {cert_count} certificate(s) configured")
            else:
                analysis['score'] += 25
                analysis['findings'].append("✅ Certificates configured")
        else:
            analysis['findings'].append("⚠️ No certificates configured")
            analysis['recommendations'].append("Configure SSL certificates for secure communications")
        
        # Check security constraints
        if policies['security_constraints']:
            if isinstance(policies['security_constraints'], list):
                constraint_count = len(policies['security_constraints'])
                if constraint_count > 0:
                    analysis['score'] += 25
                    analysis['findings'].append(f"✅ {constraint_count} security constraint(s) configured")
            else:
                analysis['score'] += 25
                analysis['findings'].append("✅ Security constraints configured")
        else:
            analysis['findings'].append("⚠️ No security constraints configured")
            analysis['recommendations'].append("Define security constraints for access control")
        
        # Determine risk level
        if analysis['score'] >= 80:
            analysis['risk_level'] = 'LOW'
        elif analysis['score'] >= 50:
            analysis['risk_level'] = 'MEDIUM'
        else:
            analysis['risk_level'] = 'HIGH'
        
        return analysis
    
    def display_security_analysis(self, atom_id: str):
        """Display security analysis for an Atom
        
        Args:
            atom_id: Atom ID
        """
        print(f"\n{'='*60}")
        print(f"Security Posture Analysis: {atom_id}")
        print(f"{'='*60}\n")
        
        analysis = self.analyze_security_posture(atom_id)
        
        # Display score
        score_pct = (analysis['score'] / analysis['max_score']) * 100
        risk_color = {'LOW': '🟢', 'MEDIUM': '🟡', 'HIGH': '🔴', 'UNKNOWN': '⚫'}
        
        print(f"Security Score: {analysis['score']}/{analysis['max_score']} ({score_pct:.0f}%)")
        print(f"Risk Level: {risk_color[analysis['risk_level']]} {analysis['risk_level']}\n")
        
        # Display findings
        if analysis['findings']:
            print("Findings:")
            for finding in analysis['findings']:
                print(f"  {finding}")
        
        # Display recommendations
        if analysis['recommendations']:
            print("\nRecommendations:")
            for i, rec in enumerate(analysis['recommendations'], 1):
                print(f"  {i}. {rec}")
        
        print()


def main():
    """Main function to handle command-line arguments"""
    parser = argparse.ArgumentParser(
        description="Manage Atom security policies",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # View security policies for an Atom
  %(prog)s --get --atom-id YOUR_ATOM_ID
  
  # Display policies in JSON format
  %(prog)s --get --atom-id YOUR_ATOM_ID --format json
  
  # Display policy summary
  %(prog)s --get --atom-id YOUR_ATOM_ID --format summary
  
  # Analyze security posture
  %(prog)s --analyze --atom-id YOUR_ATOM_ID
  
  # Verbose output
  %(prog)s --get --atom-id YOUR_ATOM_ID --verbose
        """
    )
    
    parser.add_argument('--get', action='store_true',
                       help='Get security policies for an Atom')
    parser.add_argument('--analyze', action='store_true',
                       help='Analyze security posture and provide recommendations')
    parser.add_argument('--atom-id', type=str,
                       help='Atom ID')
    parser.add_argument('--format', type=str, choices=['detailed', 'json', 'summary'],
                       default='detailed', help='Output format')
    parser.add_argument('--verbose', action='store_true',
                       help='Enable verbose output')
    
    args = parser.parse_args()
    
    # Validate arguments
    if not any([args.get, args.analyze]):
        parser.print_help()
        return 1
    
    if not args.atom_id:
        print("Error: --atom-id is required")
        return 1
    
    try:
        manager = SecurityPolicyManager(verbose=args.verbose)
        
        if args.get:
            manager.display_security_policies(args.atom_id, args.format)
        
        if args.analyze:
            manager.display_security_analysis(args.atom_id)
        
        return 0
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())