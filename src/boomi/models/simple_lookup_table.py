
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .simple_lookup_table_rows import SimpleLookupTableRows


@JsonMap({"rows": "Rows"})
class SimpleLookupTable(BaseModel):
    """SimpleLookupTable

    :param rows: rows
    :type rows: SimpleLookupTableRows
    """

    def __init__(self, rows: SimpleLookupTableRows, **kwargs):
        """SimpleLookupTable

        :param rows: rows
        :type rows: SimpleLookupTableRows
        """
        self.rows = self._define_object(rows, SimpleLookupTableRows)
        self._kwargs = kwargs
