
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .simple_lookup_table import SimpleLookupTable


@JsonMap({"table": "Table"})
class MapExtensionsSimpleLookup(BaseModel):
    """MapExtensionsSimpleLookup

    :param table: table
    :type table: SimpleLookupTable
    """

    def __init__(self, table: SimpleLookupTable, **kwargs):
        """MapExtensionsSimpleLookup

        :param table: table
        :type table: SimpleLookupTable
        """
        self.table = self._define_object(table, SimpleLookupTable)
        self._kwargs = kwargs
