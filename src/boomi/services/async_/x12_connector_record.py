
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..x12_connector_record import X12ConnectorRecordService
from ...models import X12ConnectorRecordQueryResponse, X12ConnectorRecordQueryConfig


class X12ConnectorRecordServiceAsync(X12ConnectorRecordService):
    """
    Async Wrapper for X12ConnectorRecordServiceAsync
    """

    def query_x12_connector_record(
        self, request_body: X12ConnectorRecordQueryConfig = None
    ) -> Awaitable[Union[X12ConnectorRecordQueryResponse, str]]:
        return to_async(super().query_x12_connector_record)(request_body)

    def query_more_x12_connector_record(
        self, request_body: str
    ) -> Awaitable[Union[X12ConnectorRecordQueryResponse, str]]:
        return to_async(super().query_more_x12_connector_record)(request_body)
