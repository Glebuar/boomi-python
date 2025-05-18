from boomi.resources.runs import Runs
from boomi._http import _HTTP

class DummyResp:
    def __init__(self, data):
        self._data = data
    def json(self):
        return self._data


def test_runs_summary(monkeypatch):
    http = _HTTP("base", ("u", "p"))
    calls = []
    def fake_post(path, json=None):
        calls.append((path, json))
        return DummyResp({"ok": True})
    monkeypatch.setattr(http, "post", fake_post)
    runs = Runs(http)
    result = runs.summary({"q": 1})
    assert result == {"ok": True}
    assert calls[0][0] == "/ExecutionSummaryRecord/query"
