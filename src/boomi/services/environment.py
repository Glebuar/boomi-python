
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..net.transport.utils import parse_xml_to_dict
from ..models import (
    Environment,
    EnvironmentBulkRequest,
    EnvironmentBulkResponse,
    EnvironmentMapExtension,
    EnvironmentQueryConfig,
    EnvironmentQueryResponse,
)


class EnvironmentService(BaseService):

    @cast_models
    def create_environment(
        self, request_body: Environment = None
    ) -> Union[Environment, str]:
        """Creates an environment having the specified name. Environment names must be unique.

        :param request_body: The request body., defaults to None
        :type request_body: Environment, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[Environment, str]
        """

        Validator(Environment).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/Environment",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return Environment._unmap(response)
        if content == "application/xml":
            return Environment._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def get_environment(self, id_: str) -> Union[Environment, str]:
        """Retrieves the properties of the environment with a specified ID.

        :param id_: A unique ID assigned by the system to the environment.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[Environment, str]
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/Environment/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return Environment._unmap(response)
        if content == "application/xml":
            return Environment._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def update_environment(
        self, id_: str, request_body: Environment = None
    ) -> Union[Environment, str]:
        """Updates the Environment object having the specified ID. You can edit the name field only.

        :param request_body: The request body., defaults to None
        :type request_body: Environment, optional
        :param id_: A unique ID assigned by the system to the environment.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[Environment, str]
        """

        Validator(Environment).is_optional().validate(request_body)
        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/Environment/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return Environment._unmap(response)
        if content == "application/xml":
            return Environment._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def delete_environment(self, id_: str) -> None:
        """Deletes the Environment object with a specified ID. It is not possible to delete an environment that has attached Runtimes or integration packs.

        :param id_: A unique ID assigned by the system to the environment.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/Environment/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("DELETE")
        )

        response, status, _ = self.send_request(serialized_request)

    @cast_models
    def bulk_environment(
        self, request_body: EnvironmentBulkRequest = None
    ) -> Union[EnvironmentBulkResponse, str]:
        """To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

        :param request_body: The request body., defaults to None
        :type request_body: EnvironmentBulkRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[EnvironmentBulkResponse, str]
        """

        Validator(EnvironmentBulkRequest).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/Environment/bulk",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return EnvironmentBulkResponse._unmap(response)
        if content == "application/xml":
            return EnvironmentBulkResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_environment(
        self, request_body: EnvironmentQueryConfig = None
    ) -> Union[EnvironmentQueryResponse, str]:
        """For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body., defaults to None
        :type request_body: EnvironmentQueryConfig, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[EnvironmentQueryResponse, str]
        """

        Validator(EnvironmentQueryConfig).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/Environment/query",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return EnvironmentQueryResponse._unmap(response)
        if content == "application/xml":
            return EnvironmentQueryResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_more_environment(
        self, request_body: str
    ) -> Union[EnvironmentQueryResponse, str]:
        """To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body.
        :type request_body: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[EnvironmentQueryResponse, str]
        """

        Validator(str).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/Environment/queryMore",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body, "text/plain")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return EnvironmentQueryResponse._unmap(response)
        if content == "application/xml":
            return EnvironmentQueryResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def update_environment_map_extension(
        self, id_: str, request_body: EnvironmentMapExtension = None
    ) -> Union[EnvironmentMapExtension, str]:
        """Updates the extended mapping configuration for the specified Environment Map Extension object ID.

        :param request_body: The request body., defaults to None
        :type request_body: EnvironmentMapExtension, optional
        :param id_: id_
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[EnvironmentMapExtension, str]
        """

        Validator(EnvironmentMapExtension).is_optional().validate(request_body)
        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/EnvironmentMapExtension/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return EnvironmentMapExtension._unmap(response)
        if content == "application/xml":
            return EnvironmentMapExtension._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)
