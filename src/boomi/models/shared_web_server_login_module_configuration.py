
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .shared_web_server_login_module_option import SharedWebServerLoginModuleOption


@JsonMap({"login_module": "loginModule"})
class SharedWebServerLoginModuleConfiguration(BaseModel):
    """SharedWebServerLoginModuleConfiguration

    :param login_module: login_module, defaults to None
    :type login_module: List[SharedWebServerLoginModuleOption], optional
    """

    def __init__(
        self, login_module: List[SharedWebServerLoginModuleOption] = SENTINEL, **kwargs
    ):
        """SharedWebServerLoginModuleConfiguration

        :param login_module: login_module, defaults to None
        :type login_module: List[SharedWebServerLoginModuleOption], optional
        """
        if login_module is not SENTINEL:
            self.login_module = self._define_list(
                login_module, SharedWebServerLoginModuleOption
            )
        self._kwargs = kwargs
