
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import (
    RuntimeReleaseSchedule,
    RuntimeReleaseScheduleBulkRequest,
    RuntimeReleaseScheduleBulkResponse,
)


class RuntimeReleaseScheduleService(BaseService):

    @cast_models
    def create_runtime_release_schedule(
        self, request_body: RuntimeReleaseSchedule = None
    ) -> Union[RuntimeReleaseSchedule, str]:
        """The CREATE operation sets a schedule for receiving updates with the scheduleType, dayOfWeek, hourOfDay, and timeZone fields.

        :param request_body: The request body., defaults to None
        :type request_body: RuntimeReleaseSchedule, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[RuntimeReleaseSchedule, str]
        """

        Validator(RuntimeReleaseSchedule).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/RuntimeReleaseSchedule",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return RuntimeReleaseSchedule._unmap(response)
        if content == "application/xml":
            return RuntimeReleaseSchedule._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def get_runtime_release_schedule(
        self, id_: str
    ) -> Union[RuntimeReleaseSchedule, str]:
        """The GET operation returns the current schedule for receiving updates on a specified Runtime, Runtime cluster, or Runtime cloud.

        :param id_: The ID of the container for which you want to set a schedule.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[RuntimeReleaseSchedule, str]
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/RuntimeReleaseSchedule/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return RuntimeReleaseSchedule._unmap(response)
        if content == "application/xml":
            return RuntimeReleaseSchedule._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def update_runtime_release_schedule(
        self, id_: str, request_body: RuntimeReleaseSchedule = None
    ) -> Union[RuntimeReleaseSchedule, str]:
        """The UPDATE operation modifies a set schedule for receiving updates.

        :param request_body: The request body., defaults to None
        :type request_body: RuntimeReleaseSchedule, optional
        :param id_: The ID of the container for which you want to set a schedule.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[RuntimeReleaseSchedule, str]
        """

        Validator(RuntimeReleaseSchedule).is_optional().validate(request_body)
        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/RuntimeReleaseSchedule/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return RuntimeReleaseSchedule._unmap(response)
        if content == "application/xml":
            return RuntimeReleaseSchedule._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def delete_runtime_release_schedule(self, id_: str) -> None:
        """The DELETE operation sets the scheduleType to NEVER, meaning that the Runtime, Runtime cluster, or Runtime cloud receives updates only during the .

        :param id_: The ID of the container for which you want to set a schedule.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/RuntimeReleaseSchedule/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("DELETE")
        )

        response, status, _ = self.send_request(serialized_request)

    @cast_models
    def bulk_runtime_release_schedule(
        self, request_body: RuntimeReleaseScheduleBulkRequest = None
    ) -> Union[RuntimeReleaseScheduleBulkResponse, str]:
        """bulk_runtime_release_schedule

        :param request_body: The request body., defaults to None
        :type request_body: RuntimeReleaseScheduleBulkRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[RuntimeReleaseScheduleBulkResponse, str]
        """

        Validator(RuntimeReleaseScheduleBulkRequest).is_optional().validate(
            request_body
        )

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/RuntimeReleaseSchedule/bulk",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return RuntimeReleaseScheduleBulkResponse._unmap(response)
        if content == "application/xml":
            return RuntimeReleaseScheduleBulkResponse._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)
