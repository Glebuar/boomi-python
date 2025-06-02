
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .cross_reference_row import CrossReferenceRow


@JsonMap({})
class CrossReferenceRows(BaseModel):
    """CrossReferenceRows

    :param row: row, defaults to None
    :type row: List[CrossReferenceRow], optional
    """

    def __init__(self, row: List[CrossReferenceRow] = SENTINEL, **kwargs):
        """CrossReferenceRows

        :param row: row, defaults to None
        :type row: List[CrossReferenceRow], optional
        """
        if row is not SENTINEL:
            self.row = self._define_list(row, CrossReferenceRow)
        self._kwargs = kwargs
