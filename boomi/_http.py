"""
Low-level HTTP helper for the Boomi SDK.

*   Adds exponential-back-off on 429
*   Provides `as_dict()` – JSON first, XML fallback, empty→None
"""

from __future__ import annotations
import time
from json import JSONDecodeError
from typing import Dict, Any, Generator, Optional

import requests
import xmltodict

from .exceptions import AuthenticationError, RateLimitError, ApiError


class _HTTP:
    def __init__(
        self,
        base: str,
        auth: tuple[str, str],
        *,
        retries: int = 3,
        timeout: int = 30,
    ):
        self.base = base.rstrip("/")
        self.auth = auth
        self.retries = retries
        self.timeout = timeout

        self.h_json = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        self.h_xml = {
            "Accept": "application/xml",
            "Content-Type": "application/xml",
        }

    # ------------------------------------------------------------------ #
    # Response → dict helper
    # ------------------------------------------------------------------ #
    @staticmethod
    def as_dict(resp: requests.Response) -> Optional[Dict[str, Any]]:
        """
        • If body is JSON → returns dict (regardless of Content-Type)
        • Else if body is XML  → xmltodict → dict
        • Else --> None  (empty 204 etc.)
        """
        if not resp.content:
            return None

        # 1) try JSON, ignore Content-Type
        try:
            return resp.json()
        except (ValueError, JSONDecodeError):
            pass

        # 2) fallback to XML
        try:
            xml_clean = resp.text.lstrip("\ufeff").strip()  # strip BOM/WS
            return xmltodict.parse(xml_clean)
        except Exception as exc:  # noqa: BLE001,E722
            raise ApiError("Unable to parse response as JSON or XML") from exc

    # ------------------------------------------------------------------ #
    # core request with retry on 429
    # ------------------------------------------------------------------ #
    def _request(self, method: str, path: str, **kw) -> requests.Response:
        url = f"{self.base}{path}"

        for attempt in range(self.retries + 1):
            resp = requests.request(
                method, url, auth=self.auth, timeout=self.timeout, **kw
            )

            if resp.status_code == 429:
                if attempt == self.retries:
                    raise RateLimitError(resp.text)
                time.sleep(2**attempt)
                continue

            if resp.status_code == 401:
                raise AuthenticationError(resp.text)
            if resp.status_code >= 400:
                raise ApiError(resp.text)
            return resp

        raise ApiError("Max retries exceeded")

    # ------------------------------------------------------------------ #
    # basic verbs
    # ------------------------------------------------------------------ #
    def get(self, path: str, **kw):
        kw.setdefault("headers", self.h_json)
        return self._request("GET", path, **kw)

    def post(self, path: str, **kw):
        # if caller passes explicit headers, respect them
        kw.setdefault("headers", self.h_json)
        return self._request("POST", path, **kw)

    def delete(self, path: str, **kw):
        kw.setdefault("headers", self.h_json)
        return self._request("DELETE", path, **kw)

    # ------------------------------------------------------------------ #
    # transparent pagination for /query + /queryMore
    # ------------------------------------------------------------------ #
    def paginate(
        self, first_resp: requests.Response
    ) -> Generator[Dict[str, Any], None, None]:
        data = first_resp.json()
        yield from data.get("result", [])
        token = data.get("queryToken")
        while token:
            more = self.post("/Component/queryMore", json={"queryToken": token})
            data = more.json()
            token = data.get("queryToken")
            yield from data.get("result", [])