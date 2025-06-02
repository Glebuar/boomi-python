
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .deployed_expired_certificate_expression import (
    DeployedExpiredCertificateExpression,
    DeployedExpiredCertificateExpressionGuard,
)
from .deployed_expired_certificate_simple_expression import (
    DeployedExpiredCertificateSimpleExpression,
)
from .deployed_expired_certificate_grouping_expression import (
    DeployedExpiredCertificateGroupingExpression,
)


@JsonMap({})
class DeployedExpiredCertificateQueryConfigQueryFilter(BaseModel):
    """DeployedExpiredCertificateQueryConfigQueryFilter

    :param expression: expression
    :type expression: DeployedExpiredCertificateExpression
    """

    def __init__(self, expression: DeployedExpiredCertificateExpression, **kwargs):
        """DeployedExpiredCertificateQueryConfigQueryFilter

        :param expression: expression
        :type expression: DeployedExpiredCertificateExpression
        """
        self.expression = DeployedExpiredCertificateExpressionGuard.return_one_of(
            expression
        )
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class DeployedExpiredCertificateQueryConfig(BaseModel):
    """DeployedExpiredCertificateQueryConfig

    :param query_filter: query_filter
    :type query_filter: DeployedExpiredCertificateQueryConfigQueryFilter
    """

    def __init__(
        self, query_filter: DeployedExpiredCertificateQueryConfigQueryFilter, **kwargs
    ):
        """DeployedExpiredCertificateQueryConfig

        :param query_filter: query_filter
        :type query_filter: DeployedExpiredCertificateQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, DeployedExpiredCertificateQueryConfigQueryFilter
        )
        self._kwargs = kwargs
