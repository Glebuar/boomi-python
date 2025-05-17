from .._http import _HTTP

class Extensions:
    def __init__(self, http: _HTTP):
        self._ = http
    get    = lambda s, env: s._.get(f"/EnvironmentExtensions/{env}").json()
    update = lambda s, env, body: s._.post(f"/EnvironmentExtensions/{env}", json=body).json()
    query  = lambda s, body: s._.post("/EnvironmentExtensions/query", json=body).json()
    query_conn_field_summary = (
        lambda s, body: s._.post(
            "/EnvironmentConnectionFieldExtensionSummary/query", json=body
        ).json()
    )