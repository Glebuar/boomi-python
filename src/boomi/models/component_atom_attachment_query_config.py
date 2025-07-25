
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .component_atom_attachment_expression import (
    ComponentAtomAttachmentExpression,
    ComponentAtomAttachmentExpressionGuard,
)
from .component_atom_attachment_simple_expression import (
    ComponentAtomAttachmentSimpleExpression,
)
from .component_atom_attachment_grouping_expression import (
    ComponentAtomAttachmentGroupingExpression,
)


@JsonMap({})
class ComponentAtomAttachmentQueryConfigQueryFilter(BaseModel):
    """ComponentAtomAttachmentQueryConfigQueryFilter

    :param expression: expression
    :type expression: ComponentAtomAttachmentExpression
    """

    def __init__(self, expression: ComponentAtomAttachmentExpression, **kwargs):
        """ComponentAtomAttachmentQueryConfigQueryFilter

        :param expression: expression
        :type expression: ComponentAtomAttachmentExpression
        """
        self.expression = ComponentAtomAttachmentExpressionGuard.return_one_of(
            expression
        )
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class ComponentAtomAttachmentQueryConfig(BaseModel):
    """ComponentAtomAttachmentQueryConfig

    :param query_filter: query_filter
    :type query_filter: ComponentAtomAttachmentQueryConfigQueryFilter
    """

    def __init__(
        self, query_filter: ComponentAtomAttachmentQueryConfigQueryFilter, **kwargs
    ):
        """ComponentAtomAttachmentQueryConfig

        :param query_filter: query_filter
        :type query_filter: ComponentAtomAttachmentQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, ComponentAtomAttachmentQueryConfigQueryFilter
        )
        self._kwargs = kwargs
