
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..account_group_account import AccountGroupAccountService
from ...models import (
    AccountGroupAccount,
    AccountGroupAccountQueryResponse,
    AccountGroupAccountQueryConfig,
)


class AccountGroupAccountServiceAsync(AccountGroupAccountService):
    """
    Async Wrapper for AccountGroupAccountServiceAsync
    """

    def create_account_group_account(
        self, request_body: AccountGroupAccount = None
    ) -> Awaitable[Union[AccountGroupAccount, str]]:
        return to_async(super().create_account_group_account)(request_body)

    def query_account_group_account(
        self, request_body: AccountGroupAccountQueryConfig = None
    ) -> Awaitable[Union[AccountGroupAccountQueryResponse, str]]:
        return to_async(super().query_account_group_account)(request_body)

    def query_more_account_group_account(
        self, request_body: str
    ) -> Awaitable[Union[AccountGroupAccountQueryResponse, str]]:
        return to_async(super().query_more_account_group_account)(request_body)

    def delete_account_group_account(self, id_: str) -> Awaitable[None]:
        return to_async(super().delete_account_group_account)(id_)
