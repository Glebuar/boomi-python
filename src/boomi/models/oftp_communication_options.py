
from __future__ import annotations
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .oftp_connection_settings import OftpConnectionSettings
from .oftp_get_options import OftpGetOptions
from .oftp_send_options import OftpSendOptions
from .oftp_listen_options import OftpListenOptions
from .shared_communication_channel import SharedCommunicationChannel


class OftpCommunicationOptionsCommunicationSetting(Enum):
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
                OftpCommunicationOptionsCommunicationSetting._member_map_.values(),
            )
        )


@JsonMap(
    {
        "communication_setting": "CommunicationSetting",
        "oftp_connection_settings": "OFTPConnectionSettings",
        "oftp_get_options": "OFTPGetOptions",
        "oftp_send_options": "OFTPSendOptions",
        "oftp_server_listen_options": "OFTPServerListenOptions",
        "shared_communication_channel": "SharedCommunicationChannel",
    }
)
class OftpCommunicationOptions(BaseModel):
    """OftpCommunicationOptions

    :param communication_setting: communication_setting, defaults to None
    :type communication_setting: OftpCommunicationOptionsCommunicationSetting, optional
    :param oftp_connection_settings: oftp_connection_settings, defaults to None
    :type oftp_connection_settings: OftpConnectionSettings, optional
    :param oftp_get_options: oftp_get_options, defaults to None
    :type oftp_get_options: OftpGetOptions, optional
    :param oftp_send_options: oftp_send_options, defaults to None
    :type oftp_send_options: OftpSendOptions, optional
    :param oftp_server_listen_options: oftp_server_listen_options, defaults to None
    :type oftp_server_listen_options: OftpListenOptions, optional
    :param shared_communication_channel: shared_communication_channel, defaults to None
    :type shared_communication_channel: SharedCommunicationChannel, optional
    """

    def __init__(
        self,
        communication_setting: OftpCommunicationOptionsCommunicationSetting = SENTINEL,
        oftp_connection_settings: OftpConnectionSettings = SENTINEL,
        oftp_get_options: OftpGetOptions = SENTINEL,
        oftp_send_options: OftpSendOptions = SENTINEL,
        oftp_server_listen_options: OftpListenOptions = SENTINEL,
        shared_communication_channel: SharedCommunicationChannel = SENTINEL,
        **kwargs,
    ):
        """OftpCommunicationOptions

        :param communication_setting: communication_setting, defaults to None
        :type communication_setting: OftpCommunicationOptionsCommunicationSetting, optional
        :param oftp_connection_settings: oftp_connection_settings, defaults to None
        :type oftp_connection_settings: OftpConnectionSettings, optional
        :param oftp_get_options: oftp_get_options, defaults to None
        :type oftp_get_options: OftpGetOptions, optional
        :param oftp_send_options: oftp_send_options, defaults to None
        :type oftp_send_options: OftpSendOptions, optional
        :param oftp_server_listen_options: oftp_server_listen_options, defaults to None
        :type oftp_server_listen_options: OftpListenOptions, optional
        :param shared_communication_channel: shared_communication_channel, defaults to None
        :type shared_communication_channel: SharedCommunicationChannel, optional
        """
        if communication_setting is not SENTINEL:
            self.communication_setting = self._enum_matching(
                communication_setting,
                OftpCommunicationOptionsCommunicationSetting.list(),
                "communication_setting",
            )
        if oftp_connection_settings is not SENTINEL:
            self.oftp_connection_settings = self._define_object(
                oftp_connection_settings, OftpConnectionSettings
            )
        if oftp_get_options is not SENTINEL:
            self.oftp_get_options = self._define_object(
                oftp_get_options, OftpGetOptions
            )
        if oftp_send_options is not SENTINEL:
            self.oftp_send_options = self._define_object(
                oftp_send_options, OftpSendOptions
            )
        if oftp_server_listen_options is not SENTINEL:
            self.oftp_server_listen_options = self._define_object(
                oftp_server_listen_options, OftpListenOptions
            )
        if shared_communication_channel is not SENTINEL:
            self.shared_communication_channel = self._define_object(
                shared_communication_channel, SharedCommunicationChannel
            )
        self._kwargs = kwargs
