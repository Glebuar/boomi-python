from .._http import _HTTP

class Execute:
    def __init__(self, http: _HTTP):
        self._ = http
    run    = lambda s, body: s._.post("/ExecuteProcess", json=body).json()
    cancel = lambda s, exec_id: s._.get(f"/CancelExecution?executionId={exec_id}")