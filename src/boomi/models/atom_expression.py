
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .atom_simple_expression import AtomSimpleExpression
from .atom_grouping_expression import AtomGroupingExpression


class AtomExpressionGuard(OneOfBaseModel):
    class_list = {
        "AtomSimpleExpression": AtomSimpleExpression,
        "AtomGroupingExpression": AtomGroupingExpression,
    }


AtomExpression = Union[AtomSimpleExpression, AtomGroupingExpression]
