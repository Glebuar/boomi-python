
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..environment_map_extensions_summary import EnvironmentMapExtensionsSummaryService
from ...models import (
    EnvironmentMapExtensionsSummaryQueryResponse,
    EnvironmentMapExtensionsSummaryQueryConfig,
)


class EnvironmentMapExtensionsSummaryServiceAsync(
    EnvironmentMapExtensionsSummaryService
):
    """
    Async Wrapper for EnvironmentMapExtensionsSummaryServiceAsync
    """

    def query_environment_map_extensions_summary(
        self, request_body: EnvironmentMapExtensionsSummaryQueryConfig = None
    ) -> Awaitable[Union[EnvironmentMapExtensionsSummaryQueryResponse, str]]:
        return to_async(super().query_environment_map_extensions_summary)(request_body)

    def query_more_environment_map_extensions_summary(
        self, request_body: str
    ) -> Awaitable[Union[EnvironmentMapExtensionsSummaryQueryResponse, str]]:
        return to_async(super().query_more_environment_map_extensions_summary)(
            request_body
        )
