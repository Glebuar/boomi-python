
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..throughput_account import ThroughputAccountService
from ...models import ThroughputAccountQueryResponse, ThroughputAccountQueryConfig


class ThroughputAccountServiceAsync(ThroughputAccountService):
    """
    Async Wrapper for ThroughputAccountServiceAsync
    """

    def query_throughput_account(
        self, request_body: ThroughputAccountQueryConfig = None
    ) -> Awaitable[Union[ThroughputAccountQueryResponse, str]]:
        return to_async(super().query_throughput_account)(request_body)

    def query_more_throughput_account(
        self, request_body: str
    ) -> Awaitable[Union[ThroughputAccountQueryResponse, str]]:
        return to_async(super().query_more_throughput_account)(request_body)
