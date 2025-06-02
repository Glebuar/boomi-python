
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..component import ComponentService
from ...models import Component, ComponentBulkResponse, ComponentBulkRequest


class ComponentServiceAsync(ComponentService):
    """
    Async Wrapper for ComponentServiceAsync
    """

    def create_component(
        self, request_body: str = None
    ) -> Awaitable[Union[Component, str]]:
        return to_async(super().create_component)(request_body)

    def get_component(self, component_id: str) -> Awaitable[Union[Component, str]]:
        return to_async(super().get_component)(component_id)

    def update_component(
        self, component_id: str, request_body: str = None
    ) -> Awaitable[Union[Component, str]]:
        return to_async(super().update_component)(component_id, request_body)

    def bulk_component(
        self, request_body: ComponentBulkRequest = None
    ) -> Awaitable[str]:
        return to_async(super().bulk_component)(request_body)
