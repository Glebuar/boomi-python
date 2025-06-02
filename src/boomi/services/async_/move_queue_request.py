
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..move_queue_request import MoveQueueRequestService
from ...models import MoveQueueRequest


class MoveQueueRequestServiceAsync(MoveQueueRequestService):
    """
    Async Wrapper for MoveQueueRequestServiceAsync
    """

    def create_move_queue_request(
        self, request_body: MoveQueueRequest = None
    ) -> Awaitable[Union[MoveQueueRequest, str]]:
        return to_async(super().create_move_queue_request)(request_body)
