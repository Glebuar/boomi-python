
from __future__ import annotations
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .as2_send_settings import As2SendSettings
from .as2_receive_options import As2ReceiveOptions
from .as2_send_options import As2SendOptions
from .shared_communication_channel import SharedCommunicationChannel


class As2CommunicationOptionsCommunicationSetting(Enum):
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
                As2CommunicationOptionsCommunicationSetting._member_map_.values(),
            )
        )


@JsonMap(
    {
        "as2_default_partner_settings": "AS2DefaultPartnerSettings",
        "as2_receive_options": "AS2ReceiveOptions",
        "as2_send_options": "AS2SendOptions",
        "as2_send_settings": "AS2SendSettings",
        "communication_setting": "CommunicationSetting",
        "shared_communication_channel": "SharedCommunicationChannel",
    }
)
class As2CommunicationOptions(BaseModel):
    """As2CommunicationOptions

    :param as2_default_partner_settings: as2_default_partner_settings, defaults to None
    :type as2_default_partner_settings: As2SendSettings, optional
    :param as2_receive_options: as2_receive_options, defaults to None
    :type as2_receive_options: As2ReceiveOptions, optional
    :param as2_send_options: as2_send_options, defaults to None
    :type as2_send_options: As2SendOptions, optional
    :param as2_send_settings: as2_send_settings, defaults to None
    :type as2_send_settings: As2SendSettings, optional
    :param communication_setting: communication_setting, defaults to None
    :type communication_setting: As2CommunicationOptionsCommunicationSetting, optional
    :param shared_communication_channel: shared_communication_channel, defaults to None
    :type shared_communication_channel: SharedCommunicationChannel, optional
    """

    def __init__(
        self,
        as2_default_partner_settings: As2SendSettings = SENTINEL,
        as2_receive_options: As2ReceiveOptions = SENTINEL,
        as2_send_options: As2SendOptions = SENTINEL,
        as2_send_settings: As2SendSettings = SENTINEL,
        communication_setting: As2CommunicationOptionsCommunicationSetting = SENTINEL,
        shared_communication_channel: SharedCommunicationChannel = SENTINEL,
        **kwargs,
    ):
        """As2CommunicationOptions

        :param as2_default_partner_settings: as2_default_partner_settings, defaults to None
        :type as2_default_partner_settings: As2SendSettings, optional
        :param as2_receive_options: as2_receive_options, defaults to None
        :type as2_receive_options: As2ReceiveOptions, optional
        :param as2_send_options: as2_send_options, defaults to None
        :type as2_send_options: As2SendOptions, optional
        :param as2_send_settings: as2_send_settings, defaults to None
        :type as2_send_settings: As2SendSettings, optional
        :param communication_setting: communication_setting, defaults to None
        :type communication_setting: As2CommunicationOptionsCommunicationSetting, optional
        :param shared_communication_channel: shared_communication_channel, defaults to None
        :type shared_communication_channel: SharedCommunicationChannel, optional
        """
        if as2_default_partner_settings is not SENTINEL:
            self.as2_default_partner_settings = self._define_object(
                as2_default_partner_settings, As2SendSettings
            )
        if as2_receive_options is not SENTINEL:
            self.as2_receive_options = self._define_object(
                as2_receive_options, As2ReceiveOptions
            )
        if as2_send_options is not SENTINEL:
            self.as2_send_options = self._define_object(
                as2_send_options, As2SendOptions
            )
        if as2_send_settings is not SENTINEL:
            self.as2_send_settings = self._define_object(
                as2_send_settings, As2SendSettings
            )
        if communication_setting is not SENTINEL:
            self.communication_setting = self._enum_matching(
                communication_setting,
                As2CommunicationOptionsCommunicationSetting.list(),
                "communication_setting",
            )
        if shared_communication_channel is not SENTINEL:
            self.shared_communication_channel = self._define_object(
                shared_communication_channel, SharedCommunicationChannel
            )
        self._kwargs = kwargs
