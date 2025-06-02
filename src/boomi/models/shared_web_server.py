
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .shared_web_server_cloud_tennant_general import SharedWebServerCloudTennantGeneral
from .shared_web_server_cors import SharedWebServerCors
from .shared_web_server_general import SharedWebServerGeneral
from .shared_web_server_user_management import SharedWebServerUserManagement


@JsonMap(
    {
        "atom_id": "atomId",
        "cloud_tennant_general": "cloudTennantGeneral",
        "cors_configuration": "corsConfiguration",
        "general_settings": "generalSettings",
        "should_restart_plugin": "shouldRestartPlugin",
        "user_management": "userManagement",
    }
)
class SharedWebServer(BaseModel):
    """SharedWebServer

    :param atom_id: atom_id
    :type atom_id: str
    :param cloud_tennant_general: cloud_tennant_general
    :type cloud_tennant_general: SharedWebServerCloudTennantGeneral
    :param cors_configuration: cors_configuration
    :type cors_configuration: SharedWebServerCors
    :param general_settings: general_settings
    :type general_settings: SharedWebServerGeneral
    :param should_restart_plugin: should_restart_plugin, defaults to None
    :type should_restart_plugin: bool, optional
    :param user_management: user_management
    :type user_management: SharedWebServerUserManagement
    """

    def __init__(
        self,
        atom_id: str,
        cloud_tennant_general: SharedWebServerCloudTennantGeneral,
        cors_configuration: SharedWebServerCors,
        general_settings: SharedWebServerGeneral,
        user_management: SharedWebServerUserManagement,
        should_restart_plugin: bool = SENTINEL,
        **kwargs,
    ):
        """SharedWebServer

        :param atom_id: atom_id
        :type atom_id: str
        :param cloud_tennant_general: cloud_tennant_general
        :type cloud_tennant_general: SharedWebServerCloudTennantGeneral
        :param cors_configuration: cors_configuration
        :type cors_configuration: SharedWebServerCors
        :param general_settings: general_settings
        :type general_settings: SharedWebServerGeneral
        :param should_restart_plugin: should_restart_plugin, defaults to None
        :type should_restart_plugin: bool, optional
        :param user_management: user_management
        :type user_management: SharedWebServerUserManagement
        """
        self.atom_id = atom_id
        self.cloud_tennant_general = self._define_object(
            cloud_tennant_general, SharedWebServerCloudTennantGeneral
        )
        self.cors_configuration = self._define_object(
            cors_configuration, SharedWebServerCors
        )
        self.general_settings = self._define_object(
            general_settings, SharedWebServerGeneral
        )
        if should_restart_plugin is not SENTINEL:
            self.should_restart_plugin = should_restart_plugin
        self.user_management = self._define_object(
            user_management, SharedWebServerUserManagement
        )
        self._kwargs = kwargs
