
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import AsyncOperationTokenResult, ListQueuesAsyncResponse


class ListQueuesService(BaseService):

    @cast_models
    def async_token_list_queues(
        self, token: str
    ) -> Union[ListQueuesAsyncResponse, str]:
        """After receiving a 200 status code response, send a second GET request where {accountId} is the ID of the account authenticating the request and sessionId is the ID provided in the initial response.

        :param token: Takes in the token from a previous call to return a result.
        :type token: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[ListQueuesAsyncResponse, str]
        """

        Validator(str).validate(token)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/async/ListQueues/response/{{token}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("token", token)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return ListQueuesAsyncResponse._unmap(response)
        if content == "application/xml":
            return ListQueuesAsyncResponse._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def async_get_list_queues(self, id_: str) -> Union[AsyncOperationTokenResult, str]:
        """To retrieve a list of message queues, Send an HTTP GET where accountId is the account that you are authenticating with and containerId is the ID of the Runtime, Runtime cluster, or Runtime cloud which owns the message queue that you want to retrieve.
         >**Note:** You can find the Account ID for an account by navigating to Settings > Account Information and Setup in the user interface. Additionally, you can find the container ID by navigating to Manage > Runtime Management and viewing the Runtime ID value on the Runtime Information panel for a selected Runtime, Runtime cluster, or Runtime cloud.

        :param id_: id_
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[AsyncOperationTokenResult, str]
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/async/ListQueues/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return AsyncOperationTokenResult._unmap(response)
        if content == "application/xml":
            return AsyncOperationTokenResult._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)
