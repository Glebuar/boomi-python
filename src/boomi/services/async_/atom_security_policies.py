
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..atom_security_policies import AtomSecurityPoliciesService
from ...models import (
    AtomSecurityPolicies,
    AsyncOperationTokenResult,
    AtomSecurityPoliciesAsyncResponse,
)


class AtomSecurityPoliciesServiceAsync(AtomSecurityPoliciesService):
    """
    Async Wrapper for AtomSecurityPoliciesServiceAsync
    """

    def update_atom_security_policies(
        self, id_: str, request_body: AtomSecurityPolicies = None
    ) -> Awaitable[Union[AtomSecurityPolicies, str]]:
        return to_async(super().update_atom_security_policies)(id_, request_body)

    def async_get_atom_security_policies(
        self, id_: str
    ) -> Awaitable[Union[AsyncOperationTokenResult, str]]:
        return to_async(super().async_get_atom_security_policies)(id_)

    def async_token_atom_security_policies(
        self, token: str
    ) -> Awaitable[Union[AtomSecurityPoliciesAsyncResponse, str]]:
        return to_async(super().async_token_atom_security_policies)(token)
