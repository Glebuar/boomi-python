
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..process import ProcessService
from ...models import (
    Process,
    ProcessBulkResponse,
    ProcessBulkRequest,
    ProcessQueryResponse,
    ProcessQueryConfig,
)


class ProcessServiceAsync(ProcessService):
    """
    Async Wrapper for ProcessServiceAsync
    """

    def get_process(self, id_: str) -> Awaitable[Union[Process, str]]:
        return to_async(super().get_process)(id_)

    def bulk_process(
        self, request_body: ProcessBulkRequest = None
    ) -> Awaitable[Union[ProcessBulkResponse, str]]:
        return to_async(super().bulk_process)(request_body)

    def query_process(
        self, request_body: ProcessQueryConfig = None
    ) -> Awaitable[Union[ProcessQueryResponse, str]]:
        return to_async(super().query_process)(request_body)

    def query_more_process(
        self, request_body: str
    ) -> Awaitable[Union[ProcessQueryResponse, str]]:
        return to_async(super().query_more_process)(request_body)
