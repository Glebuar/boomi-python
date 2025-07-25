
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .atom_expression import AtomExpression, AtomExpressionGuard
from .atom_simple_expression import AtomSimpleExpression
from .atom_grouping_expression import AtomGroupingExpression


@JsonMap({})
class AtomQueryConfigQueryFilter(BaseModel):
    """AtomQueryConfigQueryFilter

    :param expression: expression
    :type expression: AtomExpression
    """

    def __init__(self, expression: AtomExpression, **kwargs):
        """AtomQueryConfigQueryFilter

        :param expression: expression
        :type expression: AtomExpression
        """
        self.expression = AtomExpressionGuard.return_one_of(expression)
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class AtomQueryConfig(BaseModel):
    """AtomQueryConfig

    :param query_filter: query_filter
    :type query_filter: AtomQueryConfigQueryFilter
    """

    def __init__(self, query_filter: AtomQueryConfigQueryFilter, **kwargs):
        """AtomQueryConfig

        :param query_filter: query_filter
        :type query_filter: AtomQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, AtomQueryConfigQueryFilter
        )
        self._kwargs = kwargs
