
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..atom_purge import AtomPurgeService
from ...models import AtomPurge


class AtomPurgeServiceAsync(AtomPurgeService):
    """
    Async Wrapper for AtomPurgeServiceAsync
    """

    def update_atom_purge(
        self, id_: str, request_body: AtomPurge = None
    ) -> Awaitable[Union[AtomPurge, str]]:
        return to_async(super().update_atom_purge)(id_, request_body)
