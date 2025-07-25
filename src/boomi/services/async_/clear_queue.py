
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..clear_queue import ClearQueueService
from ...models import ClearQueueRequest


class ClearQueueServiceAsync(ClearQueueService):
    """
    Async Wrapper for ClearQueueServiceAsync
    """

    def execute_clear_queue(
        self, id_: str, request_body: ClearQueueRequest = None
    ) -> Awaitable[Union[ClearQueueRequest, str]]:
        return to_async(super().execute_clear_queue)(id_, request_body)
