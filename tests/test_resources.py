from boomi._http import _HTTP
from boomi.resources.execute import Execute
from boomi.resources.runs import Runs
from boomi.models import ExecuteProcessResponse, ExecutionRecord, ExecutionSummaryRecord

class DummyResp:
    def __init__(self, data):
        self._data = data
    def json(self):
        return self._data

def test_execute_run_returns_model(monkeypatch):
    http = _HTTP("base", ("u", "p"))
    monkeypatch.setattr(http, "post", lambda path, json=None: DummyResp({"executionId": "e1", "status": "OK", "started_at": "now"}))
    execute = Execute(http)
    result = execute.run({"processId": "p"})
    assert isinstance(result, ExecuteProcessResponse)
    assert result.id == "e1"


def test_runs_list_parses(monkeypatch):
    http = _HTTP("base", ("u", "p"))
    monkeypatch.setattr(http, "post", lambda path, json=None: DummyResp({"result": [{"executionId": "e1", "status": "OK", "started_at": "t"}]}))
    runs = Runs(http)
    items = runs.list({"q": 1})
    assert len(items) == 1 and isinstance(items[0], ExecutionRecord)


def test_runs_summary_parses(monkeypatch):
    http = _HTTP("base", ("u", "p"))
    monkeypatch.setattr(http, "post", lambda path, json=None: DummyResp({"result": [{"processID": "p1", "processName": "Proc"}]}))
    runs = Runs(http)
    items = runs.summary({"q": 1})
    assert len(items) == 1 and isinstance(items[0], ExecutionSummaryRecord)
