
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..execution_artifacts import ExecutionArtifactsService
from ...models import ExecutionArtifacts


class ExecutionArtifactsServiceAsync(ExecutionArtifactsService):
    """
    Async Wrapper for ExecutionArtifactsServiceAsync
    """

    def create_execution_artifacts(
        self, request_body: ExecutionArtifacts = None
    ) -> Awaitable[Union[ExecutionArtifacts, str]]:
        return to_async(super().create_execution_artifacts)(request_body)
