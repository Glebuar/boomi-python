
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..persisted_process_properties import PersistedProcessPropertiesService
from ...models import PersistedProcessProperties


class PersistedProcessPropertiesServiceAsync(PersistedProcessPropertiesService):
    """
    Async Wrapper for PersistedProcessPropertiesServiceAsync
    """

    def update_persisted_process_properties(
        self, id_: str, request_body: PersistedProcessProperties = None
    ) -> Awaitable[Union[PersistedProcessProperties, str]]:
        return to_async(super().update_persisted_process_properties)(id_, request_body)
