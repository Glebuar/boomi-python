
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..net.transport.utils import parse_xml_to_dict
from ..models import AtomCounters


class AtomCountersService(BaseService):

    @cast_models
    def update_atom_counters(
        self, id_: str, request_body: AtomCounters = None
    ) -> Union[AtomCounters, str]:
        """The UPDATE operation updates Runtime Counter values for a specific Runtime. Using the UPDATE operation overrides all settings set on the current counter. However, calling the UPDATE operation does not delete any existing counters that are not included in the `AtomCounters` object.

        :param request_body: The request body., defaults to None
        :type request_body: AtomCounters, optional
        :param id_: A unique ID assigned by the system to the Runtime.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[AtomCounters, str]
        """

        Validator(AtomCounters).is_optional().validate(request_body)
        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/AtomCounters/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return AtomCounters._unmap(response)
        if content == "application/xml":
            return AtomCounters._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)
