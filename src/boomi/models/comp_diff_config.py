
from __future__ import annotations
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .comp_diff_element import CompDiffElement


class CompDiffConfigComponentType(Enum):
    """An enumeration representing different categories.

    :cvar CERTIFICATE: "certificate"
    :vartype CERTIFICATE: str
    :cvar CONNECTORACTION: "connector-action"
    :vartype CONNECTORACTION: str
    :cvar CONNECTORSETTINGS: "connector-settings"
    :vartype CONNECTORSETTINGS: str
    :cvar CROSSREF: "crossref"
    :vartype CROSSREF: str
    :cvar DOCUMENTCACHE: "documentcache"
    :vartype DOCUMENTCACHE: str
    :cvar TRANSFORMMAP: "transform.map"
    :vartype TRANSFORMMAP: str
    :cvar TRANSFORMFUNCTION: "transform.function"
    :vartype TRANSFORMFUNCTION: str
    :cvar CERTIFICATEPGP: "certificate.pgp"
    :vartype CERTIFICATEPGP: str
    :cvar PROCESS: "process"
    :vartype PROCESS: str
    :cvar PROCESSPROPERTY: "processproperty"
    :vartype PROCESSPROPERTY: str
    :cvar PROFILEDB: "profile.db"
    :vartype PROFILEDB: str
    :cvar PROFILEEDI: "profile.edi"
    :vartype PROFILEEDI: str
    :cvar PROFILEFLATFILE: "profile.flatfile"
    :vartype PROFILEFLATFILE: str
    :cvar PROFILEXML: "profile.xml"
    :vartype PROFILEXML: str
    :cvar PROFILEJSON: "profile.json"
    :vartype PROFILEJSON: str
    :cvar QUEUE: "queue"
    :vartype QUEUE: str
    :cvar TRADINGPARTNER: "tradingpartner"
    :vartype TRADINGPARTNER: str
    :cvar TPGROUP: "tpgroup"
    :vartype TPGROUP: str
    :cvar TPORGANIZATION: "tporganization"
    :vartype TPORGANIZATION: str
    :cvar TPCOMMOPTIONS: "tpcommoptions"
    :vartype TPCOMMOPTIONS: str
    :cvar WEBSERVICE: "webservice"
    :vartype WEBSERVICE: str
    :cvar WEBSERVICEEXTERNAL: "webservice.external"
    :vartype WEBSERVICEEXTERNAL: str
    :cvar PROCESSROUTE: "processroute"
    :vartype PROCESSROUTE: str
    :cvar CUSTOMLIBRARY: "customlibrary"
    :vartype CUSTOMLIBRARY: str
    :cvar EDISTANDARD: "edistandard"
    :vartype EDISTANDARD: str
    :cvar FLOWSERVICE: "flowservice"
    :vartype FLOWSERVICE: str
    :cvar SCRIPTPROCESSING: "script.processing"
    :vartype SCRIPTPROCESSING: str
    :cvar SCRIPTMAPPING: "script.mapping"
    :vartype SCRIPTMAPPING: str
    :cvar XSLT: "xslt"
    :vartype XSLT: str
    """

    CERTIFICATE = "certificate"
    CONNECTORACTION = "connector-action"
    CONNECTORSETTINGS = "connector-settings"
    CROSSREF = "crossref"
    DOCUMENTCACHE = "documentcache"
    TRANSFORMMAP = "transform.map"
    TRANSFORMFUNCTION = "transform.function"
    CERTIFICATEPGP = "certificate.pgp"
    PROCESS = "process"
    PROCESSPROPERTY = "processproperty"
    PROFILEDB = "profile.db"
    PROFILEEDI = "profile.edi"
    PROFILEFLATFILE = "profile.flatfile"
    PROFILEXML = "profile.xml"
    PROFILEJSON = "profile.json"
    QUEUE = "queue"
    TRADINGPARTNER = "tradingpartner"
    TPGROUP = "tpgroup"
    TPORGANIZATION = "tporganization"
    TPCOMMOPTIONS = "tpcommoptions"
    WEBSERVICE = "webservice"
    WEBSERVICEEXTERNAL = "webservice.external"
    PROCESSROUTE = "processroute"
    CUSTOMLIBRARY = "customlibrary"
    EDISTANDARD = "edistandard"
    FLOWSERVICE = "flowservice"
    SCRIPTPROCESSING = "script.processing"
    SCRIPTMAPPING = "script.mapping"
    XSLT = "xslt"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, CompDiffConfigComponentType._member_map_.values())
        )


@JsonMap({"comp_diff_element": "CompDiffElement", "component_type": "componentType"})
class CompDiffConfig(BaseModel):
    """CompDiffConfig

    :param comp_diff_element: comp_diff_element, defaults to None
    :type comp_diff_element: List[CompDiffElement], optional
    :param component_type: The type of component that you want to compare., defaults to None
    :type component_type: CompDiffConfigComponentType, optional
    """

    def __init__(
        self,
        comp_diff_element: List[CompDiffElement] = SENTINEL,
        component_type: CompDiffConfigComponentType = SENTINEL,
        **kwargs,
    ):
        """CompDiffConfig

        :param comp_diff_element: comp_diff_element, defaults to None
        :type comp_diff_element: List[CompDiffElement], optional
        :param component_type: The type of component that you want to compare., defaults to None
        :type component_type: CompDiffConfigComponentType, optional
        """
        if comp_diff_element is not SENTINEL:
            self.comp_diff_element = self._define_list(
                comp_diff_element, CompDiffElement
            )
        if component_type is not SENTINEL:
            self.component_type = self._enum_matching(
                component_type, CompDiffConfigComponentType.list(), "component_type"
            )
        self._kwargs = kwargs
