
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .shared_communication_channel_component_expression import (
    SharedCommunicationChannelComponentExpression,
    SharedCommunicationChannelComponentExpressionGuard,
)
from .shared_communication_channel_component_simple_expression import (
    SharedCommunicationChannelComponentSimpleExpression,
)
from .shared_communication_channel_component_grouping_expression import (
    SharedCommunicationChannelComponentGroupingExpression,
)


@JsonMap({})
class SharedCommunicationChannelComponentQueryConfigQueryFilter(BaseModel):
    """SharedCommunicationChannelComponentQueryConfigQueryFilter

    :param expression: expression
    :type expression: SharedCommunicationChannelComponentExpression
    """

    def __init__(
        self, expression: SharedCommunicationChannelComponentExpression, **kwargs
    ):
        """SharedCommunicationChannelComponentQueryConfigQueryFilter

        :param expression: expression
        :type expression: SharedCommunicationChannelComponentExpression
        """
        self.expression = (
            SharedCommunicationChannelComponentExpressionGuard.return_one_of(expression)
        )
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class SharedCommunicationChannelComponentQueryConfig(BaseModel):
    """SharedCommunicationChannelComponentQueryConfig

    :param query_filter: query_filter
    :type query_filter: SharedCommunicationChannelComponentQueryConfigQueryFilter
    """

    def __init__(
        self,
        query_filter: SharedCommunicationChannelComponentQueryConfigQueryFilter,
        **kwargs,
    ):
        """SharedCommunicationChannelComponentQueryConfig

        :param query_filter: query_filter
        :type query_filter: SharedCommunicationChannelComponentQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, SharedCommunicationChannelComponentQueryConfigQueryFilter
        )
        self._kwargs = kwargs
