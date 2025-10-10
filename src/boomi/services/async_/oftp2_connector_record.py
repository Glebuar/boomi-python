
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..oftp2_connector_record import Oftp2ConnectorRecordService
from ...models import Oftp2ConnectorRecordQueryResponse, Oftp2ConnectorRecordQueryConfig


class Oftp2ConnectorRecordServiceAsync(Oftp2ConnectorRecordService):
    """
    Async Wrapper for Oftp2ConnectorRecordServiceAsync
    """

    def query_oftp2_connector_record(
        self, request_body: Oftp2ConnectorRecordQueryConfig = None
    ) -> Awaitable[Union[Oftp2ConnectorRecordQueryResponse, str]]:
        return to_async(super().query_oftp2_connector_record)(request_body)

    def query_more_oftp2_connector_record(
        self, request_body: str
    ) -> Awaitable[Union[Oftp2ConnectorRecordQueryResponse, str]]:
        return to_async(super().query_more_oftp2_connector_record)(request_body)
