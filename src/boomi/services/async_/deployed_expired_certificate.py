
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..deployed_expired_certificate import DeployedExpiredCertificateService
from ...models import (
    DeployedExpiredCertificateQueryResponse,
    DeployedExpiredCertificateQueryConfig,
)


class DeployedExpiredCertificateServiceAsync(DeployedExpiredCertificateService):
    """
    Async Wrapper for DeployedExpiredCertificateServiceAsync
    """

    def query_deployed_expired_certificate(
        self, request_body: DeployedExpiredCertificateQueryConfig = None
    ) -> Awaitable[Union[DeployedExpiredCertificateQueryResponse, str]]:
        return to_async(super().query_deployed_expired_certificate)(request_body)

    def query_more_deployed_expired_certificate(
        self, request_body: str
    ) -> Awaitable[Union[DeployedExpiredCertificateQueryResponse, str]]:
        return to_async(super().query_more_deployed_expired_certificate)(request_body)
