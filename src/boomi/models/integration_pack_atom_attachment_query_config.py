
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .integration_pack_atom_attachment_expression import (
    IntegrationPackAtomAttachmentExpression,
    IntegrationPackAtomAttachmentExpressionGuard,
)
from .integration_pack_atom_attachment_simple_expression import (
    IntegrationPackAtomAttachmentSimpleExpression,
)
from .integration_pack_atom_attachment_grouping_expression import (
    IntegrationPackAtomAttachmentGroupingExpression,
)


@JsonMap({})
class IntegrationPackAtomAttachmentQueryConfigQueryFilter(BaseModel):
    """IntegrationPackAtomAttachmentQueryConfigQueryFilter

    :param expression: expression
    :type expression: IntegrationPackAtomAttachmentExpression
    """

    def __init__(self, expression: IntegrationPackAtomAttachmentExpression, **kwargs):
        """IntegrationPackAtomAttachmentQueryConfigQueryFilter

        :param expression: expression
        :type expression: IntegrationPackAtomAttachmentExpression
        """
        self.expression = IntegrationPackAtomAttachmentExpressionGuard.return_one_of(
            expression
        )
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class IntegrationPackAtomAttachmentQueryConfig(BaseModel):
    """IntegrationPackAtomAttachmentQueryConfig

    :param query_filter: query_filter
    :type query_filter: IntegrationPackAtomAttachmentQueryConfigQueryFilter
    """

    def __init__(
        self,
        query_filter: IntegrationPackAtomAttachmentQueryConfigQueryFilter,
        **kwargs,
    ):
        """IntegrationPackAtomAttachmentQueryConfig

        :param query_filter: query_filter
        :type query_filter: IntegrationPackAtomAttachmentQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, IntegrationPackAtomAttachmentQueryConfigQueryFilter
        )
        self._kwargs = kwargs
