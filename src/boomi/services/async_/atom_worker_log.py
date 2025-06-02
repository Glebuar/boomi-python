
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..atom_worker_log import AtomWorkerLogService
from ...models import LogDownload, AtomWorkerLog


class AtomWorkerLogServiceAsync(AtomWorkerLogService):
    """
    Async Wrapper for AtomWorkerLogServiceAsync
    """

    def create_atom_worker_log(
        self, request_body: AtomWorkerLog = None
    ) -> Awaitable[Union[LogDownload, str]]:
        return to_async(super().create_atom_worker_log)(request_body)
