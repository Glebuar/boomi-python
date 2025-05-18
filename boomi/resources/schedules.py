from typing import Dict, Any, List
from .._http import _HTTP

class Schedules:
    _PATH = "/ProcessSchedules"

    def __init__(self, http: _HTTP):
        self._http = http

    def get(self, sid):
        return self._http.get(f"{self._PATH}/{sid}").json()

    def update(self, sid, body):
        return self._http.post(f"{self._PATH}/{sid}", json=body).json()

    def query(self, body):
        return self._http.post(f"{self._PATH}/query", json=body).json()

    def bulk(self, ids: List[str]) -> Dict[str, Any]:
        req = {"request": [{"id": i} for i in ids]}
        return self._http.post(f"{self._PATH}/bulk", json=req).json()
