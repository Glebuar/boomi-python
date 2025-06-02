
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..execution_request import ExecutionRequestService
from ...models import ExecutionRequest


class ExecutionRequestServiceAsync(ExecutionRequestService):
    """
    Async Wrapper for ExecutionRequestServiceAsync
    """

    def create_execution_request(
        self, request_body: ExecutionRequest = None
    ) -> Awaitable[Union[ExecutionRequest, str]]:
        return to_async(super().create_execution_request)(request_body)
