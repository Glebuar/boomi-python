
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import ProcessEnvironmentAttachment


class ProcessEnvironmentAttachmentService(BaseService):

    @cast_models
    def create_process_environment_attachment(
        self, request_body: ProcessEnvironmentAttachment = None
    ) -> Union[ProcessEnvironmentAttachment, str]:
        """Attaches a process having the specified ID to the environment having the specified ID.

        :param request_body: The request body., defaults to None
        :type request_body: ProcessEnvironmentAttachment, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[ProcessEnvironmentAttachment, str]
        """

        Validator(ProcessEnvironmentAttachment).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ProcessEnvironmentAttachment",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return ProcessEnvironmentAttachment._unmap(response)
        if content == "application/xml":
            return ProcessEnvironmentAttachment._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)
