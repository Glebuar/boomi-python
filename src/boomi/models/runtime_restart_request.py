
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({"runtime_id": "runtimeId"})
class RuntimeRestartRequest(BaseModel):
    """RuntimeRestartRequest

    :param message: message, defaults to None
    :type message: str, optional
    :param runtime_id: A unique ID for the runtime. Cloud attachments cannot be restarted., defaults to None
    :type runtime_id: str, optional
    """

    def __init__(self, message: str = SENTINEL, runtime_id: str = SENTINEL, **kwargs):
        """RuntimeRestartRequest

        :param message: message, defaults to None
        :type message: str, optional
        :param runtime_id: A unique ID for the runtime. Cloud attachments cannot be restarted., defaults to None
        :type runtime_id: str, optional
        """
        if message is not SENTINEL:
            self.message = message
        if runtime_id is not SENTINEL:
            self.runtime_id = runtime_id
        self._kwargs = kwargs
