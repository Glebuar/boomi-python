
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..listener_status import ListenerStatusService
from ...models import (
    AsyncOperationTokenResult,
    ListenerStatusQueryConfig,
    ListenerStatusAsyncResponse,
)


class ListenerStatusServiceAsync(ListenerStatusService):
    """
    Async Wrapper for ListenerStatusServiceAsync
    """

    def async_get_listener_status(
        self, request_body: ListenerStatusQueryConfig = None
    ) -> Awaitable[Union[AsyncOperationTokenResult, str]]:
        return to_async(super().async_get_listener_status)(request_body)

    def async_token_listener_status(
        self, token: str
    ) -> Awaitable[Union[ListenerStatusAsyncResponse, str]]:
        return to_async(super().async_token_listener_status)(token)
