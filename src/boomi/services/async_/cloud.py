
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..cloud import CloudService
from ...models import (
    Cloud,
    CloudBulkResponse,
    CloudBulkRequest,
    CloudQueryResponse,
    CloudQueryConfig,
)


class CloudServiceAsync(CloudService):
    """
    Async Wrapper for CloudServiceAsync
    """

    def get_cloud(self, id_: str) -> Awaitable[Union[Cloud, str]]:
        return to_async(super().get_cloud)(id_)

    def bulk_cloud(
        self, request_body: CloudBulkRequest = None
    ) -> Awaitable[Union[CloudBulkResponse, str]]:
        return to_async(super().bulk_cloud)(request_body)

    def query_cloud(
        self, request_body: CloudQueryConfig = None
    ) -> Awaitable[Union[CloudQueryResponse, str]]:
        return to_async(super().query_cloud)(request_body)

    def query_more_cloud(
        self, request_body: str
    ) -> Awaitable[Union[CloudQueryResponse, str]]:
        return to_async(super().query_more_cloud)(request_body)
