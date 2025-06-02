
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .edi_custom_connector_record_expression import (
    EdiCustomConnectorRecordExpression,
    EdiCustomConnectorRecordExpressionGuard,
)
from .edi_custom_connector_record_simple_expression import (
    EdiCustomConnectorRecordSimpleExpression,
)
from .edi_custom_connector_record_grouping_expression import (
    EdiCustomConnectorRecordGroupingExpression,
)


@JsonMap({})
class EdiCustomConnectorRecordQueryConfigQueryFilter(BaseModel):
    """EdiCustomConnectorRecordQueryConfigQueryFilter

    :param expression: expression
    :type expression: EdiCustomConnectorRecordExpression
    """

    def __init__(self, expression: EdiCustomConnectorRecordExpression, **kwargs):
        """EdiCustomConnectorRecordQueryConfigQueryFilter

        :param expression: expression
        :type expression: EdiCustomConnectorRecordExpression
        """
        self.expression = EdiCustomConnectorRecordExpressionGuard.return_one_of(
            expression
        )
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class EdiCustomConnectorRecordQueryConfig(BaseModel):
    """EdiCustomConnectorRecordQueryConfig

    :param query_filter: query_filter
    :type query_filter: EdiCustomConnectorRecordQueryConfigQueryFilter
    """

    def __init__(
        self, query_filter: EdiCustomConnectorRecordQueryConfigQueryFilter, **kwargs
    ):
        """EdiCustomConnectorRecordQueryConfig

        :param query_filter: query_filter
        :type query_filter: EdiCustomConnectorRecordQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, EdiCustomConnectorRecordQueryConfigQueryFilter
        )
        self._kwargs = kwargs
