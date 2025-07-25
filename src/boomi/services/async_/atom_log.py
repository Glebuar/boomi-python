
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..atom_log import AtomLogService
from ...models import LogDownload, AtomLog


class AtomLogServiceAsync(AtomLogService):
    """
    Async Wrapper for AtomLogServiceAsync
    """

    def create_atom_log(
        self, request_body: AtomLog = None
    ) -> Awaitable[Union[LogDownload, str]]:
        return to_async(super().create_atom_log)(request_body)
