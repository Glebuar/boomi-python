from .._http import _HTTP

class Packages:
    def __init__(self, http: _HTTP):
        self._ = http
    create = lambda s, cid, ver=None, notes=None: s._.post("/PackagedComponent",
        json={"componentId": cid, **({"packageVersion": ver} if ver else {}), **({"notes": notes} if notes else {})}).json()