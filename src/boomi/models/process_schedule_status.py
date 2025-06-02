
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({"atom_id": "atomId", "id_": "id", "process_id": "processId"})
class ProcessScheduleStatus(BaseModel):
    """ProcessScheduleStatus

    :param atom_id: A unique ID assigned by the system to the Runtime., defaults to None
    :type atom_id: str, optional
    :param enabled: If set to true, the schedules are in effect. Setting it to falsestops the schedules., defaults to None
    :type enabled: bool, optional
    :param id_: The object’s conceptual ID, which is synthesized from the process and Runtime IDs., defaults to None
    :type id_: str, optional
    :param process_id: A unique ID assigned by the system to the process., defaults to None
    :type process_id: str, optional
    """

    def __init__(
        self,
        atom_id: str = SENTINEL,
        enabled: bool = SENTINEL,
        id_: str = SENTINEL,
        process_id: str = SENTINEL,
        **kwargs
    ):
        """ProcessScheduleStatus

        :param atom_id: A unique ID assigned by the system to the Runtime., defaults to None
        :type atom_id: str, optional
        :param enabled: If set to true, the schedules are in effect. Setting it to falsestops the schedules., defaults to None
        :type enabled: bool, optional
        :param id_: The object’s conceptual ID, which is synthesized from the process and Runtime IDs., defaults to None
        :type id_: str, optional
        :param process_id: A unique ID assigned by the system to the process., defaults to None
        :type process_id: str, optional
        """
        if atom_id is not SENTINEL:
            self.atom_id = atom_id
        if enabled is not SENTINEL:
            self.enabled = enabled
        if id_ is not SENTINEL:
            self.id_ = id_
        if process_id is not SENTINEL:
            self.process_id = process_id
        self._kwargs = kwargs
