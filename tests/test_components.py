import pytest
from unittest.mock import MagicMock, patch
from boomi._http import _HTTP
from boomi.resources.components import Components, _HDR_XML # Import _HDR_XML for create/update tests
from boomi.models.component import Component
from typing import Union, BinaryIO, Optional, List, Dict # For type hinting
from pathlib import Path # For create/update tests

# Dummy Response Class
class DummyResp:
    def __init__(self, data, status_code=200, ok=True, content_bytes=None):
        self._data = data
        self.status_code = status_code
        self.ok = ok
        self.content = content_bytes if content_bytes is not None else b""

    def json(self):
        if not self.ok or self.status_code >= 300: # Basic error simulation for JSON
            raise Exception(f"HTTP Error {self.status_code}, Response: {self._data}")
        return self._data

@pytest.fixture
def mock_http_client():
    """Fixture to create a MagicMock instance of _HTTP."""
    mock_http = MagicMock(spec=_HTTP)
    return mock_http

@pytest.fixture
def components_resource(mock_http_client):
    """Fixture to create a Components resource instance with a mocked http client."""
    return Components(mock_http_client)

# --- Test for Components.get() ---
def test_components_get_success(components_resource, mock_http_client):
    """
    Tests Components.get() for successful JSON response and model parsing.
    """
    component_id_to_test = "comp-123"
    # Mocked API response should use keys that Pydantic model expects for deserialization.
    # If model uses aliases (e.g. alias="componentId" for field "id"),
    # then r.json() should return a dict with "componentId".
    mock_api_response = {
        "componentId": component_id_to_test, # Matches alias for 'id' field
        "name": "Test Component",
        "type": "process",
        "folderId": "folder-abc",          # Matches alias for 'folder_id' field
        "description": "A test component.",   # New field
        "version": 2                          # New field
    }
    
    # Configure the mock _http.get() call to return a DummyResp whose json() method returns our mock_api_response
    mock_http_client.get.return_value = DummyResp(data=mock_api_response)

    result_component = components_resource.get(cid=component_id_to_test)

    # Assert that _http.get was called correctly
    expected_path = f"/Component/{component_id_to_test}"
    mock_http_client.get.assert_called_once_with(expected_path) # Removed headers check as it's JSON now

    # Assert that the result is an instance of the Component model
    assert isinstance(result_component, Component)

    # Assert attributes of the Component instance
    assert result_component.id == mock_api_response["componentId"] # Access via Python field name 'id'
    assert result_component.name == mock_api_response["name"]
    assert result_component.type == mock_api_response["type"]
    assert result_component.folder_id == mock_api_response["folderId"] # Access via Python field name 'folder_id'
    assert result_component.description == mock_api_response["description"]
    assert result_component.version == mock_api_response["version"]

# --- Tests for other Component methods (create, update, delete) ---
# These methods still use XML handling internally as per components.py content.
# We will mock the XML processing parts (_attrs, ET.fromstring) for these tests.

@patch('boomi.resources.components.ET.fromstring') # Mock ElementTree.fromstring
@patch.object(Components, '_attrs') # Mock the static method _attrs
def test_components_create_success(mock_attrs, mock_et_fromstring, components_resource, mock_http_client):
    """Tests Components.create() - focusing on HTTP call, mocking XML parts."""
    xml_input_str = "<Component name='NewComponent' type='process'></Component>"
    xml_input_bytes = xml_input_str.encode()

    mock_parsed_attrs_from_xml = {"componentId": "new-comp-id", "name": "NewComponent", "type": "process", "folderId": None, "description": "", "version": 1}
    mock_attrs.return_value = mock_parsed_attrs_from_xml
    
    # DummyResp for self._http.post - its .content will be used by _attrs
    # The actual data for .json() part of DummyResp is not used by create/update
    # but .content is.
    mock_http_client.post.return_value = DummyResp(data=None, content_bytes=b"<ComponentResponse/>")


    result_component = components_resource.create(xml=xml_input_str)

    mock_http_client.post.assert_called_once_with("/Component", data=xml_input_bytes, headers=_HDR_XML)
    mock_attrs.assert_called_once_with(b"<ComponentResponse/>") # Check _attrs was called with response content

    assert isinstance(result_component, Component)
    assert result_component.id == "new-comp-id"
    assert result_component.name == "NewComponent"


@patch('boomi.resources.components.ET.fromstring')
@patch.object(Components, '_attrs')
def test_components_update_success(mock_attrs, mock_et_fromstring, components_resource, mock_http_client):
    """Tests Components.update() - focusing on HTTP call, mocking XML parts."""
    component_id_to_update = "comp-existing"
    xml_input_str = "<Component name='UpdatedComponent' type='process'></Component>"
    xml_input_bytes = xml_input_str.encode()

    mock_parsed_attrs_from_xml = {"componentId": component_id_to_update, "name": "UpdatedComponent", "type": "process", "folderId": None, "description": "", "version": 2}
    mock_attrs.return_value = mock_parsed_attrs_from_xml
    
    mock_http_client.post.return_value = DummyResp(data=None, content_bytes=b"<ComponentResponseUpdated/>")

    result_component = components_resource.update(cid=component_id_to_update, xml=xml_input_str)

    expected_path = f"/Component/{component_id_to_update}"
    mock_http_client.post.assert_called_once_with(expected_path, data=xml_input_bytes, headers=_HDR_XML)
    mock_attrs.assert_called_once_with(b"<ComponentResponseUpdated/>")

    assert isinstance(result_component, Component)
    assert result_component.name == "UpdatedComponent"
    assert result_component.version == 2


def test_components_delete_success(components_resource, mock_http_client):
    """Tests Components.delete() - focusing on HTTP call."""
    component_id_to_delete = "comp-to-delete"
    
    # .delete might return a response that .ok can be checked on, or just None
    # For this test, let's assume _http.delete returns a response-like object where .ok can be true
    mock_http_client.delete.return_value = DummyResp(data=None, ok=True) # DummyResp not strictly needed if method returns True directly

    result = components_resource.delete(cid=component_id_to_delete)

    expected_path = f"/Component/{component_id_to_delete}"
    mock_http_client.delete.assert_called_once_with(expected_path)
    assert result is True
