
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..account_group_integration_pack import AccountGroupIntegrationPackService
from ...models import (
    AccountGroupIntegrationPack,
    AccountGroupIntegrationPackBulkResponse,
    AccountGroupIntegrationPackBulkRequest,
    AccountGroupIntegrationPackQueryResponse,
    AccountGroupIntegrationPackQueryConfig,
)


class AccountGroupIntegrationPackServiceAsync(AccountGroupIntegrationPackService):
    """
    Async Wrapper for AccountGroupIntegrationPackServiceAsync
    """

    def create_account_group_integration_pack(
        self, request_body: AccountGroupIntegrationPack = None
    ) -> Awaitable[Union[AccountGroupIntegrationPack, str]]:
        return to_async(super().create_account_group_integration_pack)(request_body)

    def get_account_group_integration_pack(
        self, id_: str
    ) -> Awaitable[Union[AccountGroupIntegrationPack, str]]:
        return to_async(super().get_account_group_integration_pack)(id_)

    def delete_account_group_integration_pack(self, id_: str) -> Awaitable[None]:
        return to_async(super().delete_account_group_integration_pack)(id_)

    def bulk_account_group_integration_pack(
        self, request_body: AccountGroupIntegrationPackBulkRequest = None
    ) -> Awaitable[Union[AccountGroupIntegrationPackBulkResponse, str]]:
        return to_async(super().bulk_account_group_integration_pack)(request_body)

    def query_account_group_integration_pack(
        self, request_body: AccountGroupIntegrationPackQueryConfig = None
    ) -> Awaitable[Union[AccountGroupIntegrationPackQueryResponse, str]]:
        return to_async(super().query_account_group_integration_pack)(request_body)

    def query_more_account_group_integration_pack(
        self, request_body: str
    ) -> Awaitable[Union[AccountGroupIntegrationPackQueryResponse, str]]:
        return to_async(super().query_more_account_group_integration_pack)(request_body)
