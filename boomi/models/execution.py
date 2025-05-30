from pydantic import BaseModel, Field
from typing import Optional

class ExecutionRecord(BaseModel):
    id: str = Field(..., alias="executionId")
    status: Optional[str] = None
    execution_time: Optional[str] = Field(None, alias="executionTime")
    process_id: Optional[str] = Field(None, alias="processId")
    process_name: Optional[str] = Field(None, alias="processName")
    atom_id: Optional[str] = Field(None, alias="atomId")
    atom_name: Optional[str] = Field(None, alias="atomName")
    account: Optional[str] = None
    message: Optional[str] = None
    report_key: Optional[str] = Field(None, alias="reportKey")
    recorded_date: Optional[str] = Field(None, alias="recordedDate")
    execution_type: Optional[str] = Field(None, alias="executionType")
    execution_duration: Optional[int] = Field(None, alias="executionDuration")
    inbound_document_count: Optional[int] = Field(None, alias="inboundDocumentCount")
    outbound_document_count: Optional[int] = Field(None, alias="outboundDocumentCount")
    inbound_document_size: Optional[int] = Field(None, alias="inboundDocumentSize")
    outbound_document_size: Optional[int] = Field(None, alias="outboundDocumentSize")
    inbound_error_document_count: Optional[int] = Field(
        None, alias="inboundErrorDocumentCount"
    )
    launcher_id: Optional[str] = Field(None, alias="launcherID")
    node_id: Optional[str] = Field(None, alias="nodeId")
    original_execution_id: Optional[str] = Field(None, alias="originalExecutionId")
    parent_execution_id: Optional[str] = Field(None, alias="parentExecutionId")
    top_level_execution_id: Optional[str] = Field(None, alias="topLevelExecutionId")

# The response returned by ``/ExecuteProcess`` mirrors ``ExecutionRecord``.
class ExecuteProcessResponse(ExecutionRecord):
    pass

class ExecutionSummaryRecord(BaseModel):
    process_id: str = Field(..., alias="processID")
    process_name: str = Field(..., alias="processName")
    status: Optional[str] = None
    atom_id: Optional[str] = Field(None, alias="atomID")
    atom_name: Optional[str] = Field(None, alias="atomName")
    time_block: Optional[str] = Field(None, alias="timeBlock")

class ExecutionConnector(BaseModel):
    id: str
    execution_id: str = Field(..., alias="executionId")
    connector_type: Optional[str] = Field(None, alias="connectorType")
    action_type: Optional[str] = Field(None, alias="actionType")
    success_count: Optional[int] = Field(None, alias="successCount")
    error_count: Optional[int] = Field(None, alias="errorCount")

class GenericConnectorRecord(BaseModel):
    id: str
    execution_id: str = Field(..., alias="executionId")
    execution_connector_id: Optional[str] = Field(None, alias="executionConnectorId")
    status: Optional[str] = None
    error_message: Optional[str] = Field(None, alias="errorMessage")
    connector_type: Optional[str] = Field(None, alias="connectorType")
    connection_name: Optional[str] = Field(None, alias="connectionName")

class ExecutionCountAccount(BaseModel):
    account_id: str = Field(..., alias="accountId")
    atom_id: Optional[str] = Field(None, alias="atomId")
    date: Optional[str] = None
    failures: Optional[int] = None
    successes: Optional[int] = None

class ExecutionCountAccountGroup(ExecutionCountAccount):
    pass

class AuditLog(BaseModel):
    document_id: Optional[str] = Field(None, alias="documentId")
    action: Optional[str] = None
    date: Optional[str] = None
    level: Optional[str] = None
    message: Optional[str] = None

class Event(BaseModel):
    event_id: str = Field(..., alias="eventId")
    event_type: str = Field(..., alias="eventType")
    event_level: Optional[str] = Field(None, alias="eventLevel")
    execution_id: Optional[str] = Field(None, alias="executionId")
    atom_name: Optional[str] = Field(None, alias="atomName")
    process_name: Optional[str] = Field(None, alias="processName")
