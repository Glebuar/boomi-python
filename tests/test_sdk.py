"""Tests for the main SDK class."""

import pytest
from unittest.mock import patch, Mock
from boomi import Boomi, Environment


class TestBoomiSDK:
    """Test the main Boomi SDK class initialization and basic functionality."""

    def test_sdk_initialization_with_credentials(self):
        """Test SDK initialization with username/password credentials."""
        sdk = Boomi(
            username="test@example.com",
            password="test-password",
            account_id="test-account-123",
            timeout=5000
        )
        
        assert sdk is not None
        assert hasattr(sdk, 'account')
        assert hasattr(sdk, 'process')
        assert hasattr(sdk, 'cloud')
        assert hasattr(sdk, 'environment')

    def test_sdk_initialization_with_access_token(self):
        """Test SDK initialization with access token."""
        sdk = Boomi(
            access_token="test-token-123",
            account_id="test-account-123",
            timeout=5000
        )
        
        assert sdk is not None
        assert hasattr(sdk, 'account')
        assert hasattr(sdk, 'process')

    def test_sdk_initialization_with_environment_enum(self):
        """Test SDK initialization with Environment enum."""
        sdk = Boomi(
            username="test@example.com",
            password="test-password",
            base_url=Environment.DEFAULT,
            account_id="test-account-123"
        )
        
        assert sdk is not None
        assert sdk._base_url == Environment.DEFAULT.value

    def test_sdk_initialization_with_custom_base_url(self):
        """Test SDK initialization with custom base URL."""
        custom_url = "https://api.custom.boomi.com"
        sdk = Boomi(
            username="test@example.com",
            password="test-password",
            base_url=custom_url,
            account_id="test-account-123"
        )
        
        assert sdk is not None
        assert sdk._base_url == custom_url

    def test_sdk_has_all_expected_services(self):
        """Test that SDK has all expected service attributes."""
        sdk = Boomi(
            username="test@example.com",
            password="test-password",
            account_id="test-account-123"
        )
        
        expected_services = [
            'account', 'account_group', 'account_user_role',
            'atom', 'audit_log', 'branch', 'cloud', 'component',
            'deployment', 'environment', 'execution_record',
            'integration_pack', 'process', 'role'
        ]
        
        for service in expected_services:
            assert hasattr(sdk, service), f"SDK missing {service} service"

    def test_sdk_default_parameters(self):
        """Test SDK with default parameters."""
        sdk = Boomi()
        
        assert sdk is not None
        assert sdk._base_url is None

    @patch('boomi.sdk.AccountService')
    def test_services_initialized_with_base_url(self, mock_account_service):
        """Test that services are initialized with the correct base URL."""
        base_url = "https://api.test.boomi.com"
        Boomi(
            username="test@example.com",
            password="test-password",
            base_url=base_url,
            account_id="test-account-123"
        )
        
        mock_account_service.assert_called_with(base_url=base_url)

    def test_sdk_services_are_different_instances(self):
        """Test that different SDK instances have different service instances."""
        sdk1 = Boomi(username="user1", password="pass1", account_id="account1")
        sdk2 = Boomi(username="user2", password="pass2", account_id="account2")
        
        assert sdk1.account is not sdk2.account
        assert sdk1.process is not sdk2.process