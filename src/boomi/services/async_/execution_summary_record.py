
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..execution_summary_record import ExecutionSummaryRecordService
from ...models import (
    ExecutionSummaryRecordQueryResponse,
    ExecutionSummaryRecordQueryConfig,
)


class ExecutionSummaryRecordServiceAsync(ExecutionSummaryRecordService):
    """
    Async Wrapper for ExecutionSummaryRecordServiceAsync
    """

    def query_execution_summary_record(
        self, request_body: ExecutionSummaryRecordQueryConfig = None
    ) -> Awaitable[Union[ExecutionSummaryRecordQueryResponse, str]]:
        return to_async(super().query_execution_summary_record)(request_body)

    def query_more_execution_summary_record(
        self, request_body: str
    ) -> Awaitable[Union[ExecutionSummaryRecordQueryResponse, str]]:
        return to_async(super().query_more_execution_summary_record)(request_body)
