
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..throughput_account_group import ThroughputAccountGroupService
from ...models import (
    ThroughputAccountGroupQueryResponse,
    ThroughputAccountGroupQueryConfig,
)


class ThroughputAccountGroupServiceAsync(ThroughputAccountGroupService):
    """
    Async Wrapper for ThroughputAccountGroupServiceAsync
    """

    def query_throughput_account_group(
        self, request_body: ThroughputAccountGroupQueryConfig = None
    ) -> Awaitable[Union[ThroughputAccountGroupQueryResponse, str]]:
        return to_async(super().query_throughput_account_group)(request_body)

    def query_more_throughput_account_group(
        self, request_body: str
    ) -> Awaitable[Union[ThroughputAccountGroupQueryResponse, str]]:
        return to_async(super().query_more_throughput_account_group)(request_body)
