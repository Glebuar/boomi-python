
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .cloud_atom import CloudAtom


@JsonMap({"atom": "Atom", "id_": "id"})
class Cloud(BaseModel):
    """Cloud

    :param atom: atom, defaults to None
    :type atom: List[CloudAtom], optional
    :param id_: A unique ID assigned by the system to the Runtime cloud., defaults to None
    :type id_: str, optional
    :param name: The name of the Runtime cloud., defaults to None
    :type name: str, optional
    """

    def __init__(
        self,
        atom: List[CloudAtom] = SENTINEL,
        id_: str = SENTINEL,
        name: str = SENTINEL,
        **kwargs,
    ):
        """Cloud

        :param atom: atom, defaults to None
        :type atom: List[CloudAtom], optional
        :param id_: A unique ID assigned by the system to the Runtime cloud., defaults to None
        :type id_: str, optional
        :param name: The name of the Runtime cloud., defaults to None
        :type name: str, optional
        """
        if atom is not SENTINEL:
            self.atom = self._define_list(atom, CloudAtom)
        if id_ is not SENTINEL:
            self.id_ = id_
        if name is not SENTINEL:
            self.name = name
        self._kwargs = kwargs
