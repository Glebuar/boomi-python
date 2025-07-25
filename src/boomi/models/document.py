
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({"generic_connector_record_id": "genericConnectorRecordId"})
class Document(BaseModel):
    """Document

    :param generic_connector_record_id: generic_connector_record_id, defaults to None
    :type generic_connector_record_id: str, optional
    """

    def __init__(self, generic_connector_record_id: str = SENTINEL, **kwargs):
        """Document

        :param generic_connector_record_id: generic_connector_record_id, defaults to None
        :type generic_connector_record_id: str, optional
        """
        if generic_connector_record_id is not SENTINEL:
            self.generic_connector_record_id = generic_connector_record_id
        self._kwargs = kwargs
