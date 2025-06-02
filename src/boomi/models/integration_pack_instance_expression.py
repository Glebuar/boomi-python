
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .integration_pack_instance_simple_expression import (
    IntegrationPackInstanceSimpleExpression,
)
from .integration_pack_instance_grouping_expression import (
    IntegrationPackInstanceGroupingExpression,
)


class IntegrationPackInstanceExpressionGuard(OneOfBaseModel):
    class_list = {
        "IntegrationPackInstanceSimpleExpression": IntegrationPackInstanceSimpleExpression,
        "IntegrationPackInstanceGroupingExpression": IntegrationPackInstanceGroupingExpression,
    }


IntegrationPackInstanceExpression = Union[
    IntegrationPackInstanceSimpleExpression, IntegrationPackInstanceGroupingExpression
]
