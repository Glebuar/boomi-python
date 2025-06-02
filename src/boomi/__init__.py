
"""SDK top level package."""

__all__ = ["Boomi", "BoomiAsync", "Environment"]

def __getattr__(name):
    if name == "Boomi":
        from .sdk import Boomi as _Boomi
        return _Boomi
    if name == "BoomiAsync":
        from .sdk_async import BoomiAsync as _BoomiAsync
        return _BoomiAsync
    if name == "Environment":
        from .net.environment import Environment as _Environment
        return _Environment
    raise AttributeError(name)
