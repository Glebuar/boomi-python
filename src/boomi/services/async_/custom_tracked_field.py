
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..custom_tracked_field import CustomTrackedFieldService
from ...models import CustomTrackedFieldQueryResponse, CustomTrackedFieldQueryConfig


class CustomTrackedFieldServiceAsync(CustomTrackedFieldService):
    """
    Async Wrapper for CustomTrackedFieldServiceAsync
    """

    def query_custom_tracked_field(
        self, request_body: CustomTrackedFieldQueryConfig = None
    ) -> Awaitable[Union[CustomTrackedFieldQueryResponse, str]]:
        return to_async(super().query_custom_tracked_field)(request_body)

    def query_more_custom_tracked_field(
        self, request_body: str
    ) -> Awaitable[Union[CustomTrackedFieldQueryResponse, str]]:
        return to_async(super().query_more_custom_tracked_field)(request_body)
