
from __future__ import annotations
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .sftp_get_options import SftpGetOptions
from .sftp_send_options import SftpSendOptions
from .sftp_settings import SftpSettings
from .shared_communication_channel import SharedCommunicationChannel


class SftpCommunicationOptionsCommunicationSetting(Enum):
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
                SftpCommunicationOptionsCommunicationSetting._member_map_.values(),
            )
        )


@JsonMap(
    {
        "communication_setting": "CommunicationSetting",
        "sftp_get_options": "SFTPGetOptions",
        "sftp_send_options": "SFTPSendOptions",
        "sftp_settings": "SFTPSettings",
        "shared_communication_channel": "SharedCommunicationChannel",
    }
)
class SftpCommunicationOptions(BaseModel):
    """SftpCommunicationOptions

    :param communication_setting: communication_setting, defaults to None
    :type communication_setting: SftpCommunicationOptionsCommunicationSetting, optional
    :param sftp_get_options: sftp_get_options, defaults to None
    :type sftp_get_options: SftpGetOptions, optional
    :param sftp_send_options: sftp_send_options, defaults to None
    :type sftp_send_options: SftpSendOptions, optional
    :param sftp_settings: sftp_settings, defaults to None
    :type sftp_settings: SftpSettings, optional
    :param shared_communication_channel: shared_communication_channel, defaults to None
    :type shared_communication_channel: SharedCommunicationChannel, optional
    """

    def __init__(
        self,
        communication_setting: SftpCommunicationOptionsCommunicationSetting = SENTINEL,
        sftp_get_options: SftpGetOptions = SENTINEL,
        sftp_send_options: SftpSendOptions = SENTINEL,
        sftp_settings: SftpSettings = SENTINEL,
        shared_communication_channel: SharedCommunicationChannel = SENTINEL,
        **kwargs,
    ):
        """SftpCommunicationOptions

        :param communication_setting: communication_setting, defaults to None
        :type communication_setting: SftpCommunicationOptionsCommunicationSetting, optional
        :param sftp_get_options: sftp_get_options, defaults to None
        :type sftp_get_options: SftpGetOptions, optional
        :param sftp_send_options: sftp_send_options, defaults to None
        :type sftp_send_options: SftpSendOptions, optional
        :param sftp_settings: sftp_settings, defaults to None
        :type sftp_settings: SftpSettings, optional
        :param shared_communication_channel: shared_communication_channel, defaults to None
        :type shared_communication_channel: SharedCommunicationChannel, optional
        """
        if communication_setting is not SENTINEL:
            self.communication_setting = self._enum_matching(
                communication_setting,
                SftpCommunicationOptionsCommunicationSetting.list(),
                "communication_setting",
            )
        if sftp_get_options is not SENTINEL:
            self.sftp_get_options = self._define_object(
                sftp_get_options, SftpGetOptions
            )
        if sftp_send_options is not SENTINEL:
            self.sftp_send_options = self._define_object(
                sftp_send_options, SftpSendOptions
            )
        if sftp_settings is not SENTINEL:
            self.sftp_settings = self._define_object(sftp_settings, SftpSettings)
        if shared_communication_channel is not SENTINEL:
            self.shared_communication_channel = self._define_object(
                shared_communication_channel, SharedCommunicationChannel
            )
        self._kwargs = kwargs
