
from typing import Awaitable
from .utils.to_async import to_async
from ..worker import WorkerService


class WorkerServiceAsync(WorkerService):
    """
    Async Wrapper for WorkerServiceAsync
    """

    def create_worker(self) -> Awaitable[None]:
        return to_async(super().create_worker)()
