
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .branch_expression import BranchExpression, BranchExpressionGuard
from .branch_simple_expression import BranchSimpleExpression
from .branch_grouping_expression import BranchGroupingExpression


@JsonMap({})
class BranchQueryConfigQueryFilter(BaseModel):
    """BranchQueryConfigQueryFilter

    :param expression: expression
    :type expression: BranchExpression
    """

    def __init__(self, expression: BranchExpression, **kwargs):
        """BranchQueryConfigQueryFilter

        :param expression: expression
        :type expression: BranchExpression
        """
        self.expression = BranchExpressionGuard.return_one_of(expression)
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class BranchQueryConfig(BaseModel):
    """BranchQueryConfig

    :param query_filter: query_filter
    :type query_filter: BranchQueryConfigQueryFilter
    """

    def __init__(self, query_filter: BranchQueryConfigQueryFilter, **kwargs):
        """BranchQueryConfig

        :param query_filter: query_filter
        :type query_filter: BranchQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, BranchQueryConfigQueryFilter
        )
        self._kwargs = kwargs
