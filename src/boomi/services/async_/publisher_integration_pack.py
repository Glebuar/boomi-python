
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..publisher_integration_pack import PublisherIntegrationPackService
from ...models import (
    PublisherIntegrationPack,
    PublisherIntegrationPackBulkResponse,
    PublisherIntegrationPackBulkRequest,
    PublisherIntegrationPackQueryResponse,
    PublisherIntegrationPackQueryConfig,
)


class PublisherIntegrationPackServiceAsync(PublisherIntegrationPackService):
    """
    Async Wrapper for PublisherIntegrationPackServiceAsync
    """

    def create_publisher_integration_pack(
        self, request_body: PublisherIntegrationPack = None
    ) -> Awaitable[Union[PublisherIntegrationPack, str]]:
        return to_async(super().create_publisher_integration_pack)(request_body)

    def get_publisher_integration_pack(
        self, id_: str
    ) -> Awaitable[Union[PublisherIntegrationPack, str]]:
        return to_async(super().get_publisher_integration_pack)(id_)

    def update_publisher_integration_pack(
        self, id_: str, request_body: PublisherIntegrationPack = None
    ) -> Awaitable[Union[PublisherIntegrationPack, str]]:
        return to_async(super().update_publisher_integration_pack)(id_, request_body)

    def delete_publisher_integration_pack(self, id_: str) -> Awaitable[None]:
        return to_async(super().delete_publisher_integration_pack)(id_)

    def bulk_publisher_integration_pack(
        self, request_body: PublisherIntegrationPackBulkRequest = None
    ) -> Awaitable[Union[PublisherIntegrationPackBulkResponse, str, any]]:
        return to_async(super().bulk_publisher_integration_pack)(request_body)

    def query_publisher_integration_pack(
        self, request_body: PublisherIntegrationPackQueryConfig = None
    ) -> Awaitable[Union[PublisherIntegrationPackQueryResponse, str]]:
        return to_async(super().query_publisher_integration_pack)(request_body)

    def query_more_publisher_integration_pack(
        self, request_body: str
    ) -> Awaitable[Union[PublisherIntegrationPackQueryResponse, str]]:
        return to_async(super().query_more_publisher_integration_pack)(request_body)
