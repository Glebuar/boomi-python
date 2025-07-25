
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({"type_": "type"})
class Connector(BaseModel):
    """Connector

    :param name: The user-facing connector label of the connector type, which mimics the connector type names presented on the **Build** tab of the user interface., defaults to None
    :type name: str, optional
    :param type_: The internal and unique identifier for connector type, such as `http`, `ftp`, `greatplains`. The [Component Metadata object](/api/platformapi#tag/ComponentMetadata) refers to this field as *subType*., defaults to None
    :type type_: str, optional
    """

    def __init__(self, name: str = SENTINEL, type_: str = SENTINEL, **kwargs):
        """Connector

        :param name: The user-facing connector label of the connector type, which mimics the connector type names presented on the **Build** tab of the user interface., defaults to None
        :type name: str, optional
        :param type_: The internal and unique identifier for connector type, such as `http`, `ftp`, `greatplains`. The [Component Metadata object](/api/platformapi#tag/ComponentMetadata) refers to this field as *subType*., defaults to None
        :type type_: str, optional
        """
        if name is not SENTINEL:
            self.name = name
        if type_ is not SENTINEL:
            self.type_ = type_
        self._kwargs = kwargs
