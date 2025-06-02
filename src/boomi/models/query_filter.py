
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class QueryFilter(BaseModel):
    """QueryFilter

    :param expression: expression
    :type expression: dict
    """

    def __init__(self, expression: dict, **kwargs):
        """QueryFilter

        :param expression: expression
        :type expression: dict
        """
        self.expression = expression
        self._kwargs = kwargs
