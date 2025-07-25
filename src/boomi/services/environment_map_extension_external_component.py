
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import (
    EnvironmentMapExtensionExternalComponentQueryConfig,
    EnvironmentMapExtensionExternalComponentQueryResponse,
)


class EnvironmentMapExtensionExternalComponentService(BaseService):

    @cast_models
    def query_environment_map_extension_external_component(
        self, request_body: EnvironmentMapExtensionExternalComponentQueryConfig = None
    ) -> Union[EnvironmentMapExtensionExternalComponentQueryResponse, str]:
        """For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body., defaults to None
        :type request_body: EnvironmentMapExtensionExternalComponentQueryConfig, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[EnvironmentMapExtensionExternalComponentQueryResponse, str]
        """

        Validator(
            EnvironmentMapExtensionExternalComponentQueryConfig
        ).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/EnvironmentMapExtensionExternalComponent/query",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return EnvironmentMapExtensionExternalComponentQueryResponse._unmap(
                response
            )
        if content == "application/xml":
            return EnvironmentMapExtensionExternalComponentQueryResponse._unmap(
                response
            )
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_more_environment_map_extension_external_component(
        self, request_body: str
    ) -> Union[EnvironmentMapExtensionExternalComponentQueryResponse, str]:
        """To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body.
        :type request_body: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[EnvironmentMapExtensionExternalComponentQueryResponse, str]
        """

        Validator(str).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/EnvironmentMapExtensionExternalComponent/queryMore",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body, "text/plain")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return EnvironmentMapExtensionExternalComponentQueryResponse._unmap(
                response
            )
        if content == "application/xml":
            return EnvironmentMapExtensionExternalComponentQueryResponse._unmap(
                response
            )
        raise ApiError("Error on deserializing the response.", status, response)
