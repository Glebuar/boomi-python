
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..java_rollback import JavaRollbackService
from ...models import JavaRollback


class JavaRollbackServiceAsync(JavaRollbackService):
    """
    Async Wrapper for JavaRollbackServiceAsync
    """

    def execute_java_rollback(
        self, id_: str, request_body: JavaRollback = None
    ) -> Awaitable[Union[JavaRollback, str]]:
        return to_async(super().execute_java_rollback)(id_, request_body)
