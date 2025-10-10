
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..account_user_federation import AccountUserFederationService
from ...models import (
    AccountUserFederation,
    AccountUserFederationQueryResponse,
    AccountUserFederationQueryConfig,
)


class AccountUserFederationServiceAsync(AccountUserFederationService):
    """
    Async Wrapper for AccountUserFederationServiceAsync
    """

    def create_account_user_federation(
        self, request_body: AccountUserFederation = None
    ) -> Awaitable[Union[AccountUserFederation, str]]:
        return to_async(super().create_account_user_federation)(request_body)

    def query_account_user_federation(
        self, request_body: AccountUserFederationQueryConfig = None
    ) -> Awaitable[Union[AccountUserFederationQueryResponse, str]]:
        return to_async(super().query_account_user_federation)(request_body)

    def query_more_account_user_federation(
        self, request_body: str
    ) -> Awaitable[Union[AccountUserFederationQueryResponse, str]]:
        return to_async(super().query_more_account_user_federation)(request_body)

    def update_account_user_federation(
        self, id_: str, request_body: AccountUserFederation = None
    ) -> Awaitable[Union[AccountUserFederation, str]]:
        return to_async(super().update_account_user_federation)(id_, request_body)

    def delete_account_user_federation(self, id_: str) -> Awaitable[None]:
        return to_async(super().delete_account_user_federation)(id_)
