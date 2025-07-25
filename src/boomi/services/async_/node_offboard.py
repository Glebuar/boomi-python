
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..node_offboard import NodeOffboardService
from ...models import NodeOffboard


class NodeOffboardServiceAsync(NodeOffboardService):
    """
    Async Wrapper for NodeOffboardServiceAsync
    """

    def create_node_offboard(
        self, request_body: NodeOffboard = None
    ) -> Awaitable[Union[NodeOffboard, str]]:
        return to_async(super().create_node_offboard)(request_body)
