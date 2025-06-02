
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class FtpGetOptionsFtpAction(Enum):
    """An enumeration representing different categories.

    :cvar ACTIONGET: "actionget"
    :vartype ACTIONGET: str
    :cvar ACTIONGETDELETE: "actiongetdelete"
    :vartype ACTIONGETDELETE: str
    :cvar ACTIONGETMOVE: "actiongetmove"
    :vartype ACTIONGETMOVE: str
    """

    ACTIONGET = "actionget"
    ACTIONGETDELETE = "actiongetdelete"
    ACTIONGETMOVE = "actiongetmove"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, FtpGetOptionsFtpAction._member_map_.values())
        )


class FtpGetOptionsTransferType(Enum):
    """An enumeration representing different categories.

    :cvar ASCII: "ascii"
    :vartype ASCII: str
    :cvar BINARY: "binary"
    :vartype BINARY: str
    """

    ASCII = "ascii"
    BINARY = "binary"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, FtpGetOptionsTransferType._member_map_.values())
        )


@JsonMap(
    {
        "file_to_move": "fileToMove",
        "ftp_action": "ftpAction",
        "max_file_count": "maxFileCount",
        "remote_directory": "remoteDirectory",
        "transfer_type": "transferType",
        "use_default_get_options": "useDefaultGetOptions",
    }
)
class FtpGetOptions(BaseModel):
    """FtpGetOptions

    :param file_to_move: file_to_move
    :type file_to_move: str
    :param ftp_action: ftp_action, defaults to None
    :type ftp_action: FtpGetOptionsFtpAction, optional
    :param max_file_count: max_file_count
    :type max_file_count: int
    :param remote_directory: remote_directory
    :type remote_directory: str
    :param transfer_type: transfer_type, defaults to None
    :type transfer_type: FtpGetOptionsTransferType, optional
    :param use_default_get_options: use_default_get_options, defaults to None
    :type use_default_get_options: bool, optional
    """

    def __init__(
        self,
        file_to_move: str,
        max_file_count: int,
        remote_directory: str,
        ftp_action: FtpGetOptionsFtpAction = SENTINEL,
        transfer_type: FtpGetOptionsTransferType = SENTINEL,
        use_default_get_options: bool = SENTINEL,
        **kwargs
    ):
        """FtpGetOptions

        :param file_to_move: file_to_move
        :type file_to_move: str
        :param ftp_action: ftp_action, defaults to None
        :type ftp_action: FtpGetOptionsFtpAction, optional
        :param max_file_count: max_file_count
        :type max_file_count: int
        :param remote_directory: remote_directory
        :type remote_directory: str
        :param transfer_type: transfer_type, defaults to None
        :type transfer_type: FtpGetOptionsTransferType, optional
        :param use_default_get_options: use_default_get_options, defaults to None
        :type use_default_get_options: bool, optional
        """
        self.file_to_move = file_to_move
        if ftp_action is not SENTINEL:
            self.ftp_action = self._enum_matching(
                ftp_action, FtpGetOptionsFtpAction.list(), "ftp_action"
            )
        self.max_file_count = max_file_count
        self.remote_directory = remote_directory
        if transfer_type is not SENTINEL:
            self.transfer_type = self._enum_matching(
                transfer_type, FtpGetOptionsTransferType.list(), "transfer_type"
            )
        if use_default_get_options is not SENTINEL:
            self.use_default_get_options = use_default_get_options
        self._kwargs = kwargs
