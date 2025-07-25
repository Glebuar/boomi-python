
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..edi_custom_connector_record import EdiCustomConnectorRecordService
from ...models import (
    EdiCustomConnectorRecordQueryResponse,
    EdiCustomConnectorRecordQueryConfig,
)


class EdiCustomConnectorRecordServiceAsync(EdiCustomConnectorRecordService):
    """
    Async Wrapper for EdiCustomConnectorRecordServiceAsync
    """

    def query_edi_custom_connector_record(
        self, request_body: EdiCustomConnectorRecordQueryConfig = None
    ) -> Awaitable[Union[EdiCustomConnectorRecordQueryResponse, str]]:
        return to_async(super().query_edi_custom_connector_record)(request_body)

    def query_more_edi_custom_connector_record(
        self, request_body: str
    ) -> Awaitable[Union[EdiCustomConnectorRecordQueryResponse, str]]:
        return to_async(super().query_more_edi_custom_connector_record)(request_body)
