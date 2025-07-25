
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..release_integration_pack_status import ReleaseIntegrationPackStatusService
from ...models import (
    ReleaseIntegrationPackStatus,
    ReleaseIntegrationPackStatusBulkResponse,
    ReleaseIntegrationPackStatusBulkRequest,
)


class ReleaseIntegrationPackStatusServiceAsync(ReleaseIntegrationPackStatusService):
    """
    Async Wrapper for ReleaseIntegrationPackStatusServiceAsync
    """

    def get_release_integration_pack_status(
        self, id_: str
    ) -> Awaitable[Union[ReleaseIntegrationPackStatus, str]]:
        return to_async(super().get_release_integration_pack_status)(id_)

    def bulk_release_integration_pack_status(
        self, request_body: ReleaseIntegrationPackStatusBulkRequest = None
    ) -> Awaitable[Union[str, ReleaseIntegrationPackStatusBulkResponse]]:
        return to_async(super().bulk_release_integration_pack_status)(request_body)
