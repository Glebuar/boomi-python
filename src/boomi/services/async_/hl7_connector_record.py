
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..hl7_connector_record import Hl7ConnectorRecordService
from ...models import Hl7ConnectorRecordQueryResponse, Hl7ConnectorRecordQueryConfig


class Hl7ConnectorRecordServiceAsync(Hl7ConnectorRecordService):
    """
    Async Wrapper for Hl7ConnectorRecordServiceAsync
    """

    def query_hl7_connector_record(
        self, request_body: Hl7ConnectorRecordQueryConfig = None
    ) -> Awaitable[Union[Hl7ConnectorRecordQueryResponse, str]]:
        return to_async(super().query_hl7_connector_record)(request_body)

    def query_more_hl7_connector_record(
        self, request_body: str
    ) -> Awaitable[Union[Hl7ConnectorRecordQueryResponse, str]]:
        return to_async(super().query_more_hl7_connector_record)(request_body)
