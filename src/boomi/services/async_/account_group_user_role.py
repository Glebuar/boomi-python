
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..account_group_user_role import AccountGroupUserRoleService
from ...models import (
    AccountGroupUserRole,
    AccountGroupUserRoleQueryResponse,
    AccountGroupUserRoleQueryConfig,
)


class AccountGroupUserRoleServiceAsync(AccountGroupUserRoleService):
    """
    Async Wrapper for AccountGroupUserRoleServiceAsync
    """

    def create_account_group_user_role(
        self, request_body: AccountGroupUserRole = None
    ) -> Awaitable[Union[AccountGroupUserRole, str]]:
        return to_async(super().create_account_group_user_role)(request_body)

    def query_account_group_user_role(
        self, request_body: AccountGroupUserRoleQueryConfig = None
    ) -> Awaitable[Union[AccountGroupUserRoleQueryResponse, str]]:
        return to_async(super().query_account_group_user_role)(request_body)

    def query_more_account_group_user_role(
        self, request_body: str
    ) -> Awaitable[Union[AccountGroupUserRoleQueryResponse, str]]:
        return to_async(super().query_more_account_group_user_role)(request_body)

    def delete_account_group_user_role(self, id_: str) -> Awaitable[None]:
        return to_async(super().delete_account_group_user_role)(id_)
