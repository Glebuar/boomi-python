
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..atom_connection_field_extension_summary import (
    AtomConnectionFieldExtensionSummaryService,
)
from ...models import (
    AtomConnectionFieldExtensionSummaryQueryResponse,
    AtomConnectionFieldExtensionSummaryQueryConfig,
)


class AtomConnectionFieldExtensionSummaryServiceAsync(
    AtomConnectionFieldExtensionSummaryService
):
    """
    Async Wrapper for AtomConnectionFieldExtensionSummaryServiceAsync
    """

    def query_atom_connection_field_extension_summary(
        self, request_body: AtomConnectionFieldExtensionSummaryQueryConfig = None
    ) -> Awaitable[Union[AtomConnectionFieldExtensionSummaryQueryResponse, str]]:
        return to_async(super().query_atom_connection_field_extension_summary)(
            request_body
        )

    def query_more_atom_connection_field_extension_summary(
        self, request_body: str
    ) -> Awaitable[Union[AtomConnectionFieldExtensionSummaryQueryResponse, str]]:
        return to_async(super().query_more_atom_connection_field_extension_summary)(
            request_body
        )
