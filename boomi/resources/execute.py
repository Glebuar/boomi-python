from .._http import _HTTP
from ..models import ExecuteProcessResponse

class Execute:
    def __init__(self, http: _HTTP):
        self._ = http

    def run(self, body: dict) -> ExecuteProcessResponse:
        resp = self._.post("/ExecuteProcess", json=body)
        data = resp.json()
        if hasattr(ExecuteProcessResponse, "model_validate"):
            return ExecuteProcessResponse.model_validate(data)
        return ExecuteProcessResponse.parse_obj(data)

    cancel = lambda s, exec_id: s._.get(f"/CancelExecution?executionId={exec_id}")
