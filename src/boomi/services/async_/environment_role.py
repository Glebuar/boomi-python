
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..environment_role import EnvironmentRoleService
from ...models import (
    EnvironmentRole,
    EnvironmentRoleBulkResponse,
    EnvironmentRoleBulkRequest,
    EnvironmentRoleQueryResponse,
    EnvironmentRoleQueryConfig,
)


class EnvironmentRoleServiceAsync(EnvironmentRoleService):
    """
    Async Wrapper for EnvironmentRoleServiceAsync
    """

    def create_environment_role(
        self, request_body: EnvironmentRole = None
    ) -> Awaitable[Union[EnvironmentRole, str]]:
        return to_async(super().create_environment_role)(request_body)

    def get_environment_role(self, id_: str) -> Awaitable[Union[EnvironmentRole, str]]:
        return to_async(super().get_environment_role)(id_)

    def delete_environment_role(self, id_: str) -> Awaitable[None]:
        return to_async(super().delete_environment_role)(id_)

    def bulk_environment_role(
        self, request_body: EnvironmentRoleBulkRequest = None
    ) -> Awaitable[Union[EnvironmentRoleBulkResponse, str]]:
        return to_async(super().bulk_environment_role)(request_body)

    def query_environment_role(
        self, request_body: EnvironmentRoleQueryConfig = None
    ) -> Awaitable[Union[EnvironmentRoleQueryResponse, str]]:
        return to_async(super().query_environment_role)(request_body)

    def query_more_environment_role(
        self, request_body: str
    ) -> Awaitable[Union[EnvironmentRoleQueryResponse, str]]:
        return to_async(super().query_more_environment_role)(request_body)
