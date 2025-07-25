
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..net.transport.utils import parse_xml_to_dict
from ..models import (
    AccountGroupIntegrationPack,
    AccountGroupIntegrationPackBulkRequest,
    AccountGroupIntegrationPackBulkResponse,
    AccountGroupIntegrationPackQueryConfig,
    AccountGroupIntegrationPackQueryResponse,
)


class AccountGroupIntegrationPackService(BaseService):

    @cast_models
    def create_account_group_integration_pack(
        self, request_body: AccountGroupIntegrationPack = None
    ) -> Union[AccountGroupIntegrationPack, str]:
        """Adds an integration pack to the requesting account group.

        :param request_body: The request body., defaults to None
        :type request_body: AccountGroupIntegrationPack, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[AccountGroupIntegrationPack, str]
        """

        Validator(AccountGroupIntegrationPack).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/AccountGroupIntegrationPack",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return AccountGroupIntegrationPack._unmap(response)
        if content == "application/xml":
            return AccountGroupIntegrationPack._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def get_account_group_integration_pack(
        self, id_: str
    ) -> Union[AccountGroupIntegrationPack, str]:
        """The ordinary GET operation retrieves the properties of the AccountGroupIntegrationPack with the specified ID.
        The bulk GET operation retrieves the properties of the AccountGroupIntegrationPack with the specified IDs to a maximum of 100.
        You can obtain AccountGroupIntegrationPack IDs from the QUERY operation.

        :param id_: A unique ID assigned by the system to the integration pack.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[AccountGroupIntegrationPack, str]
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/AccountGroupIntegrationPack/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return AccountGroupIntegrationPack._unmap(response)
        if content == "application/xml":
            return AccountGroupIntegrationPack._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def delete_account_group_integration_pack(self, id_: str) -> None:
        """Removes the integration pack with a specified ID from the requesting account group.
        You can obtain this ID from a QUERY operation.

        :param id_: A unique ID assigned by the system to the integration pack.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/AccountGroupIntegrationPack/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("DELETE")
        )

        response, status, _ = self.send_request(serialized_request)

    @cast_models
    def bulk_account_group_integration_pack(
        self, request_body: AccountGroupIntegrationPackBulkRequest = None
    ) -> Union[AccountGroupIntegrationPackBulkResponse, str]:
        """The bulk GET operation returns multiple objects based on the supplied account IDs, to a maximum of 100. To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

        :param request_body: The request body., defaults to None
        :type request_body: AccountGroupIntegrationPackBulkRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[AccountGroupIntegrationPackBulkResponse, str]
        """

        Validator(AccountGroupIntegrationPackBulkRequest).is_optional().validate(
            request_body
        )

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/AccountGroupIntegrationPack/bulk",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return AccountGroupIntegrationPackBulkResponse._unmap(response)
        if content == "application/xml":
            return AccountGroupIntegrationPackBulkResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_account_group_integration_pack(
        self, request_body: AccountGroupIntegrationPackQueryConfig = None
    ) -> Union[AccountGroupIntegrationPackQueryResponse, str]:
        """Retrieves all integration packs available to the requesting account group ID.

         For general information about the structure of QUERY filters and how to handle paged results, see the Query filters and Query paging topics.

        :param request_body: The request body., defaults to None
        :type request_body: AccountGroupIntegrationPackQueryConfig, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[AccountGroupIntegrationPackQueryResponse, str]
        """

        Validator(AccountGroupIntegrationPackQueryConfig).is_optional().validate(
            request_body
        )

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/AccountGroupIntegrationPack/query",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return AccountGroupIntegrationPackQueryResponse._unmap(response)
        if content == "application/xml":
            return AccountGroupIntegrationPackQueryResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_more_account_group_integration_pack(
        self, request_body: str
    ) -> Union[AccountGroupIntegrationPackQueryResponse, str]:
        """To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body.
        :type request_body: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[AccountGroupIntegrationPackQueryResponse, str]
        """

        Validator(str).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/AccountGroupIntegrationPack/queryMore",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body, "text/plain")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return AccountGroupIntegrationPackQueryResponse._unmap(response)
        if content == "application/xml":
            return AccountGroupIntegrationPackQueryResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)
