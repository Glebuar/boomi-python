
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import (
    OrganizationComponent,
    OrganizationComponentBulkRequest,
    OrganizationComponentBulkResponse,
    OrganizationComponentQueryConfig,
    OrganizationComponentQueryResponse,
)


class OrganizationComponentService(BaseService):

    @cast_models
    def create_organization_component(
        self, request_body: OrganizationComponent = None
    ) -> Union[OrganizationComponent, str]:
        """The CREATE operation creates an Organization Component object with the specified component name.

         The request body requires the `componentName` field. If you omit the `folderName` field, it requires the `folderId` field — and vice versa. If you omit the `componentID` field, it assigns the value when you create the component. If you omit the `folderID` field, it assigns the value when you create the component.

        :param request_body: The request body., defaults to None
        :type request_body: OrganizationComponent, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[OrganizationComponent, str]
        """

        Validator(OrganizationComponent).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/OrganizationComponent",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return OrganizationComponent._unmap(response)
        if content == "application/xml":
            return OrganizationComponent._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def get_organization_component(self, id_: str) -> Union[OrganizationComponent, str]:
        """The GET operation returns a single Organization Component object based on the supplied ID. A GET operation specifying the ID of a deleted Organization Component retrieves the component. In the component, the deleted field’s value is *true*.

        :param id_: Organization component ID
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[OrganizationComponent, str]
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/OrganizationComponent/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return OrganizationComponent._unmap(response)
        if content == "application/xml":
            return OrganizationComponent._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def update_organization_component(
        self, id_: str, request_body: OrganizationComponent = None
    ) -> Union[OrganizationComponent, str]:
        """The UPDATE operation overwrites the Organization Component object with the specified component ID. An UPDATE operation specifying the ID of a deleted Organization component restores the component to a non-deleted state, assuming the request is otherwise valid.

        :param request_body: The request body., defaults to None
        :type request_body: OrganizationComponent, optional
        :param id_: Organization component ID
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[OrganizationComponent, str]
        """

        Validator(OrganizationComponent).is_optional().validate(request_body)
        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/OrganizationComponent/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return OrganizationComponent._unmap(response)
        if content == "application/xml":
            return OrganizationComponent._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def delete_organization_component(self, id_: str) -> None:
        """The DELETE operation deletes the Organization Component object with the specified component ID. A DELETE operation specifying the ID of a deleted Organization component returns a false response. If the component is deleted successfully, the response is `true`.

        :param id_: ID of the Organization component you are attempting to delete.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/OrganizationComponent/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("DELETE")
        )

        response, status, _ = self.send_request(serialized_request)

    @cast_models
    def bulk_organization_component(
        self, request_body: OrganizationComponentBulkRequest = None
    ) -> Union[str, OrganizationComponentBulkResponse]:
        """The bulk GET operation returns multiple Account objects based on the supplied account IDs, to a maximum of 100. To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

        :param request_body: The request body., defaults to None
        :type request_body: OrganizationComponentBulkRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[str, OrganizationComponentBulkResponse]
        """

        Validator(OrganizationComponentBulkRequest).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/OrganizationComponent/bulk",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/xml":
            return OrganizationComponentBulkResponse._unmap(response)
        if content == "application/json":
            return OrganizationComponentBulkResponse._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_organization_component(
        self, request_body: OrganizationComponentQueryConfig = None
    ) -> Union[OrganizationComponentQueryResponse, str]:
        """- Only the LIKE operator is allowed with a name filter. Likewise, only the EQUALS operator is permitted with a contactName, email, or phone filter.

         -   If the QUERY request includes multiple filters, you can connect the filters with a logical AND operator — the query does not support the logical OR operator .

         -   The QUERY results omit the folderName field.

         For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body., defaults to None
        :type request_body: OrganizationComponentQueryConfig, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[OrganizationComponentQueryResponse, str]
        """

        Validator(OrganizationComponentQueryConfig).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/OrganizationComponent/query",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return OrganizationComponentQueryResponse._unmap(response)
        if content == "application/xml":
            return OrganizationComponentQueryResponse._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_more_organization_component(
        self, request_body: str
    ) -> Union[OrganizationComponentQueryResponse, str]:
        """To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body.
        :type request_body: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[OrganizationComponentQueryResponse, str]
        """

        Validator(str).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/OrganizationComponent/queryMore",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body, "text/plain")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return OrganizationComponentQueryResponse._unmap(response)
        if content == "application/xml":
            return OrganizationComponentQueryResponse._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)
