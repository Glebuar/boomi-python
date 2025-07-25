
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .integration_pack_environment_attachment_expression import (
    IntegrationPackEnvironmentAttachmentExpression,
    IntegrationPackEnvironmentAttachmentExpressionGuard,
)
from .integration_pack_environment_attachment_simple_expression import (
    IntegrationPackEnvironmentAttachmentSimpleExpression,
)
from .integration_pack_environment_attachment_grouping_expression import (
    IntegrationPackEnvironmentAttachmentGroupingExpression,
)


@JsonMap({})
class IntegrationPackEnvironmentAttachmentQueryConfigQueryFilter(BaseModel):
    """IntegrationPackEnvironmentAttachmentQueryConfigQueryFilter

    :param expression: expression
    :type expression: IntegrationPackEnvironmentAttachmentExpression
    """

    def __init__(
        self, expression: IntegrationPackEnvironmentAttachmentExpression, **kwargs
    ):
        """IntegrationPackEnvironmentAttachmentQueryConfigQueryFilter

        :param expression: expression
        :type expression: IntegrationPackEnvironmentAttachmentExpression
        """
        self.expression = (
            IntegrationPackEnvironmentAttachmentExpressionGuard.return_one_of(
                expression
            )
        )
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class IntegrationPackEnvironmentAttachmentQueryConfig(BaseModel):
    """IntegrationPackEnvironmentAttachmentQueryConfig

    :param query_filter: query_filter
    :type query_filter: IntegrationPackEnvironmentAttachmentQueryConfigQueryFilter
    """

    def __init__(
        self,
        query_filter: IntegrationPackEnvironmentAttachmentQueryConfigQueryFilter,
        **kwargs,
    ):
        """IntegrationPackEnvironmentAttachmentQueryConfig

        :param query_filter: query_filter
        :type query_filter: IntegrationPackEnvironmentAttachmentQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, IntegrationPackEnvironmentAttachmentQueryConfigQueryFilter
        )
        self._kwargs = kwargs
