
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..api_usage_count import ApiUsageCountService
from ...models import ApiUsageCountQueryResponse, ApiUsageCountQueryConfig


class ApiUsageCountServiceAsync(ApiUsageCountService):
    """
    Async Wrapper for ApiUsageCountServiceAsync
    """

    def query_api_usage_count(
        self, request_body: ApiUsageCountQueryConfig = None
    ) -> Awaitable[Union[ApiUsageCountQueryResponse, str]]:
        return to_async(super().query_api_usage_count)(request_body)

    def query_more_api_usage_count(
        self, request_body: str
    ) -> Awaitable[Union[ApiUsageCountQueryResponse, str]]:
        return to_async(super().query_more_api_usage_count)(request_body)
