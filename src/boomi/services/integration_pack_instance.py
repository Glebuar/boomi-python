
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..net.transport.utils import parse_xml_to_dict
from ..models import (
    IntegrationPackInstance,
    IntegrationPackInstanceBulkRequest,
    IntegrationPackInstanceBulkResponse,
    IntegrationPackInstanceQueryConfig,
    IntegrationPackInstanceQueryResponse,
)


class IntegrationPackInstanceService(BaseService):

    @cast_models
    def create_integration_pack_instance(
        self, request_body: IntegrationPackInstance = None
    ) -> Union[IntegrationPackInstance, str]:
        """Installs an instance of the integration pack with a specific ID in the requesting account. You can set the integrationPackOverrideName field only if you configure the specified integration pack to allow multiple installs.

        :param request_body: The request body., defaults to None
        :type request_body: IntegrationPackInstance, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[IntegrationPackInstance, str]
        """

        Validator(IntegrationPackInstance).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/IntegrationPackInstance",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return IntegrationPackInstance._unmap(response)
        if content == "application/xml":
            return IntegrationPackInstance._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def get_integration_pack_instance(
        self, id_: str
    ) -> Union[IntegrationPackInstance, str]:
        """Retrieves the properties of the integration pack instance having the specified ID.

         The ordinary GET operation retrieves the properties of the integration pack instance having the specified ID. The bulk GET operation retrieves the properties of the integration pack instances having the specified IDs, to a maximum of 100. You can obtain integration pack instance IDs from the QUERY operation.

        :param id_: The integration pack instance ID.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[IntegrationPackInstance, str]
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/IntegrationPackInstance/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return IntegrationPackInstance._unmap(response)
        if content == "application/xml":
            return IntegrationPackInstance._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def delete_integration_pack_instance(self, id_: str) -> None:
        """Uninstalls the integration pack instance having a specified ID from the requesting account. You can obtain this ID from a QUERY operation.

        :param id_: The integration pack instance ID.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/IntegrationPackInstance/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("DELETE")
        )

        response, status, _ = self.send_request(serialized_request)

    @cast_models
    def bulk_integration_pack_instance(
        self, request_body: IntegrationPackInstanceBulkRequest = None
    ) -> Union[IntegrationPackInstanceBulkResponse, str]:
        """To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

        :param request_body: The request body., defaults to None
        :type request_body: IntegrationPackInstanceBulkRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[IntegrationPackInstanceBulkResponse, str]
        """

        Validator(IntegrationPackInstanceBulkRequest).is_optional().validate(
            request_body
        )

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/IntegrationPackInstance/bulk",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return IntegrationPackInstanceBulkResponse._unmap(response)
        if content == "application/xml":
            return IntegrationPackInstanceBulkResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_integration_pack_instance(
        self, request_body: IntegrationPackInstanceQueryConfig = None
    ) -> Union[IntegrationPackInstanceQueryResponse, str]:
        """For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body., defaults to None
        :type request_body: IntegrationPackInstanceQueryConfig, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[IntegrationPackInstanceQueryResponse, str]
        """

        Validator(IntegrationPackInstanceQueryConfig).is_optional().validate(
            request_body
        )

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/IntegrationPackInstance/query",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return IntegrationPackInstanceQueryResponse._unmap(response)
        if content == "application/xml":
            return IntegrationPackInstanceQueryResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_more_integration_pack_instance(
        self, request_body: str
    ) -> Union[IntegrationPackInstanceQueryResponse, str]:
        """To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body.
        :type request_body: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[IntegrationPackInstanceQueryResponse, str]
        """

        Validator(str).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/IntegrationPackInstance/queryMore",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body, "text/plain")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return IntegrationPackInstanceQueryResponse._unmap(response)
        if content == "application/xml":
            return IntegrationPackInstanceQueryResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)
