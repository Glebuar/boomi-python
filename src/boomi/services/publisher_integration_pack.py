
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import (
    PublisherIntegrationPack,
    PublisherIntegrationPackBulkRequest,
    PublisherIntegrationPackBulkResponse,
    PublisherIntegrationPackQueryConfig,
    PublisherIntegrationPackQueryResponse,
)


class PublisherIntegrationPackService(BaseService):

    @cast_models
    def create_publisher_integration_pack(
        self, request_body: PublisherIntegrationPack = None
    ) -> Union[PublisherIntegrationPack, str]:
        """Creates a single attachment or multiple attachment integration pack.

        :param request_body: The request body., defaults to None
        :type request_body: PublisherIntegrationPack, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[PublisherIntegrationPack, str]
        """

        Validator(PublisherIntegrationPack).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/PublisherIntegrationPack",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return PublisherIntegrationPack._unmap(response)
        if content == "application/xml":
            return PublisherIntegrationPack._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def get_publisher_integration_pack(
        self, id_: str
    ) -> Union[PublisherIntegrationPack, str]:
        """Retrieves the details of the integration pack and packaged components.
        The standard GET operation retrieves the properties of the integration pack with a specified ID.
        The bulk GET operation retrieves the properties of the integration packs with the specified IDs to a maximum of 100.

        :param id_: A unique ID assigned by the system to the integration pack.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[PublisherIntegrationPack, str]
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/PublisherIntegrationPack/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return PublisherIntegrationPack._unmap(response)
        if content == "application/xml":
            return PublisherIntegrationPack._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def update_publisher_integration_pack(
        self, id_: str, request_body: PublisherIntegrationPack = None
    ) -> Union[PublisherIntegrationPack, str]:
        """The Update operation adds or removes the packaged components from the publisher integration pack.
         It also updates the description field of single and multiple attachment integration packs and the name field only for a single attachment integration pack.

         >**Note:** When updating an integration pack, you must include all the packaged components associated with it in the request body.
         If a packaged component is not included, it will be deleted upon updating an integration pack.
         For example, include all packaged components while updating the integration pack name.

        :param request_body: The request body., defaults to None
        :type request_body: PublisherIntegrationPack, optional
        :param id_: id_
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[PublisherIntegrationPack, str]
        """

        Validator(PublisherIntegrationPack).is_optional().validate(request_body)
        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/PublisherIntegrationPack/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return PublisherIntegrationPack._unmap(response)
        if content == "application/xml":
            return PublisherIntegrationPack._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def delete_publisher_integration_pack(self, id_: str) -> None:
        """Deletes the publisher integration pack having a specified ID from the requesting account.
        The deleted integration pack is automatically uninstalled from all accounts where it was installed.
        Any Runtimes or environments attached to the integration pack are also detached.

        :param id_: A unique ID assigned by the system to the integration pack.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/PublisherIntegrationPack/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("DELETE")
        )

        response, status, _ = self.send_request(serialized_request)

    @cast_models
    def bulk_publisher_integration_pack(
        self, request_body: PublisherIntegrationPackBulkRequest = None
    ) -> Union[PublisherIntegrationPackBulkResponse, str, any]:
        """The bulk GET operation returns multiple objects based on the supplied account IDs, to a maximum of 100. To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

        :param request_body: The request body., defaults to None
        :type request_body: PublisherIntegrationPackBulkRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[PublisherIntegrationPackBulkResponse, str, any]
        """

        Validator(PublisherIntegrationPackBulkRequest).is_optional().validate(
            request_body
        )

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/PublisherIntegrationPack/bulk",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return PublisherIntegrationPackBulkResponse._unmap(response)
        if content == "application/xml":
            return PublisherIntegrationPackBulkResponse._unmap(response)
        if content == "example":
            return response
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_publisher_integration_pack(
        self, request_body: PublisherIntegrationPackQueryConfig = None
    ) -> Union[PublisherIntegrationPackQueryResponse, str]:
        """For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body., defaults to None
        :type request_body: PublisherIntegrationPackQueryConfig, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[PublisherIntegrationPackQueryResponse, str]
        """

        Validator(PublisherIntegrationPackQueryConfig).is_optional().validate(
            request_body
        )

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/PublisherIntegrationPack/query",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return PublisherIntegrationPackQueryResponse._unmap(response)
        if content == "application/xml":
            return PublisherIntegrationPackQueryResponse._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_more_publisher_integration_pack(
        self, request_body: str
    ) -> Union[PublisherIntegrationPackQueryResponse, str]:
        """To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body.
        :type request_body: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[PublisherIntegrationPackQueryResponse, str]
        """

        Validator(str).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/PublisherIntegrationPack/queryMore",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body, "text/plain")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return PublisherIntegrationPackQueryResponse._unmap(response)
        if content == "application/xml":
            return PublisherIntegrationPackQueryResponse._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)
