
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..net.transport.utils import parse_xml_to_dict
from ..models import ExecutionConnectorQueryConfig, ExecutionConnectorQueryResponse


class ExecutionConnectorService(BaseService):

    @cast_models
    def query_execution_connector(
        self, request_body: ExecutionConnectorQueryConfig = None
    ) -> Union[ExecutionConnectorQueryResponse, str]:
        """For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

        - The QUERY operation allows you to query the connectors involved in a process run by filtering on attributes like executionId, actionType, successCount, and so on.
         - Requires one or more execution IDs in the request body.
         - You can filter all fields except executionConnector and id.

        :param request_body: The request body., defaults to None
        :type request_body: ExecutionConnectorQueryConfig, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[ExecutionConnectorQueryResponse, str]
        """

        Validator(ExecutionConnectorQueryConfig).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ExecutionConnector/query",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return ExecutionConnectorQueryResponse._unmap(response)
        if content == "application/xml":
            return ExecutionConnectorQueryResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_more_execution_connector(
        self, request_body: str
    ) -> Union[ExecutionConnectorQueryResponse, str]:
        """To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body.
        :type request_body: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[ExecutionConnectorQueryResponse, str]
        """

        Validator(str).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ExecutionConnector/queryMore",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body, "text/plain")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return ExecutionConnectorQueryResponse._unmap(response)
        if content == "application/xml":
            return ExecutionConnectorQueryResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)
