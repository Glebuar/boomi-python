
from __future__ import annotations
from typing import Optional
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .audit_log_expression import AuditLogExpression, AuditLogExpressionGuard
from .audit_log_simple_expression import AuditLogSimpleExpression
from .audit_log_grouping_expression import AuditLogGroupingExpression


@JsonMap({})
class AuditLogQueryConfigQueryFilter(BaseModel):
    """AuditLogQueryConfigQueryFilter

    :param expression: expression
    :type expression: AuditLogExpression
    """

    def __init__(self, expression: AuditLogExpression, **kwargs):
        """AuditLogQueryConfigQueryFilter

        :param expression: expression
        :type expression: AuditLogExpression
        """
        self.expression = AuditLogExpressionGuard.return_one_of(expression)
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class AuditLogQueryConfig(BaseModel):
    """AuditLogQueryConfig

    :param query_filter: query_filter (optional)
    :type query_filter: Optional[AuditLogQueryConfigQueryFilter]
    """

    def __init__(self, query_filter: Optional[AuditLogQueryConfigQueryFilter] = None, **kwargs):
        """AuditLogQueryConfig

        :param query_filter: query_filter (optional)
        :type query_filter: Optional[AuditLogQueryConfigQueryFilter]
        """
        self.query_filter = self._define_object(
            query_filter, AuditLogQueryConfigQueryFilter
        ) if query_filter is not None else None
        self._kwargs = kwargs
