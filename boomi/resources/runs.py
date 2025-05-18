from .._http import _HTTP
from ..utils import paginate_query
from ..models import (
    ExecutionRecord,
    ExecutionSummaryRecord,
    ExecutionConnector,
    GenericConnectorRecord,
    ExecutionCountAccount,
    ExecutionCountAccountGroup,
    AuditLog,
    Event,
)

_GENERIC_PARSER = (
    GenericConnectorRecord.model_validate
    if hasattr(GenericConnectorRecord, "model_validate")
    else GenericConnectorRecord.parse_obj
)

class Runs:
    def __init__(self, http: _HTTP):
        self._http = http

    def list(self, body: dict, *, parse: bool = True):
        """Query execution records."""
        data = self._http.post("/ExecutionRecord/query", json=body).json()
        if not parse:
            return data
        if hasattr(ExecutionRecord, "model_validate"):
            return [ExecutionRecord.model_validate(r) for r in data.get("result", [])]
        return [ExecutionRecord.parse_obj(r) for r in data.get("result", [])]

    def list_more(self, token: str, *, parse: bool = True):
        """Continue a record query using ``queryToken``."""
        data = self._http.post(
            "/ExecutionRecord/queryMore", json={"queryToken": token}
        ).json()
        if not parse:
            return data
        if hasattr(ExecutionRecord, "model_validate"):
            return [ExecutionRecord.model_validate(r) for r in data.get("result", [])]
        return [ExecutionRecord.parse_obj(r) for r in data.get("result", [])]

    def summary(self, body: dict, *, parse: bool = True):
        """Query execution summary records."""
        data = self._http.post(
            "/ExecutionSummaryRecord/query", json=body
        ).json()
        if not parse:
            return data
        if hasattr(ExecutionSummaryRecord, "model_validate"):
            return [ExecutionSummaryRecord.model_validate(r) for r in data.get("result", [])]
        return [ExecutionSummaryRecord.parse_obj(r) for r in data.get("result", [])]

    def list_all(self, body: dict, *, parse: bool = True):
        """Yield all execution records for ``body`` handling pagination."""
        def first_call(payload: dict):
            return self._http.post("/ExecutionRecord/query", json=payload).json()

        def more_call(tok: str):
            return self._http.post("/ExecutionRecord/queryMore", json={"queryToken": tok}).json()

        parser = (
            ExecutionRecord.model_validate
            if hasattr(ExecutionRecord, "model_validate")
            else ExecutionRecord.parse_obj
        )

        yield from paginate_query(first_call, more_call, body, parse_item=parser, parse=parse)

    def summary_more(self, token: str, *, parse: bool = True):
        """Continue a summary query using ``queryToken``."""
        data = self._http.post(
            "/ExecutionSummaryRecord/queryMore", json={"queryToken": token}
        ).json()
        if not parse:
            return data
        if hasattr(ExecutionSummaryRecord, "model_validate"):
            return [ExecutionSummaryRecord.model_validate(r) for r in data.get("result", [])]
        return [ExecutionSummaryRecord.parse_obj(r) for r in data.get("result", [])]

    def summary_all(self, body: dict, *, parse: bool = True):
        """Yield all execution summary records for ``body`` handling pagination."""
        def first_call(payload: dict):
            return self._http.post("/ExecutionSummaryRecord/query", json=payload).json()

        def more_call(tok: str):
            return self._http.post("/ExecutionSummaryRecord/queryMore", json={"queryToken": tok}).json()

        parser = (
            ExecutionSummaryRecord.model_validate
            if hasattr(ExecutionSummaryRecord, "model_validate")
            else ExecutionSummaryRecord.parse_obj
        )

        yield from paginate_query(first_call, more_call, body, parse_item=parser, parse=parse)

    def connectors(self, body: dict, *, parse: bool = True):
        """Query execution connector records."""
        data = self._http.post("/ExecutionConnector/query", json=body).json()
        if not parse:
            return data
        if hasattr(ExecutionConnector, "model_validate"):
            return [ExecutionConnector.model_validate(r) for r in data.get("result", [])]
        return [ExecutionConnector.parse_obj(r) for r in data.get("result", [])]

    def connectors_more(self, token: str, *, parse: bool = True):
        """Fetch additional connector results via ``queryToken``."""
        data = self._http.post(
            "/ExecutionConnector/queryMore", json={"queryToken": token}
        ).json()
        if not parse:
            return data
        if hasattr(ExecutionConnector, "model_validate"):
            return [ExecutionConnector.model_validate(r) for r in data.get("result", [])]
        return [ExecutionConnector.parse_obj(r) for r in data.get("result", [])]

    def count_account(self, body: dict, *, parse: bool = True):
        """Query execution counts aggregated by account."""
        data = self._http.post("/ExecutionCountAccount/query", json=body).json()
        if not parse:
            return data
        if hasattr(ExecutionCountAccount, "model_validate"):
            return [ExecutionCountAccount.model_validate(r) for r in data.get("result", [])]
        return [ExecutionCountAccount.parse_obj(r) for r in data.get("result", [])]

    def count_account_more(self, token: str, *, parse: bool = True):
        data = self._http.post(
            "/ExecutionCountAccount/queryMore", json={"queryToken": token}
        ).json()
        if not parse:
            return data
        if hasattr(ExecutionCountAccount, "model_validate"):
            return [ExecutionCountAccount.model_validate(r) for r in data.get("result", [])]
        return [ExecutionCountAccount.parse_obj(r) for r in data.get("result", [])]

    def count_group(self, body: dict, *, parse: bool = True):
        """Query execution counts aggregated by account group."""
        data = self._http.post(
            "/ExecutionCountAccountGroup/query", json=body
        ).json()
        if not parse:
            return data
        if hasattr(ExecutionCountAccountGroup, "model_validate"):
            return [ExecutionCountAccountGroup.model_validate(r) for r in data.get("result", [])]
        return [ExecutionCountAccountGroup.parse_obj(r) for r in data.get("result", [])]

    def count_group_more(self, token: str, *, parse: bool = True):
        data = self._http.post(
            "/ExecutionCountAccountGroup/queryMore", json={"queryToken": token}
        ).json()
        if not parse:
            return data
        if hasattr(ExecutionCountAccountGroup, "model_validate"):
            return [ExecutionCountAccountGroup.model_validate(r) for r in data.get("result", [])]
        return [ExecutionCountAccountGroup.parse_obj(r) for r in data.get("result", [])]

    def artifacts(self, exec_id: str) -> str:
        """Return the download URL for execution artifacts."""
        return (
            self._http.post("/ExecutionArtifacts", json={"executionId": exec_id})
            .json()
            .get("url")
        )

    def request(self, body: dict):
        return self._http.post("/ExecutionRequest", json=body).json()

    def doc(self, gid: str, *, parse: bool = True):
        data = self._http.get(f"/GenericConnectorRecord/{gid}").json()
        if not parse:
            return data
        if hasattr(GenericConnectorRecord, "model_validate"):
            return _GENERIC_PARSER(data)
        return GenericConnectorRecord.parse_obj(data)

    def docs(self, body: dict, *, parse: bool = True):
        data = self._http.post("/GenericConnectorRecord/query", json=body).json()
        if not parse:
            return data
        if hasattr(GenericConnectorRecord, "model_validate"):
            return [_GENERIC_PARSER(r) for r in data.get("result", [])]
        return [GenericConnectorRecord.parse_obj(r) for r in data.get("result", [])]

    def docs_more(self, token: str, *, parse: bool = True):
        data = self._http.post(
            "/GenericConnectorRecord/queryMore", json={"queryToken": token}
        ).json()
        if not parse:
            return data
        if hasattr(GenericConnectorRecord, "model_validate"):
            return [_GENERIC_PARSER(r) for r in data.get("result", [])]
        return [GenericConnectorRecord.parse_obj(r) for r in data.get("result", [])]

    def as2_records(self, body: dict, *, parse: bool = True):
        """Query AS2 connector records."""
        data = self._http.post("/AS2ConnectorRecord/query", json=body).json()
        if not parse:
            return data
        return [_GENERIC_PARSER(r) for r in data.get("result", [])]

    def as2_records_more(self, token: str, *, parse: bool = True):
        """Get additional AS2 connector records."""
        data = self._http.post(
            "/AS2ConnectorRecord/queryMore", json={"queryToken": token}
        ).json()
        if not parse:
            return data
        return [_GENERIC_PARSER(r) for r in data.get("result", [])]

    def edicustom_records(self, body: dict, *, parse: bool = True):
        """Query EDI Custom connector records."""
        data = self._http.post("/EdiCustomConnectorRecord/query", json=body).json()
        if not parse:
            return data
        return [_GENERIC_PARSER(r) for r in data.get("result", [])]

    def edicustom_records_more(self, token: str, *, parse: bool = True):
        """Get additional EDI Custom connector records."""
        data = self._http.post(
            "/EdiCustomConnectorRecord/queryMore", json={"queryToken": token}
        ).json()
        if not parse:
            return data
        return [_GENERIC_PARSER(r) for r in data.get("result", [])]

    def edifact_records(self, body: dict, *, parse: bool = True):
        """Query EDIFACT connector records."""
        data = self._http.post("/EDIFACTConnectorRecord/query", json=body).json()
        if not parse:
            return data
        return [_GENERIC_PARSER(r) for r in data.get("result", [])]

    def edifact_records_more(self, token: str, *, parse: bool = True):
        """Get additional EDIFACT connector records."""
        data = self._http.post(
            "/EDIFACTConnectorRecord/queryMore", json={"queryToken": token}
        ).json()
        if not parse:
            return data
        return [_GENERIC_PARSER(r) for r in data.get("result", [])]

    def hl7_records(self, body: dict, *, parse: bool = True):
        """Query HL7 connector records."""
        data = self._http.post("/HL7ConnectorRecord/query", json=body).json()
        if not parse:
            return data
        return [_GENERIC_PARSER(r) for r in data.get("result", [])]

    def hl7_records_more(self, token: str, *, parse: bool = True):
        """Get additional HL7 connector records."""
        data = self._http.post(
            "/HL7ConnectorRecord/queryMore", json={"queryToken": token}
        ).json()
        if not parse:
            return data
        return [_GENERIC_PARSER(r) for r in data.get("result", [])]

    def odette_records(self, body: dict, *, parse: bool = True):
        """Query ODETTE connector records."""
        data = self._http.post("/ODETTEConnectorRecord/query", json=body).json()
        if not parse:
            return data
        return [_GENERIC_PARSER(r) for r in data.get("result", [])]

    def odette_records_more(self, token: str, *, parse: bool = True):
        """Get additional ODETTE connector records."""
        data = self._http.post(
            "/ODETTEConnectorRecord/queryMore", json={"queryToken": token}
        ).json()
        if not parse:
            return data
        return [_GENERIC_PARSER(r) for r in data.get("result", [])]

    def oftp2_records(self, body: dict, *, parse: bool = True):
        """Query OFTP2 connector records."""
        data = self._http.post("/OFTP2ConnectorRecord/query", json=body).json()
        if not parse:
            return data
        return [_GENERIC_PARSER(r) for r in data.get("result", [])]

    def oftp2_records_more(self, token: str, *, parse: bool = True):
        """Get additional OFTP2 connector records."""
        data = self._http.post(
            "/OFTP2ConnectorRecord/queryMore", json={"queryToken": token}
        ).json()
        if not parse:
            return data
        return [_GENERIC_PARSER(r) for r in data.get("result", [])]

    def rosetta_records(self, body: dict, *, parse: bool = True):
        """Query RosettaNet connector records."""
        data = self._http.post("/RosettaNetConnectorRecord/query", json=body).json()
        if not parse:
            return data
        return [_GENERIC_PARSER(r) for r in data.get("result", [])]

    def rosetta_records_more(self, token: str, *, parse: bool = True):
        """Get additional RosettaNet connector records."""
        data = self._http.post(
            "/RosettaNetConnectorRecord/queryMore", json={"queryToken": token}
        ).json()
        if not parse:
            return data
        return [_GENERIC_PARSER(r) for r in data.get("result", [])]

    def tradacoms_records(self, body: dict, *, parse: bool = True):
        """Query Tradacoms connector records."""
        data = self._http.post("/TradacomsConnectorRecord/query", json=body).json()
        if not parse:
            return data
        return [_GENERIC_PARSER(r) for r in data.get("result", [])]

    def tradacoms_records_more(self, token: str, *, parse: bool = True):
        """Get additional Tradacoms connector records."""
        data = self._http.post(
            "/TradacomsConnectorRecord/queryMore", json={"queryToken": token}
        ).json()
        if not parse:
            return data
        return [_GENERIC_PARSER(r) for r in data.get("result", [])]

    def x12_records(self, body: dict, *, parse: bool = True):
        """Query X12 connector records."""
        data = self._http.post("/X12ConnectorRecord/query", json=body).json()
        if not parse:
            return data
        return [_GENERIC_PARSER(r) for r in data.get("result", [])]

    def x12_records_more(self, token: str, *, parse: bool = True):
        """Get additional X12 connector records."""
        data = self._http.post(
            "/X12ConnectorRecord/queryMore", json={"queryToken": token}
        ).json()
        if not parse:
            return data
        return [_GENERIC_PARSER(r) for r in data.get("result", [])]

    def log(self, exec_id: str) -> str:
        """Return the execution log download URL."""
        return (
            self._http.post(
                "/ProcessLog", json={"executionId": exec_id, "logLevel": "ALL"}
            )
            .json()
            .get("url")
        )

    def get_log_content(self, exec_id: str) -> str:
        url = self.log(exec_id)
        import requests

        resp = requests.get(url, auth=self._http.auth, timeout=self._http.timeout)
        return resp.text

    def atom_log(self, body: dict) -> str:
        """Return Atom log download URL."""
        return self._http.post("/AtomLog", json=body).json().get("url")

    def as2_artifacts(self, body: dict) -> str:
        return self._http.post("/AtomAS2Artifacts", json=body).json().get("url")

    def worker_log(self, body: dict) -> str:
        return self._http.post("/AtomWorkerLog", json=body).json().get("url")

    def audit(self, aid: str, *, parse: bool = True):
        """Retrieve a single audit log entry."""
        data = self._http.get(f"/AuditLog/{aid}").json()
        if not parse:
            return data
        return AuditLog.model_validate(data)

    def audit_query(self, body: dict, *, parse: bool = True):
        """Query audit logs."""
        data = self._http.post("/AuditLog/query", json=body).json()
        if not parse:
            return data
        return [AuditLog.model_validate(r) for r in data.get("result", [])]

    def audit_query_more(self, token: str, *, parse: bool = True):
        """Fetch additional audit log results."""
        data = self._http.post(
            "/AuditLog/queryMore", json={"queryToken": token}
        ).json()
        if not parse:
            return data
        return [AuditLog.model_validate(r) for r in data.get("result", [])]

    def events(self, body: dict, *, parse: bool = True):
        """Query event logs."""
        data = self._http.post("/Event/query", json=body).json()
        if not parse:
            return data
        return [Event.model_validate(r) for r in data.get("result", [])]

    def events_more(self, token: str, *, parse: bool = True):
        """Fetch additional event log entries."""
        data = self._http.post(
            "/Event/queryMore", json={"queryToken": token}
        ).json()
        if not parse:
            return data
        return [Event.model_validate(r) for r in data.get("result", [])]
