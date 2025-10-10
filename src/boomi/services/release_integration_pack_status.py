
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import (
    ReleaseIntegrationPackStatus,
    ReleaseIntegrationPackStatusBulkRequest,
    ReleaseIntegrationPackStatusBulkResponse,
)


class ReleaseIntegrationPackStatusService(BaseService):

    @cast_models
    def get_release_integration_pack_status(
        self, id_: str
    ) -> Union[ReleaseIntegrationPackStatus, str]:
        """To retrieve the release status of the publisher integration pack, follow these steps:

        1. Send a POST request to the ReleaseIntegrationPackStatus object. The response will return a requestId.
        2. Use the requestId returned in Step 1 to make a subsequent call to the ReleaseIntegrationPackStatus object to retrieve detailed information about the released integration pack.
        3. Repeatedly poll the ReleaseIntegrationPackStatus object using the requestId until the details of the released integration pack are available. If the request is still in progress or scheduled, it returns an HTTP 202 status code. When the integration pack is released successfully, the ReleaseIntegrationPackStatus object returns the released details.

        :param id_: A unique ID assigned by the system to the integration pack.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[ReleaseIntegrationPackStatus, str]
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ReleaseIntegrationPackStatus/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return ReleaseIntegrationPackStatus._unmap(response)
        if content == "application/xml":
            return ReleaseIntegrationPackStatus._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def bulk_release_integration_pack_status(
        self, request_body: ReleaseIntegrationPackStatusBulkRequest = None
    ) -> Union[str, ReleaseIntegrationPackStatusBulkResponse]:
        """The bulk GET operation returns multiple objects based on the supplied account IDs, to a maximum of 100. To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

        :param request_body: The request body., defaults to None
        :type request_body: ReleaseIntegrationPackStatusBulkRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[str, ReleaseIntegrationPackStatusBulkResponse]
        """

        Validator(ReleaseIntegrationPackStatusBulkRequest).is_optional().validate(
            request_body
        )

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ReleaseIntegrationPackStatus/bulk",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/xml":
            return ReleaseIntegrationPackStatusBulkResponse._unmap(response)
        if content == "application/json":
            return ReleaseIntegrationPackStatusBulkResponse._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)
