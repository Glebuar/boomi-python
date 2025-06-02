
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..net.transport.utils import parse_xml_to_dict
from ..models import (
    AsyncOperationTokenResult,
    ListenerStatusAsyncResponse,
    ListenerStatusQueryConfig,
)


class ListenerStatusService(BaseService):

    @cast_models
    def async_get_listener_status(
        self, request_body: ListenerStatusQueryConfig = None
    ) -> Union[AsyncOperationTokenResult, str]:
        """Send an HTTP POST where {accountId} is the ID of the authenticating account for the request.
         >**Note:** For backward compatibility, Boomi continues to support the legacy URL: https://api.boomi.com/api/rest/v1/accountId/ListenerStatus/query/async.

         For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body., defaults to None
        :type request_body: ListenerStatusQueryConfig, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[AsyncOperationTokenResult, str]
        """

        Validator(ListenerStatusQueryConfig).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/async/ListenerStatus/query",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return AsyncOperationTokenResult._unmap(response)
        if content == "application/xml":
            return AsyncOperationTokenResult._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def async_token_listener_status(
        self, token: str
    ) -> Union[ListenerStatusAsyncResponse, str]:
        """The ordinary GET operation retrieves async results from the QUERY. Send an HTTP GET where {accountId} is the account that you are authenticating with and {token} is the listener status token returned by your QUERY request.
         >**Note:** For backward compatibility, Boomi continues to support the legacy URL: https://api.boomi.com/api/rest/v1/accountId/ListenerStatus/query/async.

        :param token: Takes in the token from a previous call to return a result.
        :type token: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[ListenerStatusAsyncResponse, str]
        """

        Validator(str).validate(token)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/async/ListenerStatus/response/{{token}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("token", token)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return ListenerStatusAsyncResponse._unmap(response)
        if content == "application/xml":
            return ListenerStatusAsyncResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)
