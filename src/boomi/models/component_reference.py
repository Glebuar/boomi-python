
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
            # Handle both single reference (dict) and multiple references (list)
            if isinstance(references, dict):
                # Single reference from XML attributes - wrap in list
                self.references = self._define_list([references], References)
            elif isinstance(references, list):
                # Multiple references - normal case
                self.references = self._define_list(references, References)
            else:
                # Fallback to original behavior
                self.references = self._define_list(references, References)
        self._kwargs = kwargs
