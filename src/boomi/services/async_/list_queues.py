
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..list_queues import ListQueuesService
from ...models import ListQueuesAsyncResponse, AsyncOperationTokenResult


class ListQueuesServiceAsync(ListQueuesService):
    """
    Async Wrapper for ListQueuesServiceAsync
    """

    def async_token_list_queues(
        self, token: str
    ) -> Awaitable[Union[ListQueuesAsyncResponse, str]]:
        return to_async(super().async_token_list_queues)(token)

    def async_get_list_queues(
        self, id_: str
    ) -> Awaitable[Union[AsyncOperationTokenResult, str]]:
        return to_async(super().async_get_list_queues)(id_)
