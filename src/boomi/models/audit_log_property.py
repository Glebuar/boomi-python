
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({"previous_value": "previousValue"})
class AuditLogProperty(BaseModel):
    """AuditLogProperty

    :param name: name, defaults to None
    :type name: str, optional
    :param previous_value: previous_value, defaults to None
    :type previous_value: str, optional
    :param value: value, defaults to None
    :type value: str, optional
    """

    def __init__(
        self,
        name: str = SENTINEL,
        previous_value: str = SENTINEL,
        value: str = SENTINEL,
        **kwargs
    ):
        """AuditLogProperty

        :param name: name, defaults to None
        :type name: str, optional
        :param previous_value: previous_value, defaults to None
        :type previous_value: str, optional
        :param value: value, defaults to None
        :type value: str, optional
        """
        if name is not SENTINEL:
            self.name = name
        if previous_value is not SENTINEL:
            self.previous_value = previous_value
        if value is not SENTINEL:
            self.value = value
        self._kwargs = kwargs
