
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..net.transport.utils import parse_xml_to_dict
from ..models import (
    AuditLog,
    AuditLogBulkRequest,
    AuditLogBulkResponse,
    AuditLogQueryConfig,
    AuditLogQueryResponse,
)


class AuditLogService(BaseService):

    @cast_models
    def get_audit_log(self, id_: str) -> Union[AuditLog, str]:
        """Retrieve audit information for a single audit log entry, like the audit logs action message, the audit log type, action, and modifier. For example, you can use the GET operation to retrieve the environment extensions for a certain date using the document ID.

        :param id_: id_
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[AuditLog, str]
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/AuditLog/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return AuditLog._unmap(response)
        if content == "application/xml":
            return AuditLog._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def bulk_audit_log(
        self, request_body: AuditLogBulkRequest = None
    ) -> Union[AuditLogBulkResponse, str]:
        """To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

        :param request_body: The request body., defaults to None
        :type request_body: AuditLogBulkRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[AuditLogBulkResponse, str]
        """

        Validator(AuditLogBulkRequest).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/AuditLog/bulk",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return AuditLogBulkResponse._unmap(response)
        if content == "application/xml":
            return AuditLogBulkResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_audit_log(
        self, request_body: AuditLogQueryConfig = None
    ) -> Union[AuditLogQueryResponse, str]:
        """For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body., defaults to None
        :type request_body: AuditLogQueryConfig, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[AuditLogQueryResponse, str]
        """

        Validator(AuditLogQueryConfig).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/AuditLog/query",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return AuditLogQueryResponse._unmap(response)
        if content == "application/xml":
            return AuditLogQueryResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_more_audit_log(
        self, request_body: str
    ) -> Union[AuditLogQueryResponse, str]:
        """To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body.
        :type request_body: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[AuditLogQueryResponse, str]
        """

        Validator(str).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/AuditLog/queryMore",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body, "text/plain")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return AuditLogQueryResponse._unmap(response)
        if content == "application/xml":
            return AuditLogQueryResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)
