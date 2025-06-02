
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..odette_connector_record import OdetteConnectorRecordService
from ...models import (
    OdetteConnectorRecordQueryResponse,
    OdetteConnectorRecordQueryConfig,
)


class OdetteConnectorRecordServiceAsync(OdetteConnectorRecordService):
    """
    Async Wrapper for OdetteConnectorRecordServiceAsync
    """

    def query_odette_connector_record(
        self, request_body: OdetteConnectorRecordQueryConfig = None
    ) -> Awaitable[Union[OdetteConnectorRecordQueryResponse, str]]:
        return to_async(super().query_odette_connector_record)(request_body)

    def query_more_odette_connector_record(
        self, request_body: str
    ) -> Awaitable[Union[OdetteConnectorRecordQueryResponse, str]]:
        return to_async(super().query_more_odette_connector_record)(request_body)
