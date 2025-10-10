
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .audit_log_simple_expression import AuditLogSimpleExpression
from .audit_log_grouping_expression import AuditLogGroupingExpression


class AuditLogExpressionGuard(OneOfBaseModel):
    class_list = {
        "AuditLogSimpleExpression": AuditLogSimpleExpression,
        "AuditLogGroupingExpression": AuditLogGroupingExpression,
    }


AuditLogExpression = Union[AuditLogSimpleExpression, AuditLogGroupingExpression]
