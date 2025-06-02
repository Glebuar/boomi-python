
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..net.transport.utils import parse_xml_to_dict
from ..models import ClearQueueRequest


class ClearQueueService(BaseService):

    @cast_models
    def execute_clear_queue(
        self, id_: str, request_body: ClearQueueRequest = None
    ) -> Union[ClearQueueRequest, str]:
        """- When you run the Clear queue messages action, it deletes all messages in a queue name from the queue. Note that this clears all messages in the queue; you cannot select and remove individual messages using this action. In addition, the action overrides any purge settings you might configure in the user interface.
         - The immediate response indicates success in passing the request to the Runtime.
         - If the specified Runtime queue does not contain any messages to clear, the response only returns a success message stating that the message passed even though there is no action taken on the Runtime.
         - You can use the Get queue list API action to retrieve the number of messages in a queue, which works as an alternative way to check if the clear queue message action succeeded on the Runtime.

        :param request_body: The request body., defaults to None
        :type request_body: ClearQueueRequest, optional
        :param id_: The unique ID assigned by the system to the container. The Runtime ID for Runtimes, Runtime clusters, and Runtime clouds is found in the user interface by navigating to Manage > Runtime Management and viewing the Runtime Information panel for the selected container.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[ClearQueueRequest, str]
        """

        Validator(ClearQueueRequest).is_optional().validate(request_body)
        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ClearQueue/execute/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return ClearQueueRequest._unmap(response)
        if content == "application/xml":
            return ClearQueueRequest._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)
