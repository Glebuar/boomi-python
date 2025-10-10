
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..atom_startup_properties import AtomStartupPropertiesService
from ...models import (
    AtomStartupProperties,
    AtomStartupPropertiesBulkResponse,
    AtomStartupPropertiesBulkRequest,
)


class AtomStartupPropertiesServiceAsync(AtomStartupPropertiesService):
    """
    Async Wrapper for AtomStartupPropertiesServiceAsync
    """

    def get_atom_startup_properties(
        self, id_: str
    ) -> Awaitable[Union[AtomStartupProperties, str]]:
        return to_async(super().get_atom_startup_properties)(id_)

    def bulk_atom_startup_properties(
        self, request_body: AtomStartupPropertiesBulkRequest = None
    ) -> Awaitable[Union[AtomStartupPropertiesBulkResponse, str]]:
        return to_async(super().bulk_atom_startup_properties)(request_body)
