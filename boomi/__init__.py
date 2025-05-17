"""Unofficial Boomi Platform API SDK (package root).
Exposes the public :class:`Boomi` client plus common models & exceptions.
"""
from importlib import metadata as _md
from os import getenv as _ge

from .client import Boomi
from .exceptions import BoomiError, AuthenticationError, RateLimitError, ApiError  # noqa: F401
from .models import * 

__all__ = [
    "Boomi",
    "BoomiError",
    "AuthenticationError",
    "RateLimitError",
    "ApiError",
    *[name for name in globals().keys() if name[0].isupper()],
]

try:
    __version__ = _md.version("boomi")
except _md.PackageNotFoundError:
    __version__ = "0.0.0"

# ---------------------------------------------------------------------------
# Factory to build a client from environment variables (BOOMI_ACCOUNT / USER / SECRET)
# ---------------------------------------------------------------------------

def from_env(prefix: str = "BOOMI_") -> "Boomi":
    try:
        acct = _ge(f"{prefix}ACCOUNT")
        user = _ge(f"{prefix}USER")
        pw = _ge(f"{prefix}SECRET")
    except TypeError as e:
        raise BoomiError(f"Missing env var: {e}") from None
    if not all((acct, user, pw)):
        raise BoomiError("One or more BOOMI_ env‑vars undefined")
    from .client import Boomi as _Boomi
    return _Boomi(acct, user, pw)

# provide `Boomi.from_env()` alias
Boomi.from_env = staticmethod(from_env)