
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..persisted_process_properties import PersistedProcessPropertiesService
from ...models import (
    PersistedProcessProperties,
    AsyncOperationTokenResult,
    PersistedProcessPropertiesAsyncResponse
)


class PersistedProcessPropertiesServiceAsync(PersistedProcessPropertiesService):
    """
    Async Wrapper for PersistedProcessPropertiesServiceAsync
    """

    def update_persisted_process_properties(
        self, id_: str, request_body: PersistedProcessProperties = None
    ) -> Awaitable[Union[PersistedProcessProperties, str]]:
        return to_async(super().update_persisted_process_properties)(id_, request_body)

    def async_get_persisted_process_properties(
        self, id_: str
    ) -> Awaitable[Union[AsyncOperationTokenResult, str]]:
        return to_async(super().async_get_persisted_process_properties)(id_)

    def async_token_persisted_process_properties(
        self, token: str
    ) -> Awaitable[Union[PersistedProcessPropertiesAsyncResponse, str]]:
        return to_async(super().async_token_persisted_process_properties)(token)
