from boomi.models import (
    ExecutionSummaryRecord,
    ExecutionConnector,
    GenericConnectorRecord,
    AuditLog,
    Event,
    ExecutionCountAccount,
)


def parse_model(cls, data):
    if hasattr(cls, "model_validate"):
        return cls.model_validate(data)
    return cls.parse_obj(data)


def test_summary_record_aliases():
    data = {"processID": "p1", "processName": "Proc", "status": "COMPLETE"}
    rec = parse_model(ExecutionSummaryRecord, data)
    assert rec.process_id == "p1"
    assert rec.process_name == "Proc"
    assert rec.status == "COMPLETE"


def test_execution_connector_aliases():
    data = {
        "id": "c1",
        "executionId": "e1",
        "connectorType": "HTTP",
        "successCount": 2,
    }
    rec = parse_model(ExecutionConnector, data)
    assert rec.execution_id == "e1"
    assert rec.connector_type == "HTTP"
    assert rec.success_count == 2


def test_generic_connector_record_aliases():
    data = {
        "id": "g1",
        "executionId": "e1",
        "status": "OK",
        "errorMessage": None,
    }
    rec = parse_model(GenericConnectorRecord, data)
    assert rec.id == "g1"
    assert rec.execution_id == "e1"
    assert rec.status == "OK"


def test_audit_log_aliases():
    data = {"documentId": "d1", "action": "DOWNLOAD"}
    log = parse_model(AuditLog, data)
    assert log.document_id == "d1"
    assert log.action == "DOWNLOAD"


def test_event_aliases():
    data = {"eventId": "ev1", "eventType": "process.execution", "executionId": "e1"}
    evt = parse_model(Event, data)
    assert evt.event_id == "ev1"
    assert evt.event_type == "process.execution"
    assert evt.execution_id == "e1"


def test_count_account_aliases():
    data = {
        "accountId": "a1",
        "atomId": "atom1",
        "date": "2024-01-01",
        "failures": 1,
        "successes": 2,
    }
    cnt = parse_model(ExecutionCountAccount, data)
    assert cnt.account_id == "a1"
    assert cnt.atom_id == "atom1"
    assert cnt.failures == 1
    assert cnt.successes == 2
