
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..rerun_document import RerunDocumentService
from ...models import RerunDocument


class RerunDocumentServiceAsync(RerunDocumentService):
    """
    Async Wrapper for RerunDocumentServiceAsync
    """

    def create_rerun_document(
        self, request_body: RerunDocument = None
    ) -> Awaitable[Union[RerunDocument, str]]:
        return to_async(super().create_rerun_document)(request_body)
