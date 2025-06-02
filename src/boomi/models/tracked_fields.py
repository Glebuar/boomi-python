
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .tracked_field import TrackedField


@JsonMap({"tracked_field": "trackedField"})
class TrackedFields(BaseModel):
    """Displays all the custom tracked fields from this document.

    :param tracked_field: tracked_field, defaults to None
    :type tracked_field: List[TrackedField], optional
    """

    def __init__(self, tracked_field: List[TrackedField] = SENTINEL, **kwargs):
        """Displays all the custom tracked fields from this document.

        :param tracked_field: tracked_field, defaults to None
        :type tracked_field: List[TrackedField], optional
        """
        if tracked_field is not SENTINEL:
            self.tracked_field = self._define_list(tracked_field, TrackedField)
        self._kwargs = kwargs
