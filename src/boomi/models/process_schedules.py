
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .schedule_retry import ScheduleRetry
from .schedule import Schedule


@JsonMap(
    {
        "retry": "Retry",
        "schedule": "Schedule",
        "atom_id": "atomId",
        "id_": "id",
        "process_id": "processId",
    }
)
class ProcessSchedules(BaseModel):
    """ProcessSchedules

    :param retry: retry, defaults to None
    :type retry: ScheduleRetry, optional
    :param schedule: schedule, defaults to None
    :type schedule: List[Schedule], optional
    :param atom_id: A unique ID assigned by the system to the Runtime., defaults to None
    :type atom_id: str, optional
    :param id_: The object’s conceptual ID, which is synthesized from the process and Runtime IDs., defaults to None
    :type id_: str, optional
    :param process_id: A unique ID assigned by the system to the process. Must not be a listener process., defaults to None
    :type process_id: str, optional
    """

    def __init__(
        self,
        retry: ScheduleRetry = SENTINEL,
        schedule: List[Schedule] = SENTINEL,
        atom_id: str = SENTINEL,
        id_: str = SENTINEL,
        process_id: str = SENTINEL,
        **kwargs,
    ):
        """ProcessSchedules

        :param retry: retry, defaults to None
        :type retry: ScheduleRetry, optional
        :param schedule: schedule, defaults to None
        :type schedule: List[Schedule], optional
        :param atom_id: A unique ID assigned by the system to the Runtime., defaults to None
        :type atom_id: str, optional
        :param id_: The object’s conceptual ID, which is synthesized from the process and Runtime IDs., defaults to None
        :type id_: str, optional
        :param process_id: A unique ID assigned by the system to the process. Must not be a listener process., defaults to None
        :type process_id: str, optional
        """
        if retry is not SENTINEL:
            self.retry = self._define_object(retry, ScheduleRetry)
        if schedule is not SENTINEL:
            self.schedule = self._define_list(schedule, Schedule)
        if atom_id is not SENTINEL:
            self.atom_id = atom_id
        if id_ is not SENTINEL:
            self.id_ = id_
        if process_id is not SENTINEL:
            self.process_id = process_id
        self._kwargs = kwargs
