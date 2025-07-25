
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..change_listener_status import ChangeListenerStatusService
from ...models import ChangeListenerStatusRequest


class ChangeListenerStatusServiceAsync(ChangeListenerStatusService):
    """
    Async Wrapper for ChangeListenerStatusServiceAsync
    """

    def create_change_listener_status(
        self, request_body: ChangeListenerStatusRequest = None
    ) -> Awaitable[None]:
        return to_async(super().create_change_listener_status)(request_body)
