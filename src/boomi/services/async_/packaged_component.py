
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..packaged_component import PackagedComponentService
from ...models import (
    PackagedComponent,
    PackagedComponentBulkResponse,
    PackagedComponentBulkRequest,
    PackagedComponentQueryResponse,
    PackagedComponentQueryConfig,
)


class PackagedComponentServiceAsync(PackagedComponentService):
    """
    Async Wrapper for PackagedComponentServiceAsync
    """

    def create_packaged_component(
        self, request_body: PackagedComponent = None
    ) -> Awaitable[Union[PackagedComponent, str]]:
        return to_async(super().create_packaged_component)(request_body)

    def get_packaged_component(
        self, id_: str
    ) -> Awaitable[Union[PackagedComponent, str]]:
        return to_async(super().get_packaged_component)(id_)

    def delete_packaged_component(self, id_: str) -> Awaitable[None]:
        return to_async(super().delete_packaged_component)(id_)

    def bulk_packaged_component(
        self, request_body: PackagedComponentBulkRequest = None
    ) -> Awaitable[Union[PackagedComponentBulkResponse, str]]:
        return to_async(super().bulk_packaged_component)(request_body)

    def query_packaged_component(
        self, request_body: PackagedComponentQueryConfig = None
    ) -> Awaitable[Union[PackagedComponentQueryResponse, str]]:
        return to_async(super().query_packaged_component)(request_body)

    def query_more_packaged_component(
        self, request_body: str
    ) -> Awaitable[Union[PackagedComponentQueryResponse, str]]:
        return to_async(super().query_more_packaged_component)(request_body)
