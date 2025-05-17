from .._http import _HTTP

class Environments:
    def __init__(self, http: _HTTP): self._ = http
    list = lambda s: s._.get("/Environment").json()