
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .connector_field import ConnectorField


@JsonMap({"connector_field": "connectorField"})
class ConnectorFields(BaseModel):
    """Displays all connector-related fields from the connector included in this document.

    :param connector_field: connector_field, defaults to None
    :type connector_field: List[ConnectorField], optional
    """

    def __init__(self, connector_field: List[ConnectorField] = SENTINEL, **kwargs):
        """Displays all connector-related fields from the connector included in this document.

        :param connector_field: connector_field, defaults to None
        :type connector_field: List[ConnectorField], optional
        """
        if connector_field is not SENTINEL:
            self.connector_field = self._define_list(connector_field, ConnectorField)
        self._kwargs = kwargs
