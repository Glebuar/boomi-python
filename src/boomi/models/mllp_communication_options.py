
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .mllp_send_settings import MllpSendSettings


@JsonMap({"mllp_send_settings": "MLLPSendSettings"})
class MllpCommunicationOptions(BaseModel):
    """MllpCommunicationOptions

    :param mllp_send_settings: mllp_send_settings, defaults to None
    :type mllp_send_settings: MllpSendSettings, optional
    """

    def __init__(self, mllp_send_settings: MllpSendSettings = SENTINEL, **kwargs):
        """MllpCommunicationOptions

        :param mllp_send_settings: mllp_send_settings, defaults to None
        :type mllp_send_settings: MllpSendSettings, optional
        """
        if mllp_send_settings is not SENTINEL:
            self.mllp_send_settings = self._define_object(
                mllp_send_settings, MllpSendSettings
            )
        self._kwargs = kwargs
