
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .deployed_package_simple_expression import DeployedPackageSimpleExpression
from .deployed_package_grouping_expression import DeployedPackageGroupingExpression


class DeployedPackageExpressionGuard(OneOfBaseModel):
    class_list = {
        "DeployedPackageSimpleExpression": DeployedPackageSimpleExpression,
        "DeployedPackageGroupingExpression": DeployedPackageGroupingExpression,
    }


DeployedPackageExpression = Union[
    DeployedPackageSimpleExpression, DeployedPackageGroupingExpression
]
