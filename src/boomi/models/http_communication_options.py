
from __future__ import annotations
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .http_get_options import HttpGetOptions
from .http_listen_options import HttpListenOptions
from .http_send_options import HttpSendOptions
from .http_settings import HttpSettings
from .shared_communication_channel import SharedCommunicationChannel


class HttpCommunicationOptionsCommunicationSetting(Enum):
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
                HttpCommunicationOptionsCommunicationSetting._member_map_.values(),
            )
        )


@JsonMap(
    {
        "communication_setting": "CommunicationSetting",
        "http_get_options": "HTTPGetOptions",
        "http_listen_options": "HTTPListenOptions",
        "http_send_options": "HTTPSendOptions",
        "http_settings": "HTTPSettings",
        "shared_communication_channel": "SharedCommunicationChannel",
    }
)
class HttpCommunicationOptions(BaseModel):
    """HttpCommunicationOptions

    :param communication_setting: communication_setting, defaults to None
    :type communication_setting: HttpCommunicationOptionsCommunicationSetting, optional
    :param http_get_options: http_get_options, defaults to None
    :type http_get_options: HttpGetOptions, optional
    :param http_listen_options: http_listen_options, defaults to None
    :type http_listen_options: HttpListenOptions, optional
    :param http_send_options: http_send_options, defaults to None
    :type http_send_options: HttpSendOptions, optional
    :param http_settings: http_settings, defaults to None
    :type http_settings: HttpSettings, optional
    :param shared_communication_channel: shared_communication_channel, defaults to None
    :type shared_communication_channel: SharedCommunicationChannel, optional
    """

    def __init__(
        self,
        communication_setting: HttpCommunicationOptionsCommunicationSetting = SENTINEL,
        http_get_options: HttpGetOptions = SENTINEL,
        http_listen_options: HttpListenOptions = SENTINEL,
        http_send_options: HttpSendOptions = SENTINEL,
        http_settings: HttpSettings = SENTINEL,
        shared_communication_channel: SharedCommunicationChannel = SENTINEL,
        **kwargs,
    ):
        """HttpCommunicationOptions

        :param communication_setting: communication_setting, defaults to None
        :type communication_setting: HttpCommunicationOptionsCommunicationSetting, optional
        :param http_get_options: http_get_options, defaults to None
        :type http_get_options: HttpGetOptions, optional
        :param http_listen_options: http_listen_options, defaults to None
        :type http_listen_options: HttpListenOptions, optional
        :param http_send_options: http_send_options, defaults to None
        :type http_send_options: HttpSendOptions, optional
        :param http_settings: http_settings, defaults to None
        :type http_settings: HttpSettings, optional
        :param shared_communication_channel: shared_communication_channel, defaults to None
        :type shared_communication_channel: SharedCommunicationChannel, optional
        """
        if communication_setting is not SENTINEL:
            self.communication_setting = self._enum_matching(
                communication_setting,
                HttpCommunicationOptionsCommunicationSetting.list(),
                "communication_setting",
            )
        if http_get_options is not SENTINEL:
            self.http_get_options = self._define_object(
                http_get_options, HttpGetOptions
            )
        if http_listen_options is not SENTINEL:
            self.http_listen_options = self._define_object(
                http_listen_options, HttpListenOptions
            )
        if http_send_options is not SENTINEL:
            self.http_send_options = self._define_object(
                http_send_options, HttpSendOptions
            )
        if http_settings is not SENTINEL:
            self.http_settings = self._define_object(http_settings, HttpSettings)
        if shared_communication_channel is not SENTINEL:
            self.shared_communication_channel = self._define_object(
                shared_communication_channel, SharedCommunicationChannel
            )
        self._kwargs = kwargs
