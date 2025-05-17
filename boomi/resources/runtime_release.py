from .._http import _HTTP

class RuntimeRelease:
    _P = "/RuntimeReleaseSchedule"
    def __init__(self, http: _HTTP):
        self._ = http
    create = lambda s, body: s._.post(s._P, json=body).json()
    get    = lambda s, cid: s._.get(f"{s._P}/{cid}").json()
    update = lambda s, cid, body: s._.post(f"{s._P}/{cid}", json=body).json()
    delete = lambda s, cid: s._.delete(f"{s._P}/{cid}")