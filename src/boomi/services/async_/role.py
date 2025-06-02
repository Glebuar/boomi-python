
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..role import RoleService
from ...models import (
    Role,
    RoleBulkResponse,
    RoleBulkRequest,
    RoleQueryResponse,
    RoleQueryConfig,
)


class RoleServiceAsync(RoleService):
    """
    Async Wrapper for RoleServiceAsync
    """

    def create_role(self, request_body: Role = None) -> Awaitable[Union[Role, str]]:
        return to_async(super().create_role)(request_body)

    def get_role(self, id_: str) -> Awaitable[Union[Role, str]]:
        return to_async(super().get_role)(id_)

    def update_role(
        self, id_: str, request_body: Role = None
    ) -> Awaitable[Union[Role, str]]:
        return to_async(super().update_role)(id_, request_body)

    def delete_role(self, id_: str) -> Awaitable[None]:
        return to_async(super().delete_role)(id_)

    def bulk_role(
        self, request_body: RoleBulkRequest = None
    ) -> Awaitable[Union[RoleBulkResponse, str]]:
        return to_async(super().bulk_role)(request_body)

    def query_role(
        self, request_body: RoleQueryConfig = None
    ) -> Awaitable[Union[RoleQueryResponse, str]]:
        return to_async(super().query_role)(request_body)

    def query_more_role(
        self, request_body: str
    ) -> Awaitable[Union[RoleQueryResponse, str]]:
        return to_async(super().query_more_role)(request_body)
