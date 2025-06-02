
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import (
    GenericConnectorRecord,
    GenericConnectorRecordBulkRequest,
    GenericConnectorRecordBulkResponse,
    GenericConnectorRecordQueryConfig,
    GenericConnectorRecordQueryResponse,
)


class GenericConnectorRecordService(BaseService):

    @cast_models
    def get_generic_connector_record(
        self, id_: str
    ) -> Union[GenericConnectorRecord, str]:
        """Allows you to view document metadata for exactly one document based on the provided id.

        :param id_: The ID of the GenericConnectorRecord. You obtain this ID from querying the GenericConnectorRecord object.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[GenericConnectorRecord, str]
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/GenericConnectorRecord/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return GenericConnectorRecord._unmap(response)
        if content == "application/xml":
            return GenericConnectorRecord._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def bulk_generic_connector_record(
        self, request_body: GenericConnectorRecordBulkRequest = None
    ) -> Union[GenericConnectorRecordBulkResponse, str]:
        """To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

        :param request_body: The request body., defaults to None
        :type request_body: GenericConnectorRecordBulkRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[GenericConnectorRecordBulkResponse, str]
        """

        Validator(GenericConnectorRecordBulkRequest).is_optional().validate(
            request_body
        )

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/GenericConnectorRecord/bulk",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return GenericConnectorRecordBulkResponse._unmap(response)
        if content == "application/xml":
            return GenericConnectorRecordBulkResponse._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_generic_connector_record(
        self, request_body: GenericConnectorRecordQueryConfig = None
    ) -> Union[GenericConnectorRecordQueryResponse, str]:
        """- The QUERY operation allows you to view document metadata for all documents in the run. You must query by exactly one `executionId`.
         - You cannot query `connectorFields`.

         For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body., defaults to None
        :type request_body: GenericConnectorRecordQueryConfig, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[GenericConnectorRecordQueryResponse, str]
        """

        Validator(GenericConnectorRecordQueryConfig).is_optional().validate(
            request_body
        )

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/GenericConnectorRecord/query",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return GenericConnectorRecordQueryResponse._unmap(response)
        if content == "application/xml":
            return GenericConnectorRecordQueryResponse._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_more_generic_connector_record(
        self, request_body: str
    ) -> Union[GenericConnectorRecordQueryResponse, str]:
        """To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body.
        :type request_body: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[GenericConnectorRecordQueryResponse, str]
        """

        Validator(str).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/GenericConnectorRecord/queryMore",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body, "text/plain")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return GenericConnectorRecordQueryResponse._unmap(response)
        if content == "application/xml":
            return GenericConnectorRecordQueryResponse._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)
