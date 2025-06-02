
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..net.transport.utils import parse_xml_to_dict
from ..models import (
    DeployedExpiredCertificateQueryConfig,
    DeployedExpiredCertificateQueryResponse,
)


class DeployedExpiredCertificateService(BaseService):

    @cast_models
    def query_deployed_expired_certificate(
        self, request_body: DeployedExpiredCertificateQueryConfig = None
    ) -> Union[DeployedExpiredCertificateQueryResponse, str]:
        """If a QUERY omits an explicit timespan filter — that is, the query does not use `expirationBoundary` in an expression — it applies a default timespan filter using the value of 30 and the LESS_THAN operator. This filter specifies expired certificates and certificates expiring within 30 days.

         For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body., defaults to None
        :type request_body: DeployedExpiredCertificateQueryConfig, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[DeployedExpiredCertificateQueryResponse, str]
        """

        Validator(DeployedExpiredCertificateQueryConfig).is_optional().validate(
            request_body
        )

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/DeployedExpiredCertificate/query",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return DeployedExpiredCertificateQueryResponse._unmap(response)
        if content == "application/xml":
            return DeployedExpiredCertificateQueryResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_more_deployed_expired_certificate(
        self, request_body: str
    ) -> Union[DeployedExpiredCertificateQueryResponse, str]:
        """To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body.
        :type request_body: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[DeployedExpiredCertificateQueryResponse, str]
        """

        Validator(str).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/DeployedExpiredCertificate/queryMore",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body, "text/plain")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return DeployedExpiredCertificateQueryResponse._unmap(response)
        if content == "application/xml":
            return DeployedExpiredCertificateQueryResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)
