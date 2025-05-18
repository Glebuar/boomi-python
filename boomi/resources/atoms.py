from .._http import _HTTP

class Atoms:
    def __init__(self, http: _HTTP):
        self._http = http

    def list(self):
        return self._http.get("/Atom").json()
