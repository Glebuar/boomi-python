
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class ExecutionType(Enum):
    """An enumeration representing different categories.

    :cvar EXECMANUAL: "exec_manual"
    :vartype EXECMANUAL: str
    :cvar EXECSCHED: "exec_sched"
    :vartype EXECSCHED: str
    :cvar EXECLISTENER: "exec_listener"
    :vartype EXECLISTENER: str
    :cvar EXECLISTENERBRIDGE: "exec_listener_bridge"
    :vartype EXECLISTENERBRIDGE: str
    :cvar EXECREMOTE: "exec_remote"
    :vartype EXECREMOTE: str
    :cvar RETRYMANUAL: "retry_manual"
    :vartype RETRYMANUAL: str
    :cvar RETRYSCHED: "retry_sched"
    :vartype RETRYSCHED: str
    :cvar FIBER: "fiber"
    :vartype FIBER: str
    :cvar SUBPROCESS: "sub_process"
    :vartype SUBPROCESS: str
    :cvar TESTMANUAL: "test_manual"
    :vartype TESTMANUAL: str
    :cvar TESTSUBPROCESS: "test_sub_process"
    :vartype TESTSUBPROCESS: str
    :cvar UNKNOWN: "unknown"
    :vartype UNKNOWN: str
    """

    EXECMANUAL = "exec_manual"
    EXECSCHED = "exec_sched"
    EXECLISTENER = "exec_listener"
    EXECLISTENERBRIDGE = "exec_listener_bridge"
    EXECREMOTE = "exec_remote"
    RETRYMANUAL = "retry_manual"
    RETRYSCHED = "retry_sched"
    FIBER = "fiber"
    SUBPROCESS = "sub_process"
    TESTMANUAL = "test_manual"
    TESTSUBPROCESS = "test_sub_process"
    UNKNOWN = "unknown"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, ExecutionType._member_map_.values()))


