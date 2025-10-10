
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .process_environment_attachment_expression import (
    ProcessEnvironmentAttachmentExpression,
    ProcessEnvironmentAttachmentExpressionGuard,
)
from .process_environment_attachment_simple_expression import (
    ProcessEnvironmentAttachmentSimpleExpression,
)
from .process_environment_attachment_grouping_expression import (
    ProcessEnvironmentAttachmentGroupingExpression,
)


@JsonMap({})
class ProcessEnvironmentAttachmentQueryConfigQueryFilter(BaseModel):
    """ProcessEnvironmentAttachmentQueryConfigQueryFilter

    :param expression: expression
    :type expression: ProcessEnvironmentAttachmentExpression
    """

    def __init__(self, expression: ProcessEnvironmentAttachmentExpression, **kwargs):
        """ProcessEnvironmentAttachmentQueryConfigQueryFilter

        :param expression: expression
        :type expression: ProcessEnvironmentAttachmentExpression
        """
        self.expression = ProcessEnvironmentAttachmentExpressionGuard.return_one_of(
            expression
        )
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class ProcessEnvironmentAttachmentQueryConfig(BaseModel):
    """ProcessEnvironmentAttachmentQueryConfig

    :param query_filter: query_filter
    :type query_filter: ProcessEnvironmentAttachmentQueryConfigQueryFilter
    """

    def __init__(
        self, query_filter: ProcessEnvironmentAttachmentQueryConfigQueryFilter, **kwargs
    ):
        """ProcessEnvironmentAttachmentQueryConfig

        :param query_filter: query_filter
        :type query_filter: ProcessEnvironmentAttachmentQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, ProcessEnvironmentAttachmentQueryConfigQueryFilter
        )
        self._kwargs = kwargs
