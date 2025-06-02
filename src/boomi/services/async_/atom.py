
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..atom import AtomService
from ...models import (
    Atom,
    AtomBulkResponse,
    AtomBulkRequest,
    AtomQueryResponse,
    AtomQueryConfig,
    AtomCountersAsyncResponse,
    AsyncOperationTokenResult,
    PersistedProcessPropertiesAsyncResponse,
)


class AtomServiceAsync(AtomService):
    """
    Async Wrapper for AtomServiceAsync
    """

    def create_atom(self, request_body: Atom = None) -> Awaitable[Union[Atom, str]]:
        return to_async(super().create_atom)(request_body)

    def get_atom(self, id_: str) -> Awaitable[Union[Atom, str]]:
        return to_async(super().get_atom)(id_)

    def update_atom(
        self, id_: str, request_body: Atom = None
    ) -> Awaitable[Union[Atom, str]]:
        return to_async(super().update_atom)(id_, request_body)

    def delete_atom(self, id_: str) -> Awaitable[None]:
        return to_async(super().delete_atom)(id_)

    def bulk_atom(
        self, request_body: AtomBulkRequest = None
    ) -> Awaitable[Union[AtomBulkResponse, str]]:
        return to_async(super().bulk_atom)(request_body)

    def query_atom(
        self, request_body: AtomQueryConfig = None
    ) -> Awaitable[Union[AtomQueryResponse, str]]:
        return to_async(super().query_atom)(request_body)

    def query_more_atom(
        self, request_body: str
    ) -> Awaitable[Union[AtomQueryResponse, str]]:
        return to_async(super().query_more_atom)(request_body)

    def async_token_atom_counters(
        self, token: str
    ) -> Awaitable[Union[AtomCountersAsyncResponse, str]]:
        return to_async(super().async_token_atom_counters)(token)

    def async_get_atom_counters(
        self, id_: str
    ) -> Awaitable[Union[AsyncOperationTokenResult, str]]:
        return to_async(super().async_get_atom_counters)(id_)

    def async_token_persisted_process_properties(
        self, token: str
    ) -> Awaitable[Union[PersistedProcessPropertiesAsyncResponse, str]]:
        return to_async(super().async_token_persisted_process_properties)(token)

    def async_get_persisted_process_properties(
        self, id_: str
    ) -> Awaitable[Union[AsyncOperationTokenResult, str]]:
        return to_async(super().async_get_persisted_process_properties)(id_)
