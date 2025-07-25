
from typing import Awaitable
from .utils.to_async import to_async
from ..execute_process import ExecuteProcessService


class ExecuteProcessServiceAsync(ExecuteProcessService):
    """
    Async Wrapper for ExecuteProcessServiceAsync
    """

    def create_execute_process(self) -> Awaitable[None]:
        return to_async(super().create_execute_process)()
