
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import (
    TradingPartnerProcessingGroup,
    TradingPartnerProcessingGroupBulkRequest,
    TradingPartnerProcessingGroupBulkResponse,
    TradingPartnerProcessingGroupQueryConfig,
    TradingPartnerProcessingGroupQueryResponse,
)


class TradingPartnerProcessingGroupService(BaseService):

    @cast_models
    def create_trading_partner_processing_group(
        self, request_body: TradingPartnerProcessingGroup = None
    ) -> Union[TradingPartnerProcessingGroup, str]:
        """Send an HTTP POST request where `accountId` is the ID of the authenticating account for the request.
         If you omit the folderName field, you must include the folderId field — and vice versa.

        :param request_body: The request body., defaults to None
        :type request_body: TradingPartnerProcessingGroup, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[TradingPartnerProcessingGroup, str]
        """

        Validator(TradingPartnerProcessingGroup).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/TradingPartnerProcessingGroup",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return TradingPartnerProcessingGroup._unmap(response)
        if content == "application/xml":
            return TradingPartnerProcessingGroup._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def get_trading_partner_processing_group(
        self, id_: str
    ) -> Union[TradingPartnerProcessingGroup, str]:
        """The ordinary GET operation returns a single Trading Partner Processing Group object based on the supplied ID. The bulk GET operation returns multiple Trading Partner Processing Group objects based on the supplied IDs, to a maximum of 100.
         A GET operation specifying the ID of a deleted processing group component retrieves the component. In the component, the deleted field’s value is true.

        :param id_: id_
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[TradingPartnerProcessingGroup, str]
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/TradingPartnerProcessingGroup/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return TradingPartnerProcessingGroup._unmap(response)
        if content == "application/xml":
            return TradingPartnerProcessingGroup._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def update_trading_partner_processing_group(
        self, id_: str, request_body: TradingPartnerProcessingGroup = None
    ) -> Union[TradingPartnerProcessingGroup, str]:
        """An UPDATE operation specifying the ID of a deleted processing group component restores the component to a non-deleted state, assuming the request is otherwise valid. It also overwrites the entire processing group component.

        :param request_body: The request body., defaults to None
        :type request_body: TradingPartnerProcessingGroup, optional
        :param id_: id_
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[TradingPartnerProcessingGroup, str]
        """

        Validator(TradingPartnerProcessingGroup).is_optional().validate(request_body)
        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/TradingPartnerProcessingGroup/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return TradingPartnerProcessingGroup._unmap(response)
        if content == "application/xml":
            return TradingPartnerProcessingGroup._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def delete_trading_partner_processing_group(self, id_: str) -> None:
        """A DELETE operation specifying the ID of a deleted processing group component returns a false response. If you deleted the component successfully, the response is "true".

        :param id_: id_
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/TradingPartnerProcessingGroup/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("DELETE")
        )

        response, status, _ = self.send_request(serialized_request)

    @cast_models
    def bulk_trading_partner_processing_group(
        self, request_body: TradingPartnerProcessingGroupBulkRequest = None
    ) -> Union[TradingPartnerProcessingGroupBulkResponse, str]:
        """To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

        :param request_body: The request body., defaults to None
        :type request_body: TradingPartnerProcessingGroupBulkRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[TradingPartnerProcessingGroupBulkResponse, str]
        """

        Validator(TradingPartnerProcessingGroupBulkRequest).is_optional().validate(
            request_body
        )

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/TradingPartnerProcessingGroup/bulk",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return TradingPartnerProcessingGroupBulkResponse._unmap(response)
        if content == "application/xml":
            return TradingPartnerProcessingGroupBulkResponse._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_trading_partner_processing_group(
        self, request_body: TradingPartnerProcessingGroupQueryConfig = None
    ) -> Union[TradingPartnerProcessingGroupQueryResponse, str]:
        """The QUERY operation returns all of the authenticating account’s processing group components. The operation does not return full component representations; it returns, for each result, the component’s name, ID, and folder ID.

         For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body., defaults to None
        :type request_body: TradingPartnerProcessingGroupQueryConfig, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[TradingPartnerProcessingGroupQueryResponse, str]
        """

        Validator(TradingPartnerProcessingGroupQueryConfig).is_optional().validate(
            request_body
        )

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/TradingPartnerProcessingGroup/query",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return TradingPartnerProcessingGroupQueryResponse._unmap(response)
        if content == "application/xml":
            return TradingPartnerProcessingGroupQueryResponse._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_more_trading_partner_processing_group(
        self, request_body: str
    ) -> Union[TradingPartnerProcessingGroupQueryResponse, str]:
        """To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body.
        :type request_body: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[TradingPartnerProcessingGroupQueryResponse, str]
        """

        Validator(str).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/TradingPartnerProcessingGroup/queryMore",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body, "text/plain")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return TradingPartnerProcessingGroupQueryResponse._unmap(response)
        if content == "application/xml":
            return TradingPartnerProcessingGroupQueryResponse._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)
