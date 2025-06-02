
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .references import References


@JsonMap({})
class ComponentReference(BaseModel):
    """ComponentReference

    :param references: references, defaults to None
    :type references: List[References], optional
    """

    def __init__(self, references: List[References] = SENTINEL, **kwargs):
        """ComponentReference

        :param references: references, defaults to None
        :type references: List[References], optional
        """
        if references is not SENTINEL:
            self.references = self._define_list(references, References)
        self._kwargs = kwargs
