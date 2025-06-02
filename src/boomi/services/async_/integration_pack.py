
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..integration_pack import IntegrationPackService
from ...models import (
    IntegrationPack,
    IntegrationPackBulkResponse,
    IntegrationPackBulkRequest,
    IntegrationPackQueryResponse,
    IntegrationPackQueryConfig,
)


class IntegrationPackServiceAsync(IntegrationPackService):
    """
    Async Wrapper for IntegrationPackServiceAsync
    """

    def get_integration_pack(self, id_: str) -> Awaitable[Union[IntegrationPack, str]]:
        return to_async(super().get_integration_pack)(id_)

    def bulk_integration_pack(
        self, request_body: IntegrationPackBulkRequest = None
    ) -> Awaitable[Union[IntegrationPackBulkResponse, str]]:
        return to_async(super().bulk_integration_pack)(request_body)

    def query_integration_pack(
        self, request_body: IntegrationPackQueryConfig = None
    ) -> Awaitable[Union[IntegrationPackQueryResponse, str]]:
        return to_async(super().query_integration_pack)(request_body)

    def query_more_integration_pack(
        self, request_body: str
    ) -> Awaitable[Union[IntegrationPackQueryResponse, str]]:
        return to_async(super().query_more_integration_pack)(request_body)
