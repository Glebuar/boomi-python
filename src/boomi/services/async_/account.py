
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..account import AccountService
from ...models import (
    Account,
    AccountBulkResponse,
    AccountBulkRequest,
    AccountQueryResponse,
    AccountQueryConfig,
)


class AccountServiceAsync(AccountService):
    """
    Async Wrapper for AccountServiceAsync
    """

    def get_account(self, id_: str) -> Awaitable[Union[Account, str]]:
        return to_async(super().get_account)(id_)

    def bulk_account(
        self, request_body: AccountBulkRequest = None
    ) -> Awaitable[Union[AccountBulkResponse, str]]:
        return to_async(super().bulk_account)(request_body)

    def query_account(
        self, request_body: AccountQueryConfig = None
    ) -> Awaitable[Union[AccountQueryResponse, str]]:
        return to_async(super().query_account)(request_body)

    def query_more_account(
        self, request_body: str
    ) -> Awaitable[Union[AccountQueryResponse, str]]:
        return to_async(super().query_more_account)(request_body)
