
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .deployment_simple_expression import DeploymentSimpleExpression
from .deployment_grouping_expression import DeploymentGroupingExpression


class DeploymentExpressionGuard(OneOfBaseModel):
    class_list = {
        "DeploymentSimpleExpression": DeploymentSimpleExpression,
        "DeploymentGroupingExpression": DeploymentGroupingExpression,
    }


DeploymentExpression = Union[DeploymentSimpleExpression, DeploymentGroupingExpression]
