
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..connector_document import ConnectorDocumentService
from ...models import ConnectorDocumentDownload, ConnectorDocument


class ConnectorDocumentServiceAsync(ConnectorDocumentService):
    """
    Async Wrapper for ConnectorDocumentServiceAsync
    """

    def create_connector_document(
        self, request_body: ConnectorDocument = None
    ) -> Awaitable[Union[ConnectorDocumentDownload, str]]:
        return to_async(super().create_connector_document)(request_body)
