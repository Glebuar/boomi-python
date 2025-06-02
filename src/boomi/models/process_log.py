
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class LogLevel(Enum):
    """An enumeration representing different categories.

    :cvar SEVERE: "SEVERE"
    :vartype SEVERE: str
    :cvar WARNING: "WARNING"
    :vartype WARNING: str
    :cvar INFO: "INFO"
    :vartype INFO: str
    :cvar CONFIG: "CONFIG"
    :vartype CONFIG: str
    :cvar FINE: "FINE"
    :vartype FINE: str
    :cvar FINER: "FINER"
    :vartype FINER: str
    :cvar FINEST: "FINEST"
    :vartype FINEST: str
    :cvar ALL: "ALL"
    :vartype ALL: str
    """

    SEVERE = "SEVERE"
    WARNING = "WARNING"
    INFO = "INFO"
    CONFIG = "CONFIG"
    FINE = "FINE"
    FINER = "FINER"
    FINEST = "FINEST"
    ALL = "ALL"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, LogLevel._member_map_.values()))


@JsonMap({"execution_id": "executionId", "log_level": "logLevel"})
class ProcessLog(BaseModel):
    """ProcessLog

    :param execution_id: The ID of the process run., defaults to None
    :type execution_id: str, optional
    :param log_level: The process execution log level with ALL being the default.   If you do not specify the log level, you receive all types of logs. The log level is case sensitive; you must use all uppercase letters., defaults to None
    :type log_level: LogLevel, optional
    """

    def __init__(
        self, execution_id: str = SENTINEL, log_level: LogLevel = SENTINEL, **kwargs
    ):
        """ProcessLog

        :param execution_id: The ID of the process run., defaults to None
        :type execution_id: str, optional
        :param log_level: The process execution log level with ALL being the default.   If you do not specify the log level, you receive all types of logs. The log level is case sensitive; you must use all uppercase letters., defaults to None
        :type log_level: LogLevel, optional
        """
        if execution_id is not SENTINEL:
            self.execution_id = execution_id
        if log_level is not SENTINEL:
            self.log_level = self._enum_matching(
                log_level, LogLevel.list(), "log_level"
            )
        self._kwargs = kwargs
