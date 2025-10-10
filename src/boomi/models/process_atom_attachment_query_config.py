
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .process_atom_attachment_expression import (
    ProcessAtomAttachmentExpression,
    ProcessAtomAttachmentExpressionGuard,
)
from .process_atom_attachment_simple_expression import (
    ProcessAtomAttachmentSimpleExpression,
)
from .process_atom_attachment_grouping_expression import (
    ProcessAtomAttachmentGroupingExpression,
)


@JsonMap({})
class ProcessAtomAttachmentQueryConfigQueryFilter(BaseModel):
    """ProcessAtomAttachmentQueryConfigQueryFilter

    :param expression: expression
    :type expression: ProcessAtomAttachmentExpression
    """

    def __init__(self, expression: ProcessAtomAttachmentExpression, **kwargs):
        """ProcessAtomAttachmentQueryConfigQueryFilter

        :param expression: expression
        :type expression: ProcessAtomAttachmentExpression
        """
        self.expression = ProcessAtomAttachmentExpressionGuard.return_one_of(expression)
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class ProcessAtomAttachmentQueryConfig(BaseModel):
    """ProcessAtomAttachmentQueryConfig

    :param query_filter: query_filter
    :type query_filter: ProcessAtomAttachmentQueryConfigQueryFilter
    """

    def __init__(
        self, query_filter: ProcessAtomAttachmentQueryConfigQueryFilter, **kwargs
    ):
        """ProcessAtomAttachmentQueryConfig

        :param query_filter: query_filter
        :type query_filter: ProcessAtomAttachmentQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, ProcessAtomAttachmentQueryConfigQueryFilter
        )
        self._kwargs = kwargs
