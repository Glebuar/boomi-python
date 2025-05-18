from boomi._http import _HTTP
from boomi.resources.folders import Folders
from boomi.resources.deployments import Deployments
from boomi.models.folder import Folder
from boomi.models.deployment import Deployment

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

