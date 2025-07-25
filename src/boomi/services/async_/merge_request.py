
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..merge_request import MergeRequestService
from ...models import (
    MergeRequest,
    MergeRequestBulkResponse,
    MergeRequestBulkRequest,
    MergeRequestQueryResponse,
    MergeRequestQueryConfig,
)


class MergeRequestServiceAsync(MergeRequestService):
    """
    Async Wrapper for MergeRequestServiceAsync
    """

    def create_merge_request(
        self, request_body: MergeRequest = None
    ) -> Awaitable[Union[MergeRequest, str]]:
        return to_async(super().create_merge_request)(request_body)

    def get_merge_request(self, id_: str) -> Awaitable[Union[MergeRequest, str]]:
        return to_async(super().get_merge_request)(id_)

    def update_merge_request(
        self, id_: str, request_body: MergeRequest = None
    ) -> Awaitable[Union[MergeRequest, str]]:
        return to_async(super().update_merge_request)(id_, request_body)

    def delete_merge_request(self, id_: str) -> Awaitable[None]:
        return to_async(super().delete_merge_request)(id_)

    def bulk_merge_request(
        self, request_body: MergeRequestBulkRequest = None
    ) -> Awaitable[Union[MergeRequestBulkResponse, str]]:
        return to_async(super().bulk_merge_request)(request_body)

    def execute_merge_request(
        self, id_: str, request_body: MergeRequest = None
    ) -> Awaitable[Union[MergeRequest, str]]:
        return to_async(super().execute_merge_request)(id_, request_body)

    def query_merge_request(
        self, request_body: MergeRequestQueryConfig = None
    ) -> Awaitable[Union[MergeRequestQueryResponse, str]]:
        return to_async(super().query_merge_request)(request_body)

    def query_more_merge_request(
        self, request_body: str
    ) -> Awaitable[Union[MergeRequestQueryResponse, str]]:
        return to_async(super().query_more_merge_request)(request_body)
