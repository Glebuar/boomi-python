
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class As2Workload(Enum):
    """An enumeration representing different categories.

    :cvar GENERAL: "GENERAL"
    :vartype GENERAL: str
    :cvar LOWLATENCYDEBUG: "LOW_LATENCY_DEBUG"
    :vartype LOWLATENCYDEBUG: str
    """

    GENERAL = "GENERAL"
    LOWLATENCYDEBUG = "LOW_LATENCY_DEBUG"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, As2Workload._member_map_.values()))


class FlowControlParallelProcessTypeOverride(Enum):
    """An enumeration representing different categories.

    :cvar NONE: "NONE"
    :vartype NONE: str
    :cvar THREADS: "THREADS"
    :vartype THREADS: str
    :cvar PROCESSES: "PROCESSES"
    :vartype PROCESSES: str
    """

    NONE = "NONE"
    THREADS = "THREADS"
    PROCESSES = "PROCESSES"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                FlowControlParallelProcessTypeOverride._member_map_.values(),
            )
        )


class HttpWorkload(Enum):
    """An enumeration representing different categories.

    :cvar GENERAL: "GENERAL"
    :vartype GENERAL: str
    :cvar LOWLATENCYDEBUG: "LOW_LATENCY_DEBUG"
    :vartype LOWLATENCYDEBUG: str
    :cvar LOWLATENCY: "LOW_LATENCY"
    :vartype LOWLATENCY: str
    """

    GENERAL = "GENERAL"
    LOWLATENCYDEBUG = "LOW_LATENCY_DEBUG"
    LOWLATENCY = "LOW_LATENCY"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, HttpWorkload._member_map_.values()))


