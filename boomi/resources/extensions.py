from .._http import _HTTP

class Extensions:
    def __init__(self, http: _HTTP):
        self._http = http

    def get(self, env):
        return self._http.get(f"/EnvironmentExtensions/{env}").json()

    def update(self, env, body):
        return self._http.post(f"/EnvironmentExtensions/{env}", json=body).json()

    def query(self, body):
        return self._http.post("/EnvironmentExtensions/query", json=body).json()

    def query_conn_field_summary(self, body):
        return self._http.post(
            "/EnvironmentConnectionFieldExtensionSummary/query", json=body
        ).json()
