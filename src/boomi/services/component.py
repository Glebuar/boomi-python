
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import Component, ComponentBulkRequest, ComponentBulkResponse
from ..net.transport.utils import parse_xml_to_dict


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
            return Component._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def update_component(
        self, component_id: str, request_body: str = None
    ) -> Union[Component, str]:
        """- Full updates only. No partial updates. If part of the object’s configuration is omitted, the component will be updated without that configuration.
           - The only exception is for encrypted fields such as passwords. Omitting an encrypted field from the update request will NOT impact the saved value.
         - Requests without material changes to configuration will be rejected to prevent unnecessary revisions.
         - Request will not be processed in case if the payload has invalid attributes and tags under the `<object>` section.
         - For the saved process property components, modifications to the data type are not permitted.
         - Include the `branchId` in the request body to specify the branch on which you want to update the component.
         - >**Note:** To create or update a component, you must supply a valid component XML format for the given type.

        :param request_body: The request body., defaults to None
        :type request_body: str, optional
        :param component_id: The ID of the component. The component ID is available on the Revision History dialog, which you can access from the Build page in the service. This must be omitted for the CREATE operation but it is required for the UPDATE operation.
        :type component_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[Component, str]
        """

        Validator(str).is_optional().validate(request_body)
        Validator(str).validate(component_id)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/Component/{{componentId}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("componentId", component_id)
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
    def bulk_component(self, request_body: ComponentBulkRequest = None) -> str:
        """The limit for the BULK GET operation is 5 requests. All other API objects have a limit of 100 BULK GET requests.

         To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

        :param request_body: The request body., defaults to None
        :type request_body: ComponentBulkRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
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
        return ComponentBulkResponse._unmap(response)
