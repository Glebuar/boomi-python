
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..net.transport.utils import parse_xml_to_dict
from ..models import (
    AccountUserRole,
    AccountUserRoleQueryConfig,
    AccountUserRoleQueryResponse,
)


class AccountUserRoleService(BaseService):

    @cast_models
    def create_account_user_role(
        self, request_body: AccountUserRole = None
    ) -> Union[AccountUserRole, str]:
        """Adds a user to an account. If you provide a user ID (email address) that does not exist, the system creates the user and adds them to the account.

         When creating a new user, the API request does not require the firstName and lastName fields. If you do not provide those fields, it assigns the default firstName or lastName values automatically. If you include the firstName and lastName fields in a CREATE request for a user name that exists, the request ignores those fields.

        :param request_body: The request body., defaults to None
        :type request_body: AccountUserRole, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[AccountUserRole, str]
        """

        Validator(AccountUserRole).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/AccountUserRole",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return AccountUserRole._unmap(response)
        if content == "application/xml":
            return AccountUserRole._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_account_user_role(
        self, request_body: AccountUserRoleQueryConfig = None
    ) -> Union[AccountUserRoleQueryResponse, str]:
        """For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body., defaults to None
        :type request_body: AccountUserRoleQueryConfig, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[AccountUserRoleQueryResponse, str]
        """

        Validator(AccountUserRoleQueryConfig).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/AccountUserRole/query",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return AccountUserRoleQueryResponse._unmap(response)
        if content == "application/xml":
            return AccountUserRoleQueryResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_more_account_user_role(
        self, request_body: str
    ) -> Union[AccountUserRoleQueryResponse, str]:
        """To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body.
        :type request_body: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[AccountUserRoleQueryResponse, str]
        """

        Validator(str).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/AccountUserRole/queryMore",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body, "text/plain")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return AccountUserRoleQueryResponse._unmap(response)
        if content == "application/xml":
            return AccountUserRoleQueryResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def delete_account_user_role(self, id_: str) -> None:
        """Removes the specified user by a specified conceptual Account User Role object ID from an account.

        :param id_: id_
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/AccountUserRole/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("DELETE")
        )

        response, status, _ = self.send_request(serialized_request)
