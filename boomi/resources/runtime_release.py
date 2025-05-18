from .._http import _HTTP

class RuntimeRelease:
    _P = "/RuntimeReleaseSchedule"

    def __init__(self, http: _HTTP):
        self._http = http

    def create(self, body):
        return self._http.post(self._P, json=body).json()

    def get(self, cid):
        return self._http.get(f"{self._P}/{cid}").json()

    def update(self, cid, body):
        return self._http.post(f"{self._P}/{cid}", json=body).json()

    def delete(self, cid):
        self._http.delete(f"{self._P}/{cid}")
        return True
