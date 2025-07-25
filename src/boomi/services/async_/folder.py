
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..folder import FolderService
from ...models import (
    Folder,
    FolderBulkResponse,
    FolderBulkRequest,
    FolderQueryResponse,
    FolderQueryConfig,
)


class FolderServiceAsync(FolderService):
    """
    Async Wrapper for FolderServiceAsync
    """

    def create_folder(
        self, request_body: Folder = None
    ) -> Awaitable[Union[Folder, str]]:
        return to_async(super().create_folder)(request_body)

    def get_folder(self, id_: str) -> Awaitable[Union[Folder, str]]:
        return to_async(super().get_folder)(id_)

    def update_folder(
        self, id_: str, request_body: Folder = None
    ) -> Awaitable[Union[Folder, str]]:
        return to_async(super().update_folder)(id_, request_body)

    def delete_folder(self, id_: str) -> Awaitable[None]:
        return to_async(super().delete_folder)(id_)

    def bulk_folder(
        self, request_body: FolderBulkRequest = None
    ) -> Awaitable[Union[FolderBulkResponse, str]]:
        return to_async(super().bulk_folder)(request_body)

    def query_folder(
        self, request_body: FolderQueryConfig = None
    ) -> Awaitable[Union[FolderQueryResponse, str]]:
        return to_async(super().query_folder)(request_body)

    def query_more_folder(
        self, request_body: str
    ) -> Awaitable[Union[FolderQueryResponse, str]]:
        return to_async(super().query_more_folder)(request_body)
