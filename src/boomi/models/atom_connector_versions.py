
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .connector_version import ConnectorVersion


@JsonMap({"connector_version": "ConnectorVersion", "id_": "id"})
class AtomConnectorVersions(BaseModel):
    """AtomConnectorVersions

    :param connector_version: Each pair of `name` and `version` fields represents a connector listed on the **Runtime Management page \> Runtime & Connector Versions** tab., defaults to None
    :type connector_version: List[ConnectorVersion], optional
    :param id_: The ID of the Runtime, Runtime cluster, or Runtime cloud., defaults to None
    :type id_: str, optional
    """

    def __init__(
        self,
        connector_version: List[ConnectorVersion] = SENTINEL,
        id_: str = SENTINEL,
        **kwargs,
    ):
        """AtomConnectorVersions

        :param connector_version: Each pair of `name` and `version` fields represents a connector listed on the **Runtime Management page \> Runtime & Connector Versions** tab., defaults to None
        :type connector_version: List[ConnectorVersion], optional
        :param id_: The ID of the Runtime, Runtime cluster, or Runtime cloud., defaults to None
        :type id_: str, optional
        """
        if connector_version is not SENTINEL:
            self.connector_version = self._define_list(
                connector_version, ConnectorVersion
            )
        if id_ is not SENTINEL:
            self.id_ = id_
        self._kwargs = kwargs
