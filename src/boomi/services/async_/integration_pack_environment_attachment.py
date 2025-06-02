
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..integration_pack_environment_attachment import (
    IntegrationPackEnvironmentAttachmentService,
)
from ...models import (
    IntegrationPackEnvironmentAttachment,
    IntegrationPackEnvironmentAttachmentQueryResponse,
    IntegrationPackEnvironmentAttachmentQueryConfig,
)


class IntegrationPackEnvironmentAttachmentServiceAsync(
    IntegrationPackEnvironmentAttachmentService
):
    """
    Async Wrapper for IntegrationPackEnvironmentAttachmentServiceAsync
    """

    def create_integration_pack_environment_attachment(
        self, request_body: IntegrationPackEnvironmentAttachment = None
    ) -> Awaitable[Union[IntegrationPackEnvironmentAttachment, str]]:
        return to_async(super().create_integration_pack_environment_attachment)(
            request_body
        )

    def query_integration_pack_environment_attachment(
        self, request_body: IntegrationPackEnvironmentAttachmentQueryConfig = None
    ) -> Awaitable[Union[IntegrationPackEnvironmentAttachmentQueryResponse, str]]:
        return to_async(super().query_integration_pack_environment_attachment)(
            request_body
        )

    def query_more_integration_pack_environment_attachment(
        self, request_body: str
    ) -> Awaitable[Union[IntegrationPackEnvironmentAttachmentQueryResponse, str]]:
        return to_async(super().query_more_integration_pack_environment_attachment)(
            request_body
        )

    def delete_integration_pack_environment_attachment(
        self, id_: str
    ) -> Awaitable[None]:
        return to_async(super().delete_integration_pack_environment_attachment)(id_)
