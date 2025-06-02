
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({})
class CustomFields(BaseModel):
    """CustomFields

    :param fields: fields, defaults to None
    :type fields: List[dict], optional
    """

    def __init__(self, fields: List[dict] = SENTINEL, **kwargs):
        """CustomFields

        :param fields: fields, defaults to None
        :type fields: List[dict], optional
        """
        if fields is not SENTINEL:
            self.fields = fields
        self._kwargs = kwargs
