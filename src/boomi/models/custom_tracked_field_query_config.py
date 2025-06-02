
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .custom_tracked_field_expression import (
    CustomTrackedFieldExpression,
    CustomTrackedFieldExpressionGuard,
)
from .custom_tracked_field_simple_expression import CustomTrackedFieldSimpleExpression
from .custom_tracked_field_grouping_expression import (
    CustomTrackedFieldGroupingExpression,
)


@JsonMap({})
class CustomTrackedFieldQueryConfigQueryFilter(BaseModel):
    """CustomTrackedFieldQueryConfigQueryFilter

    :param expression: expression
    :type expression: CustomTrackedFieldExpression
    """

    def __init__(self, expression: CustomTrackedFieldExpression, **kwargs):
        """CustomTrackedFieldQueryConfigQueryFilter

        :param expression: expression
        :type expression: CustomTrackedFieldExpression
        """
        self.expression = CustomTrackedFieldExpressionGuard.return_one_of(expression)
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class CustomTrackedFieldQueryConfig(BaseModel):
    """CustomTrackedFieldQueryConfig

    :param query_filter: query_filter
    :type query_filter: CustomTrackedFieldQueryConfigQueryFilter
    """

    def __init__(
        self, query_filter: CustomTrackedFieldQueryConfigQueryFilter, **kwargs
    ):
        """CustomTrackedFieldQueryConfig

        :param query_filter: query_filter
        :type query_filter: CustomTrackedFieldQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, CustomTrackedFieldQueryConfigQueryFilter
        )
        self._kwargs = kwargs
