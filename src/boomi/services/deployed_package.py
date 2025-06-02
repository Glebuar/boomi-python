
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..net.transport.utils import parse_xml_to_dict
from ..models import (
    DeployedPackage,
    DeployedPackageBulkRequest,
    DeployedPackageBulkResponse,
    DeployedPackageQueryConfig,
    DeployedPackageQueryResponse,
)


class DeployedPackageService(BaseService):

    @cast_models
    def create_deployed_package(
        self, request_body: DeployedPackage = None
    ) -> Union[DeployedPackage, str]:
        """You can use the CREATE operation in two ways:
         - With `environmentId` and `packageId`, CREATE deploys the specified packaged component to the identified environment.
         - With `environmentId` and `componentId`, CREATE packages with the specified component and deploys the package to the specified environment.
         >**Note:** By default, deployment of listener processes are in a running state. To deploy a packaged listener process in a paused state, include the `listenerStatus` field with a value of `PAUSED`.

        :param request_body: The request body., defaults to None
        :type request_body: DeployedPackage, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[DeployedPackage, str]
        """

        Validator(DeployedPackage).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/DeployedPackage",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return DeployedPackage._unmap(response)
        if content == "application/xml":
            return DeployedPackage._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def get_deployed_package(self, id_: str) -> Union[DeployedPackage, str]:
        """Returns a single Deployed Package object based on the deployment ID.

        :param id_: The Deployed Package object you are attempting to DELETE.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[DeployedPackage, str]
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/DeployedPackage/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return DeployedPackage._unmap(response)
        if content == "application/xml":
            return DeployedPackage._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def delete_deployed_package(self, id_: str) -> None:
        """Removes the packaged component from the environment each with a specific IDs.

        :param id_: id_
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/DeployedPackage/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("DELETE")
        )

        response, status, _ = self.send_request(serialized_request)

    @cast_models
    def bulk_deployed_package(
        self, request_body: DeployedPackageBulkRequest = None
    ) -> Union[DeployedPackageBulkResponse, str]:
        """To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

        :param request_body: The request body., defaults to None
        :type request_body: DeployedPackageBulkRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[DeployedPackageBulkResponse, str]
        """

        Validator(DeployedPackageBulkRequest).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/DeployedPackage/bulk",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return DeployedPackageBulkResponse._unmap(response)
        if content == "application/xml":
            return DeployedPackageBulkResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_deployed_package(
        self, request_body: DeployedPackageQueryConfig = None
    ) -> Union[DeployedPackageQueryResponse, str]:
        """For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body., defaults to None
        :type request_body: DeployedPackageQueryConfig, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[DeployedPackageQueryResponse, str]
        """

        Validator(DeployedPackageQueryConfig).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/DeployedPackage/query",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return DeployedPackageQueryResponse._unmap(response)
        if content == "application/xml":
            return DeployedPackageQueryResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_more_deployed_package(
        self, request_body: str
    ) -> Union[DeployedPackageQueryResponse, str]:
        """To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body.
        :type request_body: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[DeployedPackageQueryResponse, str]
        """

        Validator(str).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/DeployedPackage/queryMore",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body, "text/plain")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return DeployedPackageQueryResponse._unmap(response)
        if content == "application/xml":
            return DeployedPackageQueryResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)
