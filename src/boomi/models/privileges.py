
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .privilege import Privilege


@JsonMap({"privilege": "Privilege"})
class Privileges(BaseModel):
    """One or more privileges assigned to the role.

    :param privilege: privilege, defaults to None
    :type privilege: List[Privilege], optional
    """

    def __init__(self, privilege: List[Privilege] = SENTINEL, **kwargs):
        """One or more privileges assigned to the role.

        :param privilege: privilege, defaults to None
        :type privilege: List[Privilege], optional
        """
        if privilege is not SENTINEL:
            self.privilege = self._define_list(privilege, Privilege)
        self._kwargs = kwargs
