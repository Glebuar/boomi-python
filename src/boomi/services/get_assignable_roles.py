
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import Roles


class GetAssignableRolesService(BaseService):

    @cast_models
    def get_get_assignable_roles(self) -> Union[Roles, str]:
        """You can use the Get Assignable Roles operation to retrieve a list of roles that are assignable under a account.

        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[Roles, str]
        """

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/GetAssignableRoles",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return Roles._unmap(response)
        if content == "application/xml":
            return Roles._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)
