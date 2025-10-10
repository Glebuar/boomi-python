
from typing import Awaitable
from .utils.to_async import to_async
from ..account_provision import AccountProvisionService


class AccountProvisionServiceAsync(AccountProvisionService):
    """
    Async Wrapper for AccountProvisionServiceAsync
    """

    def create_account_provision(self) -> Awaitable[None]:
        return to_async(super().create_account_provision)()
