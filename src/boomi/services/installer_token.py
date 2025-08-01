
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..net.transport.utils import parse_xml_to_dict
from ..models import InstallerToken


class InstallerTokenService(BaseService):

    @cast_models
    def create_installer_token(
        self, request_body: InstallerToken = None
    ) -> Union[InstallerToken, str]:
        """Creates an installer token of a specific type that is valid for a specific number of minutes.

        :param request_body: The request body., defaults to None
        :type request_body: InstallerToken, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[InstallerToken, str]
        """

        Validator(InstallerToken).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/InstallerToken",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return InstallerToken._unmap(response)
        if content == "application/xml":
            return InstallerToken._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)
