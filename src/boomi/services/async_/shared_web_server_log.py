
from typing import Awaitable
from .utils.to_async import to_async
from ..shared_web_server_log import SharedWebServerLogService


class SharedWebServerLogServiceAsync(SharedWebServerLogService):
    """
    Async Wrapper for SharedWebServerLogServiceAsync
    """

    def create_shared_web_server_log(self) -> Awaitable[None]:
        return to_async(super().create_shared_web_server_log)()
