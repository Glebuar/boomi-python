from .._http import _HTTP
from ..models import ExecuteProcessResponse

class Execute:
    def __init__(self, http: _HTTP):
        self._http = http

    def run(self, body: dict) -> ExecuteProcessResponse:
        """Execute a process and return the execution metadata."""
        resp = self._http.post("/ExecuteProcess", json=body)
        data = resp.json()
        if hasattr(ExecuteProcessResponse, "model_validate"):
            return ExecuteProcessResponse.model_validate(data)
        return ExecuteProcessResponse.parse_obj(data)

    def cancel(self, exec_id: str) -> bool:
        """Cancel a running execution."""
        self._http.get(f"/CancelExecution?executionId={exec_id}")
        return True
