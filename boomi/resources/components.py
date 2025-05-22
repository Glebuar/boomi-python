from pathlib import Path
from typing import Union, BinaryIO
import xml.etree.ElementTree as ET
from .._http import _HTTP
from ..models.component import Component

_HDR_XML = {"Accept": "application/xml", "Content-Type": "application/xml"}

class Components:
    def __init__(self, http: _HTTP):
        self._http = http

    @staticmethod
    def _attrs(xml_bytes: bytes) -> dict:
        return dict(ET.fromstring(xml_bytes).attrib)

    # public
    def create(self, xml: Union[str, Path, BinaryIO]) -> Component:
        """Create a component from XML content."""
        xml_bytes = (
            xml.encode() if isinstance(xml, str)
            else xml.read_bytes() if isinstance(xml, Path)
            else xml.read()
        )
        r = self._http.post("/Component", data=xml_bytes, headers=_HDR_XML)
        return Component.model_validate(self._attrs(r.content))

    def get(self, cid: str) -> Component:
        """Retrieve component details by id."""
        r = self._http.get(f"/Component/{cid}", headers=_HDR_XML)
        return Component.model_validate(self._attrs(r.content))

    def update(self, cid: str, xml: Union[str, Path, BinaryIO]) -> Component:
        """Update a component with new XML content."""
        xml_bytes = (
            xml.encode() if isinstance(xml, str)
            else xml.read_bytes() if isinstance(xml, Path)
            else xml.read()
        )
        r = self._http.post(f"/Component/{cid}", data=xml_bytes, headers=_HDR_XML)
        return Component.model_validate(self._attrs(r.content))

    def delete(self, cid: str) -> bool:
        """Delete a component."""
        self._http.delete(f"/Component/{cid}")
        return True
