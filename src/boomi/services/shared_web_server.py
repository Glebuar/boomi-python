
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import (
    SharedWebServer,
    SharedWebServerBulkRequest,
    SharedWebServerBulkResponse,
)


class SharedWebServerService(BaseService):

    @cast_models
    def get_shared_web_server(self, id_: str) -> Union[SharedWebServer, str]:
        """Retrieves the details of a Shared Web Server configuration for this atom/cloud ID by its unique ID. The response can be in either XML or JSON format based on your request.

        :param id_: id_
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[SharedWebServer, str]
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/SharedWebServer/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return SharedWebServer._unmap(response)
        if content == "application/xml":
            return SharedWebServer._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def update_shared_web_server(
        self, id_: str, request_body: SharedWebServer = None
    ) -> Union[SharedWebServer, str]:
        """Updates a Shared Web Server object based on the supplied Runtime ID.

        :param request_body: The request body., defaults to None
        :type request_body: SharedWebServer, optional
        :param id_: id_
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[SharedWebServer, str]
        """

        Validator(SharedWebServer).is_optional().validate(request_body)
        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/SharedWebServer/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return SharedWebServer._unmap(response)
        if content == "application/xml":
            return SharedWebServer._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def bulk_shared_web_server(
        self, request_body: SharedWebServerBulkRequest = None
    ) -> Union[SharedWebServerBulkResponse, str]:
        """To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

        :param request_body: The request body., defaults to None
        :type request_body: SharedWebServerBulkRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[SharedWebServerBulkResponse, str]
        """

        Validator(SharedWebServerBulkRequest).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/SharedWebServer/bulk",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return SharedWebServerBulkResponse._unmap(response)
        if content == "application/xml":
            return SharedWebServerBulkResponse._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)
