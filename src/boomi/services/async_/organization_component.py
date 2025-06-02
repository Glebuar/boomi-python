
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..organization_component import OrganizationComponentService
from ...models import (
    OrganizationComponent,
    OrganizationComponentBulkResponse,
    OrganizationComponentBulkRequest,
    OrganizationComponentQueryResponse,
    OrganizationComponentQueryConfig,
)


class OrganizationComponentServiceAsync(OrganizationComponentService):
    """
    Async Wrapper for OrganizationComponentServiceAsync
    """

    def create_organization_component(
        self, request_body: OrganizationComponent = None
    ) -> Awaitable[Union[OrganizationComponent, str]]:
        return to_async(super().create_organization_component)(request_body)

    def get_organization_component(
        self, id_: str
    ) -> Awaitable[Union[OrganizationComponent, str]]:
        return to_async(super().get_organization_component)(id_)

    def update_organization_component(
        self, id_: str, request_body: OrganizationComponent = None
    ) -> Awaitable[Union[OrganizationComponent, str]]:
        return to_async(super().update_organization_component)(id_, request_body)

    def delete_organization_component(self, id_: str) -> Awaitable[None]:
        return to_async(super().delete_organization_component)(id_)

    def bulk_organization_component(
        self, request_body: OrganizationComponentBulkRequest = None
    ) -> Awaitable[Union[str, OrganizationComponentBulkResponse]]:
        return to_async(super().bulk_organization_component)(request_body)

    def query_organization_component(
        self, request_body: OrganizationComponentQueryConfig = None
    ) -> Awaitable[Union[OrganizationComponentQueryResponse, str]]:
        return to_async(super().query_organization_component)(request_body)

    def query_more_organization_component(
        self, request_body: str
    ) -> Awaitable[Union[OrganizationComponentQueryResponse, str]]:
        return to_async(super().query_more_organization_component)(request_body)
