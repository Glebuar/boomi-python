
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..environment_map_extension_user_defined_function import (
    EnvironmentMapExtensionUserDefinedFunctionService,
)
from ...models import (
    EnvironmentMapExtensionUserDefinedFunction,
    EnvironmentMapExtensionUserDefinedFunctionBulkResponse,
    EnvironmentMapExtensionUserDefinedFunctionBulkRequest,
)


class EnvironmentMapExtensionUserDefinedFunctionServiceAsync(
    EnvironmentMapExtensionUserDefinedFunctionService
):
    """
    Async Wrapper for EnvironmentMapExtensionUserDefinedFunctionServiceAsync
    """

    def create_environment_map_extension_user_defined_function(
        self, request_body: EnvironmentMapExtensionUserDefinedFunction = None
    ) -> Awaitable[Union[EnvironmentMapExtensionUserDefinedFunction, str]]:
        return to_async(super().create_environment_map_extension_user_defined_function)(
            request_body
        )

    def get_environment_map_extension_user_defined_function(
        self, id_: str
    ) -> Awaitable[Union[EnvironmentMapExtensionUserDefinedFunction, str]]:
        return to_async(super().get_environment_map_extension_user_defined_function)(
            id_
        )

    def update_environment_map_extension_user_defined_function(
        self, id_: str, request_body: EnvironmentMapExtensionUserDefinedFunction = None
    ) -> Awaitable[Union[EnvironmentMapExtensionUserDefinedFunction, str]]:
        return to_async(super().update_environment_map_extension_user_defined_function)(
            id_, request_body
        )

    def delete_environment_map_extension_user_defined_function(
        self, id_: str
    ) -> Awaitable[None]:
        return to_async(super().delete_environment_map_extension_user_defined_function)(
            id_
        )

    def bulk_environment_map_extension_user_defined_function(
        self, request_body: EnvironmentMapExtensionUserDefinedFunctionBulkRequest = None
    ) -> Awaitable[Union[EnvironmentMapExtensionUserDefinedFunctionBulkResponse, str]]:
        return to_async(super().bulk_environment_map_extension_user_defined_function)(
            request_body
        )
