from .._http import _HTTP

class Packages:
    def __init__(self, http: _HTTP):
        self._http = http

    def create(self, cid, ver=None, notes=None):
        payload = {"componentId": cid}
        if ver:
            payload["packageVersion"] = ver
        if notes:
            payload["notes"] = notes
        return self._http.post("/PackagedComponent", json=payload).json()
