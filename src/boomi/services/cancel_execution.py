
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models


class CancelExecutionService(BaseService):

    @cast_models
    def get_cancel_execution(self) -> None:
        """This API is supported by the Platform Partner APIs. Refer to the Partner API Reference.

        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/CancelExecution",
                [self.get_access_token()],
            )
            .serialize()
            .set_method("GET")
        )

        self.send_request(serialized_request)
