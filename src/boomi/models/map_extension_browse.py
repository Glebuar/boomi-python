
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .browse_field import BrowseField


@JsonMap({"browse_fields": "BrowseFields", "session_id": "sessionId"})
class MapExtensionBrowse(BaseModel):
    """MapExtensionBrowse

    :param browse_fields: browse_fields, defaults to None
    :type browse_fields: List[BrowseField], optional
    :param session_id: session_id, defaults to None
    :type session_id: str, optional
    """

    def __init__(
        self,
        browse_fields: List[BrowseField] = SENTINEL,
        session_id: str = SENTINEL,
        **kwargs,
    ):
        """MapExtensionBrowse

        :param browse_fields: browse_fields, defaults to None
        :type browse_fields: List[BrowseField], optional
        :param session_id: session_id, defaults to None
        :type session_id: str, optional
        """
        if browse_fields is not SENTINEL:
            self.browse_fields = self._define_list(browse_fields, BrowseField)
        if session_id is not SENTINEL:
            self.session_id = session_id
        self._kwargs = kwargs
