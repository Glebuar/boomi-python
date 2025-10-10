
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .schedule import Schedule


@JsonMap({"schedule": "Schedule", "max_retry": "maxRetry"})
class ScheduleRetry(BaseModel):
    """ScheduleRetry

    :param schedule: schedule, defaults to None
    :type schedule: List[Schedule], optional
    :param max_retry: (Retry schedules only) The maximum number of retries. The minimum valid value is 1; the maximum is 5., defaults to None
    :type max_retry: int, optional
    """

    def __init__(
        self, schedule: List[Schedule] = SENTINEL, max_retry: int = SENTINEL, **kwargs
    ):
        """ScheduleRetry

        :param schedule: schedule, defaults to None
        :type schedule: List[Schedule], optional
        :param max_retry: (Retry schedules only) The maximum number of retries. The minimum valid value is 1; the maximum is 5., defaults to None
        :type max_retry: int, optional
        """
        if schedule is not SENTINEL:
            self.schedule = self._define_list(schedule, Schedule)
        if max_retry is not SENTINEL:
            self.max_retry = max_retry
        self._kwargs = kwargs
