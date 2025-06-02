
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models


class ExecuteProcessService(BaseService):

    @cast_models
    def create_execute_process(self) -> None:
        """This API is documented externally. Please visit the following link for full details:

        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ExecuteProcess",
                [self.get_access_token()],
            )
            .serialize()
            .set_method("POST")
        )

        self.send_request(serialized_request)
