
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..connector import ConnectorService
from ...models import (
    Connector,
    ConnectorBulkResponse,
    ConnectorBulkRequest,
    ConnectorQueryResponse,
    ConnectorQueryConfig,
)


class ConnectorServiceAsync(ConnectorService):
    """
    Async Wrapper for ConnectorServiceAsync
    """

    def get_connector(self, connector_type: str) -> Awaitable[Union[Connector, str]]:
        return to_async(super().get_connector)(connector_type)

    def bulk_connector(
        self, request_body: ConnectorBulkRequest = None
    ) -> Awaitable[Union[ConnectorBulkResponse, str]]:
        return to_async(super().bulk_connector)(request_body)

    def query_connector(
        self, request_body: ConnectorQueryConfig = None
    ) -> Awaitable[Union[ConnectorQueryResponse, str]]:
        return to_async(super().query_connector)(request_body)

    def query_more_connector(
        self, request_body: str
    ) -> Awaitable[Union[ConnectorQueryResponse, str]]:
        return to_async(super().query_more_connector)(request_body)
