from .._http import _HTTP

class Folders:
    def __init__(self, http: _HTTP):
        self._ = http
    create = lambda s, name, parent=None: s._.post("/Folder", json={"name": name, **({"parentId": parent} if parent else {})}).json()
    get    = lambda s, fid: s._.get(f"/Folder/{fid}").json()
    delete = lambda s, fid: s._.delete(f"/Folder/{fid}")