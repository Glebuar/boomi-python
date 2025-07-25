
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..component_reference import ComponentReferenceService
from ...models import (
    ComponentReference,
    ComponentReferenceBulkResponse,
    ComponentReferenceBulkRequest,
    ComponentReferenceQueryResponse,
    ComponentReferenceQueryConfig,
)


class ComponentReferenceServiceAsync(ComponentReferenceService):
    """
    Async Wrapper for ComponentReferenceServiceAsync
    """

    def get_component_reference(
        self, component_id: str
    ) -> Awaitable[Union[ComponentReference, str]]:
        return to_async(super().get_component_reference)(component_id)

    def bulk_component_reference(
        self, request_body: ComponentReferenceBulkRequest = None
    ) -> Awaitable[Union[ComponentReferenceBulkResponse, str]]:
        return to_async(super().bulk_component_reference)(request_body)

    def query_component_reference(
        self, request_body: ComponentReferenceQueryConfig = None
    ) -> Awaitable[Union[ComponentReferenceQueryResponse, str]]:
        return to_async(super().query_component_reference)(request_body)

    def query_more_component_reference(
        self, request_body: str
    ) -> Awaitable[Union[ComponentReferenceQueryResponse, str]]:
        return to_async(super().query_more_component_reference)(request_body)
