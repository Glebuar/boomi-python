
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .custom_fields import CustomFields


@JsonMap(
    {
        "account": "account",
        "action_type": "actionType",
        "atom_id": "atomId",
        "connector_name": "connectorName",
        "connector_type": "connectorType",
        "custom_fields": "customFields",
        "date_processed": "dateProcessed",
        "document_index": "documentIndex",
        "error_message": "errorMessage",
        "execution_id": "executionId",
        "from_trading_partner": "fromTradingPartner",
        "id_": "id",
        "operation_name": "operationName",
        "size": "size",
        "successful": "successful",
        "to_trading_partner": "toTradingPartner",
    }
)
class EdiCustomConnectorRecord(BaseModel):
    """EdiCustomConnectorRecord

    :param account: The ID of the account that ran this record.
    :type account: str
    :param action_type: The type of action with which this record corresponds — *Send* for an outbound interchange, *Get* for an inbound interchange using the Disk, FTP, or SFTP communication method, or *Listen* for an inbound interchange using the AS2 or HTTP communication method.
    :type action_type: str
    :param atom_id: The ID of the Runtime that processed this record.
    :type atom_id: str
    :param connector_name: The value is *Trading Partner* for a Custom trading partner Send operation, or *Start* for a Custom trading partner Listen operation.
    :type connector_name: str
    :param connector_type: *edicustom* is the connector type for any record.
    :type connector_type: str
    :param custom_fields: custom_fields
    :type custom_fields: CustomFields
    :param date_processed: The processing date and time of this record. Format is yyyy-MM-dd'T'HH:mm:ss'Z' \(for example, 2019-09-14T15:32:00Z\).
    :type date_processed: str
    :param document_index: The numerical index of this record in the execution., defaults to None
    :type document_index: int, optional
    :param error_message: Any error message associated with this record. This field is omitted for a successful interchange.
    :type error_message: str
    :param execution_id: The ID of the run.
    :type execution_id: str
    :param from_trading_partner: The name of the sending trading partner component., defaults to None
    :type from_trading_partner: str, optional
    :param id_: The ID of this record.
    :type id_: str
    :param operation_name: The name of the operation component that processed the record.
    :type operation_name: str
    :param size: The size, in bytes, of the document that corresponds to this record., defaults to None
    :type size: int, optional
    :param successful: Whether the record is a success or error., defaults to None
    :type successful: bool, optional
    :param to_trading_partner: The name of the receiving trading partner component., defaults to None
    :type to_trading_partner: str, optional
    """

    def __init__(
        self,
        account: str,
        action_type: str,
        atom_id: str,
        connector_name: str,
        connector_type: str,
        custom_fields: CustomFields,
        date_processed: str,
        error_message: str,
        execution_id: str,
        id_: str,
        operation_name: str,
        document_index: int = SENTINEL,
        from_trading_partner: str = SENTINEL,
        size: int = SENTINEL,
        successful: bool = SENTINEL,
        to_trading_partner: str = SENTINEL,
        **kwargs,
    ):
        """EdiCustomConnectorRecord

        :param account: The ID of the account that ran this record.
        :type account: str
        :param action_type: The type of action with which this record corresponds — *Send* for an outbound interchange, *Get* for an inbound interchange using the Disk, FTP, or SFTP communication method, or *Listen* for an inbound interchange using the AS2 or HTTP communication method.
        :type action_type: str
        :param atom_id: The ID of the Runtime that processed this record.
        :type atom_id: str
        :param connector_name: The value is *Trading Partner* for a Custom trading partner Send operation, or *Start* for a Custom trading partner Listen operation.
        :type connector_name: str
        :param connector_type: *edicustom* is the connector type for any record.
        :type connector_type: str
        :param custom_fields: custom_fields
        :type custom_fields: CustomFields
        :param date_processed: The processing date and time of this record. Format is yyyy-MM-dd'T'HH:mm:ss'Z' \(for example, 2019-09-14T15:32:00Z\).
        :type date_processed: str
        :param document_index: The numerical index of this record in the execution., defaults to None
        :type document_index: int, optional
        :param error_message: Any error message associated with this record. This field is omitted for a successful interchange.
        :type error_message: str
        :param execution_id: The ID of the run.
        :type execution_id: str
        :param from_trading_partner: The name of the sending trading partner component., defaults to None
        :type from_trading_partner: str, optional
        :param id_: The ID of this record.
        :type id_: str
        :param operation_name: The name of the operation component that processed the record.
        :type operation_name: str
        :param size: The size, in bytes, of the document that corresponds to this record., defaults to None
        :type size: int, optional
        :param successful: Whether the record is a success or error., defaults to None
        :type successful: bool, optional
        :param to_trading_partner: The name of the receiving trading partner component., defaults to None
        :type to_trading_partner: str, optional
        """
        self.account = account
        self.action_type = action_type
        self.atom_id = atom_id
        self.connector_name = connector_name
        self.connector_type = connector_type
        self.custom_fields = self._define_object(custom_fields, CustomFields)
        self.date_processed = date_processed
        if document_index is not SENTINEL:
            self.document_index = document_index
        self.error_message = error_message
        self.execution_id = execution_id
        if from_trading_partner is not SENTINEL:
            self.from_trading_partner = from_trading_partner
        self.id_ = id_
        self.operation_name = operation_name
        if size is not SENTINEL:
            self.size = size
        if successful is not SENTINEL:
            self.successful = successful
        if to_trading_partner is not SENTINEL:
            self.to_trading_partner = to_trading_partner
        self._kwargs = kwargs
