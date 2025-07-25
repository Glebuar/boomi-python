
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..component_metadata import ComponentMetadataService
from ...models import (
    ComponentMetadata,
    ComponentMetadataBulkResponse,
    ComponentMetadataBulkRequest,
    ComponentMetadataQueryResponse,
    ComponentMetadataQueryConfig,
)


class ComponentMetadataServiceAsync(ComponentMetadataService):
    """
    Async Wrapper for ComponentMetadataServiceAsync
    """

    def create_component_metadata(
        self, request_body: ComponentMetadata = None
    ) -> Awaitable[Union[ComponentMetadata, str]]:
        return to_async(super().create_component_metadata)(request_body)

    def get_component_metadata(
        self, id_: str
    ) -> Awaitable[Union[ComponentMetadata, str]]:
        return to_async(super().get_component_metadata)(id_)

    def update_component_metadata(
        self, id_: str, request_body: ComponentMetadata = None
    ) -> Awaitable[Union[ComponentMetadata, str]]:
        return to_async(super().update_component_metadata)(id_, request_body)

    def delete_component_metadata(self, id_: str) -> Awaitable[None]:
        return to_async(super().delete_component_metadata)(id_)

    def bulk_component_metadata(
        self, request_body: ComponentMetadataBulkRequest = None
    ) -> Awaitable[Union[ComponentMetadataBulkResponse, str]]:
        return to_async(super().bulk_component_metadata)(request_body)

    def query_component_metadata(
        self, request_body: ComponentMetadataQueryConfig = None
    ) -> Awaitable[Union[ComponentMetadataQueryResponse, str]]:
        return to_async(super().query_component_metadata)(request_body)

    def query_more_component_metadata(
        self, request_body: str
    ) -> Awaitable[Union[ComponentMetadataQueryResponse, str]]:
        return to_async(super().query_more_component_metadata)(request_body)
