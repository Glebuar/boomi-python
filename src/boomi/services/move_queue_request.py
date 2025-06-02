
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import MoveQueueRequest


class MoveQueueRequestService(BaseService):

    @cast_models
    def create_move_queue_request(
        self, request_body: MoveQueueRequest = None
    ) -> Union[MoveQueueRequest, str]:
        """Moves messages from one Runtime queue to another.

         - You must have the **Runtime Management** privilege to use the Move queue request operation.
        - You can only move messages between queues of the same type. For example, moving queue messages from a point-to-point queue to a *Publish/Subscribe* queue results in an error.
        - Any Runtime queues that you specify in the request must currently exist on the Runtime. For clarification, you cannot create a new endpoint using the CREATE operation.
        - You must supply the *AtomID*, *SourceQueue*, *QueueName*, *DLQ*, and *DestinationQueue* fields in the request.
        - If the operation returns an error, it logs a message in the Runtime, Runtime cluster, or Runtime cloud, but is not sent to the platform.
        - You cannot track move updates directly through this operation. Instead, to see if the action is in progress or complete, use the Queue Management API or the ListQueues API to observe the number of messages in the queue.

        :param request_body: The request body., defaults to None
        :type request_body: MoveQueueRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[MoveQueueRequest, str]
        """

        Validator(MoveQueueRequest).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/MoveQueueRequest",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return MoveQueueRequest._unmap(response)
        if content == "application/xml":
            return MoveQueueRequest._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)
