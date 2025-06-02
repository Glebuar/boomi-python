
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import (
    SharedCommunicationChannelComponent,
    SharedCommunicationChannelComponentBulkRequest,
    SharedCommunicationChannelComponentBulkResponse,
    SharedCommunicationChannelComponentQueryConfig,
    SharedCommunicationChannelComponentQueryResponse,
)


class SharedCommunicationChannelComponentService(BaseService):

    @cast_models
    def create_shared_communication_channel_component(
        self, request_body: SharedCommunicationChannelComponent = None
    ) -> Union[str, SharedCommunicationChannelComponent]:
        """The sample request creates a Shared Communication Component named `Disk Comms Channel`.

        :param request_body: The request body., defaults to None
        :type request_body: SharedCommunicationChannelComponent, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[str, SharedCommunicationChannelComponent]
        """

        Validator(SharedCommunicationChannelComponent).is_optional().validate(
            request_body
        )

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/SharedCommunicationChannelComponent",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/xml":
            return SharedCommunicationChannelComponent._unmap(response)
        if content == "application/json":
            return SharedCommunicationChannelComponent._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def get_shared_communication_channel_component(
        self, id_: str
    ) -> Union[SharedCommunicationChannelComponent, str]:
        """Send an HTTP GET request where `{accountId}` is the ID of the authenticating account for the request and `{componentId}` is the ID of the component being retrieved.

        :param id_: ID of the component being retrieved.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[SharedCommunicationChannelComponent, str]
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/SharedCommunicationChannelComponent/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return SharedCommunicationChannelComponent._unmap(response)
        if content == "application/xml":
            return SharedCommunicationChannelComponent._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def update_shared_communication_channel_component(
        self, id_: str, request_body: SharedCommunicationChannelComponent = None
    ) -> Union[SharedCommunicationChannelComponent, str]:
        """The sample request updates the component named `Disk Comms Channel`.

        :param request_body: The request body., defaults to None
        :type request_body: SharedCommunicationChannelComponent, optional
        :param id_: ID of the component that needs updating.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[SharedCommunicationChannelComponent, str]
        """

        Validator(SharedCommunicationChannelComponent).is_optional().validate(
            request_body
        )
        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/SharedCommunicationChannelComponent/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return SharedCommunicationChannelComponent._unmap(response)
        if content == "application/xml":
            return SharedCommunicationChannelComponent._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def delete_shared_communication_channel_component(self, id_: str) -> None:
        """If the Shared Communication Channel component is deleted successfully, the response is `true`.

        :param id_: ID of the component that you want to delete.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/SharedCommunicationChannelComponent/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("DELETE")
        )

        response, status, _ = self.send_request(serialized_request)

    @cast_models
    def bulk_shared_communication_channel_component(
        self, request_body: SharedCommunicationChannelComponentBulkRequest = None
    ) -> Union[SharedCommunicationChannelComponentBulkResponse, str]:
        """To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

        :param request_body: The request body., defaults to None
        :type request_body: SharedCommunicationChannelComponentBulkRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[SharedCommunicationChannelComponentBulkResponse, str]
        """

        Validator(
            SharedCommunicationChannelComponentBulkRequest
        ).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/SharedCommunicationChannelComponent/bulk",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return SharedCommunicationChannelComponentBulkResponse._unmap(response)
        if content == "application/xml":
            return SharedCommunicationChannelComponentBulkResponse._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_shared_communication_channel_component(
        self, request_body: SharedCommunicationChannelComponentQueryConfig = None
    ) -> Union[SharedCommunicationChannelComponentQueryResponse, str]:
        """For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

         The sample request query returns the Shared Communication Channel components using the AS2 standard for the authenticating account.

         >**Note:** The name field in a QUERY filter represents the object's `componentName` field.

        :param request_body: The request body., defaults to None
        :type request_body: SharedCommunicationChannelComponentQueryConfig, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[SharedCommunicationChannelComponentQueryResponse, str]
        """

        Validator(
            SharedCommunicationChannelComponentQueryConfig
        ).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/SharedCommunicationChannelComponent/query",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return SharedCommunicationChannelComponentQueryResponse._unmap(response)
        if content == "application/xml":
            return SharedCommunicationChannelComponentQueryResponse._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_more_shared_communication_channel_component(
        self, request_body: str
    ) -> Union[SharedCommunicationChannelComponentQueryResponse, str]:
        """To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body.
        :type request_body: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[SharedCommunicationChannelComponentQueryResponse, str]
        """

        Validator(str).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/SharedCommunicationChannelComponent/queryMore",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body, "text/plain")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return SharedCommunicationChannelComponentQueryResponse._unmap(response)
        if content == "application/xml":
            return SharedCommunicationChannelComponentQueryResponse._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)
