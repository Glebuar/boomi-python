
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..as2_connector_record import As2ConnectorRecordService
from ...models import As2ConnectorRecordQueryResponse, As2ConnectorRecordQueryConfig


class As2ConnectorRecordServiceAsync(As2ConnectorRecordService):
    """
    Async Wrapper for As2ConnectorRecordServiceAsync
    """

    def query_as2_connector_record(
        self, request_body: As2ConnectorRecordQueryConfig = None
    ) -> Awaitable[Union[As2ConnectorRecordQueryResponse, str]]:
        return to_async(super().query_as2_connector_record)(request_body)

    def query_more_as2_connector_record(
        self, request_body: str
    ) -> Awaitable[Union[As2ConnectorRecordQueryResponse, str]]:
        return to_async(super().query_more_as2_connector_record)(request_body)
