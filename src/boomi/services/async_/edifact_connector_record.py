
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..edifact_connector_record import EdifactConnectorRecordService
from ...models import (
    EdifactConnectorRecordQueryResponse,
    EdifactConnectorRecordQueryConfig,
)


class EdifactConnectorRecordServiceAsync(EdifactConnectorRecordService):
    """
    Async Wrapper for EdifactConnectorRecordServiceAsync
    """

    def query_edifact_connector_record(
        self, request_body: EdifactConnectorRecordQueryConfig = None
    ) -> Awaitable[Union[EdifactConnectorRecordQueryResponse, str]]:
        return to_async(super().query_edifact_connector_record)(request_body)

    def query_more_edifact_connector_record(
        self, request_body: str
    ) -> Awaitable[Union[EdifactConnectorRecordQueryResponse, str]]:
        return to_async(super().query_more_edifact_connector_record)(request_body)
