
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..document_count_account import DocumentCountAccountService
from ...models import DocumentCountAccountQueryResponse, DocumentCountAccountQueryConfig


class DocumentCountAccountServiceAsync(DocumentCountAccountService):
    """
    Async Wrapper for DocumentCountAccountServiceAsync
    """

    def query_document_count_account(
        self, request_body: DocumentCountAccountQueryConfig = None
    ) -> Awaitable[Union[DocumentCountAccountQueryResponse, str]]:
        return to_async(super().query_document_count_account)(request_body)

    def query_more_document_count_account(
        self, request_body: str
    ) -> Awaitable[Union[DocumentCountAccountQueryResponse, str]]:
        return to_async(super().query_more_document_count_account)(request_body)
