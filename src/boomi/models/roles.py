
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .role import Role


@JsonMap({"role": "Role"})
class Roles(BaseModel):
    """Roles

    :param role: role, defaults to None
    :type role: List[Role], optional
    """

    def __init__(self, role: List[Role] = SENTINEL, **kwargs):
        """Roles

        :param role: role, defaults to None
        :type role: List[Role], optional
        """
        if role is not SENTINEL:
            self.role = self._define_list(role, Role)
        self._kwargs = kwargs
