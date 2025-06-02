
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..integration_pack_instance import IntegrationPackInstanceService
from ...models import (
    IntegrationPackInstance,
    IntegrationPackInstanceBulkResponse,
    IntegrationPackInstanceBulkRequest,
    IntegrationPackInstanceQueryResponse,
    IntegrationPackInstanceQueryConfig,
)


class IntegrationPackInstanceServiceAsync(IntegrationPackInstanceService):
    """
    Async Wrapper for IntegrationPackInstanceServiceAsync
    """

    def create_integration_pack_instance(
        self, request_body: IntegrationPackInstance = None
    ) -> Awaitable[Union[IntegrationPackInstance, str]]:
        return to_async(super().create_integration_pack_instance)(request_body)

    def get_integration_pack_instance(
        self, id_: str
    ) -> Awaitable[Union[IntegrationPackInstance, str]]:
        return to_async(super().get_integration_pack_instance)(id_)

    def delete_integration_pack_instance(self, id_: str) -> Awaitable[None]:
        return to_async(super().delete_integration_pack_instance)(id_)

    def bulk_integration_pack_instance(
        self, request_body: IntegrationPackInstanceBulkRequest = None
    ) -> Awaitable[Union[IntegrationPackInstanceBulkResponse, str]]:
        return to_async(super().bulk_integration_pack_instance)(request_body)

    def query_integration_pack_instance(
        self, request_body: IntegrationPackInstanceQueryConfig = None
    ) -> Awaitable[Union[IntegrationPackInstanceQueryResponse, str]]:
        return to_async(super().query_integration_pack_instance)(request_body)

    def query_more_integration_pack_instance(
        self, request_body: str
    ) -> Awaitable[Union[IntegrationPackInstanceQueryResponse, str]]:
        return to_async(super().query_more_integration_pack_instance)(request_body)
