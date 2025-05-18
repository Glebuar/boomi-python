from .._http import _HTTP

class Runs:
    def __init__(self, http: _HTTP):
        self._ = http

    list = lambda s, body: s._.post("/ExecutionRecord/query", json=body).json()
    list_more = lambda s, token: s._.post(
        "/ExecutionRecord/queryMore", json={"queryToken": token}
    ).json()

    summary = lambda s, body: s._.post(
        "/ExecutionSummaryRecord/query", json=body
    ).json()
    summary_more = lambda s, token: s._.post(
        "/ExecutionSummaryRecord/queryMore", json={"queryToken": token}
    ).json()

    connectors = lambda s, body: s._.post(
        "/ExecutionConnector/query", json=body
    ).json()
    connectors_more = lambda s, token: s._.post(
        "/ExecutionConnector/queryMore", json={"queryToken": token}
    ).json()

    count_account = lambda s, body: s._.post(
        "/ExecutionCountAccount/query", json=body
    ).json()
    count_account_more = lambda s, token: s._.post(
        "/ExecutionCountAccount/queryMore", json={"queryToken": token}
    ).json()

    count_group = lambda s, body: s._.post(
        "/ExecutionCountAccountGroup/query", json=body
    ).json()
    count_group_more = lambda s, token: s._.post(
        "/ExecutionCountAccountGroup/queryMore", json={"queryToken": token}
    ).json()

    artifacts = lambda s, exec_id: s._.post(
        "/ExecutionArtifacts", json={"executionId": exec_id}
    ).json().get("url")

    request = lambda s, body: s._.post("/ExecutionRequest", json=body).json()

    doc = lambda s, gid: s._.get(f"/GenericConnectorRecord/{gid}").json()
    docs = lambda s, body: s._.post(
        "/GenericConnectorRecord/query", json=body
    ).json()
    docs_more = lambda s, token: s._.post(
        "/GenericConnectorRecord/queryMore", json={"queryToken": token}
    ).json()

    as2_records = lambda s, body: s._.post(
        "/AS2ConnectorRecord/query", json=body
    ).json()
    as2_records_more = lambda s, token: s._.post(
        "/AS2ConnectorRecord/queryMore", json={"queryToken": token}
    ).json()

    edicustom_records = lambda s, body: s._.post(
        "/EdiCustomConnectorRecord/query", json=body
    ).json()
    edicustom_records_more = lambda s, token: s._.post(
        "/EdiCustomConnectorRecord/queryMore", json={"queryToken": token}
    ).json()

    edifact_records = lambda s, body: s._.post(
        "/EDIFACTConnectorRecord/query", json=body
    ).json()
    edifact_records_more = lambda s, token: s._.post(
        "/EDIFACTConnectorRecord/queryMore", json={"queryToken": token}
    ).json()

    hl7_records = lambda s, body: s._.post(
        "/HL7ConnectorRecord/query", json=body
    ).json()
    hl7_records_more = lambda s, token: s._.post(
        "/HL7ConnectorRecord/queryMore", json={"queryToken": token}
    ).json()

    odette_records = lambda s, body: s._.post(
        "/ODETTEConnectorRecord/query", json=body
    ).json()
    odette_records_more = lambda s, token: s._.post(
        "/ODETTEConnectorRecord/queryMore", json={"queryToken": token}
    ).json()

    oftp2_records = lambda s, body: s._.post(
        "/OFTP2ConnectorRecord/query", json=body
    ).json()
    oftp2_records_more = lambda s, token: s._.post(
        "/OFTP2ConnectorRecord/queryMore", json={"queryToken": token}
    ).json()

    rosetta_records = lambda s, body: s._.post(
        "/RosettaNetConnectorRecord/query", json=body
    ).json()
    rosetta_records_more = lambda s, token: s._.post(
        "/RosettaNetConnectorRecord/queryMore", json={"queryToken": token}
    ).json()

    tradacoms_records = lambda s, body: s._.post(
        "/TradacomsConnectorRecord/query", json=body
    ).json()
    tradacoms_records_more = lambda s, token: s._.post(
        "/TradacomsConnectorRecord/queryMore", json={"queryToken": token}
    ).json()

    x12_records = lambda s, body: s._.post(
        "/X12ConnectorRecord/query", json=body
    ).json()
    x12_records_more = lambda s, token: s._.post(
        "/X12ConnectorRecord/queryMore", json={"queryToken": token}
    ).json()

    log = lambda s, exec_id: s._.post(
        "/ProcessLog",
        json={"executionId": exec_id, "logLevel": "ALL"},
    ).json().get("url")

    atom_log = lambda s, body: s._.post("/AtomLog", json=body).json().get("url")
    as2_artifacts = lambda s, body: s._.post(
        "/AtomAS2Artifacts", json=body
    ).json().get("url")
    worker_log = lambda s, body: s._.post(
        "/AtomWorkerLog", json=body
    ).json().get("url")

    audit = lambda s, aid: s._.get(f"/AuditLog/{aid}").json()
    audit_query = lambda s, body: s._.post("/AuditLog/query", json=body).json()
    audit_query_more = lambda s, token: s._.post(
        "/AuditLog/queryMore", json={"queryToken": token}
    ).json()

    events = lambda s, body: s._.post("/Event/query", json=body).json()
    events_more = lambda s, token: s._.post(
        "/Event/queryMore", json={"queryToken": token}
    ).json()
