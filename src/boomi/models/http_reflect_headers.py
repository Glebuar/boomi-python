
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .element import Element


@JsonMap({})
class HttpReflectHeaders(BaseModel):
    """HttpReflectHeaders

    :param element: element, defaults to None
    :type element: List[Element], optional
    """

    def __init__(self, element: List[Element] = SENTINEL, **kwargs):
        """HttpReflectHeaders

        :param element: element, defaults to None
        :type element: List[Element], optional
        """
        if element is not SENTINEL:
            self.element = self._define_list(element, Element)
        self._kwargs = kwargs
