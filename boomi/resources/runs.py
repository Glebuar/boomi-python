from .._http import _HTTP

class Runs:
    def __init__(self, http: _HTTP):
        self._ = http
    list = lambda s, body: s._.post("/ExecutionRecord/query", json=body).json()
    log = lambda s, exec_id: s._.post("/ProcessLog",
        json={"executionId": exec_id, "logLevel": "ALL"}).json().get("url")
