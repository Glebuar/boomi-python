"""Test configuration and fixtures."""

import pytest
import os
from unittest.mock import Mock
from boomi import Boomi


@pytest.fixture
def mock_credentials():
    """Mock credentials for testing."""
    return {
        "account_id": "test-account-123",
        "username": "test@example.com",
        "password": "test-password",
        "timeout": 5000
    }


@pytest.fixture
def mock_sdk(mock_credentials):
    """Mock SDK instance for testing."""
    sdk = Mock(spec=Boomi)
    sdk.account_id = mock_credentials["account_id"]
    sdk.username = mock_credentials["username"]
    sdk.password = mock_credentials["password"]
    sdk.timeout = mock_credentials["timeout"]
    return sdk


@pytest.fixture
def sample_account_response():
    """Sample account API response."""
    return {
        "id": "test-account-123",
        "name": "Test Account",
        "dateCreated": "2023-01-01T00:00:00.000Z",
        "status": "active"
    }


@pytest.fixture
def sample_process_response():
    """Sample process API response."""
    return {
        "id": "process-123",
        "name": "Test Process",
        "type": "process",
        "description": "A test process"
    }


@pytest.fixture
def mock_environment_vars(monkeypatch):
    """Mock environment variables for testing."""
    monkeypatch.setenv("BOOMI_ACCOUNT", "test-account-123")
    monkeypatch.setenv("BOOMI_USER", "test@example.com")
    monkeypatch.setenv("BOOMI_SECRET", "test-password")