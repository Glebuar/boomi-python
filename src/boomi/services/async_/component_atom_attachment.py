
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..component_atom_attachment import ComponentAtomAttachmentService
from ...models import (
    ComponentAtomAttachment,
    ComponentAtomAttachmentQueryResponse,
    ComponentAtomAttachmentQueryConfig,
)


class ComponentAtomAttachmentServiceAsync(ComponentAtomAttachmentService):
    """
    Async Wrapper for ComponentAtomAttachmentServiceAsync
    """

    def create_component_atom_attachment(
        self, request_body: ComponentAtomAttachment = None
    ) -> Awaitable[Union[ComponentAtomAttachment, str]]:
        return to_async(super().create_component_atom_attachment)(request_body)

    def query_component_atom_attachment(
        self, request_body: ComponentAtomAttachmentQueryConfig = None
    ) -> Awaitable[Union[ComponentAtomAttachmentQueryResponse, str]]:
        return to_async(super().query_component_atom_attachment)(request_body)

    def query_more_component_atom_attachment(
        self, request_body: str
    ) -> Awaitable[Union[ComponentAtomAttachmentQueryResponse, str]]:
        return to_async(super().query_more_component_atom_attachment)(request_body)

    def delete_component_atom_attachment(self, id_: str) -> Awaitable[None]:
        return to_async(super().delete_component_atom_attachment)(id_)
