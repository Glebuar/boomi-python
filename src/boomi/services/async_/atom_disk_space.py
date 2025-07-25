
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..atom_disk_space import AtomDiskSpaceService
from ...models import AsyncOperationTokenResult, AtomDiskSpaceAsyncResponse


class AtomDiskSpaceServiceAsync(AtomDiskSpaceService):
    """
    Async Wrapper for AtomDiskSpaceServiceAsync
    """

    def async_get_atom_disk_space(
        self, id_: str
    ) -> Awaitable[Union[AsyncOperationTokenResult, str]]:
        return to_async(super().async_get_atom_disk_space)(id_)

    def async_token_atom_disk_space(
        self, token: str
    ) -> Awaitable[Union[AtomDiskSpaceAsyncResponse, str]]:
        return to_async(super().async_token_atom_disk_space)(token)
