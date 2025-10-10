
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..process_schedules import ProcessSchedulesService
from ...models import (
    ProcessSchedules,
    ProcessSchedulesBulkResponse,
    ProcessSchedulesBulkRequest,
    ProcessSchedulesQueryResponse,
    ProcessSchedulesQueryConfig,
)


class ProcessSchedulesServiceAsync(ProcessSchedulesService):
    """
    Async Wrapper for ProcessSchedulesServiceAsync
    """

    def get_process_schedules(
        self, id_: str
    ) -> Awaitable[Union[ProcessSchedules, str]]:
        return to_async(super().get_process_schedules)(id_)

    def update_process_schedules(
        self, id_: str, request_body: ProcessSchedules = None
    ) -> Awaitable[Union[ProcessSchedules, str]]:
        return to_async(super().update_process_schedules)(id_, request_body)

    def bulk_process_schedules(
        self, request_body: ProcessSchedulesBulkRequest = None
    ) -> Awaitable[Union[ProcessSchedulesBulkResponse, str]]:
        return to_async(super().bulk_process_schedules)(request_body)

    def query_process_schedules(
        self, request_body: ProcessSchedulesQueryConfig = None
    ) -> Awaitable[Union[ProcessSchedulesQueryResponse, str]]:
        return to_async(super().query_process_schedules)(request_body)

    def query_more_process_schedules(
        self, request_body: str
    ) -> Awaitable[Union[ProcessSchedulesQueryResponse, str]]:
        return to_async(super().query_more_process_schedules)(request_body)
