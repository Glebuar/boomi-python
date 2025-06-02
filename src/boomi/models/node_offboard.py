
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({"atom_id": "atomId", "node_id": "nodeId"})
class NodeOffboard(BaseModel):
    """NodeOffboard

    :param atom_id: A unique, -generated identifier assigned to the Runtime cluster or Runtime cloud. In the  user interface, this ID appears on the **Runtime Information** panel of Runtime Management., defaults to None
    :type atom_id: str, optional
    :param node_id: The ID of the Runtime cluster or Cloud node that is intended for deletion. In the  user interface, this ID appears on the **Cluster Status** panel of Runtime Management., defaults to None
    :type node_id: List[str], optional
    """

    def __init__(
        self, atom_id: str = SENTINEL, node_id: List[str] = SENTINEL, **kwargs
    ):
        """NodeOffboard

        :param atom_id: A unique, -generated identifier assigned to the Runtime cluster or Runtime cloud. In the  user interface, this ID appears on the **Runtime Information** panel of Runtime Management., defaults to None
        :type atom_id: str, optional
        :param node_id: The ID of the Runtime cluster or Cloud node that is intended for deletion. In the  user interface, this ID appears on the **Cluster Status** panel of Runtime Management., defaults to None
        :type node_id: List[str], optional
        """
        if atom_id is not SENTINEL:
            self.atom_id = atom_id
        if node_id is not SENTINEL:
            self.node_id = node_id
        self._kwargs = kwargs
