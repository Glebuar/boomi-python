from .._http import _HTTP
from ..models.deployment import Deployment

class Deployments:
    def __init__(self, http: _HTTP):
        self._http = http

    def deploy(self, env_id: str, pkg_id: str, notes: str = "") -> Deployment:
        """Deploy a package to an environment."""
        payload = {"environmentId": env_id, "packageId": pkg_id, "notes": notes}
        resp = self._http.post("/DeployedPackage", json=payload)
        data = resp.json()
        if hasattr(Deployment, "model_validate"):
            return Deployment.model_validate(data)
        return Deployment.parse_obj(data)
