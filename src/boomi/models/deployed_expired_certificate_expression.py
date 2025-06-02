
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .deployed_expired_certificate_simple_expression import (
    DeployedExpiredCertificateSimpleExpression,
)
from .deployed_expired_certificate_grouping_expression import (
    DeployedExpiredCertificateGroupingExpression,
)


class DeployedExpiredCertificateExpressionGuard(OneOfBaseModel):
    class_list = {
        "DeployedExpiredCertificateSimpleExpression": DeployedExpiredCertificateSimpleExpression,
        "DeployedExpiredCertificateGroupingExpression": DeployedExpiredCertificateGroupingExpression,
    }


DeployedExpiredCertificateExpression = Union[
    DeployedExpiredCertificateSimpleExpression,
    DeployedExpiredCertificateGroupingExpression,
]
