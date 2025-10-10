
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..integration_pack_atom_attachment import IntegrationPackAtomAttachmentService
from ...models import (
    IntegrationPackAtomAttachment,
    IntegrationPackAtomAttachmentQueryResponse,
    IntegrationPackAtomAttachmentQueryConfig,
)


class IntegrationPackAtomAttachmentServiceAsync(IntegrationPackAtomAttachmentService):
    """
    Async Wrapper for IntegrationPackAtomAttachmentServiceAsync
    """

    def create_integration_pack_atom_attachment(
        self, request_body: IntegrationPackAtomAttachment = None
    ) -> Awaitable[Union[IntegrationPackAtomAttachment, str]]:
        return to_async(super().create_integration_pack_atom_attachment)(request_body)

    def query_integration_pack_atom_attachment(
        self, request_body: IntegrationPackAtomAttachmentQueryConfig = None
    ) -> Awaitable[Union[IntegrationPackAtomAttachmentQueryResponse, str]]:
        return to_async(super().query_integration_pack_atom_attachment)(request_body)

    def query_more_integration_pack_atom_attachment(
        self, request_body: str
    ) -> Awaitable[Union[IntegrationPackAtomAttachmentQueryResponse, str]]:
        return to_async(super().query_more_integration_pack_atom_attachment)(
            request_body
        )

    def delete_integration_pack_atom_attachment(self, id_: str) -> Awaitable[None]:
        return to_async(super().delete_integration_pack_atom_attachment)(id_)
