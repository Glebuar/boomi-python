
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..tradacoms_connector_record import TradacomsConnectorRecordService
from ...models import (
    TradacomsConnectorRecordQueryResponse,
    TradacomsConnectorRecordQueryConfig,
)


class TradacomsConnectorRecordServiceAsync(TradacomsConnectorRecordService):
    """
    Async Wrapper for TradacomsConnectorRecordServiceAsync
    """

    def query_tradacoms_connector_record(
        self, request_body: TradacomsConnectorRecordQueryConfig = None
    ) -> Awaitable[Union[TradacomsConnectorRecordQueryResponse, str]]:
        return to_async(super().query_tradacoms_connector_record)(request_body)

    def query_more_tradacoms_connector_record(
        self, request_body: str
    ) -> Awaitable[Union[TradacomsConnectorRecordQueryResponse, str]]:
        return to_async(super().query_more_tradacoms_connector_record)(request_body)
