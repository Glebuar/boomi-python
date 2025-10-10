
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .integration_pack_instance_expression import (
    IntegrationPackInstanceExpression,
    IntegrationPackInstanceExpressionGuard,
)
from .integration_pack_instance_simple_expression import (
    IntegrationPackInstanceSimpleExpression,
)
from .integration_pack_instance_grouping_expression import (
    IntegrationPackInstanceGroupingExpression,
)


@JsonMap({})
class IntegrationPackInstanceQueryConfigQueryFilter(BaseModel):
    """IntegrationPackInstanceQueryConfigQueryFilter

    :param expression: expression
    :type expression: IntegrationPackInstanceExpression
    """

    def __init__(self, expression: IntegrationPackInstanceExpression, **kwargs):
        """IntegrationPackInstanceQueryConfigQueryFilter

        :param expression: expression
        :type expression: IntegrationPackInstanceExpression
        """
        self.expression = IntegrationPackInstanceExpressionGuard.return_one_of(
            expression
        )
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class IntegrationPackInstanceQueryConfig(BaseModel):
    """IntegrationPackInstanceQueryConfig

    :param query_filter: query_filter
    :type query_filter: IntegrationPackInstanceQueryConfigQueryFilter
    """

    def __init__(
        self, query_filter: IntegrationPackInstanceQueryConfigQueryFilter, **kwargs
    ):
        """IntegrationPackInstanceQueryConfig

        :param query_filter: query_filter
        :type query_filter: IntegrationPackInstanceQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, IntegrationPackInstanceQueryConfigQueryFilter
        )
        self._kwargs = kwargs
