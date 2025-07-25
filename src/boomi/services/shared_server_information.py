
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import (
    SharedServerInformation,
    SharedServerInformationBulkRequest,
    SharedServerInformationBulkResponse,
)


class SharedServerInformationService(BaseService):

    @cast_models
    def get_shared_server_information(
        self, id_: str
    ) -> Union[SharedServerInformation, str]:
        """Retrieve Shared Server Information records for a specific single Runtime ID.

         You can retrieve Shared Server Information records only by an ordinary GET operation specifying a single Runtime ID or a bulk GET operation with a maximum of 100 Runtime IDs. This option is because the object ID for the Shared Server Information is not available currently (except by requesting the information from services). Therefore, this operation does not return the Shared Server Information object auth field.

        :param id_: The ID of the Runtime that is hosting the shared web server.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[SharedServerInformation, str]
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/SharedServerInformation/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return SharedServerInformation._unmap(response)
        if content == "application/xml":
            return SharedServerInformation._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def update_shared_server_information(
        self, id_: str, request_body: SharedServerInformation = None
    ) -> Union[SharedServerInformation, str]:
        """Updates a Shared Server Information object based on the supplied Runtime ID.

         - The UPDATE operation updates a Shared Server Information object based on the supplied Runtime ID. To clear a field, set the attribute corresponding to that field to an empty string.

         You must have the Runtime Management privilege to perform the UPDATE operation. If you have the Runtime Management Read Access privilege, you cannot update shared server information.

         It is not possible to set authToken through this operation. This operation generates a token if it requires authentication, but a token does not currently exist. The new authToken appears in the response.
         - If you specify sslCertificateId, the certificate must be accessible by the account making the request.
         -If you do not configure the Authentication Type and Ports, using the Shared Server Information object to update only the API Type of a Runtime fails. If you are the owner of a Runtime, Runtime cluster, or Runtime cloud, you must update the API Type, Authentication Type, and HTTP Port or HTTPS Port through the Shared Server Information object for the API to succeed. Runtime cloud attachments cannot update the HTTP Port or HTTPS Port.
         - If you configure the Authentication Type and Ports, you can use the Shared Server Information object to update only the API Type of a Runtime.
         - This API does not support the configuration of multiple authentication types on a Runtime.

        :param request_body: The request body., defaults to None
        :type request_body: SharedServerInformation, optional
        :param id_: The ID of the Runtime that is hosting the shared web server.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[SharedServerInformation, str]
        """

        Validator(SharedServerInformation).is_optional().validate(request_body)
        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/SharedServerInformation/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return SharedServerInformation._unmap(response)
        if content == "application/xml":
            return SharedServerInformation._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def bulk_shared_server_information(
        self, request_body: SharedServerInformationBulkRequest = None
    ) -> Union[SharedServerInformationBulkResponse, str]:
        """To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

        :param request_body: The request body., defaults to None
        :type request_body: SharedServerInformationBulkRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[SharedServerInformationBulkResponse, str]
        """

        Validator(SharedServerInformationBulkRequest).is_optional().validate(
            request_body
        )

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/SharedServerInformation/bulk",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return SharedServerInformationBulkResponse._unmap(response)
        if content == "application/xml":
            return SharedServerInformationBulkResponse._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)
