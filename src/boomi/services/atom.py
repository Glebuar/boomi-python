
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..net.transport.utils import parse_xml_to_dict
from ..models import (
    AsyncOperationTokenResult,
    Atom,
    AtomBulkRequest,
    AtomBulkResponse,
    AtomCountersAsyncResponse,
    AtomQueryConfig,
    AtomQueryResponse,
    PersistedProcessPropertiesAsyncResponse,
)


class AtomService(BaseService):

    @cast_models
    def create_atom(self, request_body: Atom = None) -> Union[Atom, str]:
        """Creates and attaches a Runtime with the specified name to a specified Runtime cloud owned by the requesting account. This operation cannot be used to create a local Runtime. You must have the Runtime Management privilege to perform the POST operation.

         >**Note:** The `createdBy` is a system-generated or read-only field. It cannot be passed in a CREATE request.

        :param request_body: The request body., defaults to None
        :type request_body: Atom, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[Atom, str]
        """

        Validator(Atom).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/Atom",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return Atom._unmap(response)
        if content == "application/xml":
            return Atom._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def get_atom(self, id_: str) -> Union[Atom, str]:
        """Retrieves the properties of the Runtime, Runtime cluster, or Runtime cloud having the specified ID.

         For Runtime clusters and Runtime clouds that are part of a multi-node runtime, the GET operation returns values for the following additional variables:

          - *nodeId*
          - *hostName*
          - *status*
          - *clusterProblem*

          For more information on these variables, see the topic [Cluster Status panel](https://help.boomi.com/docs/Atomsphere/Integration/Integration%20management/r-atm-Cluster_Status_panel_fbdb3645-00e2-4c3c-bba8-bf5fdb0f90f6).

        :param id_: A unique ID for the Runtime, Runtime cluster, or Runtime cloud.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[Atom, str]
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/Atom/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return Atom._unmap(response)
        if content == "application/xml":
            return Atom._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def update_atom(self, id_: str, request_body: Atom = None) -> Union[Atom, str]:
        """Updates the Runtime object having the specified ID. You can only update the name, purgeHistoryDays, purgeImmediate, forceRestartTime. You must have the Runtime Management privilege to perform the UPDATE operation. If you have the Runtime Management Read Access privilege, you cannot update an Runtime.

         >**Note:** There might be a delay before you see the changes in the Runtime Information panel.

        :param request_body: The request body., defaults to None
        :type request_body: Atom, optional
        :param id_: A unique ID for the Runtime, Runtime cluster, or Runtime cloud.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[Atom, str]
        """

        Validator(Atom).is_optional().validate(request_body)
        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/Atom/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return Atom._unmap(response)
        if content == "application/xml":
            return Atom._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def delete_atom(self, id_: str) -> None:
        """Deletes the Runtime object with the specified ID. You must have the Runtime Management privilege to perform the DELETE operation. If you have the Runtime Management Read Access privilege, you cannot delete a Runtime.

        :param id_: A unique ID for the Runtime, Runtime cluster, or Runtime cloud.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/Atom/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("DELETE")
        )

        response, status, _ = self.send_request(serialized_request)

    @cast_models
    def bulk_atom(
        self, request_body: AtomBulkRequest = None
    ) -> Union[AtomBulkResponse, str]:
        """To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

        :param request_body: The request body., defaults to None
        :type request_body: AtomBulkRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[AtomBulkResponse, str]
        """

        Validator(AtomBulkRequest).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/Atom/bulk",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return AtomBulkResponse._unmap(response)
        if content == "application/xml":
            return AtomBulkResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_atom(
        self, request_body: AtomQueryConfig = None
    ) -> Union[AtomQueryResponse, str]:
        """Use either `BROKER` or `GATEWAY` with either the CONTAINS or NOT_CONTAINS operator to filter by API Gateways and Authentication Brokers that you own.

         For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body., defaults to None
        :type request_body: AtomQueryConfig, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[AtomQueryResponse, str]
        """

        Validator(AtomQueryConfig).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/Atom/query",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return AtomQueryResponse._unmap(response)
        if content == "application/xml":
            return AtomQueryResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_more_atom(self, request_body: str) -> Union[AtomQueryResponse, str]:
        """To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body.
        :type request_body: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[AtomQueryResponse, str]
        """

        Validator(str).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/Atom/queryMore",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body, "text/plain")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return AtomQueryResponse._unmap(response)
        if content == "application/xml":
            return AtomQueryResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def async_token_atom_counters(
        self, token: str
    ) -> Union[AtomCountersAsyncResponse, str]:
        """For a response, use the token from the initial GET response in a new request.

        :param token: Takes in the token from a previous call to return a result.
        :type token: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[AtomCountersAsyncResponse, str]
        """

        Validator(str).validate(token)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/async/AtomCounters/response/{{token}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("token", token)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return AtomCountersAsyncResponse._unmap(response)
        if content == "application/xml":
            return AtomCountersAsyncResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def async_get_atom_counters(
        self, id_: str
    ) -> Union[AsyncOperationTokenResult, str]:
        """The GET operation returns the current state of the counter names and values for the specified Runtime. The initial GET operation returns a token for the specified Runtime.
         `accountId` is the Platform account that you are authenticating with and `id` is the Runtime ID for the counters you are attempting to GET.

        :param id_: id_
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[AsyncOperationTokenResult, str]
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/async/AtomCounters/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return AsyncOperationTokenResult._unmap(response)
        if content == "application/xml":
            return AsyncOperationTokenResult._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def async_token_persisted_process_properties(
        self, token: str
    ) -> Union[PersistedProcessPropertiesAsyncResponse, str]:
        """For a response, use the token from the response in a new request.

        :param token: Takes in the token from a previous call to return a result.
        :type token: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[PersistedProcessPropertiesAsyncResponse, str]
        """

        Validator(str).validate(token)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/async/PersistedProcessProperties/response/{{token}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("token", token)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return PersistedProcessPropertiesAsyncResponse._unmap(response)
        if content == "application/xml":
            return PersistedProcessPropertiesAsyncResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def async_get_persisted_process_properties(
        self, id_: str
    ) -> Union[AsyncOperationTokenResult, str]:
        """The GET operation returns the current state of the Persisted Process properties names and values for the specified Runtime.
         The initial GET operation returns a token for the specified Runtime.

        :param id_: id_
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[AsyncOperationTokenResult, str]
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/async/PersistedProcessProperties/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return AsyncOperationTokenResult._unmap(response)
        if content == "application/xml":
            return AsyncOperationTokenResult._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)
