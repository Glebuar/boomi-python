
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..process_log import ProcessLogService
from ...models import LogDownload, ProcessLog


class ProcessLogServiceAsync(ProcessLogService):
    """
    Async Wrapper for ProcessLogServiceAsync
    """

    def create_process_log(
        self, request_body: ProcessLog = None
    ) -> Awaitable[Union[LogDownload, str]]:
        return to_async(super().create_process_log)(request_body)
