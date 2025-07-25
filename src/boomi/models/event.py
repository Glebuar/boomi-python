
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap(
    {
        "account_id": "accountId",
        "atom_id": "atomId",
        "atom_name": "atomName",
        "end_time": "endTime",
        "error_document_count": "errorDocumentCount",
        "error_type": "errorType",
        "errored_step_label": "erroredStepLabel",
        "errored_step_type": "erroredStepType",
        "event_date": "eventDate",
        "event_id": "eventId",
        "event_level": "eventLevel",
        "event_type": "eventType",
        "execution_id": "executionId",
        "inbound_document_count": "inboundDocumentCount",
        "outbound_document_count": "outboundDocumentCount",
        "process_id": "processId",
        "process_name": "processName",
        "record_date": "recordDate",
        "start_time": "startTime",
        "top_level_process_id": "topLevelProcessId",
        "update_date": "updateDate",
    }
)
class Event(BaseModel):
    """Event

    :param account_id: The ID of the account in which this event occurred.
    :type account_id: str
    :param atom_id: The ID of the Runtime on which the event occurred.
    :type atom_id: str
    :param atom_name: The name of the Runtime on which the event occurred.
    :type atom_name: str
    :param classification: The classification \(PROD or TEST\) associated with the environment in which the process ran, or to which the Runtime is attached. The classification PROD is returned in the QUERY result if you do not enable environments in the account.
    :type classification: str
    :param end_time: The end date and time of the run \(for applicable events\).
    :type end_time: str
    :param environment: The name of the environment in which the process ran, or to which the Runtime is attached. If you do not enable environments in the account, the QUERY does not return this field in the QUERY result.
    :type environment: str
    :param error: he error message \(for applicable events\).
    :type error: str
    :param error_document_count: The number of documents in an error status for the run \(for applicable events\)., defaults to None
    :type error_document_count: int, optional
    :param error_type: DOCUMENT, if the error applied to one or more documents, or PROCESS, if the error occurred at the process level \(for applicable events\).
    :type error_type: str
    :param errored_step_label: The label of the step in which the error occurred \(for applicable events\).
    :type errored_step_label: str
    :param errored_step_type: The type of the step in which the error occurred — for example, Start, Connector \(for applicable events\).
    :type errored_step_type: str
    :param event_date: The date and time the event occurred.
    :type event_date: str
    :param event_id: The ID of the event.
    :type event_id: str
    :param event_level: The notification level of the event \(INFO, WARNING, ERROR\).
    :type event_level: str
    :param event_type: The type of the event \(atom.status, process.execution, process.missedSchedule, user.notification\).
    :type event_type: str
    :param execution_id: The run ID of the process \(for applicable events\).
    :type execution_id: str
    :param inbound_document_count: The number of inbound documents for the run \(for applicable events\)., defaults to None
    :type inbound_document_count: int, optional
    :param outbound_document_count: The number of outbound documents for the run \(for applicable events\)., defaults to None
    :type outbound_document_count: int, optional
    :param process_id: The ID of the sub-process ONLY when using the ‘Notify’ shape with the 'Generate Platform Event' option and when the process is executed in the 'General' and 'Bridge' modes.
    :type process_id: str
    :param process_name: The name of the process \(for applicable events\).
    :type process_name: str
    :param record_date: The date and time the event recorded.
    :type record_date: str
    :param start_time: The start date and time of the run \(for applicable events\).
    :type start_time: str
    :param status: User-specified message for an event of type user.notification. For other types of events, the event status — for example, COMPLETE, ERROR.
    :type status: str
    :param title: For an event of type user.notification, the title of the originating step.
    :type title: str
    :param top_level_process_id: The ID of the parent process.
    :type top_level_process_id: str
    :param update_date: update_date
    :type update_date: str
    """

    def __init__(
        self,
        account_id: str,
        atom_id: str,
        atom_name: str,
        classification: str,
        end_time: str,
        environment: str,
        error: str,
        error_type: str,
        errored_step_label: str,
        errored_step_type: str,
        event_date: str,
        event_id: str,
        event_level: str,
        event_type: str,
        execution_id: str,
        process_id: str,
        process_name: str,
        record_date: str,
        start_time: str,
        status: str,
        title: str,
        top_level_process_id: str,
        update_date: str,
        error_document_count: int = SENTINEL,
        inbound_document_count: int = SENTINEL,
        outbound_document_count: int = SENTINEL,
        **kwargs
    ):
        """Event

        :param account_id: The ID of the account in which this event occurred.
        :type account_id: str
        :param atom_id: The ID of the Runtime on which the event occurred.
        :type atom_id: str
        :param atom_name: The name of the Runtime on which the event occurred.
        :type atom_name: str
        :param classification: The classification \(PROD or TEST\) associated with the environment in which the process ran, or to which the Runtime is attached. The classification PROD is returned in the QUERY result if you do not enable environments in the account.
        :type classification: str
        :param end_time: The end date and time of the run \(for applicable events\).
        :type end_time: str
        :param environment: The name of the environment in which the process ran, or to which the Runtime is attached. If you do not enable environments in the account, the QUERY does not return this field in the QUERY result.
        :type environment: str
        :param error: he error message \(for applicable events\).
        :type error: str
        :param error_document_count: The number of documents in an error status for the run \(for applicable events\)., defaults to None
        :type error_document_count: int, optional
        :param error_type: DOCUMENT, if the error applied to one or more documents, or PROCESS, if the error occurred at the process level \(for applicable events\).
        :type error_type: str
        :param errored_step_label: The label of the step in which the error occurred \(for applicable events\).
        :type errored_step_label: str
        :param errored_step_type: The type of the step in which the error occurred — for example, Start, Connector \(for applicable events\).
        :type errored_step_type: str
        :param event_date: The date and time the event occurred.
        :type event_date: str
        :param event_id: The ID of the event.
        :type event_id: str
        :param event_level: The notification level of the event \(INFO, WARNING, ERROR\).
        :type event_level: str
        :param event_type: The type of the event \(atom.status, process.execution, process.missedSchedule, user.notification\).
        :type event_type: str
        :param execution_id: The run ID of the process \(for applicable events\).
        :type execution_id: str
        :param inbound_document_count: The number of inbound documents for the run \(for applicable events\)., defaults to None
        :type inbound_document_count: int, optional
        :param outbound_document_count: The number of outbound documents for the run \(for applicable events\)., defaults to None
        :type outbound_document_count: int, optional
        :param process_id: The ID of the sub-process ONLY when using the ‘Notify’ shape with the 'Generate Platform Event' option and when the process is executed in the 'General' and 'Bridge' modes.
        :type process_id: str
        :param process_name: The name of the process \(for applicable events\).
        :type process_name: str
        :param record_date: The date and time the event recorded.
        :type record_date: str
        :param start_time: The start date and time of the run \(for applicable events\).
        :type start_time: str
        :param status: User-specified message for an event of type user.notification. For other types of events, the event status — for example, COMPLETE, ERROR.
        :type status: str
        :param title: For an event of type user.notification, the title of the originating step.
        :type title: str
        :param top_level_process_id: The ID of the parent process.
        :type top_level_process_id: str
        :param update_date: update_date
        :type update_date: str
        """
        self.account_id = account_id
        self.atom_id = atom_id
        self.atom_name = atom_name
        self.classification = classification
        self.end_time = end_time
        self.environment = environment
        self.error = error
        if error_document_count is not SENTINEL:
            self.error_document_count = error_document_count
        self.error_type = error_type
        self.errored_step_label = errored_step_label
        self.errored_step_type = errored_step_type
        self.event_date = event_date
        self.event_id = event_id
        self.event_level = event_level
        self.event_type = event_type
        self.execution_id = execution_id
        if inbound_document_count is not SENTINEL:
            self.inbound_document_count = inbound_document_count
        if outbound_document_count is not SENTINEL:
            self.outbound_document_count = outbound_document_count
        self.process_id = process_id
        self.process_name = process_name
        self.record_date = record_date
        self.start_time = start_time
        self.status = status
        self.title = title
        self.top_level_process_id = top_level_process_id
        self.update_date = update_date
        self._kwargs = kwargs
