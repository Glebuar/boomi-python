from .._http import _HTTP
from ..models.folder import Folder
from typing import Optional

class Folders:
    def __init__(self, http: _HTTP):
        self._http = http

    def create(self, name: str, parent: Optional[str] = None) -> Folder:
        """Create a folder optionally under ``parent``."""
        payload = {"name": name, **({"parentId": parent} if parent else {})}
        resp = self._http.post("/Folder", json=payload)
        data = resp.json()
        if hasattr(Folder, "model_validate"):
            return Folder.model_validate(data)
        return Folder.parse_obj(data)

    def get(self, fid: str) -> Folder:
        """Retrieve folder details by id."""
        resp = self._http.get(f"/Folder/{fid}")
        data = resp.json()
        if hasattr(Folder, "model_validate"):
            return Folder.model_validate(data)
        return Folder.parse_obj(data)

    def delete(self, fid: str) -> bool:
        """Delete a folder."""
        self._http.delete(f"/Folder/{fid}")
        return True
