
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
        "id_": "id",
        "initiator_ssidcode": "initiator_ssidcode",
        "nareas": "nareas",
        "nareast": "nareast",
        "objecttype": "objecttype",
        "operation_name": "operationName",
        "responder_ssidcode": "responder_ssidcode",
        "sfidciph": "sfidciph",
        "sfidcomp": "sfidcomp",
        "sfiddate": "sfiddate",
        "sfiddesc": "sfiddesc",
        "sfiddest": "sfiddest",
        "sfiddsn": "sfiddsn",
        "sfidenv": "sfidenv",
        "sfidorig": "sfidorig",
        "sfidosiz": "sfidosiz",
        "sfidsec": "sfidsec",
        "sfidsign": "sfidsign",
        "sfidtime": "sfidtime",
        "size": "size",
        "status": "status",
        "successful": "successful",
        "ticker": "ticker",
    }
)
class Oftp2ConnectorRecord(BaseModel):
    """Oftp2ConnectorRecord

    :param account: The ID of the account from which you ran this record.
    :type account: str
    :param action_type: The type of action with which this record corresponds - Send, Get or Listen.
    :type action_type: str
    :param atom_id: The ID of the Runtime that processed this record.
    :type atom_id: str
    :param connector_name: For the OFTP2 Client, the value is oftp Connector and for the OFTP2 Server, the value is oftpserver Connector.
    :type connector_name: str
    :param connector_type: The type of connector to which this record corresponds- oftp for OFTP2 Client or oftpserver for OFTP2 Server.
    :type connector_type: str
    :param custom_fields: custom_fields
    :type custom_fields: CustomFields
    :param date_processed: The processing date and time of this record. The format is yyyy-MM-dd'T'HH:mm:ss'Z', for example, 2013-08-08T15:32:00Z.
    :type date_processed: str
    :param document_index: The numerical index of this record in the run., defaults to None
    :type document_index: int, optional
    :param error_message: error_message
    :type error_message: str
    :param execution_id: The ID of the execution run.
    :type execution_id: str
    :param id_: The ID of this record.
    :type id_: str
    :param initiator_ssidcode: The Initiator's Identification Code., defaults to None
    :type initiator_ssidcode: str, optional
    :param nareas: Only displays if the transmission failed. The reason numeric code for the failure., defaults to None
    :type nareas: str, optional
    :param nareast: Only displays if the transmission failed. The reason text for the failure., defaults to None
    :type nareast: str, optional
    :param objecttype: objecttype, defaults to None
    :type objecttype: str, optional
    :param operation_name: The name of the operation component that processed this record.
    :type operation_name: str
    :param responder_ssidcode: The Responder's Identification Code., defaults to None
    :type responder_ssidcode: str, optional
    :param sfidciph: Indicates which cipher suite was used to sign or encrypt the file. The cipher suite in this value should also be used when a signed EERP or NERP is requested.\<br /\>-`00` - No security services\<br /\>-`01` - 3DES_EDE_CBC_3KEY\<br /\> -`02` - AES_256_CBC, defaults to None
    :type sfidciph: str, optional
    :param sfidcomp: Indicates whether an algorithm was used to compress the file.\<br /\>-`0` - No compression\<br /\>-`1` - Compressed with an algorithm., defaults to None
    :type sfidcomp: str, optional
    :param sfiddate: The date when the virtual file was created. The format is yyyy-MM-dd, for example 2023-06-07., defaults to None
    :type sfiddate: str, optional
    :param sfiddesc: The description of the virtual file., defaults to None
    :type sfiddesc: str, optional
    :param sfiddest: The destination Odette ID for the virtual file., defaults to None
    :type sfiddest: str, optional
    :param sfiddsn: The dataset name of the virtual file being transferred., defaults to None
    :type sfiddsn: str, optional
    :param sfidenv: The enveloping format used in the file.\<br /\>-`0` - No enveloped\<br /\>-`1` - File is enveloped using CMS, defaults to None
    :type sfidenv: str, optional
    :param sfidorig: The originator of the virtual file., defaults to None
    :type sfidorig: str, optional
    :param sfidosiz: The size of the original file., defaults to None
    :type sfidosiz: str, optional
    :param sfidsec: Indicates whether the file has been signed or encrypted before transmission. The following values are possible:\<br /\>-`00` - No security services\<br /\>-`01` - Encrypted\<br /\>-`02` - Signed\<br /\>-`03` - Encrypted and signed, defaults to None
    :type sfidsec: str, optional
    :param sfidsign: Whether the EERP returned for the file must be signed.\<br /\>-`Y` - the EERP must be signed\<br /\>-`N` - The EERP must not be signed, defaults to None
    :type sfidsign: str, optional
    :param sfidtime: The time when the virtual file was created. The format is HH:mm:ss.SSSX, where X is the ticker, for example 10:06:46.2389., defaults to None
    :type sfidtime: str, optional
    :param size: The size, in bytes, of the document that corresponds to this record., defaults to None
    :type size: int, optional
    :param status: Whether the file transmission is pending an acknowledgment, acknowledged as a success or an error., defaults to None
    :type status: str, optional
    :param successful: Whether the record is a success or error., defaults to None
    :type successful: bool, optional
    :param ticker: ticker, defaults to None
    :type ticker: str, optional
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
        initiator_ssidcode: str = SENTINEL,
        nareas: str = SENTINEL,
        nareast: str = SENTINEL,
        objecttype: str = SENTINEL,
        responder_ssidcode: str = SENTINEL,
        sfidciph: str = SENTINEL,
        sfidcomp: str = SENTINEL,
        sfiddate: str = SENTINEL,
        sfiddesc: str = SENTINEL,
        sfiddest: str = SENTINEL,
        sfiddsn: str = SENTINEL,
        sfidenv: str = SENTINEL,
        sfidorig: str = SENTINEL,
        sfidosiz: str = SENTINEL,
        sfidsec: str = SENTINEL,
        sfidsign: str = SENTINEL,
        sfidtime: str = SENTINEL,
        size: int = SENTINEL,
        status: str = SENTINEL,
        successful: bool = SENTINEL,
        ticker: str = SENTINEL,
        **kwargs,
    ):
        """Oftp2ConnectorRecord

        :param account: The ID of the account from which you ran this record.
        :type account: str
        :param action_type: The type of action with which this record corresponds - Send, Get or Listen.
        :type action_type: str
        :param atom_id: The ID of the Runtime that processed this record.
        :type atom_id: str
        :param connector_name: For the OFTP2 Client, the value is oftp Connector and for the OFTP2 Server, the value is oftpserver Connector.
        :type connector_name: str
        :param connector_type: The type of connector to which this record corresponds- oftp for OFTP2 Client or oftpserver for OFTP2 Server.
        :type connector_type: str
        :param custom_fields: custom_fields
        :type custom_fields: CustomFields
        :param date_processed: The processing date and time of this record. The format is yyyy-MM-dd'T'HH:mm:ss'Z', for example, 2013-08-08T15:32:00Z.
        :type date_processed: str
        :param document_index: The numerical index of this record in the run., defaults to None
        :type document_index: int, optional
        :param error_message: error_message
        :type error_message: str
        :param execution_id: The ID of the execution run.
        :type execution_id: str
        :param id_: The ID of this record.
        :type id_: str
        :param initiator_ssidcode: The Initiator's Identification Code., defaults to None
        :type initiator_ssidcode: str, optional
        :param nareas: Only displays if the transmission failed. The reason numeric code for the failure., defaults to None
        :type nareas: str, optional
        :param nareast: Only displays if the transmission failed. The reason text for the failure., defaults to None
        :type nareast: str, optional
        :param objecttype: objecttype, defaults to None
        :type objecttype: str, optional
        :param operation_name: The name of the operation component that processed this record.
        :type operation_name: str
        :param responder_ssidcode: The Responder's Identification Code., defaults to None
        :type responder_ssidcode: str, optional
        :param sfidciph: Indicates which cipher suite was used to sign or encrypt the file. The cipher suite in this value should also be used when a signed EERP or NERP is requested.\<br /\>-`00` - No security services\<br /\>-`01` - 3DES_EDE_CBC_3KEY\<br /\> -`02` - AES_256_CBC, defaults to None
        :type sfidciph: str, optional
        :param sfidcomp: Indicates whether an algorithm was used to compress the file.\<br /\>-`0` - No compression\<br /\>-`1` - Compressed with an algorithm., defaults to None
        :type sfidcomp: str, optional
        :param sfiddate: The date when the virtual file was created. The format is yyyy-MM-dd, for example 2023-06-07., defaults to None
        :type sfiddate: str, optional
        :param sfiddesc: The description of the virtual file., defaults to None
        :type sfiddesc: str, optional
        :param sfiddest: The destination Odette ID for the virtual file., defaults to None
        :type sfiddest: str, optional
        :param sfiddsn: The dataset name of the virtual file being transferred., defaults to None
        :type sfiddsn: str, optional
        :param sfidenv: The enveloping format used in the file.\<br /\>-`0` - No enveloped\<br /\>-`1` - File is enveloped using CMS, defaults to None
        :type sfidenv: str, optional
        :param sfidorig: The originator of the virtual file., defaults to None
        :type sfidorig: str, optional
        :param sfidosiz: The size of the original file., defaults to None
        :type sfidosiz: str, optional
        :param sfidsec: Indicates whether the file has been signed or encrypted before transmission. The following values are possible:\<br /\>-`00` - No security services\<br /\>-`01` - Encrypted\<br /\>-`02` - Signed\<br /\>-`03` - Encrypted and signed, defaults to None
        :type sfidsec: str, optional
        :param sfidsign: Whether the EERP returned for the file must be signed.\<br /\>-`Y` - the EERP must be signed\<br /\>-`N` - The EERP must not be signed, defaults to None
        :type sfidsign: str, optional
        :param sfidtime: The time when the virtual file was created. The format is HH:mm:ss.SSSX, where X is the ticker, for example 10:06:46.2389., defaults to None
        :type sfidtime: str, optional
        :param size: The size, in bytes, of the document that corresponds to this record., defaults to None
        :type size: int, optional
        :param status: Whether the file transmission is pending an acknowledgment, acknowledged as a success or an error., defaults to None
        :type status: str, optional
        :param successful: Whether the record is a success or error., defaults to None
        :type successful: bool, optional
        :param ticker: ticker, defaults to None
        :type ticker: str, optional
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
        self.id_ = id_
        if initiator_ssidcode is not SENTINEL:
            self.initiator_ssidcode = initiator_ssidcode
        if nareas is not SENTINEL:
            self.nareas = nareas
        if nareast is not SENTINEL:
            self.nareast = nareast
        if objecttype is not SENTINEL:
            self.objecttype = objecttype
        self.operation_name = operation_name
        if responder_ssidcode is not SENTINEL:
            self.responder_ssidcode = responder_ssidcode
        if sfidciph is not SENTINEL:
            self.sfidciph = sfidciph
        if sfidcomp is not SENTINEL:
            self.sfidcomp = sfidcomp
        if sfiddate is not SENTINEL:
            self.sfiddate = sfiddate
        if sfiddesc is not SENTINEL:
            self.sfiddesc = sfiddesc
        if sfiddest is not SENTINEL:
            self.sfiddest = sfiddest
        if sfiddsn is not SENTINEL:
            self.sfiddsn = sfiddsn
        if sfidenv is not SENTINEL:
            self.sfidenv = sfidenv
        if sfidorig is not SENTINEL:
            self.sfidorig = sfidorig
        if sfidosiz is not SENTINEL:
            self.sfidosiz = sfidosiz
        if sfidsec is not SENTINEL:
            self.sfidsec = sfidsec
        if sfidsign is not SENTINEL:
            self.sfidsign = sfidsign
        if sfidtime is not SENTINEL:
            self.sfidtime = sfidtime
        if size is not SENTINEL:
            self.size = size
        if status is not SENTINEL:
            self.status = status
        if successful is not SENTINEL:
            self.successful = successful
        if ticker is not SENTINEL:
            self.ticker = ticker
        self._kwargs = kwargs
