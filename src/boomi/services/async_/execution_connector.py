
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..execution_connector import ExecutionConnectorService
from ...models import ExecutionConnectorQueryResponse, ExecutionConnectorQueryConfig


class ExecutionConnectorServiceAsync(ExecutionConnectorService):
    """
    Async Wrapper for ExecutionConnectorServiceAsync
    """

    def query_execution_connector(
        self, request_body: ExecutionConnectorQueryConfig = None
    ) -> Awaitable[Union[ExecutionConnectorQueryResponse, str]]:
        return to_async(super().query_execution_connector)(request_body)

    def query_more_execution_connector(
        self, request_body: str
    ) -> Awaitable[Union[ExecutionConnectorQueryResponse, str]]:
        return to_async(super().query_more_execution_connector)(request_body)
