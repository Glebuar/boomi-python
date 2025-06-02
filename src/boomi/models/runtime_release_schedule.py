
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class ScheduleType(Enum):
    """An enumeration representing different categories.

    :cvar NEVER: "NEVER"
    :vartype NEVER: str
    :cvar FIRST: "FIRST"
    :vartype FIRST: str
    :cvar LAST: "LAST"
    :vartype LAST: str
    """

    NEVER = "NEVER"
    FIRST = "FIRST"
    LAST = "LAST"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, ScheduleType._member_map_.values()))


@JsonMap(
    {
        "atom_id": "atomId",
        "day_of_week": "dayOfWeek",
        "hour_of_day": "hourOfDay",
        "schedule_type": "scheduleType",
        "time_zone": "timeZone",
    }
)
class RuntimeReleaseSchedule(BaseModel):
    """RuntimeReleaseSchedule

    :param atom_id: The ID of the container for which you want to set a schedule.
    :type atom_id: str
    :param day_of_week: The day of the week that you want to receive updates on the Runtime, Runtime cluster, or Runtime cloud. \<br /\> 1. Required if scheduleType is set to FIRST or LAST
    :type day_of_week: str
    :param hour_of_day: The hour of the day that you want to receive updates on the Runtime, Runtime cluster, or Runtime cloud. 1. Must be between 0-23\<br /\> 2. Required if scheduleType is set to FIRST or LAST, defaults to None
    :type hour_of_day: int, optional
    :param schedule_type: Required. Determines whether you want to receive the updates when available, and if so, whether you receive them in the first or second \(last\) week they are available prior to the .-   FIRST - Update within the first week that updates are available\<br /\> 1. LAST - Update within the second week that updates are available\<br /\>2. NEVER - Update with the
    :type schedule_type: ScheduleType
    :param time_zone: The time zone of your set schedule. \<br /\>1. Must be a [valid time zone](/api/platformapi#section/Introduction/Valid-time-zones) \<br /\>2. Required if scheduleType is set to FIRST or LAST
    :type time_zone: str
    """

    def __init__(
        self,
        atom_id: str,
        day_of_week: str,
        schedule_type: ScheduleType,
        time_zone: str,
        hour_of_day: int = SENTINEL,
        **kwargs
    ):
        """RuntimeReleaseSchedule

        :param atom_id: The ID of the container for which you want to set a schedule.
        :type atom_id: str
        :param day_of_week: The day of the week that you want to receive updates on the Runtime, Runtime cluster, or Runtime cloud. \<br /\> 1. Required if scheduleType is set to FIRST or LAST
        :type day_of_week: str
        :param hour_of_day: The hour of the day that you want to receive updates on the Runtime, Runtime cluster, or Runtime cloud. 1. Must be between 0-23\<br /\> 2. Required if scheduleType is set to FIRST or LAST, defaults to None
        :type hour_of_day: int, optional
        :param schedule_type: Required. Determines whether you want to receive the updates when available, and if so, whether you receive them in the first or second \(last\) week they are available prior to the .-   FIRST - Update within the first week that updates are available\<br /\> 1. LAST - Update within the second week that updates are available\<br /\>2. NEVER - Update with the
        :type schedule_type: ScheduleType
        :param time_zone: The time zone of your set schedule. \<br /\>1. Must be a [valid time zone](/api/platformapi#section/Introduction/Valid-time-zones) \<br /\>2. Required if scheduleType is set to FIRST or LAST
        :type time_zone: str
        """
        self.atom_id = atom_id
        self.day_of_week = day_of_week
        if hour_of_day is not SENTINEL:
            self.hour_of_day = hour_of_day
        self.schedule_type = self._enum_matching(
            schedule_type, ScheduleType.list(), "schedule_type"
        )
        self.time_zone = time_zone
        self._kwargs = kwargs
