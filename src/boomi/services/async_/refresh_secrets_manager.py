
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..refresh_secrets_manager import RefreshSecretsManagerService
from ...models import SecretsManagerRefreshResponse, SecretsManagerRefreshRequest


class RefreshSecretsManagerServiceAsync(RefreshSecretsManagerService):
    """
    Async Wrapper for RefreshSecretsManagerServiceAsync
    """

    def refresh_secrets_manager(
        self, request_body: SecretsManagerRefreshRequest = None
    ) -> Awaitable[Union[SecretsManagerRefreshResponse, str]]:
        return to_async(super().refresh_secrets_manager)(request_body)
