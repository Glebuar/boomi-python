
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..account_sso_config import AccountSsoConfigService
from ...models import (
    AccountSsoConfig,
    AccountSsoConfigBulkResponse,
    AccountSsoConfigBulkRequest,
)


class AccountSsoConfigServiceAsync(AccountSsoConfigService):
    """
    Async Wrapper for AccountSsoConfigServiceAsync
    """

    def get_account_sso_config(
        self, id_: str
    ) -> Awaitable[Union[AccountSsoConfig, str]]:
        return to_async(super().get_account_sso_config)(id_)

    def update_account_sso_config(
        self, id_: str, request_body: AccountSsoConfig = None
    ) -> Awaitable[Union[AccountSsoConfig, str]]:
        return to_async(super().update_account_sso_config)(id_, request_body)

    def delete_account_sso_config(self, id_: str) -> Awaitable[None]:
        return to_async(super().delete_account_sso_config)(id_)

    def bulk_account_sso_config(
        self, request_body: AccountSsoConfigBulkRequest = None
    ) -> Awaitable[Union[AccountSsoConfigBulkResponse, str]]:
        return to_async(super().bulk_account_sso_config)(request_body)
