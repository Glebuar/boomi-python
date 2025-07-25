
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..runtime_restart_request import RuntimeRestartRequestService
from ...models import RuntimeRestartRequest


class RuntimeRestartRequestServiceAsync(RuntimeRestartRequestService):
    """
    Async Wrapper for RuntimeRestartRequestServiceAsync
    """

    def create_runtime_restart_request(
        self, request_body: RuntimeRestartRequest = None
    ) -> Awaitable[Union[RuntimeRestartRequest, str]]:
        return to_async(super().create_runtime_restart_request)(request_body)
