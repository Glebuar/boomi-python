
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..shared_web_server import SharedWebServerService
from ...models import (
    SharedWebServer,
    SharedWebServerBulkResponse,
    SharedWebServerBulkRequest,
)


class SharedWebServerServiceAsync(SharedWebServerService):
    """
    Async Wrapper for SharedWebServerServiceAsync
    """

    def get_shared_web_server(self, id_: str) -> Awaitable[Union[SharedWebServer, str]]:
        return to_async(super().get_shared_web_server)(id_)

    def update_shared_web_server(
        self, id_: str, request_body: SharedWebServer = None
    ) -> Awaitable[Union[SharedWebServer, str]]:
        return to_async(super().update_shared_web_server)(id_, request_body)

    def bulk_shared_web_server(
        self, request_body: SharedWebServerBulkRequest = None
    ) -> Awaitable[Union[SharedWebServerBulkResponse, str]]:
        return to_async(super().bulk_shared_web_server)(request_body)
