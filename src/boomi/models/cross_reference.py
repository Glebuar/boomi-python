
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .cross_reference_rows import CrossReferenceRows


@JsonMap(
    {
        "cross_reference_rows": "CrossReferenceRows",
        "id_": "id",
        "override_values": "overrideValues",
    }
)
class CrossReference(BaseModel):
    """CrossReference

    :param cross_reference_rows: cross_reference_rows
    :type cross_reference_rows: CrossReferenceRows
    :param id_: id_, defaults to None
    :type id_: str, optional
    :param name: name, defaults to None
    :type name: str, optional
    :param override_values: override_values, defaults to None
    :type override_values: bool, optional
    """

    def __init__(
        self,
        cross_reference_rows: CrossReferenceRows,
        id_: str = SENTINEL,
        name: str = SENTINEL,
        override_values: bool = SENTINEL,
        **kwargs,
    ):
        """CrossReference

        :param cross_reference_rows: cross_reference_rows
        :type cross_reference_rows: CrossReferenceRows
        :param id_: id_, defaults to None
        :type id_: str, optional
        :param name: name, defaults to None
        :type name: str, optional
        :param override_values: override_values, defaults to None
        :type override_values: bool, optional
        """
        self.cross_reference_rows = self._define_object(
            cross_reference_rows, CrossReferenceRows
        )
        if id_ is not SENTINEL:
            self.id_ = id_
        if name is not SENTINEL:
            self.name = name
        if override_values is not SENTINEL:
            self.override_values = override_values
        self._kwargs = kwargs
