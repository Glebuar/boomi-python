
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({"process_id": "processId"})
class ProcessingGroupDefaultRouting(BaseModel):
    """ProcessingGroupDefaultRouting

    :param process_id: process_id, defaults to None
    :type process_id: str, optional
    """

    def __init__(self, process_id: str = SENTINEL, **kwargs):
        """ProcessingGroupDefaultRouting

        :param process_id: process_id, defaults to None
        :type process_id: str, optional
        """
        if process_id is not SENTINEL:
            self.process_id = process_id
        self._kwargs = kwargs
