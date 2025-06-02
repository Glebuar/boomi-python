
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap(
    {
        "header_field_name": "headerFieldName",
        "target_property_name": "targetPropertyName",
    }
)
class Header(BaseModel):
    """Header

    :param header_field_name: header_field_name, defaults to None
    :type header_field_name: str, optional
    :param target_property_name: target_property_name, defaults to None
    :type target_property_name: str, optional
    """

    def __init__(
        self,
        header_field_name: str = SENTINEL,
        target_property_name: str = SENTINEL,
        **kwargs
    ):
        """Header

        :param header_field_name: header_field_name, defaults to None
        :type header_field_name: str, optional
        :param target_property_name: target_property_name, defaults to None
        :type target_property_name: str, optional
        """
        if header_field_name is not SENTINEL:
            self.header_field_name = header_field_name
        if target_property_name is not SENTINEL:
            self.target_property_name = target_property_name
        self._kwargs = kwargs
