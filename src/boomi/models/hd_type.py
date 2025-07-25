
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap(
    {
        "namespace_id": "namespaceId",
        "universal_id": "universalId",
        "universal_id_type": "universalIdType",
    }
)
class HdType(BaseModel):
    """HdType

    :param namespace_id: namespace_id, defaults to None
    :type namespace_id: str, optional
    :param universal_id: universal_id, defaults to None
    :type universal_id: str, optional
    :param universal_id_type: universal_id_type, defaults to None
    :type universal_id_type: str, optional
    """

    def __init__(
        self,
        namespace_id: str = SENTINEL,
        universal_id: str = SENTINEL,
        universal_id_type: str = SENTINEL,
        **kwargs
    ):
        """HdType

        :param namespace_id: namespace_id, defaults to None
        :type namespace_id: str, optional
        :param universal_id: universal_id, defaults to None
        :type universal_id: str, optional
        :param universal_id_type: universal_id_type, defaults to None
        :type universal_id_type: str, optional
        """
        if namespace_id is not SENTINEL:
            self.namespace_id = namespace_id
        if universal_id is not SENTINEL:
            self.universal_id = universal_id
        if universal_id_type is not SENTINEL:
            self.universal_id_type = universal_id_type
        self._kwargs = kwargs
