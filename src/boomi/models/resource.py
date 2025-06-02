
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class ObjectType(Enum):
    """An enumeration representing different categories.

    :cvar CLOUD: "Cloud"
    :vartype CLOUD: str
    :cvar CONNECTOR: "Connector"
    :vartype CONNECTOR: str
    :cvar DATAHUBMODEL: "Data Hub Model"
    :vartype DATAHUBMODEL: str
    :cvar INTEGRATIONPACK: "Integration Pack"
    :vartype INTEGRATIONPACK: str
    :cvar PUBLISHEDPROCESS: "Published Process"
    :vartype PUBLISHEDPROCESS: str
    :cvar ROLE: "Role"
    :vartype ROLE: str
    """

    CLOUD = "Cloud"
    CONNECTOR = "Connector"
    DATAHUBMODEL = "Data Hub Model"
    INTEGRATIONPACK = "Integration Pack"
    PUBLISHEDPROCESS = "Published Process"
    ROLE = "Role"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, ObjectType._member_map_.values()))


@JsonMap(
    {
        "object_type": "objectType",
        "resource_id": "resourceId",
        "resource_name": "resourceName",
    }
)
class Resource(BaseModel):
    """Resource

    :param object_type: Resource object type details., defaults to None
    :type object_type: ObjectType, optional
    :param resource_id: Account group resource ID.
    :type resource_id: str
    :param resource_name: Account group resource name.
    :type resource_name: str
    """

    def __init__(
        self,
        resource_id: str,
        resource_name: str,
        object_type: ObjectType = SENTINEL,
        **kwargs
    ):
        """Resource

        :param object_type: Resource object type details., defaults to None
        :type object_type: ObjectType, optional
        :param resource_id: Account group resource ID.
        :type resource_id: str
        :param resource_name: Account group resource name.
        :type resource_name: str
        """
        if object_type is not SENTINEL:
            self.object_type = self._enum_matching(
                object_type, ObjectType.list(), "object_type"
            )
        self.resource_id = resource_id
        self.resource_name = resource_name
        self._kwargs = kwargs
