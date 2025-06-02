
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..rosetta_net_connector_record import RosettaNetConnectorRecordService
from ...models import (
    RosettaNetConnectorRecordQueryResponse,
    RosettaNetConnectorRecordQueryConfig,
)


class RosettaNetConnectorRecordServiceAsync(RosettaNetConnectorRecordService):
    """
    Async Wrapper for RosettaNetConnectorRecordServiceAsync
    """

    def query_rosetta_net_connector_record(
        self, request_body: RosettaNetConnectorRecordQueryConfig = None
    ) -> Awaitable[Union[RosettaNetConnectorRecordQueryResponse, str]]:
        return to_async(super().query_rosetta_net_connector_record)(request_body)

    def query_more_rosetta_net_connector_record(
        self, request_body: str
    ) -> Awaitable[Union[RosettaNetConnectorRecordQueryResponse, str]]:
        return to_async(super().query_more_rosetta_net_connector_record)(request_body)
