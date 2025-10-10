
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..net.transport.utils import parse_xml_to_dict
from ..models import (
    AtomStartupProperties,
    AtomStartupPropertiesBulkRequest,
    AtomStartupPropertiesBulkResponse,
)


class AtomStartupPropertiesService(BaseService):

    @cast_models
    def get_atom_startup_properties(
        self, id_: str
    ) -> Union[AtomStartupProperties, str]:
        """Retrieves the startup properties for the Runtime, Runtime cluster, or Runtime cloud with the specified ID.

        :param id_: A unique ID for the Runtime, Runtime cluster, or Runtime cloud. (This API is not applicable for runtimes attached to clouds)
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[AtomStartupProperties, str]
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/AtomStartupProperties/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return AtomStartupProperties._unmap(response)
        if content == "application/xml":
            return AtomStartupProperties._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def bulk_atom_startup_properties(
        self, request_body: AtomStartupPropertiesBulkRequest = None
    ) -> Union[AtomStartupPropertiesBulkResponse, str]:
        """To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

        :param request_body: The request body., defaults to None
        :type request_body: AtomStartupPropertiesBulkRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[AtomStartupPropertiesBulkResponse, str]
        """

        Validator(AtomStartupPropertiesBulkRequest).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/AtomStartupProperties/bulk",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return AtomStartupPropertiesBulkResponse._unmap(response)
        if content == "application/xml":
            return AtomStartupPropertiesBulkResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)
