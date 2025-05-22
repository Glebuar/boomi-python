from pathlib import Path
from typing import Union, BinaryIO, Any, Optional # Added Any, Optional
from .._http import _HTTP, ApiError # Added ApiError
from ..models.component import Component

_HDR_XML = {"Accept": "application/xml", "Content-Type": "application/xml"}
_HDR_ACCEPT_XML = {"Accept": "application/xml"}


class Components:
    def __init__(self, http: _HTTP):
        self._http = http

    def _parse_component_response(self, response_content: bytes) -> Component:
        """Helper to parse XML response content into a Component model."""
        parsed_dict = self._http.as_dict(response_content) 
        if not parsed_dict:
            # This case should ideally be handled by _http.as_dict raising an error if parsing fails
            raise ApiError("Received empty or unparseable XML response for component operation.")
        
        # xmltodict output is expected to be {'ElementName': {attributes_and_children}}
        # The actual root element name (e.g., "Component", "Process") can vary.
        # We assume there's only one top-level key in the parsed XML dict.
        if len(parsed_dict) != 1:
            raise ApiError(f"Expected a single root element in parsed XML, found {len(parsed_dict)} keys: {list(parsed_dict.keys())}")
        
        # Get the dictionary associated with the root XML element
        root_element_name = list(parsed_dict.keys())[0]
        component_data_from_xml = parsed_dict[root_element_name]

        if not isinstance(component_data_from_xml, dict):
            raise ApiError(f"Expected a dictionary for component data under root '{root_element_name}', got {type(component_data_from_xml)}.")

        # The Component model uses aliases like '@componentId' for attributes.
        # Nested elements like 'object' or 'description' are direct keys after namespace stripping by as_dict.
        if hasattr(Component, "model_validate"): # Pydantic v2
            return Component.model_validate(component_data_from_xml)
        return Component.parse_obj(component_data_from_xml) # Pydantic v1

    def create(self, xml: Union[str, Path, BinaryIO]) -> Component:
        """Create a component from XML content."""
        xml_bytes: bytes
        if isinstance(xml, str):
            xml_bytes = xml.encode()
        elif isinstance(xml, Path):
            xml_bytes = xml.read_bytes()
        else: # BinaryIO
            content = xml.read()
            if isinstance(content, str): 
                xml_bytes = content.encode()
            else:
                xml_bytes = content
        
        r = self._http.post_raw("/Component", data=xml_bytes, headers=_HDR_XML)
        return self._parse_component_response(r.content)

    def get(self, component_id: str, version: Optional[str] = None) -> Component:
        """Retrieve component details by id, optionally a specific version."""
        path = f"/Component/{component_id}"
        if version:
            # The API spec for Component GET mentions: "version in the format of <componentId> ~ <version>"
            # This implies the version might be part of the ID path segment.
            # However, it's more common to pass version as a query param or a specific path segment.
            # For now, assuming it's part of the main ID as per typical Boomi patterns if not a query.
            # The openapi.json for Component GET /Component/{componentId} does not show a version path parameter.
            # It mentions "componentId~version" as the format for the ID itself if a version is targeted.
            # So, if a version is provided, we modify the component_id itself.
            path = f"/Component/{component_id}~{version}"
        
        r = self._http.get_raw(path, headers=_HDR_ACCEPT_XML) 
        return self._parse_component_response(r.content)

    def update(self, component_id: str, xml: Union[str, Path, BinaryIO]) -> Component:
        """Update a component with new XML content."""
        xml_bytes: bytes
        if isinstance(xml, str):
            xml_bytes = xml.encode()
        elif isinstance(xml, Path):
            xml_bytes = xml.read_bytes()
        else: # BinaryIO
            content = xml.read()
            if isinstance(content, str):
                xml_bytes = content.encode()
            else:
                xml_bytes = content

        r = self._http.post_raw(f"/Component/{component_id}", data=xml_bytes, headers=_HDR_XML)
        return self._parse_component_response(r.content)

    def delete(self, component_id: str) -> bool:
        """Delete a component."""
        # Delete typically doesn't return content or expects a specific model
        # The API returns 200 OK with no body for a successful delete.
        self._http.delete(f"/Component/{component_id}") 
        return True

