
from __future__ import annotations
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .disk_get_options import DiskGetOptions
from .disk_send_options import DiskSendOptions
from .shared_communication_channel import SharedCommunicationChannel


class DiskCommunicationOptionsCommunicationSetting(Enum):
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
                DiskCommunicationOptionsCommunicationSetting._member_map_.values(),
            )
        )


@JsonMap(
    {
        "communication_setting": "CommunicationSetting",
        "disk_get_options": "DiskGetOptions",
        "disk_send_options": "DiskSendOptions",
        "shared_communication_channel": "SharedCommunicationChannel",
    }
)
class DiskCommunicationOptions(BaseModel):
    """DiskCommunicationOptions

    :param communication_setting: communication_setting, defaults to None
    :type communication_setting: DiskCommunicationOptionsCommunicationSetting, optional
    :param disk_get_options: disk_get_options, defaults to None
    :type disk_get_options: DiskGetOptions, optional
    :param disk_send_options: disk_send_options, defaults to None
    :type disk_send_options: DiskSendOptions, optional
    :param shared_communication_channel: shared_communication_channel, defaults to None
    :type shared_communication_channel: SharedCommunicationChannel, optional
    """

    def __init__(
        self,
        communication_setting: DiskCommunicationOptionsCommunicationSetting = SENTINEL,
        disk_get_options: DiskGetOptions = SENTINEL,
        disk_send_options: DiskSendOptions = SENTINEL,
        shared_communication_channel: SharedCommunicationChannel = SENTINEL,
        **kwargs,
    ):
        """DiskCommunicationOptions

        :param communication_setting: communication_setting, defaults to None
        :type communication_setting: DiskCommunicationOptionsCommunicationSetting, optional
        :param disk_get_options: disk_get_options, defaults to None
        :type disk_get_options: DiskGetOptions, optional
        :param disk_send_options: disk_send_options, defaults to None
        :type disk_send_options: DiskSendOptions, optional
        :param shared_communication_channel: shared_communication_channel, defaults to None
        :type shared_communication_channel: SharedCommunicationChannel, optional
        """
        if communication_setting is not SENTINEL:
            self.communication_setting = self._enum_matching(
                communication_setting,
                DiskCommunicationOptionsCommunicationSetting.list(),
                "communication_setting",
            )
        if disk_get_options is not SENTINEL:
            self.disk_get_options = self._define_object(
                disk_get_options, DiskGetOptions
            )
        if disk_send_options is not SENTINEL:
            self.disk_send_options = self._define_object(
                disk_send_options, DiskSendOptions
            )
        if shared_communication_channel is not SENTINEL:
            self.shared_communication_channel = self._define_object(
                shared_communication_channel, SharedCommunicationChannel
            )
        self._kwargs = kwargs
