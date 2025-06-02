
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..connection_licensing_report import ConnectionLicensingReportService
from ...models import ConnectionLicensingDownload, ConnectionLicensingReport


class ConnectionLicensingReportServiceAsync(ConnectionLicensingReportService):
    """
    Async Wrapper for ConnectionLicensingReportServiceAsync
    """

    def create_connection_licensing_report(
        self, request_body: ConnectionLicensingReport = None
    ) -> Awaitable[Union[ConnectionLicensingDownload, str]]:
        return to_async(super().create_connection_licensing_report)(request_body)
