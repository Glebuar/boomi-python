
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class ApiUsageCountClassification(Enum):
    """An enumeration representing different categories.

    :cvar PROD: "PROD"
    :vartype PROD: str
    :cvar TEST: "TEST"
    :vartype TEST: str
    """

    PROD = "PROD"
    TEST = "TEST"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, ApiUsageCountClassification._member_map_.values())
        )


@JsonMap(
    {
        "error_count": "errorCount",
        "process_date": "processDate",
        "success_count": "successCount",
    }
)
class ApiUsageCount(BaseModel):
    """ApiUsageCount

    :param classification: The environment classification., defaults to None
    :type classification: ApiUsageCountClassification, optional
    :param error_count: The count of unsuccessful process runs, where the status is error or aborted., defaults to None
    :type error_count: int, optional
    :param process_date: The start time of the day, in UTC.   Date with the format yyyy-MM-dd'T'HH:mm:ss'Z' — for example, 2017-09-01T00:00:00Z.To specify a time block, use the BETWEEN operator with two arguments, one representing the start time and the other representing the end time.   Boomi recommends specifying a time block in all queries, particularly for heavy users of Low Latency processes, as a means of preventing the return of excessively large amounts of data., defaults to None
    :type process_date: str, optional
    :param success_count: The count of successful process runs, where a successful run is one with a status of complete., defaults to None
    :type success_count: int, optional
    """

    def __init__(
        self,
        classification: ApiUsageCountClassification = SENTINEL,
        error_count: int = SENTINEL,
        process_date: str = SENTINEL,
        success_count: int = SENTINEL,
        **kwargs
    ):
        """ApiUsageCount

        :param classification: The environment classification., defaults to None
        :type classification: ApiUsageCountClassification, optional
        :param error_count: The count of unsuccessful process runs, where the status is error or aborted., defaults to None
        :type error_count: int, optional
        :param process_date: The start time of the day, in UTC.   Date with the format yyyy-MM-dd'T'HH:mm:ss'Z' — for example, 2017-09-01T00:00:00Z.To specify a time block, use the BETWEEN operator with two arguments, one representing the start time and the other representing the end time.   Boomi recommends specifying a time block in all queries, particularly for heavy users of Low Latency processes, as a means of preventing the return of excessively large amounts of data., defaults to None
        :type process_date: str, optional
        :param success_count: The count of successful process runs, where a successful run is one with a status of complete., defaults to None
        :type success_count: int, optional
        """
        if classification is not SENTINEL:
            self.classification = self._enum_matching(
                classification, ApiUsageCountClassification.list(), "classification"
            )
        if error_count is not SENTINEL:
            self.error_count = error_count
        if process_date is not SENTINEL:
            self.process_date = process_date
        if success_count is not SENTINEL:
            self.success_count = success_count
        self._kwargs = kwargs
