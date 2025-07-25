
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({"generic_connector_record_id": "genericConnectorRecordId"})
class ConnectorDocument(BaseModel):
    """ConnectorDocument

    :param generic_connector_record_id: The ID of the individual document that you want to download. You can retrieve the `genericConnectorRecordId` by means of a QUERY operation on the [Generic Connector Record](/api/platformapi#tag/GenericConnectorRecord) object., defaults to None
    :type generic_connector_record_id: str, optional
    """

    def __init__(self, generic_connector_record_id: str = SENTINEL, **kwargs):
        """ConnectorDocument

        :param generic_connector_record_id: The ID of the individual document that you want to download. You can retrieve the `genericConnectorRecordId` by means of a QUERY operation on the [Generic Connector Record](/api/platformapi#tag/GenericConnectorRecord) object., defaults to None
        :type generic_connector_record_id: str, optional
        """
        if generic_connector_record_id is not SENTINEL:
            self.generic_connector_record_id = generic_connector_record_id
        self._kwargs = kwargs
