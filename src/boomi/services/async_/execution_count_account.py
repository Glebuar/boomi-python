
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..execution_count_account import ExecutionCountAccountService
from ...models import (
    ExecutionCountAccountQueryResponse,
    ExecutionCountAccountQueryConfig,
)


class ExecutionCountAccountServiceAsync(ExecutionCountAccountService):
    """
    Async Wrapper for ExecutionCountAccountServiceAsync
    """

    def query_execution_count_account(
        self, request_body: ExecutionCountAccountQueryConfig = None
    ) -> Awaitable[Union[ExecutionCountAccountQueryResponse, str]]:
        return to_async(super().query_execution_count_account)(request_body)

    def query_more_execution_count_account(
        self, request_body: str
    ) -> Awaitable[Union[ExecutionCountAccountQueryResponse, str]]:
        return to_async(super().query_more_execution_count_account)(request_body)
