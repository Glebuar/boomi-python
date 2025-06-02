
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..atom_counters import AtomCountersService
from ...models import AtomCounters


class AtomCountersServiceAsync(AtomCountersService):
    """
    Async Wrapper for AtomCountersServiceAsync
    """

    def update_atom_counters(
        self, id_: str, request_body: AtomCounters = None
    ) -> Awaitable[Union[AtomCounters, str]]:
        return to_async(super().update_atom_counters)(id_, request_body)
