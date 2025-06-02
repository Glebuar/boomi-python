
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..environment import EnvironmentService
from ...models import (
    Environment,
    EnvironmentBulkResponse,
    EnvironmentBulkRequest,
    EnvironmentQueryResponse,
    EnvironmentQueryConfig,
    EnvironmentMapExtension,
)


class EnvironmentServiceAsync(EnvironmentService):
    """
    Async Wrapper for EnvironmentServiceAsync
    """

    def create_environment(
        self, request_body: Environment = None
    ) -> Awaitable[Union[Environment, str]]:
        return to_async(super().create_environment)(request_body)

    def get_environment(self, id_: str) -> Awaitable[Union[Environment, str]]:
        return to_async(super().get_environment)(id_)

    def update_environment(
        self, id_: str, request_body: Environment = None
    ) -> Awaitable[Union[Environment, str]]:
        return to_async(super().update_environment)(id_, request_body)

    def delete_environment(self, id_: str) -> Awaitable[None]:
        return to_async(super().delete_environment)(id_)

    def bulk_environment(
        self, request_body: EnvironmentBulkRequest = None
    ) -> Awaitable[Union[EnvironmentBulkResponse, str]]:
        return to_async(super().bulk_environment)(request_body)

    def query_environment(
        self, request_body: EnvironmentQueryConfig = None
    ) -> Awaitable[Union[EnvironmentQueryResponse, str]]:
        return to_async(super().query_environment)(request_body)

    def query_more_environment(
        self, request_body: str
    ) -> Awaitable[Union[EnvironmentQueryResponse, str]]:
        return to_async(super().query_more_environment)(request_body)

    def update_environment_map_extension(
        self, id_: str, request_body: EnvironmentMapExtension = None
    ) -> Awaitable[Union[EnvironmentMapExtension, str]]:
        return to_async(super().update_environment_map_extension)(id_, request_body)
