
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .browse_field import BrowseField


@JsonMap({"browse_field": "BrowseField", "connection_id": "connectionId"})
class MapExtensionBrowseData(BaseModel):
    """Fields defining the credentials for connecting to the external service for the purpose of reimporting the source of destination profile to retrieve custom fields. You use these fields in the Environment Map Extension object's EXECUTE action.

    :param browse_field: browse_field, defaults to None
    :type browse_field: List[BrowseField], optional
    :param connection_id: connection_id, defaults to None
    :type connection_id: str, optional
    """

    def __init__(
        self,
        browse_field: List[BrowseField] = SENTINEL,
        connection_id: str = SENTINEL,
        **kwargs,
    ):
        """Fields defining the credentials for connecting to the external service for the purpose of reimporting the source of destination profile to retrieve custom fields. You use these fields in the Environment Map Extension object's EXECUTE action.

        :param browse_field: browse_field, defaults to None
        :type browse_field: List[BrowseField], optional
        :param connection_id: connection_id, defaults to None
        :type connection_id: str, optional
        """
        if browse_field is not SENTINEL:
            self.browse_field = self._define_list(browse_field, BrowseField)
        if connection_id is not SENTINEL:
            self.connection_id = connection_id
        self._kwargs = kwargs
