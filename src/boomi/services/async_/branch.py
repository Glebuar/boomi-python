
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..branch import BranchService
from ...models import (
    Branch,
    BranchBulkResponse,
    BranchBulkRequest,
    BranchQueryResponse,
    BranchQueryConfig,
)


class BranchServiceAsync(BranchService):
    """
    Async Wrapper for BranchServiceAsync
    """

    def create_branch(
        self, request_body: Branch = None
    ) -> Awaitable[Union[Branch, str]]:
        return to_async(super().create_branch)(request_body)

    def get_branch(self, id_: str) -> Awaitable[Union[Branch, str]]:
        return to_async(super().get_branch)(id_)

    def update_branch(
        self, id_: str, request_body: Branch = None
    ) -> Awaitable[Union[Branch, str]]:
        return to_async(super().update_branch)(id_, request_body)

    def delete_branch(self, id_: str) -> Awaitable[None]:
        return to_async(super().delete_branch)(id_)

    def bulk_branch(
        self, request_body: BranchBulkRequest = None
    ) -> Awaitable[Union[BranchBulkResponse, str]]:
        return to_async(super().bulk_branch)(request_body)

    def query_branch(
        self, request_body: BranchQueryConfig = None
    ) -> Awaitable[Union[BranchQueryResponse, str]]:
        return to_async(super().query_branch)(request_body)

    def query_more_branch(
        self, request_body: str
    ) -> Awaitable[Union[BranchQueryResponse, str]]:
        return to_async(super().query_more_branch)(request_body)
