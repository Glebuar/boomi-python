
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..shared_server_information import SharedServerInformationService
from ...models import (
    SharedServerInformation,
    SharedServerInformationBulkResponse,
    SharedServerInformationBulkRequest,
)


class SharedServerInformationServiceAsync(SharedServerInformationService):
    """
    Async Wrapper for SharedServerInformationServiceAsync
    """

    def get_shared_server_information(
        self, id_: str
    ) -> Awaitable[Union[SharedServerInformation, str]]:
        return to_async(super().get_shared_server_information)(id_)

    def update_shared_server_information(
        self, id_: str, request_body: SharedServerInformation = None
    ) -> Awaitable[Union[SharedServerInformation, str]]:
        return to_async(super().update_shared_server_information)(id_, request_body)

    def bulk_shared_server_information(
        self, request_body: SharedServerInformationBulkRequest = None
    ) -> Awaitable[Union[SharedServerInformationBulkResponse, str]]:
        return to_async(super().bulk_shared_server_information)(request_body)
