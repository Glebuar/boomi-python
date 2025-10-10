
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({"worker_id": "workerId"})
class AtomWorkerLog(BaseModel):
    """AtomWorkerLog

    :param worker_id: The name of an execution worker. Locate the name of an execution worker by navigating to the Runtime Workers panel in Manage \> Runtime Management on the user interface., defaults to None
    :type worker_id: str, optional
    """

    def __init__(self, worker_id: str = SENTINEL, **kwargs):
        """AtomWorkerLog

        :param worker_id: The name of an execution worker. Locate the name of an execution worker by navigating to the Runtime Workers panel in Manage \> Runtime Management on the user interface., defaults to None
        :type worker_id: str, optional
        """
        if worker_id is not SENTINEL:
            self.worker_id = worker_id
        self._kwargs = kwargs
