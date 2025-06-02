
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..component_environment_attachment import ComponentEnvironmentAttachmentService
from ...models import (
    ComponentEnvironmentAttachment,
    ComponentEnvironmentAttachmentQueryResponse,
    ComponentEnvironmentAttachmentQueryConfig,
)


class ComponentEnvironmentAttachmentServiceAsync(ComponentEnvironmentAttachmentService):
    """
    Async Wrapper for ComponentEnvironmentAttachmentServiceAsync
    """

    def create_component_environment_attachment(
        self, request_body: ComponentEnvironmentAttachment = None
    ) -> Awaitable[Union[ComponentEnvironmentAttachment, str]]:
        return to_async(super().create_component_environment_attachment)(request_body)

    def query_component_environment_attachment(
        self, request_body: ComponentEnvironmentAttachmentQueryConfig = None
    ) -> Awaitable[Union[ComponentEnvironmentAttachmentQueryResponse, str]]:
        return to_async(super().query_component_environment_attachment)(request_body)

    def query_more_component_environment_attachment(
        self, request_body: str
    ) -> Awaitable[Union[ComponentEnvironmentAttachmentQueryResponse, str]]:
        return to_async(super().query_more_component_environment_attachment)(
            request_body
        )

    def delete_component_environment_attachment(self, id_: str) -> Awaitable[None]:
        return to_async(super().delete_component_environment_attachment)(id_)
