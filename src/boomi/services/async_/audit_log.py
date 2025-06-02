
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..audit_log import AuditLogService
from ...models import (
    AuditLog,
    AuditLogBulkResponse,
    AuditLogBulkRequest,
    AuditLogQueryResponse,
    AuditLogQueryConfig,
)


class AuditLogServiceAsync(AuditLogService):
    """
    Async Wrapper for AuditLogServiceAsync
    """

    def get_audit_log(self, id_: str) -> Awaitable[Union[AuditLog, str]]:
        return to_async(super().get_audit_log)(id_)

    def bulk_audit_log(
        self, request_body: AuditLogBulkRequest = None
    ) -> Awaitable[Union[AuditLogBulkResponse, str]]:
        return to_async(super().bulk_audit_log)(request_body)

    def query_audit_log(
        self, request_body: AuditLogQueryConfig = None
    ) -> Awaitable[Union[AuditLogQueryResponse, str]]:
        return to_async(super().query_audit_log)(request_body)

    def query_more_audit_log(
        self, request_body: str
    ) -> Awaitable[Union[AuditLogQueryResponse, str]]:
        return to_async(super().query_more_audit_log)(request_body)
