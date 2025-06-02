
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..account_cloud_attachment_properties import (
    AccountCloudAttachmentPropertiesService,
)
from ...models import (
    AccountCloudAttachmentProperties,
    AsyncOperationTokenResult,
    AccountCloudAttachmentPropertiesAsyncResponse,
)


class AccountCloudAttachmentPropertiesServiceAsync(
    AccountCloudAttachmentPropertiesService
):
    """
    Async Wrapper for AccountCloudAttachmentPropertiesServiceAsync
    """

    def update_account_cloud_attachment_properties(
        self, id_: str, request_body: AccountCloudAttachmentProperties = None
    ) -> Awaitable[Union[AccountCloudAttachmentProperties, str]]:
        return to_async(super().update_account_cloud_attachment_properties)(
            id_, request_body
        )

    def async_get_account_cloud_attachment_properties(
        self, id_: str
    ) -> Awaitable[Union[AsyncOperationTokenResult, str]]:
        return to_async(super().async_get_account_cloud_attachment_properties)(id_)

    def async_token_account_cloud_attachment_properties(
        self, token: str
    ) -> Awaitable[Union[AccountCloudAttachmentPropertiesAsyncResponse, str]]:
        return to_async(super().async_token_account_cloud_attachment_properties)(token)
