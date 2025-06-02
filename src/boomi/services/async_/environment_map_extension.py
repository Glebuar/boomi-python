
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..environment_map_extension import EnvironmentMapExtensionService
from ...models import (
    EnvironmentMapExtension,
    EnvironmentMapExtensionBulkResponse,
    EnvironmentMapExtensionBulkRequest,
)


class EnvironmentMapExtensionServiceAsync(EnvironmentMapExtensionService):
    """
    Async Wrapper for EnvironmentMapExtensionServiceAsync
    """

    def get_environment_map_extension(
        self, id_: str
    ) -> Awaitable[Union[EnvironmentMapExtension, str]]:
        return to_async(super().get_environment_map_extension)(id_)

    def bulk_environment_map_extension(
        self, request_body: EnvironmentMapExtensionBulkRequest = None
    ) -> Awaitable[Union[EnvironmentMapExtensionBulkResponse, str]]:
        return to_async(super().bulk_environment_map_extension)(request_body)

    def execute_environment_map_extension(
        self, id_: str, request_body: EnvironmentMapExtension = None
    ) -> Awaitable[Union[EnvironmentMapExtension, str]]:
        return to_async(super().execute_environment_map_extension)(id_, request_body)