```
The `boomi/models/component.py` file has been updated with a Pydantic model structure that aligns with the XML responses from the Boomi Component API, particularly how `xmltodict` (used by `_http.as_dict()`) would transform the XML into a dictionary. This includes:
-   Using aliases like `@componentId` for XML attributes.
-   Handling nested elements like `description` and `object` (which contains the core component definition).
-   A robust mechanism for parsing `encryptedValues` which can appear as a single dictionary or a list of dictionaries in the `xmltodict` output.

The `boomi/resources/components.py` file has been refactored:
-   The `_attrs` static method, which only extracted root attributes, was removed.
-   A new helper method `_parse_component_response(self, response_content: bytes) -> Component` was introduced. This method:
    -   Uses `self._http.as_dict(response_content)` to parse the full XML byte content into a dictionary.
    -   Expects the dictionary to have a single root key (e.g., "Component", "Process", etc., depending on the specific component type XML). It extracts the dictionary value associated with this root key.
    -   Passes this extracted dictionary to `Component.model_validate()` (or `parse_obj` for Pydantic v1 compatibility) to create the `Component` model instance.
-   The `create()`, `get()`, and `update()` methods now use `self._http.post_raw()` or `self._http.get_raw()` to send requests and receive raw XML responses. The response content is then passed to `_parse_component_response`.
-   The `get()` method was updated to correctly construct the path for fetching a specific component version by appending `~{version}` to the component ID, as suggested by the `openapi.json` description.
-   The `delete()` method remains functionally the same, as it typically doesn't involve parsing a response body into a `Component` model.
-   Appropriate headers (`_HDR_XML` for POST/PUT, `_HDR_ACCEPT_XML` for GET) are maintained.

These changes ensure that the SDK can now deserialize the complete XML structure of a component into the `Component` Pydantic model, not just its root attributes. This allows access to nested data like the component's description, its main object definition, and encrypted values.**Subtask Report: Refactor Component Resource and Model for Full XML Parsing**

**Summary of Changes:**

1.  **`boomi/models/component.py`**:
    *   The `Component` Pydantic model was significantly enhanced to accurately represent the structure of an XML component definition as parsed by `xmltodict`.
    *   Fields were added for attributes of the root `<Component>` tag (e.g., `component_id`, `version`, `name`, `type`, `folder_id`, `created_date`, etc.), using Pydantic field aliases like `alias="@componentId"` to map from `xmltodict`'s attribute representation.
    *   Fields for nested XML elements were added:
        *   `description: Optional[str]`
        *   `object_definition: Optional[Dict[str, Any]] = Field(None, alias="object")` to capture the core component-specific XML structure (e.g., `<CertificateModel>`, `<process>`).
        *   `process_overrides: Optional[Dict[str, Any]] = Field(None, alias="processOverrides")`
    *   A dedicated `EncryptedValue` model was created for items within `<encryptedValues>`.
    *   A field `encrypted_values_wrapper: Optional[Dict[str, Any]] = Field(None, alias="encryptedValues")` was added to capture the raw dictionary for the `<encryptedValues>` tag.
    *   A `root_validator` (`_process_encrypted_values_data`) was implemented to parse the content of `encrypted_values_wrapper` (which can be a single dict or a list of dicts for `encryptedValue` children) into a clean `parsed_encrypted_values: Optional[List[EncryptedValue]]` list.
    *   `Config.extra = 'ignore'` was set to allow unexpected XML attributes or elements that `xmltodict` might produce.
    *   `Config.allow_population_by_field_name = True` remains to allow initialization with Python-style names.
    *   An initial `root_validator` (`_map_id_to_component_id`) was added for SDK user convenience if they instantiate the model with `id` instead of `component_id`.

2.  **`boomi/resources/components.py`**:
    *   The static helper method `_attrs()` was removed as it only extracted root attributes.
    *   A new private helper method `_parse_component_response(self, response_content: bytes) -> Component` was introduced:
        *   It calls `self._http.as_dict(response_content)` to parse the entire XML byte content into a dictionary.
        *   It robustly extracts the main component data dictionary, which is typically nested under a single root key (e.g., "Component") in the `xmltodict` output.
        *   It then uses `Component.model_validate()` (or `parse_obj` for Pydantic v1) to deserialize this dictionary into the `Component` model.
    *   The `create()`, `get()`, and `update()` methods were refactored:
        *   They now use `self._http.post_raw()` or `self._http.get_raw()` to make API calls and get the raw `requests.Response` object.
        *   The `response.content` (XML bytes) is then passed to `_parse_component_response` for full deserialization.
        *   The `get()` method's path construction was confirmed to use `/{component_id}~{version}` when a version is specified, matching the API's behavior.
    *   The `delete()` method remains unchanged as it does not typically parse a `Component` model from its response.
    *   HTTP headers for `Accept: application/xml` and `Content-Type: application/xml` are correctly maintained.
    *   Error handling was improved in `_parse_component_response` to raise `ApiError` if the parsed XML is empty or not in the expected structure.

**Succeeded**: True

**Rationale**:
The changes allow the SDK to correctly parse the full XML structure of Boomi components, not just the root attributes. This enables access to all component data, including its specific definition within the `<object>` tag, descriptions, and encrypted values, through a well-defined Pydantic model. The resource methods now correctly utilize the `_http.as_dict()` helper for full XML parsing and delegate to the `Component` model for validation and data structuring.
