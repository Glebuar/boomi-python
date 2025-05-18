from boomi._http import _HTTP
from boomi.resources.folders import Folders
from boomi.resources.deployments import Deployments
from boomi.models.folder import Folder
from boomi.models.deployment import Deployment
from boomi.resources.execute import Execute
from boomi.resources.runs import Runs
from boomi.models import (
    ExecuteProcessResponse,
    ExecutionRecord,
    ExecutionSummaryRecord,
    GenericConnectorRecord,
)

class DummyResp:
    def __init__(self, data):
        self._data = data
    def json(self):
        return self._data


def test_folders_return_models(monkeypatch):
    http = _HTTP("base", ("u", "p"))

    def fake_post(path, json=None):
        assert path == "/Folder"
        return DummyResp({"folderId": "f1", "name": json["name"]})

    def fake_get(path, **kw):
        assert path == "/Folder/f1"
        return DummyResp({"folderId": "f1", "name": "F1"})

    monkeypatch.setattr(http, "post", fake_post)
    monkeypatch.setattr(http, "get", fake_get)

    folders = Folders(http)
    folder = folders.create("F1")
    assert isinstance(folder, Folder)
    assert folder.id == "f1"

    fetched = folders.get("f1")
    assert isinstance(fetched, Folder)
    assert fetched.name == "F1"


def test_deployments_return_models(monkeypatch):
    http = _HTTP("base", ("u", "p"))

    def fake_post(path, json=None):
        assert path == "/DeployedPackage"
        return DummyResp({
            "deploymentId": "d1",
            "componentId": json["packageId"],
            "environmentId": json["environmentId"],
        })

    monkeypatch.setattr(http, "post", fake_post)

    deps = Deployments(http)
    dep = deps.deploy("env", "pkg")
    assert isinstance(dep, Deployment)
    assert dep.environment_id == "env"
   
  
def test_execute_run_returns_model(monkeypatch):
    http = _HTTP("base", ("u", "p"))
    monkeypatch.setattr(http, "post", lambda path, json=None: DummyResp({"executionId": "e1", "status": "OK", "executionTime": "now"}))
    execute = Execute(http)
    result = execute.run({"processId": "p"})
    assert isinstance(result, ExecuteProcessResponse)
    assert result.id == "e1"
    assert result.execution_time == "now"


def test_runs_list_parses(monkeypatch):
    http = _HTTP("base", ("u", "p"))
    monkeypatch.setattr(http, "post", lambda path, json=None: DummyResp({"result": [{"executionId": "e1", "status": "OK", "executionTime": "t"}]}))
    runs = Runs(http)
    items = runs.list({"q": 1})
    assert len(items) == 1 and isinstance(items[0], ExecutionRecord)
    assert items[0].execution_time == "t"


def test_runs_summary_parses(monkeypatch):
    http = _HTTP("base", ("u", "p"))
    monkeypatch.setattr(http, "post", lambda path, json=None: DummyResp({"result": [{"processID": "p1", "processName": "Proc"}]}))
    runs = Runs(http)
    items = runs.summary({"q": 1})
    assert len(items) == 1 and isinstance(items[0], ExecutionSummaryRecord)


def test_runs_list_more(monkeypatch):
    http = _HTTP("base", ("u", "p"))

    def fake_post(path, json=None):
        assert path == "/ExecutionRecord/queryMore"
        return DummyResp({"result": [{"executionId": "e2", "status": "OK", "executionTime": "t2"}]})

    monkeypatch.setattr(http, "post", fake_post)

    runs = Runs(http)
    items = runs.list_more("tok")
    assert len(items) == 1 and items[0].id == "e2"


def test_runs_summary_more(monkeypatch):
    http = _HTTP("base", ("u", "p"))

    def fake_post(path, json=None):
        assert path == "/ExecutionSummaryRecord/queryMore"
        return DummyResp({"result": [{"processID": "p2", "processName": "P"}]})

    monkeypatch.setattr(http, "post", fake_post)
    runs = Runs(http)
    items = runs.summary_more("tok")
    assert len(items) == 1 and items[0].process_id == "p2"


def test_connectors_parse(monkeypatch):
    http = _HTTP("base", ("u", "p"))

    def fake_post(path, json=None):
        assert path == "/ExecutionConnector/query"
        return DummyResp({"result": [{"id": "c1", "executionId": "e"}]})

    monkeypatch.setattr(http, "post", fake_post)
    runs = Runs(http)
    items = runs.connectors({})
    assert len(items) == 1 and items[0].id == "c1"
    raw = runs.connectors({}, parse=False)
    assert raw["result"][0]["id"] == "c1"


def test_connectors_more(monkeypatch):
    http = _HTTP("base", ("u", "p"))

    def fake_post(path, json=None):
        assert path == "/ExecutionConnector/queryMore"
        return DummyResp({"result": [{"id": "c2", "executionId": "e"}]})

    monkeypatch.setattr(http, "post", fake_post)
    runs = Runs(http)
    items = runs.connectors_more("tok")
    assert len(items) == 1 and items[0].id == "c2"


def test_count_account_group(monkeypatch):
    http = _HTTP("base", ("u", "p"))

    def fake_post(path, json=None):
        if path.endswith("Account/query"):
            return DummyResp({"result": [{"accountId": "A"}]})
        else:
            return DummyResp({"result": [{"accountId": "B"}]})

    monkeypatch.setattr(http, "post", fake_post)
    runs = Runs(http)
    acc = runs.count_account({})
    grp = runs.count_group({})
    assert acc[0].account_id == "A"
    assert grp[0].account_id == "B"


def test_special_connector_records(monkeypatch):
    http = _HTTP("base", ("u", "p"))

    def fake_post(path, json=None):
        return DummyResp({"result": [{"id": "r1", "executionId": "e"}]})

    monkeypatch.setattr(http, "post", fake_post)
    runs = Runs(http)
    items = runs.as2_records({})
    assert isinstance(items[0], GenericConnectorRecord)
    raw = runs.hl7_records({}, parse=False)
    assert raw["result"][0]["id"] == "r1"


def test_artifacts(monkeypatch):
    http = _HTTP("base", ("u", "p"))
    monkeypatch.setattr(http, "post", lambda path, json=None: DummyResp({"url": "http://a"}))
    runs = Runs(http)
    assert runs.artifacts("e1") == "http://a"


def test_log_url(monkeypatch):
    http = _HTTP("base", ("u", "p"))
    monkeypatch.setattr(http, "post", lambda path, json=None: DummyResp({"url": "http://x"}))
    runs = Runs(http)
    assert runs.log("e1") == "http://x"


def test_execute_cancel(monkeypatch):
    http = _HTTP("base", ("u", "p"))
    monkeypatch.setattr(http, "get", lambda path: DummyResp({}))
    execute = Execute(http)
    assert execute.cancel("e1") is True
