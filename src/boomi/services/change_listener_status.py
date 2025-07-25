
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import ChangeListenerStatusRequest


class ChangeListenerStatusService(BaseService):

    @cast_models
    def create_change_listener_status(
        self, request_body: ChangeListenerStatusRequest = None
    ) -> None:
        """You can use the changeListenerStatus operation to pause, resume, or restart listeners. A successful changeListenerStatus call returns an empty changeListenerStatusResponse to indicate acceptance of the request.

        :param request_body: The request body., defaults to None
        :type request_body: ChangeListenerStatusRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(ChangeListenerStatusRequest).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ChangeListenerStatus",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
