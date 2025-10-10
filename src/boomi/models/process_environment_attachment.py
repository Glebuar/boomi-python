
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap(
    {
        "component_type": "componentType",
        "environment_id": "environmentId",
        "id_": "id",
        "process_id": "processId",
    }
)
class ProcessEnvironmentAttachment(BaseModel):
    """ProcessEnvironmentAttachment

    :param component_type: component_type, defaults to None
    :type component_type: str, optional
    :param environment_id: environment_id, defaults to None
    :type environment_id: str, optional
    :param id_: id_, defaults to None
    :type id_: str, optional
    :param process_id: process_id, defaults to None
    :type process_id: str, optional
    """

    def __init__(
        self,
        component_type: str = SENTINEL,
        environment_id: str = SENTINEL,
        id_: str = SENTINEL,
        process_id: str = SENTINEL,
        **kwargs
    ):
        """ProcessEnvironmentAttachment

        :param component_type: component_type, defaults to None
        :type component_type: str, optional
        :param environment_id: environment_id, defaults to None
        :type environment_id: str, optional
        :param id_: id_, defaults to None
        :type id_: str, optional
        :param process_id: process_id, defaults to None
        :type process_id: str, optional
        """
        if component_type is not SENTINEL:
            self.component_type = component_type
        if environment_id is not SENTINEL:
            self.environment_id = environment_id
        if id_ is not SENTINEL:
            self.id_ = id_
        if process_id is not SENTINEL:
            self.process_id = process_id
        self._kwargs = kwargs
