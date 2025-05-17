from .._http import _HTTP

class Deployments:
    def __init__(self, http: _HTTP):
        self._ = http
    deploy = lambda s, env_id, pkg_id, notes="": s._.post("/DeployedPackage",
        json={"environmentId": env_id, "packageId": pkg_id, "notes": notes}).json()