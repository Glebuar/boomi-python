
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..deployed_package import DeployedPackageService
from ...models import (
    DeployedPackage,
    DeployedPackageBulkResponse,
    DeployedPackageBulkRequest,
    DeployedPackageQueryResponse,
    DeployedPackageQueryConfig,
)


class DeployedPackageServiceAsync(DeployedPackageService):
    """
    Async Wrapper for DeployedPackageServiceAsync
    """

    def create_deployed_package(
        self, request_body: DeployedPackage = None
    ) -> Awaitable[Union[DeployedPackage, str]]:
        return to_async(super().create_deployed_package)(request_body)

    def get_deployed_package(self, id_: str) -> Awaitable[Union[DeployedPackage, str]]:
        return to_async(super().get_deployed_package)(id_)

    def delete_deployed_package(self, id_: str) -> Awaitable[None]:
        return to_async(super().delete_deployed_package)(id_)

    def bulk_deployed_package(
        self, request_body: DeployedPackageBulkRequest = None
    ) -> Awaitable[Union[DeployedPackageBulkResponse, str]]:
        return to_async(super().bulk_deployed_package)(request_body)

    def query_deployed_package(
        self, request_body: DeployedPackageQueryConfig = None
    ) -> Awaitable[Union[DeployedPackageQueryResponse, str]]:
        return to_async(super().query_deployed_package)(request_body)

    def query_more_deployed_package(
        self, request_body: str
    ) -> Awaitable[Union[DeployedPackageQueryResponse, str]]:
        return to_async(super().query_more_deployed_package)(request_body)
