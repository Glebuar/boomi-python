
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..environment_map_extension_user_defined_function_summary import (
    EnvironmentMapExtensionUserDefinedFunctionSummaryService,
)
from ...models import (
    EnvironmentMapExtensionUserDefinedFunctionSummaryQueryResponse,
    EnvironmentMapExtensionUserDefinedFunctionSummaryQueryConfig,
)


class EnvironmentMapExtensionUserDefinedFunctionSummaryServiceAsync(
    EnvironmentMapExtensionUserDefinedFunctionSummaryService
):
    """
    Async Wrapper for EnvironmentMapExtensionUserDefinedFunctionSummaryServiceAsync
    """

    def query_environment_map_extension_user_defined_function_summary(
        self,
        request_body: EnvironmentMapExtensionUserDefinedFunctionSummaryQueryConfig = None,
    ) -> Awaitable[
        Union[EnvironmentMapExtensionUserDefinedFunctionSummaryQueryResponse, str]
    ]:
        return to_async(
            super().query_environment_map_extension_user_defined_function_summary
        )(request_body)

    def query_more_environment_map_extension_user_defined_function_summary(
        self, request_body: str
    ) -> Awaitable[
        Union[EnvironmentMapExtensionUserDefinedFunctionSummaryQueryResponse, str]
    ]:
        return to_async(
            super().query_more_environment_map_extension_user_defined_function_summary
        )(request_body)
