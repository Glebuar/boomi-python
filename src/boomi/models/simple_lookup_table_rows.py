
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .simple_lookup_table_row import SimpleLookupTableRow


@JsonMap({"row": "Row"})
class SimpleLookupTableRows(BaseModel):
    """SimpleLookupTableRows

    :param row: row, defaults to None
    :type row: List[SimpleLookupTableRow], optional
    """

    def __init__(self, row: List[SimpleLookupTableRow] = SENTINEL, **kwargs):
        """SimpleLookupTableRows

        :param row: row, defaults to None
        :type row: List[SimpleLookupTableRow], optional
        """
        if row is not SENTINEL:
            self.row = self._define_list(row, SimpleLookupTableRow)
        self._kwargs = kwargs
