
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class WriteOption(Enum):
    """An enumeration representing different categories.

    :cvar UNIQUE: "unique"
    :vartype UNIQUE: str
    :cvar OVER: "over"
    :vartype OVER: str
    :cvar APPEND: "append"
    :vartype APPEND: str
    :cvar ABORT: "abort"
    :vartype ABORT: str
    """

    UNIQUE = "unique"
    OVER = "over"
    APPEND = "append"
    ABORT = "abort"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, WriteOption._member_map_.values()))


@JsonMap(
    {
        "create_directory": "createDirectory",
        "send_directory": "sendDirectory",
        "use_default_send_options": "useDefaultSendOptions",
        "write_option": "writeOption",
    }
)
class DiskSendOptions(BaseModel):
    """DiskSendOptions

    :param create_directory: create_directory, defaults to None
    :type create_directory: bool, optional
    :param send_directory: send_directory
    :type send_directory: str
    :param use_default_send_options: use_default_send_options, defaults to None
    :type use_default_send_options: bool, optional
    :param write_option: write_option, defaults to None
    :type write_option: WriteOption, optional
    """

    def __init__(
        self,
        send_directory: str,
        create_directory: bool = SENTINEL,
        use_default_send_options: bool = SENTINEL,
        write_option: WriteOption = SENTINEL,
        **kwargs
    ):
        """DiskSendOptions

        :param create_directory: create_directory, defaults to None
        :type create_directory: bool, optional
        :param send_directory: send_directory
        :type send_directory: str
        :param use_default_send_options: use_default_send_options, defaults to None
        :type use_default_send_options: bool, optional
        :param write_option: write_option, defaults to None
        :type write_option: WriteOption, optional
        """
        if create_directory is not SENTINEL:
            self.create_directory = create_directory
        self.send_directory = send_directory
        if use_default_send_options is not SENTINEL:
            self.use_default_send_options = use_default_send_options
        if write_option is not SENTINEL:
            self.write_option = self._enum_matching(
                write_option, WriteOption.list(), "write_option"
            )
        self._kwargs = kwargs
