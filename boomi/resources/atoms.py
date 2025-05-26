from .._http import _HTTP
from typing import List, Optional


class Atoms:

    def __init__(self, http: _HTTP):
        self._http = http

    def list(self, query_payload: Optional[dict]=None) ->List[dict]:
        if query_payload:
            return self._http.post('/Atom/query', json=query_payload).json()
        else:
            return self._http.get('/Atom').json()

    def post_atom_disable(self, atomid_val: str, payload: dict) ->dict:
        return self._http.post(f'/atom/{atomid_val}/disable', json=payload
            ).json()

    def post_atom_query(self, query_payload: dict) ->List[dict]:
        return self._http.post('/atom/query', json=query_payload).json()
