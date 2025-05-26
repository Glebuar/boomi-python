from .._http import _HTTP


class Accounts:

    def __init__(self, http: _HTTP):
        self._http = http

    def get_account_details(self, accountid_val: str) ->dict:
        return self._http.get(f'/account/{accountid_val}/details').json()

    def get_account_list(self) ->List[dict]:
        return self._http.get('/account').json()
