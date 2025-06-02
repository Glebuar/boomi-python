
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..account_cloud_attachment_quota import AccountCloudAttachmentQuotaService
from ...models import (
    AccountCloudAttachmentQuota,
    AccountCloudAttachmentQuotaBulkResponse,
    AccountCloudAttachmentQuotaBulkRequest,
)


class AccountCloudAttachmentQuotaServiceAsync(AccountCloudAttachmentQuotaService):
    """
    Async Wrapper for AccountCloudAttachmentQuotaServiceAsync
    """

    def create_account_cloud_attachment_quota(
        self, request_body: AccountCloudAttachmentQuota = None
    ) -> Awaitable[Union[AccountCloudAttachmentQuota, str]]:
        return to_async(super().create_account_cloud_attachment_quota)(request_body)

    def get_account_cloud_attachment_quota(
        self, id_: str
    ) -> Awaitable[Union[AccountCloudAttachmentQuota, str]]:
        return to_async(super().get_account_cloud_attachment_quota)(id_)

    def update_account_cloud_attachment_quota(
        self, id_: str, request_body: AccountCloudAttachmentQuota = None
    ) -> Awaitable[Union[AccountCloudAttachmentQuota, str]]:
        return to_async(super().update_account_cloud_attachment_quota)(
            id_, request_body
        )

    def delete_account_cloud_attachment_quota(self, id_: str) -> Awaitable[None]:
        return to_async(super().delete_account_cloud_attachment_quota)(id_)

    def bulk_account_cloud_attachment_quota(
        self, request_body: AccountCloudAttachmentQuotaBulkRequest = None
    ) -> Awaitable[Union[AccountCloudAttachmentQuotaBulkResponse, str]]:
        return to_async(super().bulk_account_cloud_attachment_quota)(request_body)
