from boomi._http import _HTTP
from boomi.resources.folders import Folders
from boomi.resources.deployments import Deployments
from boomi.models.folder import Folder
from boomi.models.deployment import Deployment
from boomi.resources.execute import Execute
from boomi.resources.runs import Runs
from boomi.models import ExecuteProcessResponse, ExecutionRecord, ExecutionSummaryRecord

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