
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .folder_simple_expression import FolderSimpleExpression
from .folder_grouping_expression import FolderGroupingExpression


class FolderExpressionGuard(OneOfBaseModel):
    class_list = {
        "FolderSimpleExpression": FolderSimpleExpression,
        "FolderGroupingExpression": FolderGroupingExpression,
    }


FolderExpression = Union[FolderSimpleExpression, FolderGroupingExpression]
