
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .role_reference import RoleReference


@JsonMap({"role_reference": "RoleReference"})
class PermittedRoles(BaseModel):
    """Optional. The defined role assigned to the available folder object.

    :param role_reference: role_reference, defaults to None
    :type role_reference: List[RoleReference], optional
    """

    def __init__(self, role_reference: List[RoleReference] = SENTINEL, **kwargs):
        """Optional. The defined role assigned to the available folder object.

        :param role_reference: role_reference, defaults to None
        :type role_reference: List[RoleReference], optional
        """
        if role_reference is not SENTINEL:
            self.role_reference = self._define_list(role_reference, RoleReference)
        self._kwargs = kwargs
