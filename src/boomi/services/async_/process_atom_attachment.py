
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..process_atom_attachment import ProcessAtomAttachmentService
from ...models import (
    ProcessAtomAttachment,
    ProcessAtomAttachmentQueryResponse,
    ProcessAtomAttachmentQueryConfig,
)


class ProcessAtomAttachmentServiceAsync(ProcessAtomAttachmentService):
    """
    Async Wrapper for ProcessAtomAttachmentServiceAsync
    """

    def create_process_atom_attachment(
        self, request_body: ProcessAtomAttachment = None
    ) -> Awaitable[Union[ProcessAtomAttachment, str]]:
        return to_async(super().create_process_atom_attachment)(request_body)

    def query_process_atom_attachment(
        self, request_body: ProcessAtomAttachmentQueryConfig = None
    ) -> Awaitable[Union[ProcessAtomAttachmentQueryResponse, str]]:
        return to_async(super().query_process_atom_attachment)(request_body)

    def query_more_process_atom_attachment(
        self, request_body: str
    ) -> Awaitable[Union[ProcessAtomAttachmentQueryResponse, str]]:
        return to_async(super().query_more_process_atom_attachment)(request_body)

    def delete_process_atom_attachment(self, id_: str) -> Awaitable[None]:
        return to_async(super().delete_process_atom_attachment)(id_)
