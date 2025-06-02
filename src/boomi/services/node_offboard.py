
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import NodeOffboard


class NodeOffboardService(BaseService):

    @cast_models
    def create_node_offboard(
        self, request_body: NodeOffboard = None
    ) -> Union[NodeOffboard, str]:
        """Employs a POST method to delete a node. After you successfully perform the POST operation, the nodes status immediately changes to `Deleting` on the Cluster Status panel of the interface.

        :param request_body: The request body., defaults to None
        :type request_body: NodeOffboard, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[NodeOffboard, str]
        """

        Validator(NodeOffboard).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/NodeOffboard",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return NodeOffboard._unmap(response)
        if content == "application/xml":
            return NodeOffboard._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)
