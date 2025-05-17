from typing import Dict, Any, List
from .._http import _HTTP

class Schedules:
    _PATH = "/ProcessSchedules"
    def __init__(self, http: _HTTP):
        self._ = http
    get    = lambda s, sid: s._.get(f"{s._PATH}/{sid}").json()
    update = lambda s, sid, body: s._.post(f"{s._PATH}/{sid}", json=body).json()
    query  = lambda s, body: s._.post(f"{s._PATH}/query", json=body).json()
    def bulk(self, ids: List[str]) -> Dict[str, Any]:
        req = {"request": [{"id": i} for i in ids]}
        return self._.post(f"{self._PATH}/bulk", json=req).json()