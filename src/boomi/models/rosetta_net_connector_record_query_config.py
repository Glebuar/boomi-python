
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .rosetta_net_connector_record_expression import (
    RosettaNetConnectorRecordExpression,
    RosettaNetConnectorRecordExpressionGuard,
)
from .rosetta_net_connector_record_simple_expression import (
    RosettaNetConnectorRecordSimpleExpression,
)
from .rosetta_net_connector_record_grouping_expression import (
    RosettaNetConnectorRecordGroupingExpression,
)


@JsonMap({})
class RosettaNetConnectorRecordQueryConfigQueryFilter(BaseModel):
    """RosettaNetConnectorRecordQueryConfigQueryFilter

    :param expression: expression
    :type expression: RosettaNetConnectorRecordExpression
    """

    def __init__(self, expression: RosettaNetConnectorRecordExpression, **kwargs):
        """RosettaNetConnectorRecordQueryConfigQueryFilter

        :param expression: expression
        :type expression: RosettaNetConnectorRecordExpression
        """
        self.expression = RosettaNetConnectorRecordExpressionGuard.return_one_of(
            expression
        )
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class RosettaNetConnectorRecordQueryConfig(BaseModel):
    """RosettaNetConnectorRecordQueryConfig

    :param query_filter: query_filter
    :type query_filter: RosettaNetConnectorRecordQueryConfigQueryFilter
    """

    def __init__(
        self, query_filter: RosettaNetConnectorRecordQueryConfigQueryFilter, **kwargs
    ):
        """RosettaNetConnectorRecordQueryConfig

        :param query_filter: query_filter
        :type query_filter: RosettaNetConnectorRecordQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, RosettaNetConnectorRecordQueryConfigQueryFilter
        )
        self._kwargs = kwargs
