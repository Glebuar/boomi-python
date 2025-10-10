
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..net.transport.utils import parse_xml_to_dict
from ..models import AtomPurge


class AtomPurgeService(BaseService):

    @cast_models
    def update_atom_purge(
        self, id_: str, request_body: AtomPurge = None
    ) -> Union[AtomPurge, str]:
        """You can use the Purge Runtime cloud attachment operation to programmatically start the purge process for test and browse components, logs, processed documents, and temporary data for a Runtime Cloud attachment.

        :param request_body: The request body., defaults to None
        :type request_body: AtomPurge, optional
        :param id_: The unique ID assigned by the system to the Runtime cloud attachment. The Runtime ID is found in the user interface by navigating to **Manage > Runtime Management** and viewing the Runtime Information panel for a selected Runtime.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[AtomPurge, str]
        """

        Validator(AtomPurge).is_optional().validate(request_body)
        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/AtomPurge/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return AtomPurge._unmap(response)
        if content == "application/xml":
            return AtomPurge._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)
