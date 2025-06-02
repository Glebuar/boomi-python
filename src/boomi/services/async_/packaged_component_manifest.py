
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..packaged_component_manifest import PackagedComponentManifestService
from ...models import (
    PackagedComponentManifest,
    PackagedComponentManifestBulkResponse,
    PackagedComponentManifestBulkRequest,
)


class PackagedComponentManifestServiceAsync(PackagedComponentManifestService):
    """
    Async Wrapper for PackagedComponentManifestServiceAsync
    """

    def get_packaged_component_manifest(
        self, package_id: str
    ) -> Awaitable[Union[PackagedComponentManifest, str]]:
        return to_async(super().get_packaged_component_manifest)(package_id)

    def bulk_packaged_component_manifest(
        self, request_body: PackagedComponentManifestBulkRequest = None
    ) -> Awaitable[Union[PackagedComponentManifestBulkResponse, str]]:
        return to_async(super().bulk_packaged_component_manifest)(request_body)
