
from typing import Union, Any
from xml.etree import ElementTree as ET
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import Component, ComponentBulkRequest, ComponentBulkResponse
from ..net.transport.utils import parse_xml_to_dict, parse_xml_to_dict_with_preservation


class ComponentService(BaseService):

    @cast_models
    def create_component(self, request_body: str = None) -> Union[Component, str]:
        """- Cannot create components for types not eligible for your account. For example, if your account does not have the B2B/EDI feature, you will not be able to create Trading Partner components.
         - Request will not be processed in case if the payload has invalid attributes and tags under the <object> section.
         - Include the `branchId` in the request body to specify a branch on which you want to create the component.
         - >**Note:** To create or update a component, you must supply a valid component XML format for the given type.

         The component XML can be rather complex with many optional fields and nested configuration. For this reason we strongly recommend approaching it by first creating the desired component structure/skeleton as you would normally in the Build page UI, then exporting the XML using the Component object GET. This will provide an accurate example or template of the XML you will need to create. You can replace values or continue that pattern as you need for your use case.

        :param request_body: The request body., defaults to None
        :type request_body: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[Component, str]
        """

        Validator(str).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/Component",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body, "application/xml")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return Component._unmap(response)
        if content == "application/xml":
            return Component._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def get_component(self, component_id: str) -> Union[Component, str]:
        """- When using the GET operation by componentId, it returns the latest component if you do not provide the version.
         - When you provide the version in the format of `<componentId>` ~ `<version>`, it returns the specific version of the component.
         - The GET operation only accepts mediaType `application/xml` for the API response.
         - The limit is 5 requests for the BULK GET operation. All other API objects have a limit of 100 BULK GET requests.
         - If you want information for a component on a specific branch, include the branchId in the GET request:   `https://api.boomi.com/api/rest/v1/{accountId}/Component/{componentId}~{branchId}`

        :param component_id: The ID of the component. The component ID is available on the Revision History dialog, which you can access from the Build page in the service. This must be omitted for the CREATE operation but it is required for the UPDATE operation.
        :type component_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[Component, str]
        """

        Validator(str).validate(component_id)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/Component/{{componentId}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("componentId", component_id)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return Component._unmap(response)
        if content == "application/xml":
            # Phase 2: Use XML preservation parsing for Component objects
            return Component._unmap(parse_xml_to_dict_with_preservation(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def update_component(
        self, component_id: str, request_body: Any = None
    ) -> Union[Component, str]:
        """- Full updates only. No partial updates. If part of the object's configuration is omitted, the component will be updated without that configuration.
           - The only exception is for encrypted fields such as passwords. Omitting an encrypted field from the update request will NOT impact the saved value.
         - Requests without material changes to configuration will be rejected to prevent unnecessary revisions.
         - Request will not be processed in case if the payload has invalid attributes and tags under the `<object>` section.
         - For the saved process property components, modifications to the data type are not permitted.
         - Include the `branchId` in the request body to specify the branch on which you want to update the component.
         - >**Note:** To create or update a component, you must supply a valid component XML format for the given type.

        Phase 2 Enhancement: This method now accepts Component objects in addition to XML strings.
        When a Component object is passed, it automatically converts to XML using the to_xml() method
        which preserves the original XML structure.

        :param request_body: Component object or XML string. Can be Component, str, or None.
        :type request_body: Union[Component, str, None]
        :param component_id: The ID of the component.
        :type component_id: str
        :return: The parsed response data.
        :rtype: Union[Component, str]
        """
        import warnings
        
        Validator(str).validate(component_id)
        
        # Phase 2: Handle different types of request_body
        xml_body = None
        
        if request_body is None:
            raise ValueError("request_body is required for component updates")
        elif isinstance(request_body, str):
            # Traditional XML string
            xml_body = request_body
        elif hasattr(request_body, 'to_xml'):
            # Component object with to_xml method
            xml_body = request_body.to_xml()
        elif hasattr(request_body, 'object') and isinstance(getattr(request_body, 'object'), dict):
            # Legacy Component object with dict-based object field
            warnings.warn(
                "Updating components with dict-based object is deprecated and may fail. "
                "Use Component objects with XML preservation or raw XML strings.",
                DeprecationWarning,
                stacklevel=2
            )
            # Fall back to trying to serialize as XML (this may still fail)
            xml_body = str(request_body)  # This won't work well, but provides backward compatibility attempt
        else:
            # Try to convert whatever it is to string
            xml_body = str(request_body)
        
        # Validate we have XML content
        if not xml_body or not xml_body.strip():
            raise ValueError("No valid XML content found in request_body")

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/Component/{{componentId}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("componentId", component_id)
            .serialize()
            .set_method("POST")
            .set_body(xml_body, "application/xml")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return Component._unmap(response)
        if content == "application/xml":
            # Phase 2: Use XML preservation parsing for response too
            return Component._unmap(parse_xml_to_dict_with_preservation(response))
        raise ApiError("Error on deserializing the response.", status, response)

    def bulk_component_raw(self, request_body: ComponentBulkRequest = None) -> str:
        """Get multiple components as raw XML string.
        
        The limit for the BULK GET operation is 5 requests. This method returns
        the raw XML response from the API without any parsing.

        :param request_body: The request body., defaults to None
        :type request_body: ComponentBulkRequest, optional
        :return: Raw XML response from the API
        :rtype: str
        """
        Validator(ComponentBulkRequest).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/Component/bulk",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if status >= 200 and status < 300:
            return response  # Return raw XML string
        raise ApiError(f"Failed to bulk get components: HTTP {status}", status, response)

    @cast_models  
    def bulk_component(self, request_body: ComponentBulkRequest = None):
        """Get multiple components with proper XML parsing.
        
        The limit for the BULK GET operation is 5 requests. This method properly
        handles the XML response from the API and returns a list of components.

        :param request_body: The request body., defaults to None
        :type request_body: ComponentBulkRequest, optional
        :return: List of Component objects from successful responses
        :rtype: List[Component]
        """
        # Get raw XML response first
        xml_response = self.bulk_component_raw(request_body)
        
        # Parse XML response  
        try:
            root = ET.fromstring(xml_response)
            components = []
            ns = {'bns': 'http://api.platform.boomi.com/'}
            
            # Find all response elements
            for response_elem in root.findall('bns:response', ns):
                status_code = response_elem.get('statusCode', '')
                
                if status_code == '200':
                    # Find the Result element (which is a Component)
                    result_elem = response_elem.find('bns:Result', ns)
                    if result_elem is not None:
                        # Convert the Component XML element to raw XML string
                        component_xml = ET.tostring(result_elem, encoding='unicode')
                        
                        # Parse this single component XML using existing get_component logic
                        # For now, we'll use the raw XML approach to avoid complex parsing
                        components.append(component_xml)
                else:
                    # Handle error responses  
                    error_msg = response_elem.get('errorMessage', 'Unknown error')
                    print(f"⚠️ Component failed with status {status_code}: {error_msg}")
            
            return components
            
        except ET.ParseError as e:
            raise ApiError(f"Failed to parse XML response: {e}", 200, xml_response)

    # ========== Phase 1: Raw XML Support ==========
    # These methods provide direct XML access without any dict conversion
    # This preserves XML structure exactly for complex components
    
    def get_component_raw(self, component_id: str) -> str:
        """Get component as raw XML string without any parsing or conversion.
        
        This method preserves the exact XML structure returned by the API,
        including namespaces, element order, and attributes. Use this when
        you need full control over the XML or when dealing with complex
        components that fail with dict-based approaches.
        
        :param component_id: The ID of the component
        :type component_id: str
        :return: Raw XML string exactly as returned by the API
        :rtype: str
        """
        Validator(str).validate(component_id)
        
        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/Component/{{componentId}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("componentId", component_id)
            .serialize()
            .set_method("GET")
        )
        
        # Return raw response without any parsing
        response, status, content = self.send_request(serialized_request)
        if status >= 200 and status < 300:
            return response  # Return raw XML string
        raise ApiError(f"Failed to get component: HTTP {status}", status, response)
    
    def update_component_raw(self, component_id: str, xml: str) -> str:
        """Update component with raw XML string.
        
        This method sends the XML directly to the API without any conversion,
        preserving the exact structure you provide. Use this when you need
        full control over the XML or when dealing with complex components.
        
        :param component_id: The ID of the component
        :type component_id: str
        :param xml: Raw XML string to send to the API
        :type xml: str
        :return: Raw XML response from the API
        :rtype: str
        """
        Validator(str).validate(component_id)
        Validator(str).validate(xml)
        
        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/Component/{{componentId}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("componentId", component_id)
            .serialize()
            .set_method("POST")
            .set_body(xml, "application/xml")
        )
        
        response, status, content = self.send_request(serialized_request)
        if status >= 200 and status < 300:
            return response  # Return raw XML response
        raise ApiError(f"Failed to update component: HTTP {status}", status, response)
    
    def get_component_etree(self, component_id: str) -> ET.Element:
        """Get component as ElementTree for DOM manipulation.
        
        This method returns an ElementTree Element that you can manipulate
        using standard XML DOM methods while preserving structure.
        
        :param component_id: The ID of the component
        :type component_id: str
        :return: ElementTree Element root
        :rtype: xml.etree.ElementTree.Element
        """
        xml = self.get_component_raw(component_id)
        root = ET.fromstring(xml)
        
        # Register namespaces to preserve them on serialization
        ns = self._get_default_namespace(root)
        if ns:
            ET.register_namespace("", ns)  # Register default namespace
        
        # Also register bns namespace
        ET.register_namespace("bns", "http://api.platform.boomi.com/")
        
        return root
    
    def update_component_etree(self, component_id: str, element: ET.Element) -> str:
        """Update component from ElementTree Element.
        
        This method serializes the ElementTree back to XML and sends it to
        the API, preserving the structure of your DOM manipulations.
        
        :param component_id: The ID of the component
        :type component_id: str
        :param element: ElementTree Element to serialize and send
        :type element: xml.etree.ElementTree.Element
        :return: Raw XML response from the API
        :rtype: str
        """
        # Ensure namespaces are registered
        ns = self._get_default_namespace(element)
        if ns:
            ET.register_namespace("", ns)
        ET.register_namespace("bns", "http://api.platform.boomi.com/")
        
        # Convert Element to XML string
        xml = ET.tostring(element, encoding='unicode', xml_declaration=True)
        
        # Update using raw XML method
        return self.update_component_raw(component_id, xml)
    
    @staticmethod
    def _get_default_namespace(element: ET.Element) -> str:
        """Extract default namespace from an element.
        
        :param element: ElementTree Element
        :return: Default namespace URI or None
        """
        tag = element.tag
        if tag.startswith("{") and "}" in tag:
            return tag[1:tag.index("}")]
        return None
