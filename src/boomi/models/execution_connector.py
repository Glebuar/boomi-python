
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap(
    {
        "action_type": "actionType",
        "connector_type": "connectorType",
        "error_count": "errorCount",
        "execution_connector": "executionConnector",
        "execution_id": "executionId",
        "id_": "id",
        "is_start_shape": "isStartShape",
        "record_type": "recordType",
        "success_count": "successCount",
    }
)
class ExecutionConnector(BaseModel):
    """ExecutionConnector

    :param action_type: The type of action performed by the connector, as defined in the Connector Operation component \(for example: GET, SEND, QUERY, UPDATE, and so on\). The value varies by individual connector., defaults to None
    :type action_type: str, optional
    :param connector_type: The internal and unique identifier for a connector type.\<br /\>1. For **Connectors**, connectorType is the type of Connector \(for example: `http`, `ftp`, `greatplains`\).\<br /\>2. For **Trading Partners**, connectorType is the type of documentstandard the Trading Partner uses \(for example: hl7, edifact, x12\).\<br /\>3. For a **No Data Start** shape or a **Return Documents** shape, the connectorType is either nodata or return, respectively., defaults to None
    :type connector_type: str, optional
    :param error_count: The count of unsuccessful documents on the given execution connector, where the status is **error** or **aborted**., defaults to None
    :type error_count: int, optional
    :param execution_connector: The executionConnector field represents the operation performed by the execution connector. This field's value varies between Connectors, Trading Partners, and Return Documents shapes:\<br /\>1. For **Connectors** such as Disk, FTP, HTTP, and so on. The executionConnector is the user-defined name of the associated connector operation component. If the user did not change the operation component name in the user interface, this field adopts a default name pattern of `New \<connector type\> Connector Operation.`\<br /\>2. For **Trading Partners**, executionConnector is the type of communication method that the Trading Partner uses \(for example: `disk`, `as2`, and so on\).\<br /\>3.  For **Return Documents**, executionConnector is the user -defined display name of the Return Documents shape in the process canvas. If you do not configure a display name, executionConnector is the internal shape name, for example "shape2" or "shape8."\<br /\>4. For a **No Data or Data Passthrough Start shape**, executionConnector is always `start`, indicating that the connector was a Start shape., defaults to None
    :type execution_connector: str, optional
    :param execution_id: The ID of the process run., defaults to None
    :type execution_id: str, optional
    :param id_: A unique ID generated for this connector record., defaults to None
    :type id_: str, optional
    :param is_start_shape: If the value is set to true, this indicates the given execution connector is the **Start** shape of the process. If the value is set to false, this indicates that the given execution connector is not the **Start**shape of the process., defaults to None
    :type is_start_shape: bool, optional
    :param record_type: The type of connector record: tradingpartner, connector, nodata, or return., defaults to None
    :type record_type: str, optional
    :param size: The total size of all documents tracked by the given execution connector, in bytes., defaults to None
    :type size: int, optional
    :param success_count: The count of successful documents on the given execution connector, where a successful run is one with a status of **complete**., defaults to None
    :type success_count: int, optional
    """

    def __init__(
        self,
        action_type: str = SENTINEL,
        connector_type: str = SENTINEL,
        error_count: int = SENTINEL,
        execution_connector: str = SENTINEL,
        execution_id: str = SENTINEL,
        id_: str = SENTINEL,
        is_start_shape: bool = SENTINEL,
        record_type: str = SENTINEL,
        size: int = SENTINEL,
        success_count: int = SENTINEL,
        **kwargs
    ):
        """ExecutionConnector

        :param action_type: The type of action performed by the connector, as defined in the Connector Operation component \(for example: GET, SEND, QUERY, UPDATE, and so on\). The value varies by individual connector., defaults to None
        :type action_type: str, optional
        :param connector_type: The internal and unique identifier for a connector type.\<br /\>1. For **Connectors**, connectorType is the type of Connector \(for example: `http`, `ftp`, `greatplains`\).\<br /\>2. For **Trading Partners**, connectorType is the type of documentstandard the Trading Partner uses \(for example: hl7, edifact, x12\).\<br /\>3. For a **No Data Start** shape or a **Return Documents** shape, the connectorType is either nodata or return, respectively., defaults to None
        :type connector_type: str, optional
        :param error_count: The count of unsuccessful documents on the given execution connector, where the status is **error** or **aborted**., defaults to None
        :type error_count: int, optional
        :param execution_connector: The executionConnector field represents the operation performed by the execution connector. This field's value varies between Connectors, Trading Partners, and Return Documents shapes:\<br /\>1. For **Connectors** such as Disk, FTP, HTTP, and so on. The executionConnector is the user-defined name of the associated connector operation component. If the user did not change the operation component name in the user interface, this field adopts a default name pattern of `New \<connector type\> Connector Operation.`\<br /\>2. For **Trading Partners**, executionConnector is the type of communication method that the Trading Partner uses \(for example: `disk`, `as2`, and so on\).\<br /\>3.  For **Return Documents**, executionConnector is the user -defined display name of the Return Documents shape in the process canvas. If you do not configure a display name, executionConnector is the internal shape name, for example "shape2" or "shape8."\<br /\>4. For a **No Data or Data Passthrough Start shape**, executionConnector is always `start`, indicating that the connector was a Start shape., defaults to None
        :type execution_connector: str, optional
        :param execution_id: The ID of the process run., defaults to None
        :type execution_id: str, optional
        :param id_: A unique ID generated for this connector record., defaults to None
        :type id_: str, optional
        :param is_start_shape: If the value is set to true, this indicates the given execution connector is the **Start** shape of the process. If the value is set to false, this indicates that the given execution connector is not the **Start**shape of the process., defaults to None
        :type is_start_shape: bool, optional
        :param record_type: The type of connector record: tradingpartner, connector, nodata, or return., defaults to None
        :type record_type: str, optional
        :param size: The total size of all documents tracked by the given execution connector, in bytes., defaults to None
        :type size: int, optional
        :param success_count: The count of successful documents on the given execution connector, where a successful run is one with a status of **complete**., defaults to None
        :type success_count: int, optional
        """
        if action_type is not SENTINEL:
            self.action_type = action_type
        if connector_type is not SENTINEL:
            self.connector_type = connector_type
        if error_count is not SENTINEL:
            self.error_count = error_count
        if execution_connector is not SENTINEL:
            self.execution_connector = execution_connector
        if execution_id is not SENTINEL:
            self.execution_id = execution_id
        if id_ is not SENTINEL:
            self.id_ = id_
        if is_start_shape is not SENTINEL:
            self.is_start_shape = is_start_shape
        if record_type is not SENTINEL:
            self.record_type = record_type
        if size is not SENTINEL:
            self.size = size
        if success_count is not SENTINEL:
            self.success_count = success_count
        self._kwargs = kwargs
