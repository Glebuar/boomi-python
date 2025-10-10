
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..account_group import AccountGroupService
from ...models import (
    AccountGroup,
    AccountGroupBulkResponse,
    AccountGroupBulkRequest,
    AccountGroupQueryResponse,
    AccountGroupQueryConfig,
)


class AccountGroupServiceAsync(AccountGroupService):
    """
    Async Wrapper for AccountGroupServiceAsync
    """

    def create_account_group(
        self, request_body: AccountGroup = None
    ) -> Awaitable[Union[AccountGroup, str]]:
        return to_async(super().create_account_group)(request_body)

    def get_account_group(self, id_: str) -> Awaitable[Union[AccountGroup, str]]:
        return to_async(super().get_account_group)(id_)

    def update_account_group(
        self, id_: str, request_body: AccountGroup = None
    ) -> Awaitable[Union[AccountGroup, str]]:
        return to_async(super().update_account_group)(id_, request_body)

    def bulk_account_group(
        self, request_body: AccountGroupBulkRequest = None
    ) -> Awaitable[Union[AccountGroupBulkResponse, str]]:
        return to_async(super().bulk_account_group)(request_body)

    def query_account_group(
        self, request_body: AccountGroupQueryConfig = None
    ) -> Awaitable[Union[AccountGroupQueryResponse, str]]:
        return to_async(super().query_account_group)(request_body)

    def query_more_account_group(
        self, request_body: str
    ) -> Awaitable[Union[AccountGroupQueryResponse, str]]:
        return to_async(super().query_more_account_group)(request_body)
