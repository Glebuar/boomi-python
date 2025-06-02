
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .environment_atom_attachment_expression import (
    EnvironmentAtomAttachmentExpression,
    EnvironmentAtomAttachmentExpressionGuard,
)
from .environment_atom_attachment_simple_expression import (
    EnvironmentAtomAttachmentSimpleExpression,
)
from .environment_atom_attachment_grouping_expression import (
    EnvironmentAtomAttachmentGroupingExpression,
)


@JsonMap({})
class EnvironmentAtomAttachmentQueryConfigQueryFilter(BaseModel):
    """EnvironmentAtomAttachmentQueryConfigQueryFilter

    :param expression: expression
    :type expression: EnvironmentAtomAttachmentExpression
    """

    def __init__(self, expression: EnvironmentAtomAttachmentExpression, **kwargs):
        """EnvironmentAtomAttachmentQueryConfigQueryFilter

        :param expression: expression
        :type expression: EnvironmentAtomAttachmentExpression
        """
        self.expression = EnvironmentAtomAttachmentExpressionGuard.return_one_of(
            expression
        )
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class EnvironmentAtomAttachmentQueryConfig(BaseModel):
    """EnvironmentAtomAttachmentQueryConfig

    :param query_filter: query_filter
    :type query_filter: EnvironmentAtomAttachmentQueryConfigQueryFilter
    """

    def __init__(
        self, query_filter: EnvironmentAtomAttachmentQueryConfigQueryFilter, **kwargs
    ):
        """EnvironmentAtomAttachmentQueryConfig

        :param query_filter: query_filter
        :type query_filter: EnvironmentAtomAttachmentQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, EnvironmentAtomAttachmentQueryConfigQueryFilter
        )
        self._kwargs = kwargs
