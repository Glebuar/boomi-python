
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .component_environment_attachment_expression import (
    ComponentEnvironmentAttachmentExpression,
    ComponentEnvironmentAttachmentExpressionGuard,
)
from .component_environment_attachment_simple_expression import (
    ComponentEnvironmentAttachmentSimpleExpression,
)
from .component_environment_attachment_grouping_expression import (
    ComponentEnvironmentAttachmentGroupingExpression,
)


@JsonMap({})
class ComponentEnvironmentAttachmentQueryConfigQueryFilter(BaseModel):
    """ComponentEnvironmentAttachmentQueryConfigQueryFilter

    :param expression: expression
    :type expression: ComponentEnvironmentAttachmentExpression
    """

    def __init__(self, expression: ComponentEnvironmentAttachmentExpression, **kwargs):
        """ComponentEnvironmentAttachmentQueryConfigQueryFilter

        :param expression: expression
        :type expression: ComponentEnvironmentAttachmentExpression
        """
        self.expression = ComponentEnvironmentAttachmentExpressionGuard.return_one_of(
            expression
        )
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class ComponentEnvironmentAttachmentQueryConfig(BaseModel):
    """ComponentEnvironmentAttachmentQueryConfig

    :param query_filter: query_filter
    :type query_filter: ComponentEnvironmentAttachmentQueryConfigQueryFilter
    """

    def __init__(
        self,
        query_filter: ComponentEnvironmentAttachmentQueryConfigQueryFilter,
        **kwargs,
    ):
        """ComponentEnvironmentAttachmentQueryConfig

        :param query_filter: query_filter
        :type query_filter: ComponentEnvironmentAttachmentQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, ComponentEnvironmentAttachmentQueryConfigQueryFilter
        )
        self._kwargs = kwargs
