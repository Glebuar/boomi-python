
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..execution_count_account_group import ExecutionCountAccountGroupService
from ...models import (
    ExecutionCountAccountGroupQueryResponse,
    ExecutionCountAccountGroupQueryConfig,
)


class ExecutionCountAccountGroupServiceAsync(ExecutionCountAccountGroupService):
    """
    Async Wrapper for ExecutionCountAccountGroupServiceAsync
    """

    def query_execution_count_account_group(
        self, request_body: ExecutionCountAccountGroupQueryConfig = None
    ) -> Awaitable[Union[ExecutionCountAccountGroupQueryResponse, str]]:
        return to_async(super().query_execution_count_account_group)(request_body)

    def query_more_execution_count_account_group(
        self, request_body: str
    ) -> Awaitable[Union[ExecutionCountAccountGroupQueryResponse, str]]:
        return to_async(super().query_more_execution_count_account_group)(request_body)
