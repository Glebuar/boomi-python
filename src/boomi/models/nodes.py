
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .node_details import NodeDetails


@JsonMap({})
class Nodes(BaseModel):
    """Nodes

    :param node: node, defaults to None
    :type node: List[NodeDetails], optional
    """

    def __init__(self, node: List[NodeDetails] = SENTINEL, **kwargs):
        """Nodes

        :param node: node, defaults to None
        :type node: List[NodeDetails], optional
        """
        if node is not SENTINEL:
            self.node = self._define_list(node, NodeDetails)
        self._kwargs = kwargs
