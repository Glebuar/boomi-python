
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..release_integration_pack import ReleaseIntegrationPackService
from ...models import ReleaseIntegrationPack


class ReleaseIntegrationPackServiceAsync(ReleaseIntegrationPackService):
    """
    Async Wrapper for ReleaseIntegrationPackServiceAsync
    """

    def create_release_integration_pack(
        self, request_body: ReleaseIntegrationPack = None
    ) -> Awaitable[Union[ReleaseIntegrationPack, str]]:
        return to_async(super().create_release_integration_pack)(request_body)

    def update_release_integration_pack(
        self, id_: str, request_body: ReleaseIntegrationPack = None
    ) -> Awaitable[Union[ReleaseIntegrationPack, str]]:
        return to_async(super().update_release_integration_pack)(id_, request_body)
