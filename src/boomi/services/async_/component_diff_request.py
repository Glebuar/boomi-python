
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..component_diff_request import ComponentDiffRequestService
from ...models import (
    ComponentDiffResponseCreate,
    ComponentDiffRequest,
    ComponentDiffRequestBulkResponse,
    ComponentDiffRequestBulkRequest,
)


class ComponentDiffRequestServiceAsync(ComponentDiffRequestService):
    """
    Async Wrapper for ComponentDiffRequestServiceAsync
    """

    def create_component_diff_request(
        self, request_body: ComponentDiffRequest = None
    ) -> Awaitable[Union[ComponentDiffResponseCreate, str]]:
        return to_async(super().create_component_diff_request)(request_body)

    def get_component_diff_request(
        self, component_id: str
    ) -> Awaitable[Union[ComponentDiffRequest, str]]:
        return to_async(super().get_component_diff_request)(component_id)

    def bulk_component_diff_request(
        self, request_body: ComponentDiffRequestBulkRequest = None
    ) -> Awaitable[Union[ComponentDiffRequestBulkResponse, str]]:
        return to_async(super().bulk_component_diff_request)(request_body)
