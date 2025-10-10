
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..net.transport.utils import parse_xml_to_dict
from ..models import (
    AccountUserFederation,
    AccountUserFederationQueryConfig,
    AccountUserFederationQueryResponse,
)


class AccountUserFederationService(BaseService):

    @cast_models
    def create_account_user_federation(
        self, request_body: AccountUserFederation = None
    ) -> Union[AccountUserFederation, str]:
        """Enables single sign-on for a specific user under a specific account using a specific federation ID. The user is not visible in the Setup page unless you assign one or more roles to that user.

        :param request_body: The request body., defaults to None
        :type request_body: AccountUserFederation, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[AccountUserFederation, str]
        """

        Validator(AccountUserFederation).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/AccountUserFederation",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return AccountUserFederation._unmap(response)
        if content == "application/xml":
            return AccountUserFederation._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_account_user_federation(
        self, request_body: AccountUserFederationQueryConfig = None
    ) -> Union[AccountUserFederationQueryResponse, str]:
        """For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body., defaults to None
        :type request_body: AccountUserFederationQueryConfig, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[AccountUserFederationQueryResponse, str]
        """

        Validator(AccountUserFederationQueryConfig).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/AccountUserFederation/query",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return AccountUserFederationQueryResponse._unmap(response)
        if content == "application/xml":
            return AccountUserFederationQueryResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_more_account_user_federation(
        self, request_body: str
    ) -> Union[AccountUserFederationQueryResponse, str]:
        """To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body.
        :type request_body: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[AccountUserFederationQueryResponse, str]
        """

        Validator(str).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/AccountUserFederation/queryMore",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body, "text/plain")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return AccountUserFederationQueryResponse._unmap(response)
        if content == "application/xml":
            return AccountUserFederationQueryResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def update_account_user_federation(
        self, id_: str, request_body: AccountUserFederation = None
    ) -> Union[AccountUserFederation, str]:
        """Updates the federation ID of a specific user in a specific account.

        :param request_body: The request body., defaults to None
        :type request_body: AccountUserFederation, optional
        :param id_: id_
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[AccountUserFederation, str]
        """

        Validator(AccountUserFederation).is_optional().validate(request_body)
        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/AccountUserFederation/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return AccountUserFederation._unmap(response)
        if content == "application/xml":
            return AccountUserFederation._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def delete_account_user_federation(self, id_: str) -> None:
        """Disables single sign-on for the user specified by the conceptual Account User Federation object ID.

        :param id_: id_
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/AccountUserFederation/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("DELETE")
        )

        response, status, _ = self.send_request(serialized_request)
