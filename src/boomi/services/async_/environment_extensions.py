
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..environment_extensions import EnvironmentExtensionsService
from ...models import (
    EnvironmentExtensions,
    EnvironmentExtensionsBulkResponse,
    EnvironmentExtensionsBulkRequest,
    EnvironmentExtensionsQueryResponse,
    EnvironmentExtensionsQueryConfig,
)


class EnvironmentExtensionsServiceAsync(EnvironmentExtensionsService):
    """
    Async Wrapper for EnvironmentExtensionsServiceAsync
    """

    def get_environment_extensions(
        self, id_: str
    ) -> Awaitable[Union[EnvironmentExtensions, str]]:
        return to_async(super().get_environment_extensions)(id_)

    def update_environment_extensions(
        self, id_: str, request_body: EnvironmentExtensions = None
    ) -> Awaitable[Union[EnvironmentExtensions, str]]:
        return to_async(super().update_environment_extensions)(id_, request_body)

    def bulk_environment_extensions(
        self, request_body: EnvironmentExtensionsBulkRequest = None
    ) -> Awaitable[Union[EnvironmentExtensionsBulkResponse, str]]:
        return to_async(super().bulk_environment_extensions)(request_body)

    def query_environment_extensions(
        self, request_body: EnvironmentExtensionsQueryConfig = None
    ) -> Awaitable[Union[EnvironmentExtensionsQueryResponse, str]]:
        return to_async(super().query_environment_extensions)(request_body)

    def query_more_environment_extensions(
        self, request_body: str
    ) -> Awaitable[Union[EnvironmentExtensionsQueryResponse, str]]:
        return to_async(super().query_more_environment_extensions)(request_body)
