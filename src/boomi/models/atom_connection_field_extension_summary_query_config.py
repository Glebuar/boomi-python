
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .atom_connection_field_extension_summary_expression import (
    AtomConnectionFieldExtensionSummaryExpression,
    AtomConnectionFieldExtensionSummaryExpressionGuard,
)
from .atom_connection_field_extension_summary_simple_expression import (
    AtomConnectionFieldExtensionSummarySimpleExpression,
)
from .atom_connection_field_extension_summary_grouping_expression import (
    AtomConnectionFieldExtensionSummaryGroupingExpression,
)


@JsonMap({})
class AtomConnectionFieldExtensionSummaryQueryConfigQueryFilter(BaseModel):
    """AtomConnectionFieldExtensionSummaryQueryConfigQueryFilter

    :param expression: expression
    :type expression: AtomConnectionFieldExtensionSummaryExpression
    """

    def __init__(
        self, expression: AtomConnectionFieldExtensionSummaryExpression, **kwargs
    ):
        """AtomConnectionFieldExtensionSummaryQueryConfigQueryFilter

        :param expression: expression
        :type expression: AtomConnectionFieldExtensionSummaryExpression
        """
        self.expression = (
            AtomConnectionFieldExtensionSummaryExpressionGuard.return_one_of(expression)
        )
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class AtomConnectionFieldExtensionSummaryQueryConfig(BaseModel):
    """AtomConnectionFieldExtensionSummaryQueryConfig

    :param query_filter: query_filter
    :type query_filter: AtomConnectionFieldExtensionSummaryQueryConfigQueryFilter
    """

    def __init__(
        self,
        query_filter: AtomConnectionFieldExtensionSummaryQueryConfigQueryFilter,
        **kwargs,
    ):
        """AtomConnectionFieldExtensionSummaryQueryConfig

        :param query_filter: query_filter
        :type query_filter: AtomConnectionFieldExtensionSummaryQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, AtomConnectionFieldExtensionSummaryQueryConfigQueryFilter
        )
        self._kwargs = kwargs
