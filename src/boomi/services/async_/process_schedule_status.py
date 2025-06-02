
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..process_schedule_status import ProcessScheduleStatusService
from ...models import (
    ProcessScheduleStatus,
    ProcessScheduleStatusBulkResponse,
    ProcessScheduleStatusBulkRequest,
    ProcessScheduleStatusQueryResponse,
    ProcessScheduleStatusQueryConfig,
)


class ProcessScheduleStatusServiceAsync(ProcessScheduleStatusService):
    """
    Async Wrapper for ProcessScheduleStatusServiceAsync
    """

    def get_process_schedule_status(
        self, id_: str
    ) -> Awaitable[Union[ProcessScheduleStatus, str]]:
        return to_async(super().get_process_schedule_status)(id_)

    def update_process_schedule_status(
        self, id_: str, request_body: ProcessScheduleStatus = None
    ) -> Awaitable[Union[ProcessScheduleStatus, str]]:
        return to_async(super().update_process_schedule_status)(id_, request_body)

    def bulk_process_schedule_status(
        self, request_body: ProcessScheduleStatusBulkRequest = None
    ) -> Awaitable[Union[ProcessScheduleStatusBulkResponse, str]]:
        return to_async(super().bulk_process_schedule_status)(request_body)

    def query_process_schedule_status(
        self, request_body: ProcessScheduleStatusQueryConfig = None
    ) -> Awaitable[Union[ProcessScheduleStatusQueryResponse, str]]:
        return to_async(super().query_process_schedule_status)(request_body)

    def query_more_process_schedule_status(
        self, request_body: str
    ) -> Awaitable[Union[ProcessScheduleStatusQueryResponse, str]]:
        return to_async(super().query_more_process_schedule_status)(request_body)
