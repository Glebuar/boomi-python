
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..process_environment_attachment import ProcessEnvironmentAttachmentService
from ...models import ProcessEnvironmentAttachment


class ProcessEnvironmentAttachmentServiceAsync(ProcessEnvironmentAttachmentService):
    """
    Async Wrapper for ProcessEnvironmentAttachmentServiceAsync
    """

    def create_process_environment_attachment(
        self, request_body: ProcessEnvironmentAttachment = None
    ) -> Awaitable[Union[ProcessEnvironmentAttachment, str]]:
        return to_async(super().create_process_environment_attachment)(request_body)
