
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..environment_map_extension_external_component import (
    EnvironmentMapExtensionExternalComponentService,
)
from ...models import (
    EnvironmentMapExtensionExternalComponentQueryResponse,
    EnvironmentMapExtensionExternalComponentQueryConfig,
)


class EnvironmentMapExtensionExternalComponentServiceAsync(
    EnvironmentMapExtensionExternalComponentService
):
    """
    Async Wrapper for EnvironmentMapExtensionExternalComponentServiceAsync
    """

    def query_environment_map_extension_external_component(
        self, request_body: EnvironmentMapExtensionExternalComponentQueryConfig = None
    ) -> Awaitable[Union[EnvironmentMapExtensionExternalComponentQueryResponse, str]]:
        return to_async(super().query_environment_map_extension_external_component)(
            request_body
        )

    def query_more_environment_map_extension_external_component(
        self, request_body: str
    ) -> Awaitable[Union[EnvironmentMapExtensionExternalComponentQueryResponse, str]]:
        return to_async(
            super().query_more_environment_map_extension_external_component
        )(request_body)
