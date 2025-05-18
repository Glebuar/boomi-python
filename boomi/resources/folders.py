from .._http import _HTTP
from ..models.folder import Folder

class Folders:
    def __init__(self, http: _HTTP):
        self._ = http

    def create(self, name: str, parent: str | None = None) -> Folder:
        payload = {"name": name, **({"parentId": parent} if parent else {})}
        resp = self._.post("/Folder", json=payload)
        data = resp.json()
        if hasattr(Folder, "model_validate"):
            return Folder.model_validate(data)
        return Folder.parse_obj(data)

    def get(self, fid: str) -> Folder:
        resp = self._.get(f"/Folder/{fid}")
        data = resp.json()
        if hasattr(Folder, "model_validate"):
            return Folder.model_validate(data)
        return Folder.parse_obj(data)

    delete = lambda self, fid: self._.delete(f"/Folder/{fid}")
