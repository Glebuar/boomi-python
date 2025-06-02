
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..runtime_release_schedule import RuntimeReleaseScheduleService
from ...models import (
    RuntimeReleaseSchedule,
    RuntimeReleaseScheduleBulkResponse,
    RuntimeReleaseScheduleBulkRequest,
)


class RuntimeReleaseScheduleServiceAsync(RuntimeReleaseScheduleService):
    """
    Async Wrapper for RuntimeReleaseScheduleServiceAsync
    """

    def create_runtime_release_schedule(
        self, request_body: RuntimeReleaseSchedule = None
    ) -> Awaitable[Union[RuntimeReleaseSchedule, str]]:
        return to_async(super().create_runtime_release_schedule)(request_body)

    def get_runtime_release_schedule(
        self, id_: str
    ) -> Awaitable[Union[RuntimeReleaseSchedule, str]]:
        return to_async(super().get_runtime_release_schedule)(id_)

    def update_runtime_release_schedule(
        self, id_: str, request_body: RuntimeReleaseSchedule = None
    ) -> Awaitable[Union[RuntimeReleaseSchedule, str]]:
        return to_async(super().update_runtime_release_schedule)(id_, request_body)

    def delete_runtime_release_schedule(self, id_: str) -> Awaitable[None]:
        return to_async(super().delete_runtime_release_schedule)(id_)

    def bulk_runtime_release_schedule(
        self, request_body: RuntimeReleaseScheduleBulkRequest = None
    ) -> Awaitable[Union[RuntimeReleaseScheduleBulkResponse, str]]:
        return to_async(super().bulk_runtime_release_schedule)(request_body)
