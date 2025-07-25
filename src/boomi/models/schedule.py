
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({"days_of_month": "daysOfMonth", "days_of_week": "daysOfWeek"})
class Schedule(BaseModel):
    """Schedule

    :param days_of_month: 1 is the first day of the month and 31 is the last day of the month., defaults to None
    :type days_of_month: str, optional
    :param days_of_week: 1 is Sunday and 7 is Saturday., defaults to None
    :type days_of_week: str, optional
    :param hours: Uses a 24-hour clock. 0 is midnight and 12 is noon., defaults to None
    :type hours: str, optional
    :param minutes: 0 is the first minute of the hour — for example, 1:00 A.M.59 is the last minute of the hour — for example, 1:59 A.M., defaults to None
    :type minutes: str, optional
    :param months: 1 is January and 12 is December. In most cases this is set to an asterisk [*]., defaults to None
    :type months: str, optional
    :param years: The standard year format. In most cases this is set to an asterisk [*]., defaults to None
    :type years: str, optional
    """

    def __init__(
        self,
        days_of_month: str = SENTINEL,
        days_of_week: str = SENTINEL,
        hours: str = SENTINEL,
        minutes: str = SENTINEL,
        months: str = SENTINEL,
        years: str = SENTINEL,
        **kwargs
    ):
        """Schedule

        :param days_of_month: 1 is the first day of the month and 31 is the last day of the month., defaults to None
        :type days_of_month: str, optional
        :param days_of_week: 1 is Sunday and 7 is Saturday., defaults to None
        :type days_of_week: str, optional
        :param hours: Uses a 24-hour clock. 0 is midnight and 12 is noon., defaults to None
        :type hours: str, optional
        :param minutes: 0 is the first minute of the hour — for example, 1:00 A.M.59 is the last minute of the hour — for example, 1:59 A.M., defaults to None
        :type minutes: str, optional
        :param months: 1 is January and 12 is December. In most cases this is set to an asterisk [*]., defaults to None
        :type months: str, optional
        :param years: The standard year format. In most cases this is set to an asterisk [*]., defaults to None
        :type years: str, optional
        """
        if days_of_month is not SENTINEL:
            self.days_of_month = days_of_month
        if days_of_week is not SENTINEL:
            self.days_of_week = days_of_week
        if hours is not SENTINEL:
            self.hours = hours
        if minutes is not SENTINEL:
            self.minutes = minutes
        if months is not SENTINEL:
            self.months = months
        if years is not SENTINEL:
            self.years = years
        self._kwargs = kwargs
