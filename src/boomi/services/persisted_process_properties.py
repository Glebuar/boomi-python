
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..net.transport.utils import parse_xml_to_dict
from ..models import (
    PersistedProcessProperties,
    AsyncOperationTokenResult,
    PersistedProcessPropertiesAsyncResponse
)


class PersistedProcessPropertiesService(BaseService):

    @cast_models
    def update_persisted_process_properties(
        self, id_: str, request_body: PersistedProcessProperties = None
    ) -> Union[PersistedProcessProperties, str]:
        """The UPDATE operation updates Persisted Process Property values for the specified Runtime. Using the UPDATE operation overrides all current property settings. Therefore, strongly recommends that you include a complete list of all Persisted Process properties you want to keep or update. If you do not list a current persisted process property in the Persisted Process properties object, the UPDATE operation deletes those properties.

        >**Note:** You can update the Persisted Process properties if you have either the Runtime Management privilege or the Runtime Management Read Access, along with the Persisted Process Property Read and Write Access privilege.

        :param request_body: The request body., defaults to None
        :type request_body: PersistedProcessProperties, optional
        :param id_: A unique ID assigned by the system to the Runtime.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[PersistedProcessProperties, str]
        """

        Validator(PersistedProcessProperties).is_optional().validate(request_body)
        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/PersistedProcessProperties/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return PersistedProcessProperties._unmap(response)
        if content == "application/xml":
            return PersistedProcessProperties._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def async_get_persisted_process_properties(
        self, id_: str
    ) -> Union[AsyncOperationTokenResult, str]:
        """The GET operation returns the current state of the Persisted Process properties names and values for the specified Runtime.
        The initial GET operation returns a token for the specified Runtime.

        :param id_: A unique ID assigned by the system to the Runtime.
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
                f"{self.base_url or Environment.DEFAULT.url}/async/PersistedProcessProperties/{{id}}",
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
    def async_token_persisted_process_properties(
        self, token: str
    ) -> Union[PersistedProcessPropertiesAsyncResponse, str]:
        """For a response, use the token from the response in a new request.

        :param token: Takes in the token from a previous call to return a result.
        :type token: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[PersistedProcessPropertiesAsyncResponse, str]
        """

        Validator(str).validate(token)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/async/PersistedProcessProperties/response/{{token}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("token", token)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return PersistedProcessPropertiesAsyncResponse._unmap(response)
        if content == "application/xml":
            return PersistedProcessPropertiesAsyncResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)
