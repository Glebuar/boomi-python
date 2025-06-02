
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({"component_id": "componentId"})
class SharedCommunicationChannel(BaseModel):
    """SharedCommunicationChannel

    :param component_id: component_id, defaults to None
    :type component_id: str, optional
    """

    def __init__(self, component_id: str = SENTINEL, **kwargs):
        """SharedCommunicationChannel

        :param component_id: component_id, defaults to None
        :type component_id: str, optional
        """
        if component_id is not SENTINEL:
            self.component_id = component_id
        self._kwargs = kwargs
