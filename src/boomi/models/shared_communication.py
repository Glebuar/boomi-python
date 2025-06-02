
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .field import Field


@JsonMap({"id_": "id", "type_": "type"})
class SharedCommunication(BaseModel):
    """SharedCommunication

    :param field: field, defaults to None
    :type field: List[Field], optional
    :param id_: id_, defaults to None
    :type id_: str, optional
    :param name: name, defaults to None
    :type name: str, optional
    :param type_: type_, defaults to None
    :type type_: str, optional
    """

    def __init__(
        self,
        field: List[Field] = SENTINEL,
        id_: str = SENTINEL,
        name: str = SENTINEL,
        type_: str = SENTINEL,
        **kwargs,
    ):
        """SharedCommunication

        :param field: field, defaults to None
        :type field: List[Field], optional
        :param id_: id_, defaults to None
        :type id_: str, optional
        :param name: name, defaults to None
        :type name: str, optional
        :param type_: type_, defaults to None
        :type type_: str, optional
        """
        if field is not SENTINEL:
            self.field = self._define_list(field, Field)
        if id_ is not SENTINEL:
            self.id_ = id_
        if name is not SENTINEL:
            self.name = name
        if type_ is not SENTINEL:
            self.type_ = type_
        self._kwargs = kwargs
