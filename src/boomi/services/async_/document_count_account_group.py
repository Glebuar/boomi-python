
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..document_count_account_group import DocumentCountAccountGroupService
from ...models import (
    DocumentCountAccountGroupQueryResponse,
    DocumentCountAccountGroupQueryConfig,
)


class DocumentCountAccountGroupServiceAsync(DocumentCountAccountGroupService):
    """
    Async Wrapper for DocumentCountAccountGroupServiceAsync
    """

    def query_document_count_account_group(
        self, request_body: DocumentCountAccountGroupQueryConfig = None
    ) -> Awaitable[Union[DocumentCountAccountGroupQueryResponse, str]]:
        return to_async(super().query_document_count_account_group)(request_body)

    def query_more_document_count_account_group(
        self, request_body: str
    ) -> Awaitable[Union[DocumentCountAccountGroupQueryResponse, str]]:
        return to_async(super().query_more_document_count_account_group)(request_body)
