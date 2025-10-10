
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..net.transport.utils import parse_xml_to_dict
from ..models import AsyncOperationTokenResult, AtomDiskSpaceAsyncResponse


class AtomDiskSpaceService(BaseService):

    @cast_models
    def async_get_atom_disk_space(
        self, id_: str
    ) -> Union[AsyncOperationTokenResult, str]:
        """The GET operation returns the current disk usage state of the given Runtime cloud attachment.
         The initial GET operation returns a token for the specified Runtime cloud attachment. Subsequent GET operations return status code 202 (while the request is in progress) based on the returned token.
         This first request is required to retrieve the authenticating token, which is used in a subsequent GET request.
         >**Note:** `accountId` must always refer to the account ID of the parent Runtime cloud and not that of the attachment.

        :param id_: ID of the Runtime cloud attachment.
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
                f"{self.base_url or Environment.DEFAULT.url}/async/AtomDiskSpace/{{id}}",
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
            return AsyncOperationTokenResult._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def async_token_atom_disk_space(
        self, token: str
    ) -> Union[AtomDiskSpaceAsyncResponse, str]:
        """Send a second HTTP GET request where accountId is the ID of the authenticating account for the request, and token is the token returned in the initial response. This second request authenticates the retrieval of the Runtime cloud attachments' disk space usage.
         >**Note:** `accountId` must always refer to the account ID of the parent Runtime cloud and not that of the attachment.

        :param token: Takes in the token from a previous call to return a result.
        :type token: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[AtomDiskSpaceAsyncResponse, str]
        """

        Validator(str).validate(token)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/async/AtomDiskSpace/response/{{token}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("token", token)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return AtomDiskSpaceAsyncResponse._unmap(response)
        if content == "application/xml":
            return AtomDiskSpaceAsyncResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)
