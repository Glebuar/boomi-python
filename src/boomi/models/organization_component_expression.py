
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .organization_component_simple_expression import (
    OrganizationComponentSimpleExpression,
)
from .organization_component_grouping_expression import (
    OrganizationComponentGroupingExpression,
)


class OrganizationComponentExpressionGuard(OneOfBaseModel):
    class_list = {
        "OrganizationComponentSimpleExpression": OrganizationComponentSimpleExpression,
        "OrganizationComponentGroupingExpression": OrganizationComponentGroupingExpression,
    }


OrganizationComponentExpression = Union[
    OrganizationComponentSimpleExpression, OrganizationComponentGroupingExpression
]
