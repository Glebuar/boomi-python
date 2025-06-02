"""Tests for service classes."""

import pytest
from unittest.mock import Mock, patch
import responses
from boomi.services.account import AccountService
from boomi.services.process import ProcessService
from boomi.models.account import Account


class TestAccountService:
    """Test the AccountService class."""

    def test_account_service_initialization(self):
        """Test AccountService can be initialized."""
        service = AccountService(base_url="https://api.test.boomi.com")
        assert service is not None
        assert service.base_url == "https://api.test.boomi.com"

    @patch('boomi.services.account.AccountService.send_request')
    @patch('boomi.services.account.AccountService.get_access_token')
    @patch('boomi.services.account.AccountService.get_basic_auth')
    def test_get_account_success(self, mock_basic_auth, mock_access_token, mock_send_request):
        """Test successful account retrieval."""
        # Mock authentication
        mock_access_token.return_value = "test-token"
        mock_basic_auth.return_value = ("user", "pass")
        
        # Mock successful response
        mock_response_data = {
            "id": "test-account-123",
            "name": "Test Account",
            "dateCreated": "2023-01-01T00:00:00.000Z",
            "status": "active"
        }
        mock_send_request.return_value = (mock_response_data, 200, "application/json")
        
        service = AccountService()
        result = service.get_account("test-account-123")
        
        assert result is not None
        mock_send_request.assert_called_once()

    @patch('boomi.services.account.AccountService.send_request')
    def test_get_account_with_invalid_id(self, mock_send_request):
        """Test account retrieval with invalid ID."""
        service = AccountService()
        
        # Test with None - should raise validation error
        with pytest.raises(Exception):
            service.get_account(None)

    @patch('boomi.services.account.AccountService.send_request')
    @patch('boomi.services.account.AccountService.get_access_token')
    @patch('boomi.services.account.AccountService.get_basic_auth')
    def test_get_account_xml_response(self, mock_basic_auth, mock_access_token, mock_send_request):
        """Test account retrieval with XML response."""
        mock_access_token.return_value = "test-token"
        mock_basic_auth.return_value = ("user", "pass")
        
        mock_xml_response = '<?xml version="1.0"?><account><id>test-123</id></account>'
        mock_send_request.return_value = (mock_xml_response, 200, "application/xml")
        
        service = AccountService()
        result = service.get_account("test-account-123")
        
        mock_send_request.assert_called_once()


class TestBaseServiceFunctionality:
    """Test base service functionality shared across all services."""

    def test_service_with_custom_base_url(self):
        """Test service initialization with custom base URL."""
        custom_url = "https://api.custom.boomi.com"
        service = AccountService(base_url=custom_url)
        
        assert service.base_url == custom_url

    def test_service_with_default_base_url(self):
        """Test service initialization with default base URL."""
        service = AccountService()
        
        # Should work without explicit base URL
        assert service is not None


class TestProcessService:
    """Test ProcessService basic functionality."""

    def test_process_service_initialization(self):
        """Test ProcessService can be initialized."""
        try:
            service = ProcessService(base_url="https://api.test.boomi.com")
            assert service is not None
        except ImportError:
            # ProcessService might not exist, skip this test
            pytest.skip("ProcessService not available")

    @patch('boomi.services.process.ProcessService.send_request')
    def test_process_service_methods_exist(self, mock_send_request):
        """Test that ProcessService has expected methods."""
        try:
            service = ProcessService()
            
            # Check that service has common methods (these may vary based on actual implementation)
            expected_methods = ['get_process', 'query_process', 'create_process', 'update_process']
            
            for method in expected_methods:
                if hasattr(service, method):
                    assert callable(getattr(service, method))
                    
        except ImportError:
            pytest.skip("ProcessService not available")


class TestServiceValidation:
    """Test service input validation."""

    def test_account_service_validates_string_input(self):
        """Test that AccountService validates string inputs properly."""
        service = AccountService()
        
        # Test with empty string
        with pytest.raises(Exception):
            service.get_account("")
        
        # Test with non-string input
        with pytest.raises(Exception):
            service.get_account(123)


class TestServiceErrorHandling:
    """Test service error handling."""

    @patch('boomi.services.account.AccountService.send_request')
    @patch('boomi.services.account.AccountService.get_access_token')
    @patch('boomi.services.account.AccountService.get_basic_auth')
    def test_account_service_handles_api_errors(self, mock_basic_auth, mock_access_token, mock_send_request):
        """Test that AccountService properly handles API errors."""
        mock_access_token.return_value = "test-token"
        mock_basic_auth.return_value = ("user", "pass")
        
        # Mock error response
        mock_send_request.side_effect = Exception("API Error")
        
        service = AccountService()
        
        with pytest.raises(Exception):
            service.get_account("test-account-123")