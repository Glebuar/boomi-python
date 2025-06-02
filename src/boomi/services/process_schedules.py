
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..net.transport.utils import parse_xml_to_dict
from ..models import (
    ProcessSchedules,
    ProcessSchedulesBulkRequest,
    ProcessSchedulesBulkResponse,
    ProcessSchedulesQueryConfig,
    ProcessSchedulesQueryResponse,
)


class ProcessSchedulesService(BaseService):

    @cast_models
    def get_process_schedules(self, id_: str) -> Union[ProcessSchedules, str]:
        """Retrieves the Process Schedules object with a specific conceptual ID.

         The ordinary GET operation retrieves the Process Schedules object with a specific conceptual ID. The bulk GET operation retrieves the Process Schedules objects with specific conceptual IDs to a maximum of 100. In addition, you can obtain conceptual IDs from the QUERY operation.

        :param id_: The object’s conceptual ID, which is synthesized from the process and Runtime IDs.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[ProcessSchedules, str]
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ProcessSchedules/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return ProcessSchedules._unmap(response)
        if content == "application/xml":
            return ProcessSchedules._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def update_process_schedules(
        self, id_: str, request_body: ProcessSchedules = None
    ) -> Union[ProcessSchedules, str]:
        """Clears and updates the process run schedules specified in the Process Schedules object with a specific ID. The body of the request must specify not only the conceptual object ID but also the Runtime and process IDs. You can obtain the object ID from a QUERY operation.

        A Process Schedules object exists for every deployed process. If you do not update the schedule, the object is empty and a run schedule is not in effect.

        >**Note:** Listener processes cannot be scheduled. If a listener process is referenced, the call will fail with a 400 status code.

        You must have the **Runtime Management** privilege and the **Scheduling** privilege to perform the UPDATE operation. If you have the **Runtime Management Read Access** privilege, you cannot update process run schedules.

        >**Note:** After you update run schedules for a process on a Runtime, those schedules appear in the **Scheduling** dialog using the Advanced (cron) syntax.

        You can additionally employ a Bulk UPDATE operation for the Process Schedules object. See related links for more information about performing a Bulk UPDATE operation.

        :param request_body: The request body., defaults to None
        :type request_body: ProcessSchedules, optional
        :param id_: The object’s conceptual ID, which is synthesized from the process and Runtime IDs.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[ProcessSchedules, str]
        """

        Validator(ProcessSchedules).is_optional().validate(request_body)
        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ProcessSchedules/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return ProcessSchedules._unmap(response)
        if content == "application/xml":
            return ProcessSchedules._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def bulk_process_schedules(
        self, request_body: ProcessSchedulesBulkRequest = None
    ) -> Union[ProcessSchedulesBulkResponse, str]:
        """To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

        :param request_body: The request body., defaults to None
        :type request_body: ProcessSchedulesBulkRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[ProcessSchedulesBulkResponse, str]
        """

        Validator(ProcessSchedulesBulkRequest).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ProcessSchedules/bulk",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return ProcessSchedulesBulkResponse._unmap(response)
        if content == "application/xml":
            return ProcessSchedulesBulkResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_process_schedules(
        self, request_body: ProcessSchedulesQueryConfig = None
    ) -> Union[ProcessSchedulesQueryResponse, str]:
        """For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body., defaults to None
        :type request_body: ProcessSchedulesQueryConfig, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[ProcessSchedulesQueryResponse, str]
        """

        Validator(ProcessSchedulesQueryConfig).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ProcessSchedules/query",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return ProcessSchedulesQueryResponse._unmap(response)
        if content == "application/xml":
            return ProcessSchedulesQueryResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_more_process_schedules(
        self, request_body: str
    ) -> Union[ProcessSchedulesQueryResponse, str]:
        """To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body.
        :type request_body: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[ProcessSchedulesQueryResponse, str]
        """

        Validator(str).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ProcessSchedules/queryMore",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body, "text/plain")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return ProcessSchedulesQueryResponse._unmap(response)
        if content == "application/xml":
            return ProcessSchedulesQueryResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)