@JsonMap(
    {
        "account_disk_usage": "accountDiskUsage",
        "as2_workload": "as2Workload",
        "atom_input_size": "atomInputSize",
        "atom_output_overflow_size": "atomOutputOverflowSize",
        "atom_working_overflow_size": "atomWorkingOverflowSize",
        "cloud_account_execution_limit": "cloudAccountExecutionLimit",
        "cloud_account_execution_warning_offset": "cloudAccountExecutionWarningOffset",
        "container_id": "containerId",
        "download_runnerlogs": "downloadRunnerlogs",
        "enable_account_data_archiving": "enableAccountDataArchiving",
        "enable_atom_worker_warmup": "enableAtomWorkerWarmup",
        "flow_control_parallel_process_type_override": "flowControlParallelProcessTypeOverride",
        "http_request_rate": "httpRequestRate",
        "http_workload": "httpWorkload",
        "listener_max_concurrent_executions": "listenerMaxConcurrentExecutions",
        "max_connector_track_docs": "maxConnectorTrackDocs",
        "min_numberof_atom_workers": "minNumberofAtomWorkers",
        "numberof_atom_workers": "numberofAtomWorkers",
        "queue_incoming_message_rate_limit": "queueIncomingMessageRateLimit",
        "session_id": "sessionId",
        "status_code": "statusCode",
        "test_mode_max_doc_bytes": "testModeMaxDocBytes",
        "test_mode_max_docs": "testModeMaxDocs",
        "worker_elastic_scaling_threshold": "workerElasticScalingThreshold",
        "worker_max_execution_time": "workerMaxExecutionTime",
        "worker_max_general_execution_time": "workerMaxGeneralExecutionTime",
        "worker_max_queued_executions": "workerMaxQueuedExecutions",
        "worker_max_running_executions": "workerMaxRunningExecutions",
        "worker_queued_execution_timeout": "workerQueuedExecutionTimeout",
    }
)
class AccountCloudAttachmentProperties(BaseModel):
    """AccountCloudAttachmentProperties

    :param account_disk_usage: Represented in bytes, this property sets the size limit for an account that uses the private Runtime cloud., defaults to None
    :type account_disk_usage: int, optional
    :param as2_workload: Used to select the process run mode for AS2 listener processes.Accepted values:\<br /\>1. inherited — \(Default\) The setting is inherited from the Runtime cluster.\<br /\>2. general — The default process mode for all new processes.\<br /\>3. low\_latency\_debug — All AS2 listener processes use an execution worker.  \>**Note:** After you change this property value you must restart the Runtime cloud cluster or Runtime. \<br /\>\<br /\>If you select Low\_Latency\_Debug, Trading Partner components that use AS2 listeners also use that run mode., defaults to None
    :type as2_workload: As2Workload, optional
    :param atom_input_size: Represented in bytes. For Web Services Server listener processes, limits the input size of a web service request. If reaching this limit, it rejects the request.For Flow Services Server listener processes, limits the request size and response size. If reaching this limit, it rejects the request. If reaching this limit, it rejects the request with a 400 error code. If reaching the limit on a response, it rejects the request with a 503 error code., defaults to None
    :type atom_input_size: int, optional
    :param atom_output_overflow_size: Represented in bytes, if specified, this value must be a positive number. For Runtime worker processes, this property limits the number of bytes per output datastore maintained in memory before overflowing to disk., defaults to None
    :type atom_output_overflow_size: int, optional
    :param atom_working_overflow_size: Represented in bytes. For Runtime worker processes, this property limits the number of bytes per working datastore maintained in memory before overflowing to disk., defaults to None
    :type atom_working_overflow_size: int, optional
    :param cloud_account_execution_limit: The total number of concurrent runs allowed. If specified, this value must be a positive number. If this field does not contain a value, there is no limit. On a Cloud, for this limit to take effect, you must also set the **Cloud Partition Size** property. The **Cloud Partition Size** property is set in the **Properties** panel, under **Runtime Management**., defaults to None
    :type cloud_account_execution_limit: int, optional
    :param cloud_account_execution_warning_offset: If specified, this value must be a positive number. If this field does not contain a value, it does not generate a warning. This value is subtracted from the Account Concurrent Execution Limit to determine when the Runtime generates a warning that the account is close to exceeding its number of concurrent runs. For example, if this property is set to 5 and the Account Concurrent Execution Limit is set to 20, the Runtime generates a warning in the container log when the account exceeds 15 concurrent runs., defaults to None
    :type cloud_account_execution_warning_offset: int, optional
    :param container_id: container_id, defaults to None
    :type container_id: str, optional
    :param download_runnerlogs: Runtime cloud owners can set this property to give account users or specific tenants the ability to download Runtime Worker log files from **Runtime Management** and run artifacts from **Process Reporting**.Accepted values:\<br /\>1. Inherited \(false\) — The setting is inherited from the Runtime cloud cluster, and the feature is turned off.\<br /\>2. False — The feature is not enabled, and users cannot download Runtime Worker logs or run artifacts.\<br /\>3. True — \(default\) The feature is enabled. Users can download Runtime Worker logs and run artifacts.  \>**Note:** This property is turned on automatically for public Runtime clouds., defaults to None
    :type download_runnerlogs: bool, optional
    :param enable_account_data_archiving: Accepted values:\<br /\>1. inherited- \(plus the value of the setting being inherited. For example, inherited\(true\) or inherited\(false\)\) indicates that the property inherits what is set in the Runtime cloud cluster.\<br /\>2. true- If true or Inherited \(true\), the owner of the selected attached Runtime can enable [processed document archiving](https://help.boomi.com/bundle/integration/page/c-atm-Processed_document_archiving.html).\<br /\>3. false- indicates that the feature is not enabled., defaults to None
    :type enable_account_data_archiving: bool, optional
    :param enable_atom_worker_warmup: Accepted values:\<br /\>1. inherited- indicating that the property inherits what is set in the Runtime cloud cluster.\<br /\>2. true- indicating that when an execution worker is within 30 minutes of shutting down, the Cloud starts \(“warm-up”\) another Runtime worker to replace it.\<br /\>3. false- indicates that you did not enable the feature. You can use this feature if you provision your account with at least one Runtime worker. If you provision your account with more than one execution worker, and if there are multiple execution workers within 30 minutes of shutting down, then by default it replaces only one execution worker. However, if one of those execution workers has a load greater than “LOW”, then it is replaced even though there is another execution worker running. If you have set the **Minimum Execution Workers** property, then it replaces the appropriate number of execution workers so that you do not go below the minimum., defaults to None
    :type enable_atom_worker_warmup: bool, optional
    :param flow_control_parallel_process_type_override: Overrides the **Parallel Process Type** setting in **Flow Control** shapes at a global Runtime cloud or Attachment Quota level. You can set the property only if you are a private Runtime cloud owner.The default value is NONE., defaults to None
    :type flow_control_parallel_process_type_override: FlowControlParallelProcessTypeOverride, optional
    :param http_request_rate: Limits the number of Web Services Server requests per second. This limitation is per node in the Runtime cloud, and per Cloud or Runtime attachment \(*not* per account\).If it exceeds this value, callers receive a 503 error. After you change this property value you must restart the Runtime cloud cluster or Runtime.   \>**Note:** If you set an HTTP Request Rate value, API Management uses this limit before the values specified in the API Contract for Rate Limit or Quota Limit., defaults to None
    :type http_request_rate: int, optional
    :param http_workload: Accepted values:\<br /\>1. inherited- \(plus the value of the setting being inherited. For example, inherited\(true\) or inherited\(false\)\) indicating that the property inherits what is set in the Runtime cloud cluster.\<br /\>2. general- The default process mode for all new processes. General mode processes do not use an execution worker, but Low\_Latency mode processes do use one.\<br /\>3. low\_latency- All Web Services Server processes use an execution worker and run in Low\_Latency mode.\<br /\>4. low\_latency\_debug- All Web Services Server processes use an execution worker. Processes configured in Generalmode run in Low\_Latency\_Debug mode., defaults to None
    :type http_workload: HttpWorkload, optional
    :param listener_max_concurrent_executions: The maximum number of concurrent runs allowed per listener — that is, the maximum listener pool size., defaults to None
    :type listener_max_concurrent_executions: int, optional
    :param max_connector_track_docs: You must set a positive integer less than or equal to 10,000. For example, in a process run, the maximum number of connector tracking generated documents for a single connector step.After reaching this limit, it does not report more tracking documents to the platform for that step in that run., defaults to None
    :type max_connector_track_docs: int, optional
    :param min_numberof_atom_workers: The minimum number of execution workers that run continuously in the Cloud.If this property is set to a number greater than zero, then a few minutes after the Cloud starts and stabilizes, this number of execution workers begin to run. Their starting is not dependent upon receiving incoming process run requests. This behavior is like having multiple runners at the starting line of a race. All runners are ready and start to run as soon as the starter pistol is fired. This property works in conjunction with the **Execution Worker Warmup Enabled** property. If you set **Minimum Execution Workers** \\> 0, then it enables Execution Worker Warmup behavior. As your minimum number of execution workers reach the end of their life span, they are replaced with new execution workers. If the load on active execution workers drop, the Runtime cloud reduces the number of execution workers to the value you set for this property.   \>**Note:** Setting this property to a number greater than the number of provisioned execution workers in your account does not cause additional execution workers to run. If you would like to have additional execution workers provisioned in your account, contact the Support team., defaults to None
    :type min_numberof_atom_workers: int, optional
    :param numberof_atom_workers: Allocated number of execution workers., defaults to None
    :type numberof_atom_workers: int, optional
    :param queue_incoming_message_rate_limit: The maximum number of requests the attachment is allowed to send to the Shared Queue Server per minute. The limit is only enforced if the Incoming Message Rate Limit is set in the underlying cloud Queue Shared Server. If a value is not set or is less than 1, the Shared Queue Server limit is used. The message is rejected if the limit is exceeded and should be retried from within the integration process. The limit is enforced per cloud node., defaults to None
    :type queue_incoming_message_rate_limit: int, optional
    :param session_id: session_id, defaults to None
    :type session_id: str, optional
    :param status_code: status_code, defaults to None
    :type status_code: int, optional
    :param test_mode_max_doc_bytes: Represented in bytes, the maximum aggregate data size across the run of a process in test mode. A negative value means there is no maximum.This field is present only if you enable the enhanced test mode feature in the account. If you want to enable this feature, contact your sales representative., defaults to None
    :type test_mode_max_doc_bytes: int, optional
    :param test_mode_max_docs: The maximum number of files \(documents\) per inbound connector shape during the run of a process in test mode. A negative value means there is no maximum.This field is present only if you enable enhanced test mode feature in the account., defaults to None
    :type test_mode_max_docs: int, optional
    :param worker_elastic_scaling_threshold: worker_elastic_scaling_threshold, defaults to None
    :type worker_elastic_scaling_threshold: int, optional
    :param worker_max_execution_time: Maximum run time in milliseconds for Execution worker processes. For example, an accepted value is 30000. After this amount of time passes, a 522 HTTP status code message is returned to the client saying that the process exceeds the time limit and then cancels the process run. After you change this property value, you must restart the Runtime cloud cluster or Runtime., defaults to None
    :type worker_max_execution_time: int, optional
    :param worker_max_general_execution_time: Maximum run time in milliseconds for Execution worker processes that use Low\_Latency\_Debug mode. For example, an accepted value is 60000. After you change this property value, you must restart the Runtime cloud cluster or Runtime., defaults to None
    :type worker_max_general_execution_time: int, optional
    :param worker_max_queued_executions: Maximum number of extra processes that can queue in a single Execution worker, when the maximum number of processes is running. If specified, this value must be a positive number. After you change this property value you must restart the Runtime cloud cluster or Runtime., defaults to None
    :type worker_max_queued_executions: int, optional
    :param worker_max_running_executions: The maximum number of simultaneous processes that can run in a single Execution worker.After you change this property value, you must restart the Runtime cloud cluster or Runtime., defaults to None
    :type worker_max_running_executions: int, optional
    :param worker_queued_execution_timeout: Maximum time that a job in the queue can wait to run. After this amount of time, the job fails with a time-out exception.For example, an accepted value is 0:10:00. After you change this property value you must restart the Runtime cloud cluster or Runtime., defaults to None
    :type worker_queued_execution_timeout: int, optional
    """

    def __init__(
        self,
        account_disk_usage: int = SENTINEL,
        as2_workload: As2Workload = SENTINEL,
        atom_input_size: int = SENTINEL,
        atom_output_overflow_size: int = SENTINEL,
        atom_working_overflow_size: int = SENTINEL,
        cloud_account_execution_limit: int = SENTINEL,
        cloud_account_execution_warning_offset: int = SENTINEL,
        container_id: str = SENTINEL,
        download_runnerlogs: bool = SENTINEL,
        enable_account_data_archiving: bool = SENTINEL,
        enable_atom_worker_warmup: bool = SENTINEL,
        flow_control_parallel_process_type_override: FlowControlParallelProcessTypeOverride = SENTINEL,
        http_request_rate: int = SENTINEL,
        http_workload: HttpWorkload = SENTINEL,
        listener_max_concurrent_executions: int = SENTINEL,
        max_connector_track_docs: int = SENTINEL,
        min_numberof_atom_workers: int = SENTINEL,
        numberof_atom_workers: int = SENTINEL,
        queue_incoming_message_rate_limit: int = SENTINEL,
        session_id: str = SENTINEL,
        status_code: int = SENTINEL,
        test_mode_max_doc_bytes: int = SENTINEL,
        test_mode_max_docs: int = SENTINEL,
        worker_elastic_scaling_threshold: int = SENTINEL,
        worker_max_execution_time: int = SENTINEL,
        worker_max_general_execution_time: int = SENTINEL,
        worker_max_queued_executions: int = SENTINEL,
        worker_max_running_executions: int = SENTINEL,
        worker_queued_execution_timeout: int = SENTINEL,
        **kwargs
    ):
        """AccountCloudAttachmentProperties

        :param account_disk_usage: Represented in bytes, this property sets the size limit for an account that uses the private Runtime cloud., defaults to None
        :type account_disk_usage: int, optional
        :param as2_workload: Used to select the process run mode for AS2 listener processes.Accepted values:\<br /\>1. inherited — \(Default\) The setting is inherited from the Runtime cluster.\<br /\>2. general — The default process mode for all new processes.\<br /\>3. low\_latency\_debug — All AS2 listener processes use an execution worker.  \>**Note:** After you change this property value you must restart the Runtime cloud cluster or Runtime. \<br /\>\<br /\>If you select Low\_Latency\_Debug, Trading Partner components that use AS2 listeners also use that run mode., defaults to None
        :type as2_workload: As2Workload, optional
        :param atom_input_size: Represented in bytes. For Web Services Server listener processes, limits the input size of a web service request. If reaching this limit, it rejects the request.For Flow Services Server listener processes, limits the request size and response size. If reaching this limit, it rejects the request. If reaching this limit, it rejects the request with a 400 error code. If reaching the limit on a response, it rejects the request with a 503 error code., defaults to None
        :type atom_input_size: int, optional
        :param atom_output_overflow_size: Represented in bytes, if specified, this value must be a positive number. For Runtime worker processes, this property limits the number of bytes per output datastore maintained in memory before overflowing to disk., defaults to None
        :type atom_output_overflow_size: int, optional
        :param atom_working_overflow_size: Represented in bytes. For Runtime worker processes, this property limits the number of bytes per working datastore maintained in memory before overflowing to disk., defaults to None
        :type atom_working_overflow_size: int, optional
        :param cloud_account_execution_limit: The total number of concurrent runs allowed. If specified, this value must be a positive number. If this field does not contain a value, there is no limit. On a Cloud, for this limit to take effect, you must also set the **Cloud Partition Size** property. The **Cloud Partition Size** property is set in the **Properties** panel, under **Runtime Management**., defaults to None
        :type cloud_account_execution_limit: int, optional
        :param cloud_account_execution_warning_offset: If specified, this value must be a positive number. If this field does not contain a value, it does not generate a warning. This value is subtracted from the Account Concurrent Execution Limit to determine when the Runtime generates a warning that the account is close to exceeding its number of concurrent runs. For example, if this property is set to 5 and the Account Concurrent Execution Limit is set to 20, the Runtime generates a warning in the container log when the account exceeds 15 concurrent runs., defaults to None
        :type cloud_account_execution_warning_offset: int, optional
        :param container_id: container_id, defaults to None
        :type container_id: str, optional
        :param download_runnerlogs: Runtime cloud owners can set this property to give account users or specific tenants the ability to download Runtime Worker log files from **Runtime Management** and run artifacts from **Process Reporting**.Accepted values:\<br /\>1. Inherited \(false\) — The setting is inherited from the Runtime cloud cluster, and the feature is turned off.\<br /\>2. False — The feature is not enabled, and users cannot download Runtime Worker logs or run artifacts.\<br /\>3. True — \(default\) The feature is enabled. Users can download Runtime Worker logs and run artifacts.  \>**Note:** This property is turned on automatically for public Runtime clouds., defaults to None
        :type download_runnerlogs: bool, optional
        :param enable_account_data_archiving: Accepted values:\<br /\>1. inherited- \(plus the value of the setting being inherited. For example, inherited\(true\) or inherited\(false\)\) indicates that the property inherits what is set in the Runtime cloud cluster.\<br /\>2. true- If true or Inherited \(true\), the owner of the selected attached Runtime can enable [processed document archiving](https://help.boomi.com/bundle/integration/page/c-atm-Processed_document_archiving.html).\<br /\>3. false- indicates that the feature is not enabled., defaults to None
        :type enable_account_data_archiving: bool, optional
        :param enable_atom_worker_warmup: Accepted values:\<br /\>1. inherited- indicating that the property inherits what is set in the Runtime cloud cluster.\<br /\>2. true- indicating that when an execution worker is within 30 minutes of shutting down, the Cloud starts \(“warm-up”\) another Runtime worker to replace it.\<br /\>3. false- indicates that you did not enable the feature. You can use this feature if you provision your account with at least one Runtime worker. If you provision your account with more than one execution worker, and if there are multiple execution workers within 30 minutes of shutting down, then by default it replaces only one execution worker. However, if one of those execution workers has a load greater than “LOW”, then it is replaced even though there is another execution worker running. If you have set the **Minimum Execution Workers** property, then it replaces the appropriate number of execution workers so that you do not go below the minimum., defaults to None
        :type enable_atom_worker_warmup: bool, optional
        :param flow_control_parallel_process_type_override: Overrides the **Parallel Process Type** setting in **Flow Control** shapes at a global Runtime cloud or Attachment Quota level. You can set the property only if you are a private Runtime cloud owner.The default value is NONE., defaults to None
        :type flow_control_parallel_process_type_override: FlowControlParallelProcessTypeOverride, optional
        :param http_request_rate: Limits the number of Web Services Server requests per second. This limitation is per node in the Runtime cloud, and per Cloud or Runtime attachment \(*not* per account\).If it exceeds this value, callers receive a 503 error. After you change this property value you must restart the Runtime cloud cluster or Runtime.   \>**Note:** If you set an HTTP Request Rate value, API Management uses this limit before the values specified in the API Contract for Rate Limit or Quota Limit., defaults to None
        :type http_request_rate: int, optional
        :param http_workload: Accepted values:\<br /\>1. inherited- \(plus the value of the setting being inherited. For example, inherited\(true\) or inherited\(false\)\) indicating that the property inherits what is set in the Runtime cloud cluster.\<br /\>2. general- The default process mode for all new processes. General mode processes do not use an execution worker, but Low\_Latency mode processes do use one.\<br /\>3. low\_latency- All Web Services Server processes use an execution worker and run in Low\_Latency mode.\<br /\>4. low\_latency\_debug- All Web Services Server processes use an execution worker. Processes configured in Generalmode run in Low\_Latency\_Debug mode., defaults to None
        :type http_workload: HttpWorkload, optional
        :param listener_max_concurrent_executions: The maximum number of concurrent runs allowed per listener — that is, the maximum listener pool size., defaults to None
        :type listener_max_concurrent_executions: int, optional
        :param max_connector_track_docs: You must set a positive integer less than or equal to 10,000. For example, in a process run, the maximum number of connector tracking generated documents for a single connector step.After reaching this limit, it does not report more tracking documents to the platform for that step in that run., defaults to None
        :type max_connector_track_docs: int, optional
        :param min_numberof_atom_workers: The minimum number of execution workers that run continuously in the Cloud.If this property is set to a number greater than zero, then a few minutes after the Cloud starts and stabilizes, this number of execution workers begin to run. Their starting is not dependent upon receiving incoming process run requests. This behavior is like having multiple runners at the starting line of a race. All runners are ready and start to run as soon as the starter pistol is fired. This property works in conjunction with the **Execution Worker Warmup Enabled** property. If you set **Minimum Execution Workers** \\> 0, then it enables Execution Worker Warmup behavior. As your minimum number of execution workers reach the end of their life span, they are replaced with new execution workers. If the load on active execution workers drop, the Runtime cloud reduces the number of execution workers to the value you set for this property.   \>**Note:** Setting this property to a number greater than the number of provisioned execution workers in your account does not cause additional execution workers to run. If you would like to have additional execution workers provisioned in your account, contact the Support team., defaults to None
        :type min_numberof_atom_workers: int, optional
        :param numberof_atom_workers: Allocated number of execution workers., defaults to None
        :type numberof_atom_workers: int, optional
        :param queue_incoming_message_rate_limit: The maximum number of requests the attachment is allowed to send to the Shared Queue Server per minute. The limit is only enforced if the Incoming Message Rate Limit is set in the underlying cloud Queue Shared Server. If a value is not set or is less than 1, the Shared Queue Server limit is used. The message is rejected if the limit is exceeded and should be retried from within the integration process. The limit is enforced per cloud node., defaults to None
        :type queue_incoming_message_rate_limit: int, optional
        :param session_id: session_id, defaults to None
        :type session_id: str, optional
        :param status_code: status_code, defaults to None
        :type status_code: int, optional
        :param test_mode_max_doc_bytes: Represented in bytes, the maximum aggregate data size across the run of a process in test mode. A negative value means there is no maximum.This field is present only if you enable the enhanced test mode feature in the account. If you want to enable this feature, contact your sales representative., defaults to None
        :type test_mode_max_doc_bytes: int, optional
        :param test_mode_max_docs: The maximum number of files \(documents\) per inbound connector shape during the run of a process in test mode. A negative value means there is no maximum.This field is present only if you enable enhanced test mode feature in the account., defaults to None
        :type test_mode_max_docs: int, optional
        :param worker_elastic_scaling_threshold: worker_elastic_scaling_threshold, defaults to None
        :type worker_elastic_scaling_threshold: int, optional
        :param worker_max_execution_time: Maximum run time in milliseconds for Execution worker processes. For example, an accepted value is 30000. After this amount of time passes, a 522 HTTP status code message is returned to the client saying that the process exceeds the time limit and then cancels the process run. After you change this property value, you must restart the Runtime cloud cluster or Runtime., defaults to None
        :type worker_max_execution_time: int, optional
        :param worker_max_general_execution_time: Maximum run time in milliseconds for Execution worker processes that use Low\_Latency\_Debug mode. For example, an accepted value is 60000. After you change this property value, you must restart the Runtime cloud cluster or Runtime., defaults to None
        :type worker_max_general_execution_time: int, optional
        :param worker_max_queued_executions: Maximum number of extra processes that can queue in a single Execution worker, when the maximum number of processes is running. If specified, this value must be a positive number. After you change this property value you must restart the Runtime cloud cluster or Runtime., defaults to None
        :type worker_max_queued_executions: int, optional
        :param worker_max_running_executions: The maximum number of simultaneous processes that can run in a single Execution worker.After you change this property value, you must restart the Runtime cloud cluster or Runtime., defaults to None
        :type worker_max_running_executions: int, optional
        :param worker_queued_execution_timeout: Maximum time that a job in the queue can wait to run. After this amount of time, the job fails with a time-out exception.For example, an accepted value is 0:10:00. After you change this property value you must restart the Runtime cloud cluster or Runtime., defaults to None
        :type worker_queued_execution_timeout: int, optional
        """
        if account_disk_usage is not SENTINEL:
            self.account_disk_usage = account_disk_usage
        if as2_workload is not SENTINEL:
            self.as2_workload = self._enum_matching(
                as2_workload, As2Workload.list(), "as2_workload"
            )
        if atom_input_size is not SENTINEL:
            self.atom_input_size = atom_input_size
        if atom_output_overflow_size is not SENTINEL:
            self.atom_output_overflow_size = atom_output_overflow_size
        if atom_working_overflow_size is not SENTINEL:
            self.atom_working_overflow_size = atom_working_overflow_size
        if cloud_account_execution_limit is not SENTINEL:
            self.cloud_account_execution_limit = cloud_account_execution_limit
        if cloud_account_execution_warning_offset is not SENTINEL:
            self.cloud_account_execution_warning_offset = (
                cloud_account_execution_warning_offset
            )
        if container_id is not SENTINEL:
            self.container_id = container_id
        if download_runnerlogs is not SENTINEL:
            self.download_runnerlogs = download_runnerlogs
        if enable_account_data_archiving is not SENTINEL:
            self.enable_account_data_archiving = enable_account_data_archiving
        if enable_atom_worker_warmup is not SENTINEL:
            self.enable_atom_worker_warmup = enable_atom_worker_warmup
        if flow_control_parallel_process_type_override is not SENTINEL:
            self.flow_control_parallel_process_type_override = self._enum_matching(
                flow_control_parallel_process_type_override,
                FlowControlParallelProcessTypeOverride.list(),
                "flow_control_parallel_process_type_override",
            )
        if http_request_rate is not SENTINEL:
            self.http_request_rate = http_request_rate
        if http_workload is not SENTINEL:
            self.http_workload = self._enum_matching(
                http_workload, HttpWorkload.list(), "http_workload"
            )
        if listener_max_concurrent_executions is not SENTINEL:
            self.listener_max_concurrent_executions = listener_max_concurrent_executions
        if max_connector_track_docs is not SENTINEL:
            self.max_connector_track_docs = max_connector_track_docs
        if min_numberof_atom_workers is not SENTINEL:
            self.min_numberof_atom_workers = min_numberof_atom_workers
        if numberof_atom_workers is not SENTINEL:
            self.numberof_atom_workers = numberof_atom_workers
        if queue_incoming_message_rate_limit is not SENTINEL:
            self.queue_incoming_message_rate_limit = queue_incoming_message_rate_limit
        if session_id is not SENTINEL:
            self.session_id = session_id
        if status_code is not SENTINEL:
            self.status_code = status_code
        if test_mode_max_doc_bytes is not SENTINEL:
            self.test_mode_max_doc_bytes = test_mode_max_doc_bytes
        if test_mode_max_docs is not SENTINEL:
            self.test_mode_max_docs = test_mode_max_docs
        if worker_elastic_scaling_threshold is not SENTINEL:
            self.worker_elastic_scaling_threshold = worker_elastic_scaling_threshold
        if worker_max_execution_time is not SENTINEL:
            self.worker_max_execution_time = worker_max_execution_time
        if worker_max_general_execution_time is not SENTINEL:
            self.worker_max_general_execution_time = worker_max_general_execution_time
        if worker_max_queued_executions is not SENTINEL:
            self.worker_max_queued_executions = worker_max_queued_executions
        if worker_max_running_executions is not SENTINEL:
            self.worker_max_running_executions = worker_max_running_executions
        if worker_queued_execution_timeout is not SENTINEL:
            self.worker_queued_execution_timeout = worker_queued_execution_timeout
        self._kwargs = kwargs
