
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..environment_atom_attachment import EnvironmentAtomAttachmentService
from ...models import (
    EnvironmentAtomAttachment,
    EnvironmentAtomAttachmentQueryResponse,
    EnvironmentAtomAttachmentQueryConfig,
)


class EnvironmentAtomAttachmentServiceAsync(EnvironmentAtomAttachmentService):
    """
    Async Wrapper for EnvironmentAtomAttachmentServiceAsync
    """

    def create_environment_atom_attachment(
        self, request_body: EnvironmentAtomAttachment = None
    ) -> Awaitable[Union[EnvironmentAtomAttachment, str]]:
        return to_async(super().create_environment_atom_attachment)(request_body)

    def query_environment_atom_attachment(
        self, request_body: EnvironmentAtomAttachmentQueryConfig = None
    ) -> Awaitable[Union[EnvironmentAtomAttachmentQueryResponse, str]]:
        return to_async(super().query_environment_atom_attachment)(request_body)

    def query_more_environment_atom_attachment(
        self, request_body: str
    ) -> Awaitable[Union[EnvironmentAtomAttachmentQueryResponse, str]]:
        return to_async(super().query_more_environment_atom_attachment)(request_body)

    def delete_environment_atom_attachment(self, id_: str) -> Awaitable[None]:
        return to_async(super().delete_environment_atom_attachment)(id_)
