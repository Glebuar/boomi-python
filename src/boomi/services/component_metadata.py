
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..net.transport.utils import parse_xml_to_dict
from ..models import (
    ComponentMetadata,
    ComponentMetadataBulkRequest,
    ComponentMetadataBulkResponse,
    ComponentMetadataQueryConfig,
    ComponentMetadataQueryResponse,
)


class ComponentMetadataService(BaseService):

    @cast_models
    def create_component_metadata(
        self, request_body: ComponentMetadata = None
    ) -> Union[ComponentMetadata, str]:
        """The ability to create a new component is not supported at this time. Although, you can create a deleted component, but you cannot create a new component. You will receive an error if you do not specify the deleted component ID in the create request.

        :param request_body: The request body., defaults to None
        :type request_body: ComponentMetadata, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[ComponentMetadata, str]
        """

        Validator(ComponentMetadata).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ComponentMetadata",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return ComponentMetadata._unmap(response)
        if content == "application/xml":
            return ComponentMetadata._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def get_component_metadata(self, id_: str) -> Union[ComponentMetadata, str]:
        """Returns the latest component revision if you do not provide the version. Providing the version in the format of `<componentId>` ~ `<version>`, returns the specific version of the component.

        :param id_: Required. Read only. The ID of the component. The component ID is available on the Revision History dialog, which you can access from the Build page in the service.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[ComponentMetadata, str]
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ComponentMetadata/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return ComponentMetadata._unmap(response)
        if content == "application/xml":
            return ComponentMetadata._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def update_component_metadata(
        self, id_: str, request_body: ComponentMetadata = None
    ) -> Union[ComponentMetadata, str]:
        """Only `name` and `folderId` may be updated. They are optional and will only be modified if included in the UPDATE request. `folderId` must be a valid, non-deleted folder. If `folderId` is included in the request but with a blank value, it defaults to the root folder.

        :param request_body: The request body., defaults to None
        :type request_body: ComponentMetadata, optional
        :param id_: Required. Read only. The ID of the component. The component ID is available on the Revision History dialog, which you can access from the Build page in the service.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[ComponentMetadata, str]
        """

        Validator(ComponentMetadata).is_optional().validate(request_body)
        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ComponentMetadata/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return ComponentMetadata._unmap(response)
        if content == "application/xml":
            return ComponentMetadata._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def delete_component_metadata(self, id_: str) -> None:
        """Lets you delete required components. Note that deleting a component does NOT delete dependent components.

        :param id_: Required. Read only. The ID of the component. The component ID is available on the Revision History dialog, which you can access from the Build page in the service.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ComponentMetadata/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("DELETE")
        )

        response, status, _ = self.send_request(serialized_request)

    @cast_models
    def bulk_component_metadata(
        self, request_body: ComponentMetadataBulkRequest = None
    ) -> Union[ComponentMetadataBulkResponse, str]:
        """To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

        :param request_body: The request body., defaults to None
        :type request_body: ComponentMetadataBulkRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[ComponentMetadataBulkResponse, str]
        """

        Validator(ComponentMetadataBulkRequest).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ComponentMetadata/bulk",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return ComponentMetadataBulkResponse._unmap(response)
        if content == "application/xml":
            return ComponentMetadataBulkResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_component_metadata(
        self, request_body: ComponentMetadataQueryConfig = None
    ) -> Union[ComponentMetadataQueryResponse, str]:
        """- By default, QUERY results include previous revisions including deleted versions. Use query filters to exclude previous and deleted versions if desired. For more examples of querying components, see Component Metadata API example requests mentioned above in the API description.
         - The `version` field must be accompanied by the `componentId` field. You can query all other fields.
         - The `copiedFromComponentId` field must accompany the `copiedFromComponentVersion` field.

         For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body., defaults to None
        :type request_body: ComponentMetadataQueryConfig, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[ComponentMetadataQueryResponse, str]
        """

        Validator(ComponentMetadataQueryConfig).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ComponentMetadata/query",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return ComponentMetadataQueryResponse._unmap(response)
        if content == "application/xml":
            return ComponentMetadataQueryResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_more_component_metadata(
        self, request_body: str
    ) -> Union[ComponentMetadataQueryResponse, str]:
        """To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body.
        :type request_body: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[ComponentMetadataQueryResponse, str]
        """

        Validator(str).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ComponentMetadata/queryMore",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body, "text/plain")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return ComponentMetadataQueryResponse._unmap(response)
        if content == "application/xml":
            return ComponentMetadataQueryResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)
