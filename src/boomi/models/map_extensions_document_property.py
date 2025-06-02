
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap(
    {
        "default_value": "defaultValue",
        "property_id": "propertyId",
        "property_name": "propertyName",
    }
)
class MapExtensionsDocumentProperty(BaseModel):
    """MapExtensionsDocumentProperty

    :param default_value: default_value, defaults to None
    :type default_value: str, optional
    :param persist: persist, defaults to None
    :type persist: bool, optional
    :param property_id: property_id, defaults to None
    :type property_id: str, optional
    :param property_name: property_name, defaults to None
    :type property_name: str, optional
    """

    def __init__(
        self,
        default_value: str = SENTINEL,
        persist: bool = SENTINEL,
        property_id: str = SENTINEL,
        property_name: str = SENTINEL,
        **kwargs
    ):
        """MapExtensionsDocumentProperty

        :param default_value: default_value, defaults to None
        :type default_value: str, optional
        :param persist: persist, defaults to None
        :type persist: bool, optional
        :param property_id: property_id, defaults to None
        :type property_id: str, optional
        :param property_name: property_name, defaults to None
        :type property_name: str, optional
        """
        if default_value is not SENTINEL:
            self.default_value = default_value
        if persist is not SENTINEL:
            self.persist = persist
        if property_id is not SENTINEL:
            self.property_id = property_id
        if property_name is not SENTINEL:
            self.property_name = property_name
        self._kwargs = kwargs
