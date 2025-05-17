"""High‑level root object that groups all resource managers."""
from __future__ import annotations
from typing import Optional

from ._http import _HTTP
from .resources.components import Components
from .resources.deployments import Deployments
from .resources.runs import Runs
from .resources.folders import Folders
from .resources.schedules import Schedules
from .resources.packages import Packages
from .resources.atoms import Atoms
from .resources.environments import Environments
from .resources.runtime_release import RuntimeRelease
from .resources.execute import Execute
from .resources.extensions import Extensions

class Boomi:
    """Fluent client for the Boomi Platform REST API."""

    def __init__(self, account_id: str, user: str, secret: str, *, retries: int = 3, timeout: int = 30):
        base = f"https://api.boomi.com/api/rest/v1/{account_id}"
        http = _HTTP(base, (user, secret), retries=retries, timeout=timeout)

        self.components = Components(http)
        self.folders = Folders(http)
        self.packages = Packages(http)
        self.deployments = Deployments(http)
        self.atoms = Atoms(http)
        self.environments = Environments(http)
        self.runs = Runs(http)
        self.schedules = Schedules(http)
        self.extensions = Extensions(http)
        self.runtime = RuntimeRelease(http)
        self.execute = Execute(http)

    # short‑hand constructor from env vars -------------------------------
    @classmethod
    def from_env(cls, prefix: str = "BOOMI_") -> "Boomi":
        import os
        try:
            acct = os.environ[f"{prefix}ACCOUNT"]
            user = os.environ[f"{prefix}USER"]
            pw = os.environ[f"{prefix}SECRET"]
        except KeyError as e:
            raise ValueError(f"Missing env var: {e}") from None
        return cls(acct, user, pw)