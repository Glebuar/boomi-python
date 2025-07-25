
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..account_user_role import AccountUserRoleService
from ...models import (
    AccountUserRole,
    AccountUserRoleQueryResponse,
    AccountUserRoleQueryConfig,
)


class AccountUserRoleServiceAsync(AccountUserRoleService):
    """
    Async Wrapper for AccountUserRoleServiceAsync
    """

    def create_account_user_role(
        self, request_body: AccountUserRole = None
    ) -> Awaitable[Union[AccountUserRole, str]]:
        return to_async(super().create_account_user_role)(request_body)

    def query_account_user_role(
        self, request_body: AccountUserRoleQueryConfig = None
    ) -> Awaitable[Union[AccountUserRoleQueryResponse, str]]:
        return to_async(super().query_account_user_role)(request_body)

    def query_more_account_user_role(
        self, request_body: str
    ) -> Awaitable[Union[AccountUserRoleQueryResponse, str]]:
        return to_async(super().query_more_account_user_role)(request_body)

    def delete_account_user_role(self, id_: str) -> Awaitable[None]:
        return to_async(super().delete_account_user_role)(id_)
