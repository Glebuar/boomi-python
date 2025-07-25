
from typing import Awaitable
from .utils.to_async import to_async
from ..cancel_execution import CancelExecutionService


class CancelExecutionServiceAsync(CancelExecutionService):
    """
    Async Wrapper for CancelExecutionServiceAsync
    """

    def get_cancel_execution(self) -> Awaitable[None]:
        return to_async(super().get_cancel_execution)()
