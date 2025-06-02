
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class FtpSendOptionsFtpAction(Enum):
    """An enumeration representing different categories.

    :cvar ACTIONPUTRENAME: "actionputrename"
    :vartype ACTIONPUTRENAME: str
    :cvar ACTIONPUTAPPEND: "actionputappend"
    :vartype ACTIONPUTAPPEND: str
    :cvar ACTIONPUTERROR: "actionputerror"
    :vartype ACTIONPUTERROR: str
    :cvar ACTIONPUTOVERWRITE: "actionputoverwrite"
    :vartype ACTIONPUTOVERWRITE: str
    """

    ACTIONPUTRENAME = "actionputrename"
    ACTIONPUTAPPEND = "actionputappend"
    ACTIONPUTERROR = "actionputerror"
    ACTIONPUTOVERWRITE = "actionputoverwrite"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, FtpSendOptionsFtpAction._member_map_.values())
        )


class FtpSendOptionsTransferType(Enum):
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
            map(lambda x: x.value, FtpSendOptionsTransferType._member_map_.values())
        )


@JsonMap(
    {
        "ftp_action": "ftpAction",
        "move_to_directory": "moveToDirectory",
        "remote_directory": "remoteDirectory",
        "transfer_type": "transferType",
        "use_default_send_options": "useDefaultSendOptions",
    }
)
class FtpSendOptions(BaseModel):
    """FtpSendOptions

    :param ftp_action: ftp_action, defaults to None
    :type ftp_action: FtpSendOptionsFtpAction, optional
    :param move_to_directory: move_to_directory
    :type move_to_directory: str
    :param remote_directory: remote_directory
    :type remote_directory: str
    :param transfer_type: transfer_type, defaults to None
    :type transfer_type: FtpSendOptionsTransferType, optional
    :param use_default_send_options: use_default_send_options, defaults to None
    :type use_default_send_options: bool, optional
    """

    def __init__(
        self,
        move_to_directory: str,
        remote_directory: str,
        ftp_action: FtpSendOptionsFtpAction = SENTINEL,
        transfer_type: FtpSendOptionsTransferType = SENTINEL,
        use_default_send_options: bool = SENTINEL,
        **kwargs
    ):
        """FtpSendOptions

        :param ftp_action: ftp_action, defaults to None
        :type ftp_action: FtpSendOptionsFtpAction, optional
        :param move_to_directory: move_to_directory
        :type move_to_directory: str
        :param remote_directory: remote_directory
        :type remote_directory: str
        :param transfer_type: transfer_type, defaults to None
        :type transfer_type: FtpSendOptionsTransferType, optional
        :param use_default_send_options: use_default_send_options, defaults to None
        :type use_default_send_options: bool, optional
        """
        if ftp_action is not SENTINEL:
            self.ftp_action = self._enum_matching(
                ftp_action, FtpSendOptionsFtpAction.list(), "ftp_action"
            )
        self.move_to_directory = move_to_directory
        self.remote_directory = remote_directory
        if transfer_type is not SENTINEL:
            self.transfer_type = self._enum_matching(
                transfer_type, FtpSendOptionsTransferType.list(), "transfer_type"
            )
        if use_default_send_options is not SENTINEL:
            self.use_default_send_options = use_default_send_options
        self._kwargs = kwargs