@JsonMap(
    {
        "atom_id": "atomId",
        "atom_name": "atomName",
        "execution_duration": "executionDuration",
        "execution_id": "executionId",
        "execution_time": "executionTime",
        "execution_type": "executionType",
        "inbound_document_count": "inboundDocumentCount",
        "inbound_document_size": "inboundDocumentSize",
        "inbound_error_document_count": "inboundErrorDocumentCount",
        "launcher_id": "launcherID",
        "node_id": "nodeId",
        "original_execution_id": "originalExecutionId",
        "outbound_document_count": "outboundDocumentCount",
        "outbound_document_size": "outboundDocumentSize",
        "parent_execution_id": "parentExecutionId",
        "process_id": "processId",
        "process_name": "processName",
        "recorded_date": "recordedDate",
        "report_key": "reportKey",
        "top_level_execution_id": "topLevelExecutionId",
    }
)
class ExecutionRecord(BaseModel):
    """ExecutionRecord

    :param account: The ID of the account in which you ran this execution.
    :type account: str
    :param atom_id: The ID of the Runtime the on which the process ran.
    :type atom_id: str
    :param atom_name: The name of the Runtime on which the process ran.
    :type atom_name: str
    :param execution_duration: The number of milliseconds it took to run the process., defaults to None
    :type execution_duration: int, optional
    :param execution_id: The ID of the execution.
    :type execution_id: str
    :param execution_time: The start date and time this run.
    :type execution_time: str
    :param execution_type: Indicates how initiation of the process run occurred. Possible values are:\<br /\>-   *exec*\_*listener* \(run initiated by a listener request\)\<br /\>- *exec*\_*manual* \(manual run\)\<br /\>- *exec*\_*sched* \(scheduled run\)\<br /\>- *retry*\_*manual* \(manual retry\)\<br /\>- *retry*\_*sched* \(scheduled retry\)\<br /\>- *sub*\_*process* \(subprocess call\)\<br /\>- *test*\_*manual* \(test mode run\)
    :type execution_type: ExecutionType
    :param inbound_document_count: The number of processed inbound documents., defaults to None
    :type inbound_document_count: int, optional
    :param inbound_document_size: The aggregate size in bytes of the processed inbound documents., defaults to None
    :type inbound_document_size: int, optional
    :param inbound_error_document_count: The number of processed inbound documents with errors., defaults to None
    :type inbound_error_document_count: int, optional
    :param launcher_id: The API Service component that kicks off the run.\<br /\>\<br /\> **Note:** The Runtime must have the **API Type** set to **Advanced** on the **Shared Web Server** tab of **Runtime Management** to specify the launcherID.
    :type launcher_id: str
    :param message: Any error message returned from the run.
    :type message: str
    :param node_id: The ID of the Molecule node in which the run occurred for a process run in a Runtime cluster or Runtime cloud. For a run occurring in a Runtime, this field is omitted.
    :type node_id: str
    :param original_execution_id: The original execution ID, if this execution is a retry.
    :type original_execution_id: str
    :param outbound_document_count: The number of processed outbound documents., defaults to None
    :type outbound_document_count: int, optional
    :param outbound_document_size: The aggregate size in bytes of the processed outbound documents., defaults to None
    :type outbound_document_size: int, optional
    :param parent_execution_id: The ID of the run of the parent process, if this run and the parent process’ run were both subprocesses.
    :type parent_execution_id: str
    :param process_id: The ID of the run process.
    :type process_id: str
    :param process_name: The name of the run process.
    :type process_name: str
    :param recorded_date: The end time when the process execution completes.
    :type recorded_date: str
    :param report_key: The web service user that authenticated to make the run request.\<br /\>\<br /\>**Note:** For Runtimes with an Authentication Type of External Provider, the reportKey is the API Key. Otherwise, it is the specified user name.
    :type report_key: str
    :param status: The status of the run. Possible values are:\<br /\>- *ABORTED*\<br /\>- *COMPLETE*\<br /\>- *COMPLETE*\_*WARN*\<br /\>- *DISCARDED*\<br /\>- *ERROR*\<br /\>- *INPROCESS*\<br /\>- *STARTED*
    :type status: str
    :param top_level_execution_id: The ID of the run of the top-level process, if this run is a subprocess.
    :type top_level_execution_id: str
    """

    def __init__(
        self,
        account: str,
        atom_id: str,
        atom_name: str,
        execution_id: str,
        execution_time: str,
        execution_type: ExecutionType,
        launcher_id: str,
        message: str,
        node_id: str,
        original_execution_id: str,
        parent_execution_id: str,
        process_id: str,
        process_name: str,
        recorded_date: str,
        report_key: str,
        status: str,
        top_level_execution_id: str,
        execution_duration: int = SENTINEL,
        inbound_document_count: int = SENTINEL,
        inbound_document_size: int = SENTINEL,
        inbound_error_document_count: int = SENTINEL,
        outbound_document_count: int = SENTINEL,
        outbound_document_size: int = SENTINEL,
        **kwargs
    ):
        """ExecutionRecord

        :param account: The ID of the account in which you ran this execution.
        :type account: str
        :param atom_id: The ID of the Runtime the on which the process ran.
        :type atom_id: str
        :param atom_name: The name of the Runtime on which the process ran.
        :type atom_name: str
        :param execution_duration: The number of milliseconds it took to run the process., defaults to None
        :type execution_duration: int, optional
        :param execution_id: The ID of the execution.
        :type execution_id: str
        :param execution_time: The start date and time this run.
        :type execution_time: str
        :param execution_type: Indicates how initiation of the process run occurred. Possible values are:\<br /\>-   *exec*\_*listener* \(run initiated by a listener request\)\<br /\>- *exec*\_*manual* \(manual run\)\<br /\>- *exec*\_*sched* \(scheduled run\)\<br /\>- *retry*\_*manual* \(manual retry\)\<br /\>- *retry*\_*sched* \(scheduled retry\)\<br /\>- *sub*\_*process* \(subprocess call\)\<br /\>- *test*\_*manual* \(test mode run\)
        :type execution_type: ExecutionType
        :param inbound_document_count: The number of processed inbound documents., defaults to None
        :type inbound_document_count: int, optional
        :param inbound_document_size: The aggregate size in bytes of the processed inbound documents., defaults to None
        :type inbound_document_size: int, optional
        :param inbound_error_document_count: The number of processed inbound documents with errors., defaults to None
        :type inbound_error_document_count: int, optional
        :param launcher_id: The API Service component that kicks off the run.\<br /\>\<br /\> **Note:** The Runtime must have the **API Type** set to **Advanced** on the **Shared Web Server** tab of **Runtime Management** to specify the launcherID.
        :type launcher_id: str
        :param message: Any error message returned from the run.
        :type message: str
        :param node_id: The ID of the Molecule node in which the run occurred for a process run in a Runtime cluster or Runtime cloud. For a run occurring in a Runtime, this field is omitted.
        :type node_id: str
        :param original_execution_id: The original execution ID, if this execution is a retry.
        :type original_execution_id: str
        :param outbound_document_count: The number of processed outbound documents., defaults to None
        :type outbound_document_count: int, optional
        :param outbound_document_size: The aggregate size in bytes of the processed outbound documents., defaults to None
        :type outbound_document_size: int, optional
        :param parent_execution_id: The ID of the run of the parent process, if this run and the parent process’ run were both subprocesses.
        :type parent_execution_id: str
        :param process_id: The ID of the run process.
        :type process_id: str
        :param process_name: The name of the run process.
        :type process_name: str
        :param recorded_date: The end time when the process execution completes.
        :type recorded_date: str
        :param report_key: The web service user that authenticated to make the run request.\<br /\>\<br /\>**Note:** For Runtimes with an Authentication Type of External Provider, the reportKey is the API Key. Otherwise, it is the specified user name.
        :type report_key: str
        :param status: The status of the run. Possible values are:\<br /\>- *ABORTED*\<br /\>- *COMPLETE*\<br /\>- *COMPLETE*\_*WARN*\<br /\>- *DISCARDED*\<br /\>- *ERROR*\<br /\>- *INPROCESS*\<br /\>- *STARTED*
        :type status: str
        :param top_level_execution_id: The ID of the run of the top-level process, if this run is a subprocess.
        :type top_level_execution_id: str
        """
        self.account = account
        self.atom_id = atom_id
        self.atom_name = atom_name
        if execution_duration is not SENTINEL:
            self.execution_duration = execution_duration
        self.execution_id = execution_id
        self.execution_time = execution_time
        self.execution_type = self._enum_matching(
            execution_type, ExecutionType.list(), "execution_type"
        )
        if inbound_document_count is not SENTINEL:
            self.inbound_document_count = inbound_document_count
        if inbound_document_size is not SENTINEL:
            self.inbound_document_size = inbound_document_size
        if inbound_error_document_count is not SENTINEL:
            self.inbound_error_document_count = inbound_error_document_count
        self.launcher_id = launcher_id
        self.message = message
        self.node_id = node_id
        self.original_execution_id = original_execution_id
        if outbound_document_count is not SENTINEL:
            self.outbound_document_count = outbound_document_count
        if outbound_document_size is not SENTINEL:
            self.outbound_document_size = outbound_document_size
        self.parent_execution_id = parent_execution_id
        self.process_id = process_id
        self.process_name = process_name
        self.recorded_date = recorded_date
        self.report_key = report_key
        self.status = status
        self.top_level_execution_id = top_level_execution_id
        self._kwargs = kwargs
