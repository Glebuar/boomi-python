
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..installer_token import InstallerTokenService
from ...models import InstallerToken


class InstallerTokenServiceAsync(InstallerTokenService):
    """
    Async Wrapper for InstallerTokenServiceAsync
    """

    def create_installer_token(
        self, request_body: InstallerToken = None
    ) -> Awaitable[Union[InstallerToken, str]]:
        return to_async(super().create_installer_token)(request_body)
