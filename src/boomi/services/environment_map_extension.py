
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import (
    EnvironmentMapExtension,
    EnvironmentMapExtensionBulkRequest,
    EnvironmentMapExtensionBulkResponse,
)


class EnvironmentMapExtensionService(BaseService):

    @cast_models
    def get_environment_map_extension(
        self, id_: str
    ) -> Union[EnvironmentMapExtension, str]:
        """Retrieves an extensible map by its Environment Map Extension object ID.

         >**Note:** Extending a source or destination profile by means of browsing an external account may require including credentials in the request. The GET operation uses the credentials from the original process for the browse connection. However, because credential reuse can be problematic when sharing processes in Integration Packs, use the EXECUTE operation instead.

        :param id_: id_
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[EnvironmentMapExtension, str]
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/EnvironmentMapExtension/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return EnvironmentMapExtension._unmap(response)
        if content == "application/xml":
            return EnvironmentMapExtension._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def bulk_environment_map_extension(
        self, request_body: EnvironmentMapExtensionBulkRequest = None
    ) -> Union[EnvironmentMapExtensionBulkResponse, str]:
        """To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

        :param request_body: The request body., defaults to None
        :type request_body: EnvironmentMapExtensionBulkRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[EnvironmentMapExtensionBulkResponse, str]
        """

        Validator(EnvironmentMapExtensionBulkRequest).is_optional().validate(
            request_body
        )

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/EnvironmentMapExtension/bulk",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return EnvironmentMapExtensionBulkResponse._unmap(response)
        if content == "application/xml":
            return EnvironmentMapExtensionBulkResponse._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def execute_environment_map_extension(
        self, id_: str, request_body: EnvironmentMapExtension = None
    ) -> Union[EnvironmentMapExtension, str]:
        """Use the EXECUTE operation when you want to customize XML profiles by reimporting them from endpoint applications. The EXECUTE operation returns the current Environment Map Extension configuration similar to the GET operation.

         It also accepts connection credentials and automatically connects to the external application to retrieve additional custom fields for that profile. You must have the Runtime Management privilege to perform the EXECUTE operation. If you have the Runtime Management Read Access privilege, you cannot post connection credentials.

         For information about using these operations to retrieve or update map functions, refer to [Environment Map Extension functions](/docs/APIs/PlatformAPI/Environment_Map_Extension_functions).

         Include the `SourceBrowse` and `DestinationBrowse` sections as appropriate to browse the respective profile and include the required BrowseFields for the given connector. If you need to call the EXECUTE action repeatedly for the same map, you can alternatively use the `sessionId` to avoid having to supply the connector fields in subsequent calls. Session caching lasts about 30 minutes.

        :param request_body: The request body., defaults to None
        :type request_body: EnvironmentMapExtension, optional
        :param id_: id_
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[EnvironmentMapExtension, str]
        """

        Validator(EnvironmentMapExtension).is_optional().validate(request_body)
        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/EnvironmentMapExtension/execute/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return EnvironmentMapExtension._unmap(response)
        if content == "application/xml":
            return EnvironmentMapExtension._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)
