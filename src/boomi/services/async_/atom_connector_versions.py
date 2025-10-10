
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..atom_connector_versions import AtomConnectorVersionsService
from ...models import (
    AtomConnectorVersions,
    AtomConnectorVersionsBulkResponse,
    AtomConnectorVersionsBulkRequest,
)


class AtomConnectorVersionsServiceAsync(AtomConnectorVersionsService):
    """
    Async Wrapper for AtomConnectorVersionsServiceAsync
    """

    def get_atom_connector_versions(
        self, id_: str
    ) -> Awaitable[Union[AtomConnectorVersions, str]]:
        return to_async(super().get_atom_connector_versions)(id_)

    def bulk_atom_connector_versions(
        self, request_body: AtomConnectorVersionsBulkRequest = None
    ) -> Awaitable[Union[AtomConnectorVersionsBulkResponse, str]]:
        return to_async(super().bulk_atom_connector_versions)(request_body)
