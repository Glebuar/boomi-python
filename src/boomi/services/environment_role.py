
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..net.transport.utils import parse_xml_to_dict
from ..models import (
    EnvironmentRole,
    EnvironmentRoleBulkRequest,
    EnvironmentRoleBulkResponse,
    EnvironmentRoleQueryConfig,
    EnvironmentRoleQueryResponse,
)


class EnvironmentRoleService(BaseService):

    @cast_models
    def create_environment_role(
        self, request_body: EnvironmentRole = None
    ) -> Union[EnvironmentRole, str]:
        """Associates a role with an environment. You must have the Runtime Management privilege to perform the CREATE operation.

        :param request_body: The request body., defaults to None
        :type request_body: EnvironmentRole, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[EnvironmentRole, str]
        """

        Validator(EnvironmentRole).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/EnvironmentRole",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return EnvironmentRole._unmap(response)
        if content == "application/xml":
            return EnvironmentRole._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def get_environment_role(self, id_: str) -> Union[EnvironmentRole, str]:
        """Returns a single Environment Role object based on the supplied environment role ID.

        :param id_: The Environment Role object you are attempting to get.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[EnvironmentRole, str]
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/EnvironmentRole/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return EnvironmentRole._unmap(response)
        if content == "application/xml":
            return EnvironmentRole._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def delete_environment_role(self, id_: str) -> None:
        """Removes the association between a role and an environment.

         You must have the Runtime Management privilege to perform the DELETE operation. If you have the Runtime Management privilege, you cannot delete associations between roles and environments.

        :param id_: The Environment Role object you are attempting to delete.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/EnvironmentRole/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("DELETE")
        )

        response, status, _ = self.send_request(serialized_request)

    @cast_models
    def bulk_environment_role(
        self, request_body: EnvironmentRoleBulkRequest = None
    ) -> Union[EnvironmentRoleBulkResponse, str]:
        """To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

        :param request_body: The request body., defaults to None
        :type request_body: EnvironmentRoleBulkRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[EnvironmentRoleBulkResponse, str]
        """

        Validator(EnvironmentRoleBulkRequest).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/EnvironmentRole/bulk",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return EnvironmentRoleBulkResponse._unmap(response)
        if content == "application/xml":
            return EnvironmentRoleBulkResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_environment_role(
        self, request_body: EnvironmentRoleQueryConfig = None
    ) -> Union[EnvironmentRoleQueryResponse, str]:
        """For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body., defaults to None
        :type request_body: EnvironmentRoleQueryConfig, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[EnvironmentRoleQueryResponse, str]
        """

        Validator(EnvironmentRoleQueryConfig).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/EnvironmentRole/query",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return EnvironmentRoleQueryResponse._unmap(response)
        if content == "application/xml":
            return EnvironmentRoleQueryResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_more_environment_role(
        self, request_body: str
    ) -> Union[EnvironmentRoleQueryResponse, str]:
        """To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body.
        :type request_body: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[EnvironmentRoleQueryResponse, str]
        """

        Validator(str).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/EnvironmentRole/queryMore",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body, "text/plain")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return EnvironmentRoleQueryResponse._unmap(response)
        if content == "application/xml":
            return EnvironmentRoleQueryResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)
