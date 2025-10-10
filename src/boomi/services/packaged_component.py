
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..net.transport.utils import parse_xml_to_dict
from ..models import (
    PackagedComponent,
    PackagedComponentBulkRequest,
    PackagedComponentBulkResponse,
    PackagedComponentQueryConfig,
    PackagedComponentQueryResponse,
)


class PackagedComponentService(BaseService):

    @cast_models
    def create_packaged_component(
        self, request_body: PackagedComponent = None
    ) -> Union[PackagedComponent, str]:
        """- You can use the CREATE operation to perform two different actions. For example, you can create a new packaged component from a specific component ID, or you can restore a deleted packaged component. Both actions use the same object endpoint. However, the information required in the request body differs.
          -  **To create a new packaged component**, you must include a component ID in the request body. You create a packaged component for the specified componentId. Optionally, you can specify a packageVersion value and notes about the package version.
             >**Note:** You cannot add package versions and notes after creating the packaged component. However, if not specified, automatically assigns a numerical version number to your new packaged component.
          -  **To restore or recover a deleted packaged component**, you must specify the packageId, componentId, and packageVersion. You can query the Packaged Component object for a list of deleted packaged components.
         - Specify a `branchName` to create a packaged component on a particular branch. If `branchName` is not provided, the default working branch is used.

        :param request_body: The request body., defaults to None
        :type request_body: PackagedComponent, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[PackagedComponent, str]
        """

        Validator(PackagedComponent).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/PackagedComponent",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return PackagedComponent._unmap(response)
        if content == "application/xml":
            return PackagedComponent._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def get_packaged_component(self, id_: str) -> Union[PackagedComponent, str]:
        """Retrieves the packaged component with the specified ID.

        :param id_: id_
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[PackagedComponent, str]
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/PackagedComponent/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return PackagedComponent._unmap(response)
        if content == "application/xml":
            return PackagedComponent._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def delete_packaged_component(self, id_: str) -> None:
        """- The DELETE operation deletes a specific packaged component version. The id that you provide in the endpoint represents a Packaged Component ID. You can retrieve the Packaged Component ID (packageId) using the GET and QUERY operations, or by viewing the **Packaged Component History** dialog for a specific version in the Integration user interface.
          >**Note:** You can restore deleted packaged components using the CREATE operation. See the section **Using the CREATE operation** for more details.

        - You cannot delete a packaged component if it is already in use. If currently deployed, a packaged component is considered in use if it is used in the **Process Library** or as part of an integration pack.

        :param id_: id_
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/PackagedComponent/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("DELETE")
        )

        response, status, _ = self.send_request(serialized_request)

    @cast_models
    def bulk_packaged_component(
        self, request_body: PackagedComponentBulkRequest = None
    ) -> Union[PackagedComponentBulkResponse, str]:
        """To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

        :param request_body: The request body., defaults to None
        :type request_body: PackagedComponentBulkRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[PackagedComponentBulkResponse, str]
        """

        Validator(PackagedComponentBulkRequest).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/PackagedComponent/bulk",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return PackagedComponentBulkResponse._unmap(response)
        if content == "application/xml":
            return PackagedComponentBulkResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_packaged_component(
        self, request_body: PackagedComponentQueryConfig = None
    ) -> Union[PackagedComponentQueryResponse, str]:
        """For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body., defaults to None
        :type request_body: PackagedComponentQueryConfig, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[PackagedComponentQueryResponse, str]
        """

        Validator(PackagedComponentQueryConfig).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/PackagedComponent/query",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return PackagedComponentQueryResponse._unmap(response)
        if content == "application/xml":
            return PackagedComponentQueryResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_more_packaged_component(
        self, request_body: str
    ) -> Union[PackagedComponentQueryResponse, str]:
        """To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body.
        :type request_body: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[PackagedComponentQueryResponse, str]
        """

        Validator(str).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/PackagedComponent/queryMore",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body, "text/plain")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return PackagedComponentQueryResponse._unmap(response)
        if content == "application/xml":
            return PackagedComponentQueryResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)
