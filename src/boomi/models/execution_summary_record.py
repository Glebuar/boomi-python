
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap(
    {
        "account_id": "accountID",
        "atom_id": "atomID",
        "atom_name": "atomName",
        "elapsed_time": "elapsedTime",
        "elapsed_var_sum": "elapsedVarSum",
        "execution_count": "executionCount",
        "inbound_doc_count": "inboundDocCount",
        "inbound_doc_size": "inboundDocSize",
        "launch_elapsed_time": "launchElapsedTime",
        "launcher_id": "launcherID",
        "max_elapsed_time": "maxElapsedTime",
        "outbound_doc_count": "outboundDocCount",
        "outbound_doc_size": "outboundDocSize",
        "process_id": "processID",
        "process_name": "processName",
        "report_key": "reportKey",
        "return_doc_count": "returnDocCount",
        "return_doc_size": "returnDocSize",
        "time_block": "timeBlock",
    }
)
class ExecutionSummaryRecord(BaseModel):
    """ExecutionSummaryRecord

    :param account_id: The account under which the processes ran., defaults to None
    :type account_id: str, optional
    :param atom_id: The component ID of the Runtime on which the processes ran., defaults to None
    :type atom_id: str, optional
    :param atom_name: The name of the Runtime on which the runs occurred., defaults to None
    :type atom_name: str, optional
    :param elapsed_time: The aggregate elapsed processing time, in milliseconds, of the runs that occurred., defaults to None
    :type elapsed_time: int, optional
    :param elapsed_var_sum: A composite value enabling computation of the standard deviation of elapsed run time for the processes that occurred using the [parallel algorithm](http://en.wikipedia.org/wiki/Algorithms_for_calculating_variance#Parallel_algorithm)., defaults to None
    :type elapsed_var_sum: float, optional
    :param execution_count: The number of runs that occurred., defaults to None
    :type execution_count: int, optional
    :param inbound_doc_count: The aggregate number of processed inbound documents for the runs that occurred., defaults to None
    :type inbound_doc_count: int, optional
    :param inbound_doc_size: The aggregate size, in bytes, of the processed inbound documents for the runs that occurred., defaults to None
    :type inbound_doc_size: int, optional
    :param launch_elapsed_time: The aggregate elapsed wait time, in milliseconds, before the start of processing for the runs that occurred., defaults to None
    :type launch_elapsed_time: int, optional
    :param launcher_id: The API Service component that kicks off the run.\<br /\> **Note:** The Runtime must have the **API Type** set to **Advanced** on the **Shared Web Server** tab of **Runtime Management** to specify launcherId., defaults to None
    :type launcher_id: str, optional
    :param max_elapsed_time: The time, in milliseconds, it took for the most time-consuming run that occurred., defaults to None
    :type max_elapsed_time: int, optional
    :param outbound_doc_count: The aggregate number of processed outbound documents for the runs that occurred., defaults to None
    :type outbound_doc_count: int, optional
    :param outbound_doc_size: The aggregate size, in bytes, of the processed outbound documents for the runs that occurred., defaults to None
    :type outbound_doc_size: int, optional
    :param process_id: The component ID of the processes that ran., defaults to None
    :type process_id: str, optional
    :param process_name: The name of the process that was run., defaults to None
    :type process_name: str, optional
    :param report_key: The web service user that authenticated to make the run request. \<br /\>**Note:** For Runtimes with an Authentication Type of External Provider, the reportKey is the API Key. Otherwise, it is the specified user name., defaults to None
    :type report_key: str, optional
    :param return_doc_count: The aggregate number of resulting documents for the runs that occurred., defaults to None
    :type return_doc_count: int, optional
    :param return_doc_size: The aggregate size, in bytes, of resulting documents for the runs that occurred., defaults to None
    :type return_doc_size: int, optional
    :param status: The status of the runs. Allowed values include COMPLETE, COMPLETE\_WARN, ERROR., defaults to None
    :type status: str, optional
    :param time_block: The start time of the represented time block., defaults to None
    :type time_block: str, optional
    """

    def __init__(
        self,
        account_id: str = SENTINEL,
        atom_id: str = SENTINEL,
        atom_name: str = SENTINEL,
        elapsed_time: int = SENTINEL,
        elapsed_var_sum: float = SENTINEL,
        execution_count: int = SENTINEL,
        inbound_doc_count: int = SENTINEL,
        inbound_doc_size: int = SENTINEL,
        launch_elapsed_time: int = SENTINEL,
        launcher_id: str = SENTINEL,
        max_elapsed_time: int = SENTINEL,
        outbound_doc_count: int = SENTINEL,
        outbound_doc_size: int = SENTINEL,
        process_id: str = SENTINEL,
        process_name: str = SENTINEL,
        report_key: str = SENTINEL,
        return_doc_count: int = SENTINEL,
        return_doc_size: int = SENTINEL,
        status: str = SENTINEL,
        time_block: str = SENTINEL,
        **kwargs
    ):
        """ExecutionSummaryRecord

        :param account_id: The account under which the processes ran., defaults to None
        :type account_id: str, optional
        :param atom_id: The component ID of the Runtime on which the processes ran., defaults to None
        :type atom_id: str, optional
        :param atom_name: The name of the Runtime on which the runs occurred., defaults to None
        :type atom_name: str, optional
        :param elapsed_time: The aggregate elapsed processing time, in milliseconds, of the runs that occurred., defaults to None
        :type elapsed_time: int, optional
        :param elapsed_var_sum: A composite value enabling computation of the standard deviation of elapsed run time for the processes that occurred using the [parallel algorithm](http://en.wikipedia.org/wiki/Algorithms_for_calculating_variance#Parallel_algorithm)., defaults to None
        :type elapsed_var_sum: float, optional
        :param execution_count: The number of runs that occurred., defaults to None
        :type execution_count: int, optional
        :param inbound_doc_count: The aggregate number of processed inbound documents for the runs that occurred., defaults to None
        :type inbound_doc_count: int, optional
        :param inbound_doc_size: The aggregate size, in bytes, of the processed inbound documents for the runs that occurred., defaults to None
        :type inbound_doc_size: int, optional
        :param launch_elapsed_time: The aggregate elapsed wait time, in milliseconds, before the start of processing for the runs that occurred., defaults to None
        :type launch_elapsed_time: int, optional
        :param launcher_id: The API Service component that kicks off the run.\<br /\> **Note:** The Runtime must have the **API Type** set to **Advanced** on the **Shared Web Server** tab of **Runtime Management** to specify launcherId., defaults to None
        :type launcher_id: str, optional
        :param max_elapsed_time: The time, in milliseconds, it took for the most time-consuming run that occurred., defaults to None
        :type max_elapsed_time: int, optional
        :param outbound_doc_count: The aggregate number of processed outbound documents for the runs that occurred., defaults to None
        :type outbound_doc_count: int, optional
        :param outbound_doc_size: The aggregate size, in bytes, of the processed outbound documents for the runs that occurred., defaults to None
        :type outbound_doc_size: int, optional
        :param process_id: The component ID of the processes that ran., defaults to None
        :type process_id: str, optional
        :param process_name: The name of the process that was run., defaults to None
        :type process_name: str, optional
        :param report_key: The web service user that authenticated to make the run request. \<br /\>**Note:** For Runtimes with an Authentication Type of External Provider, the reportKey is the API Key. Otherwise, it is the specified user name., defaults to None
        :type report_key: str, optional
        :param return_doc_count: The aggregate number of resulting documents for the runs that occurred., defaults to None
        :type return_doc_count: int, optional
        :param return_doc_size: The aggregate size, in bytes, of resulting documents for the runs that occurred., defaults to None
        :type return_doc_size: int, optional
        :param status: The status of the runs. Allowed values include COMPLETE, COMPLETE\_WARN, ERROR., defaults to None
        :type status: str, optional
        :param time_block: The start time of the represented time block., defaults to None
        :type time_block: str, optional
        """
        if account_id is not SENTINEL:
            self.account_id = account_id
        if atom_id is not SENTINEL:
            self.atom_id = atom_id
        if atom_name is not SENTINEL:
            self.atom_name = atom_name
        if elapsed_time is not SENTINEL:
            self.elapsed_time = elapsed_time
        if elapsed_var_sum is not SENTINEL:
            self.elapsed_var_sum = elapsed_var_sum
        if execution_count is not SENTINEL:
            self.execution_count = execution_count
        if inbound_doc_count is not SENTINEL:
            self.inbound_doc_count = inbound_doc_count
        if inbound_doc_size is not SENTINEL:
            self.inbound_doc_size = inbound_doc_size
        if launch_elapsed_time is not SENTINEL:
            self.launch_elapsed_time = launch_elapsed_time
        if launcher_id is not SENTINEL:
            self.launcher_id = launcher_id
        if max_elapsed_time is not SENTINEL:
            self.max_elapsed_time = max_elapsed_time
        if outbound_doc_count is not SENTINEL:
            self.outbound_doc_count = outbound_doc_count
        if outbound_doc_size is not SENTINEL:
            self.outbound_doc_size = outbound_doc_size
        if process_id is not SENTINEL:
            self.process_id = process_id
        if process_name is not SENTINEL:
            self.process_name = process_name
        if report_key is not SENTINEL:
            self.report_key = report_key
        if return_doc_count is not SENTINEL:
            self.return_doc_count = return_doc_count
        if return_doc_size is not SENTINEL:
            self.return_doc_size = return_doc_size
        if status is not SENTINEL:
            self.status = status
        if time_block is not SENTINEL:
            self.time_block = time_block
        self._kwargs = kwargs
