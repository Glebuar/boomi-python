
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..deployment import DeploymentService
from ...models import (
    Deployment,
    DeploymentBulkResponse,
    DeploymentBulkRequest,
    DeploymentQueryResponse,
    DeploymentQueryConfig,
    ProcessEnvironmentAttachmentQueryResponse,
    ProcessEnvironmentAttachmentQueryConfig,
)


class DeploymentServiceAsync(DeploymentService):
    """
    Async Wrapper for DeploymentServiceAsync
    """

    def create_deployment(
        self, request_body: Deployment = None
    ) -> Awaitable[Union[Deployment, str]]:
        return to_async(super().create_deployment)(request_body)

    def get_deployment(self, id_: str) -> Awaitable[Union[Deployment, str]]:
        return to_async(super().get_deployment)(id_)

    def bulk_deployment(
        self, request_body: DeploymentBulkRequest = None
    ) -> Awaitable[Union[DeploymentBulkResponse, str]]:
        return to_async(super().bulk_deployment)(request_body)

    def query_deployment(
        self, request_body: DeploymentQueryConfig = None
    ) -> Awaitable[Union[DeploymentQueryResponse, str]]:
        return to_async(super().query_deployment)(request_body)

    def query_more_deployment(
        self, request_body: str
    ) -> Awaitable[Union[DeploymentQueryResponse, str]]:
        return to_async(super().query_more_deployment)(request_body)

    def query_process_environment_attachment(
        self, request_body: ProcessEnvironmentAttachmentQueryConfig = None
    ) -> Awaitable[Union[ProcessEnvironmentAttachmentQueryResponse, str]]:
        return to_async(super().query_process_environment_attachment)(request_body)

    def query_more_process_environment_attachment(
        self, request_body: str
    ) -> Awaitable[Union[ProcessEnvironmentAttachmentQueryResponse, str]]:
        return to_async(super().query_more_process_environment_attachment)(request_body)

    def delete_process_environment_attachment(self, id_: str) -> Awaitable[None]:
        return to_async(super().delete_process_environment_attachment)(id_)
