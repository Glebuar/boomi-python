
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..net.transport.utils import parse_xml_to_dict
from ..models import (
    ProcessScheduleStatus,
    ProcessScheduleStatusBulkRequest,
    ProcessScheduleStatusBulkResponse,
    ProcessScheduleStatusQueryConfig,
    ProcessScheduleStatusQueryResponse,
)


class ProcessScheduleStatusService(BaseService):

    @cast_models
    def get_process_schedule_status(
        self, id_: str
    ) -> Union[ProcessScheduleStatus, str]:
        """Retrieves the Process Schedule Status object with a specified conceptual ID.

         The ordinary GET operation retrieves the Process Schedules object with a specific conceptual ID. The bulk GET operation retrieves the Process Schedules objects with specific conceptual IDs to a maximum of 100. In addition, you can obtain conceptual IDs from the QUERY operation.

        :param id_: The object’s conceptual ID, which is synthesized from the process and Runtime IDs.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[ProcessScheduleStatus, str]
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ProcessScheduleStatus/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return ProcessScheduleStatus._unmap(response)
        if content == "application/xml":
            return ProcessScheduleStatus._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def update_process_schedule_status(
        self, id_: str, request_body: ProcessScheduleStatus = None
    ) -> Union[ProcessScheduleStatus, str]:
        """Stops or resumes process run schedules for a deployed process.

         The body of the request must specify not only the conceptual Process Schedule Status object ID but also the Runtime and process IDs. You can obtain the object ID from a QUERY operation.

         You must have the Runtime Management privilege and the Scheduling privilege to perform the UPDATE operation. If you have the Runtime Management Read Accessprivilege, you cannot update the status of process run schedules.

        :param request_body: The request body., defaults to None
        :type request_body: ProcessScheduleStatus, optional
        :param id_: id_
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[ProcessScheduleStatus, str]
        """

        Validator(ProcessScheduleStatus).is_optional().validate(request_body)
        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ProcessScheduleStatus/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return ProcessScheduleStatus._unmap(response)
        if content == "application/xml":
            return ProcessScheduleStatus._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def bulk_process_schedule_status(
        self, request_body: ProcessScheduleStatusBulkRequest = None
    ) -> Union[ProcessScheduleStatusBulkResponse, str]:
        """To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

        :param request_body: The request body., defaults to None
        :type request_body: ProcessScheduleStatusBulkRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[ProcessScheduleStatusBulkResponse, str]
        """

        Validator(ProcessScheduleStatusBulkRequest).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ProcessScheduleStatus/bulk",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return ProcessScheduleStatusBulkResponse._unmap(response)
        if content == "application/xml":
            return ProcessScheduleStatusBulkResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_process_schedule_status(
        self, request_body: ProcessScheduleStatusQueryConfig = None
    ) -> Union[ProcessScheduleStatusQueryResponse, str]:
        """For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body., defaults to None
        :type request_body: ProcessScheduleStatusQueryConfig, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[ProcessScheduleStatusQueryResponse, str]
        """

        Validator(ProcessScheduleStatusQueryConfig).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ProcessScheduleStatus/query",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return ProcessScheduleStatusQueryResponse._unmap(response)
        if content == "application/xml":
            return ProcessScheduleStatusQueryResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_more_process_schedule_status(
        self, request_body: str
    ) -> Union[ProcessScheduleStatusQueryResponse, str]:
        """To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body.
        :type request_body: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[ProcessScheduleStatusQueryResponse, str]
        """

        Validator(str).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ProcessScheduleStatus/queryMore",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body, "text/plain")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return ProcessScheduleStatusQueryResponse._unmap(response)
        if content == "application/xml":
            return ProcessScheduleStatusQueryResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)
