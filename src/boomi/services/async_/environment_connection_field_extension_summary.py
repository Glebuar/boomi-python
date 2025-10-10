
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..environment_connection_field_extension_summary import (
    EnvironmentConnectionFieldExtensionSummaryService,
)
from ...models import (
    EnvironmentConnectionFieldExtensionSummaryQueryResponse,
    EnvironmentConnectionFieldExtensionSummaryQueryConfig,
)


class EnvironmentConnectionFieldExtensionSummaryServiceAsync(
    EnvironmentConnectionFieldExtensionSummaryService
):
    """
    Async Wrapper for EnvironmentConnectionFieldExtensionSummaryServiceAsync
    """

    def query_environment_connection_field_extension_summary(
        self, request_body: EnvironmentConnectionFieldExtensionSummaryQueryConfig = None
    ) -> Awaitable[Union[EnvironmentConnectionFieldExtensionSummaryQueryResponse, str]]:
        return to_async(super().query_environment_connection_field_extension_summary)(
            request_body
        )

    def query_more_environment_connection_field_extension_summary(
        self, request_body: str
    ) -> Awaitable[Union[EnvironmentConnectionFieldExtensionSummaryQueryResponse, str]]:
        return to_async(
            super().query_more_environment_connection_field_extension_summary
        )(request_body)
