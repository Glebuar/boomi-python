
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..java_upgrade import JavaUpgradeService
from ...models import JavaUpgrade


class JavaUpgradeServiceAsync(JavaUpgradeService):
    """
    Async Wrapper for JavaUpgradeServiceAsync
    """

    def create_java_upgrade(
        self, request_body: JavaUpgrade = None
    ) -> Awaitable[Union[JavaUpgrade, str]]:
        return to_async(super().create_java_upgrade)(request_body)
