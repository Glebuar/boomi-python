import pytest
from unittest.mock import MagicMock
from boomi._http import _HTTP # Assuming _HTTP can be instantiated for mocking
from boomi.resources.atoms import Atoms
from typing import Optional, List, Dict # Dict for payloads/responses

# Dummy Response Class as per conventions
class DummyResp:
    def __init__(self, data, status_code=200, ok=True):
        self._data = data
        self.status_code = status_code
        self.ok = ok

    def json(self):
        return self._data

@pytest.fixture
def mock_http_client():
    """Fixture to create a MagicMock instance of _HTTP."""
    # Create a MagicMock for the _HTTP client instance
    # This allows us to mock its methods like get, post, etc.
    mock_http = MagicMock(spec=_HTTP)
    return mock_http

@pytest.fixture
def atoms_resource(mock_http_client):
    """Fixture to create an Atoms resource instance with a mocked http client."""
    return Atoms(mock_http_client)

# --- Tests for Atoms.list() ---
def test_atoms_list_get_no_payload(atoms_resource, mock_http_client):
    """
    Tests Atoms.list() when no query_payload is provided (GET /Atom).
    Corresponds to: test_atoms_list_refactored_success (scenario 1)
    """
    mock_api_response_data = [{"id": "atom1", "name": "Atom One"}]
    mock_http_client.get.return_value = DummyResp(mock_api_response_data)

    result = atoms_resource.list()

    mock_http_client.get.assert_called_once_with("/Atom")
    assert result == mock_api_response_data

def test_atoms_list_post_with_payload(atoms_resource, mock_http_client):
    """
    Tests Atoms.list() when a query_payload is provided (POST /Atom/query).
    Corresponds to: test_atoms_list_refactored_success (scenario 2)
    """
    query_payload = {"QueryFilter": {"expression": {"operator": "EQUALS", "property": "status", "argument": ["online"]}}}
    mock_api_response_data = [{"id": "atom2", "name": "Atom Two", "status": "online"}]
    
    mock_http_client.post.return_value = DummyResp(mock_api_response_data)

    result = atoms_resource.list(query_payload=query_payload)

    mock_http_client.post.assert_called_once_with("/Atom/query", json=query_payload)
    assert result == mock_api_response_data

# --- Tests for Atoms.post_atom_disable() ---
def test_post_atom_disable(atoms_resource, mock_http_client):
    """
    Tests Atoms.post_atom_disable().
    Corresponds to: test_post_atom_disable_success
    """
    atom_id_to_disable = "atom-123"
    request_payload = {"reason": "maintenance"}
    mock_api_response_data = {"status": "disabled_request_received"} # Example response

    mock_http_client.post.return_value = DummyResp(mock_api_response_data)

    result = atoms_resource.post_atom_disable(atomid_val=atom_id_to_disable, payload=request_payload)

    expected_path = f"/atom/{atom_id_to_disable}/disable"
    mock_http_client.post.assert_called_once_with(expected_path, json=request_payload)
    assert result == mock_api_response_data

# --- Tests for Atoms.post_atom_query() ---
def test_post_atom_query(atoms_resource, mock_http_client):
    """
    Tests Atoms.post_atom_query().
    Corresponds to: test_post_atom_query_success
    """
    query_payload = {"QueryFilter": {"expression": {"operator": "EQUALS", "property": "type", "argument": ["CLOUD"]}}}
    mock_api_response_data = [{"id": "atom3", "name": "Cloud Atom", "type": "CLOUD"}]

    mock_http_client.post.return_value = DummyResp(mock_api_response_data)

    result = atoms_resource.post_atom_query(query_payload=query_payload)

    mock_http_client.post.assert_called_once_with("/atom/query", json=query_payload)
    assert result == mock_api_response_data
