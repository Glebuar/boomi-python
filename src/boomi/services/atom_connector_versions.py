
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..net.transport.utils import parse_xml_to_dict
from ..models import (
    AtomConnectorVersions,
    AtomConnectorVersionsBulkRequest,
    AtomConnectorVersionsBulkResponse,
)


class AtomConnectorVersionsService(BaseService):

    @cast_models
    def get_atom_connector_versions(
        self, id_: str
    ) -> Union[AtomConnectorVersions, str]:
        """Retrieves the properties of connectors used by the Runtime, Runtime cluster, or Runtime cloud with specified ID.

        :param id_: The ID of the Runtime, Runtime cluster, or Runtime cloud.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[AtomConnectorVersions, str]
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/AtomConnectorVersions/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return AtomConnectorVersions._unmap(response)
        if content == "application/xml":
            return AtomConnectorVersions._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def bulk_atom_connector_versions(
        self, request_body: AtomConnectorVersionsBulkRequest = None
    ) -> Union[AtomConnectorVersionsBulkResponse, str]:
        """To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

        :param request_body: The request body., defaults to None
        :type request_body: AtomConnectorVersionsBulkRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[AtomConnectorVersionsBulkResponse, str]
        """

        Validator(AtomConnectorVersionsBulkRequest).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/AtomConnectorVersions/bulk",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return AtomConnectorVersionsBulkResponse._unmap(response)
        if content == "application/xml":
            return AtomConnectorVersionsBulkResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)
