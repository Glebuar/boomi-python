import json
from unittest.mock import patch
import pytest
import requests

from boomi._http import _HTTP
from boomi.exceptions import AuthenticationError, RateLimitError


def make_response(status=200, content=b"{}"):
    resp = requests.Response()
    resp.status_code = status
    resp._content = content
    return resp


def test_as_dict_json():
    resp = make_response(content=b'{"a": 1}')
    assert _HTTP.as_dict(resp) == {"a": 1}


def test_as_dict_xml():
    xml = b"<root><a>1</a></root>"
    resp = make_response(content=xml)
    assert _HTTP.as_dict(resp) == {"root": {"a": "1"}}


def test_as_dict_empty():
    resp = make_response(content=b"", status=204)
    assert _HTTP.as_dict(resp) is None


def test_request_retries_on_429(monkeypatch):
    calls = []

    def fake_request(method, url, auth=None, timeout=None, **kw):
        resp = requests.Response()
        resp._content = b"{}"
        if not calls:
            resp.status_code = 429
        else:
            resp.status_code = 200
        calls.append(1)
        return resp

    monkeypatch.setattr(requests, "request", fake_request)
    http = _HTTP("https://api", ("u", "p"), retries=1)
    with patch("time.sleep") as ts:
        resp = http._request("GET", "/x")
        ts.assert_called_once()
    assert len(calls) == 2
    assert resp.status_code == 200


def test_request_authentication_error(monkeypatch):
    def fake_request(method, url, auth=None, timeout=None, **kw):
        return make_response(status=401)

    monkeypatch.setattr(requests, "request", fake_request)
    http = _HTTP("https://api", ("u", "p"))
    with pytest.raises(AuthenticationError):
        http._request("GET", "/x")


def test_paginate(monkeypatch):
    first = make_response(content=b'{"result": [1], "queryToken": "t"}')
    more = make_response(content=b'{"result": [2]}')

    http = _HTTP("https://api", ("u", "p"))
    monkeypatch.setattr(http, "post", lambda path, json=None: more)

    results = list(http.paginate(first))
    assert results == [1, 2]
