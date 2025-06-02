
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .component_info import ComponentInfo


@JsonMap({"component_info": "componentInfo", "package_id": "packageId"})
class PackagedComponentManifest(BaseModel):
    """PackagedComponentManifest

    :param component_info: component_info, defaults to None
    :type component_info: List[ComponentInfo], optional
    :param package_id: The ID of the packaged component.
    :type package_id: str
    """

    def __init__(
        self, package_id: str, component_info: List[ComponentInfo] = SENTINEL, **kwargs
    ):
        """PackagedComponentManifest

        :param component_info: component_info, defaults to None
        :type component_info: List[ComponentInfo], optional
        :param package_id: The ID of the packaged component.
        :type package_id: str
        """
        if component_info is not SENTINEL:
            self.component_info = self._define_list(component_info, ComponentInfo)
        self.package_id = package_id
        self._kwargs = kwargs
