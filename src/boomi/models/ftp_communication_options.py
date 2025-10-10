
from __future__ import annotations
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .ftp_get_options import FtpGetOptions
from .ftp_send_options import FtpSendOptions
from .ftp_settings import FtpSettings
from .shared_communication_channel import SharedCommunicationChannel


class FtpCommunicationOptionsCommunicationSetting(Enum):
    """An enumeration representing different categories.

    :cvar DEFAULT: "default"
    :vartype DEFAULT: str
    :cvar CUSTOM: "custom"
    :vartype CUSTOM: str
    :cvar COMPONENT: "component"
    :vartype COMPONENT: str
    """

    DEFAULT = "default"
    CUSTOM = "custom"
    COMPONENT = "component"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                FtpCommunicationOptionsCommunicationSetting._member_map_.values(),
            )
        )


@JsonMap(
    {
        "communication_setting": "CommunicationSetting",
        "ftp_get_options": "FTPGetOptions",
        "ftp_send_options": "FTPSendOptions",
        "ftp_settings": "FTPSettings",
        "shared_communication_channel": "SharedCommunicationChannel",
    }
)
class FtpCommunicationOptions(BaseModel):
    """FtpCommunicationOptions

    :param communication_setting: communication_setting, defaults to None
    :type communication_setting: FtpCommunicationOptionsCommunicationSetting, optional
    :param ftp_get_options: ftp_get_options, defaults to None
    :type ftp_get_options: FtpGetOptions, optional
    :param ftp_send_options: ftp_send_options, defaults to None
    :type ftp_send_options: FtpSendOptions, optional
    :param ftp_settings: ftp_settings, defaults to None
    :type ftp_settings: FtpSettings, optional
    :param shared_communication_channel: shared_communication_channel, defaults to None
    :type shared_communication_channel: SharedCommunicationChannel, optional
    """

    def __init__(
        self,
        communication_setting: FtpCommunicationOptionsCommunicationSetting = SENTINEL,
        ftp_get_options: FtpGetOptions = SENTINEL,
        ftp_send_options: FtpSendOptions = SENTINEL,
        ftp_settings: FtpSettings = SENTINEL,
        shared_communication_channel: SharedCommunicationChannel = SENTINEL,
        **kwargs,
    ):
        """FtpCommunicationOptions

        :param communication_setting: communication_setting, defaults to None
        :type communication_setting: FtpCommunicationOptionsCommunicationSetting, optional
        :param ftp_get_options: ftp_get_options, defaults to None
        :type ftp_get_options: FtpGetOptions, optional
        :param ftp_send_options: ftp_send_options, defaults to None
        :type ftp_send_options: FtpSendOptions, optional
        :param ftp_settings: ftp_settings, defaults to None
        :type ftp_settings: FtpSettings, optional
        :param shared_communication_channel: shared_communication_channel, defaults to None
        :type shared_communication_channel: SharedCommunicationChannel, optional
        """
        if communication_setting is not SENTINEL:
            self.communication_setting = self._enum_matching(
                communication_setting,
                FtpCommunicationOptionsCommunicationSetting.list(),
                "communication_setting",
            )
        if ftp_get_options is not SENTINEL:
            self.ftp_get_options = self._define_object(ftp_get_options, FtpGetOptions)
        if ftp_send_options is not SENTINEL:
            self.ftp_send_options = self._define_object(
                ftp_send_options, FtpSendOptions
            )
        if ftp_settings is not SENTINEL:
            self.ftp_settings = self._define_object(ftp_settings, FtpSettings)
        if shared_communication_channel is not SENTINEL:
            self.shared_communication_channel = self._define_object(
                shared_communication_channel, SharedCommunicationChannel
            )
        self._kwargs = kwargs
