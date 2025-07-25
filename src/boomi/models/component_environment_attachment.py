
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap(
    {
        "component_id": "componentId",
        "component_type": "componentType",
        "environment_id": "environmentId",
        "id_": "id",
    }
)
class ComponentEnvironmentAttachment(BaseModel):
    """ComponentEnvironmentAttachment

    :param component_id: component_id, defaults to None
    :type component_id: str, optional
    :param component_type: component_type, defaults to None
    :type component_type: str, optional
    :param environment_id: environment_id, defaults to None
    :type environment_id: str, optional
    :param id_: id_, defaults to None
    :type id_: str, optional
    """

    def __init__(
        self,
        component_id: str = SENTINEL,
        component_type: str = SENTINEL,
        environment_id: str = SENTINEL,
        id_: str = SENTINEL,
        **kwargs
    ):
        """ComponentEnvironmentAttachment

        :param component_id: component_id, defaults to None
        :type component_id: str, optional
        :param component_type: component_type, defaults to None
        :type component_type: str, optional
        :param environment_id: environment_id, defaults to None
        :type environment_id: str, optional
        :param id_: id_, defaults to None
        :type id_: str, optional
        """
        if component_id is not SENTINEL:
            self.component_id = component_id
        if component_type is not SENTINEL:
            self.component_type = component_type
        if environment_id is not SENTINEL:
            self.environment_id = environment_id
        if id_ is not SENTINEL:
            self.id_ = id_
        self._kwargs = kwargs
