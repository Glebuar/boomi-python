
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .map_extensions_node import MapExtensionsNode


@JsonMap({"node": "Node", "component_id": "componentId", "type_": "type"})
class MapExtensionsProfile(BaseModel):
    """Represents the fields in a source or destination profile of the given map, and specifies the section of the map in which to extend.

     >**Note:** You cannot add or create new fields in the object's request body. You must add new fields in the user interface of the underlying Map component or from a dynamic reimport. See the Customizing profiles section later in this topic.

    The following SourceProfile attributes define fields in the source profile:

    - componentId - represents the object definition extension ID. A GET request returns this value.
    - name - the user-defined field label(s) found in the source profile.
    - xpath - represents the field location in the source profile hierarchy.

    :param node: node, defaults to None
    :type node: List[MapExtensionsNode], optional
    :param component_id: component_id, defaults to None
    :type component_id: str, optional
    :param type_: type_, defaults to None
    :type type_: str, optional
    """

    def __init__(
        self,
        node: List[MapExtensionsNode] = SENTINEL,
        component_id: str = SENTINEL,
        type_: str = SENTINEL,
        **kwargs,
    ):
        """Represents the fields in a source or destination profile of the given map, and specifies the section of the map in which to extend.

         >**Note:** You cannot add or create new fields in the object's request body. You must add new fields in the user interface of the underlying Map component or from a dynamic reimport. See the Customizing profiles section later in this topic.

        The following SourceProfile attributes define fields in the source profile:

        - componentId - represents the object definition extension ID. A GET request returns this value.
        - name - the user-defined field label(s) found in the source profile.
        - xpath - represents the field location in the source profile hierarchy.

        :param node: node, defaults to None
        :type node: List[MapExtensionsNode], optional
        :param component_id: component_id, defaults to None
        :type component_id: str, optional
        :param type_: type_, defaults to None
        :type type_: str, optional
        """
        if node is not SENTINEL:
            self.node = self._define_list(node, MapExtensionsNode)
        if component_id is not SENTINEL:
            self.component_id = component_id
        if type_ is not SENTINEL:
            self.type_ = type_
        self._kwargs = kwargs
