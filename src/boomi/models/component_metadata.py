
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class ComponentMetadataType(Enum):
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
        return list(map(lambda x: x.value, ComponentMetadataType._member_map_.values()))


@JsonMap(
    {
        "branch_id": "branchId",
        "branch_name": "branchName",
        "component_id": "componentId",
        "copied_from_component_id": "copiedFromComponentId",
        "copied_from_component_version": "copiedFromComponentVersion",
        "created_by": "createdBy",
        "created_date": "createdDate",
        "current_version": "currentVersion",
        "folder_id": "folderId",
        "folder_name": "folderName",
        "modified_by": "modifiedBy",
        "modified_date": "modifiedDate",
        "sub_type": "subType",
        "type_": "type",
    }
)
class ComponentMetadata(BaseModel):
    """ComponentMetadata

    :param branch_id: If specified, the branch on which you want to manage the component., defaults to None
    :type branch_id: str, optional
    :param branch_name: branch_name, defaults to None
    :type branch_name: str, optional
    :param component_id: Required. Read only. The ID of the component. The component ID is available on the Revision History dialog, which you can access from the Build page in the service., defaults to None
    :type component_id: str, optional
    :param copied_from_component_id: Read only. If you copied the component, this field is the ID of the original component from where you copied the component., defaults to None
    :type copied_from_component_id: str, optional
    :param copied_from_component_version: Read only. If you copied the component, this field is the revision number of the original component you copied., defaults to None
    :type copied_from_component_version: int, optional
    :param created_by: Read only. User name of the user who created the component., defaults to None
    :type created_by: str, optional
    :param created_date: Read only. Date and time., defaults to None
    :type created_date: str, optional
    :param current_version: Read only. Indicates if the value specified in the version field is the most current and latest revision number created for the component on the **Build** tab. A value of True indicates that the revision number is the most current revision number on the **Build** tab, whereas False indicates that the version field value is not the most current revision number., defaults to None
    :type current_version: bool, optional
    :param deleted: Read only. Indicates if the component is deleted. A value of True indicates a deleted status, whereas False indicates an active status., defaults to None
    :type deleted: bool, optional
    :param folder_id: The ID of the folder where the component currently resides., defaults to None
    :type folder_id: str, optional
    :param folder_name: Read only. The folder location of the component within Component Explorer., defaults to None
    :type folder_name: str, optional
    :param modified_by: Read only. User name of the user who last modified the component., defaults to None
    :type modified_by: str, optional
    :param modified_date: Read only. Date and time., defaults to None
    :type modified_date: str, optional
    :param name: Read only., defaults to None
    :type name: str, optional
    :param sub_type: Read only. Used by connector-related components \(connections and operations\) to identify the connector type. Subtype values are the internal connector ID, not the user-facing name.See [Connector object](/api/platformapi#tag/Connector)., defaults to None
    :type sub_type: str, optional
    :param type_: Read only. The type of component. See the section **Component Types** later in this topic for a complete list of component type values, defaults to None
    :type type_: ComponentMetadataType, optional
    :param version: Read only., defaults to None
    :type version: int, optional
    """

    def __init__(
        self,
        branch_id: str = SENTINEL,
        branch_name: str = SENTINEL,
        component_id: str = SENTINEL,
        copied_from_component_id: str = SENTINEL,
        copied_from_component_version: int = SENTINEL,
        created_by: str = SENTINEL,
        created_date: str = SENTINEL,
        current_version: bool = SENTINEL,
        deleted: bool = SENTINEL,
        folder_id: str = SENTINEL,
        folder_name: str = SENTINEL,
        modified_by: str = SENTINEL,
        modified_date: str = SENTINEL,
        name: str = SENTINEL,
        sub_type: str = SENTINEL,
        type_: ComponentMetadataType = SENTINEL,
        version: int = SENTINEL,
        **kwargs
    ):
        """ComponentMetadata

        :param branch_id: If specified, the branch on which you want to manage the component., defaults to None
        :type branch_id: str, optional
        :param branch_name: branch_name, defaults to None
        :type branch_name: str, optional
        :param component_id: Required. Read only. The ID of the component. The component ID is available on the Revision History dialog, which you can access from the Build page in the service., defaults to None
        :type component_id: str, optional
        :param copied_from_component_id: Read only. If you copied the component, this field is the ID of the original component from where you copied the component., defaults to None
        :type copied_from_component_id: str, optional
        :param copied_from_component_version: Read only. If you copied the component, this field is the revision number of the original component you copied., defaults to None
        :type copied_from_component_version: int, optional
        :param created_by: Read only. User name of the user who created the component., defaults to None
        :type created_by: str, optional
        :param created_date: Read only. Date and time., defaults to None
        :type created_date: str, optional
        :param current_version: Read only. Indicates if the value specified in the version field is the most current and latest revision number created for the component on the **Build** tab. A value of True indicates that the revision number is the most current revision number on the **Build** tab, whereas False indicates that the version field value is not the most current revision number., defaults to None
        :type current_version: bool, optional
        :param deleted: Read only. Indicates if the component is deleted. A value of True indicates a deleted status, whereas False indicates an active status., defaults to None
        :type deleted: bool, optional
        :param folder_id: The ID of the folder where the component currently resides., defaults to None
        :type folder_id: str, optional
        :param folder_name: Read only. The folder location of the component within Component Explorer., defaults to None
        :type folder_name: str, optional
        :param modified_by: Read only. User name of the user who last modified the component., defaults to None
        :type modified_by: str, optional
        :param modified_date: Read only. Date and time., defaults to None
        :type modified_date: str, optional
        :param name: Read only., defaults to None
        :type name: str, optional
        :param sub_type: Read only. Used by connector-related components \(connections and operations\) to identify the connector type. Subtype values are the internal connector ID, not the user-facing name.See [Connector object](/api/platformapi#tag/Connector)., defaults to None
        :type sub_type: str, optional
        :param type_: Read only. The type of component. See the section **Component Types** later in this topic for a complete list of component type values, defaults to None
        :type type_: ComponentMetadataType, optional
        :param version: Read only., defaults to None
        :type version: int, optional
        """
        if branch_id is not SENTINEL:
            self.branch_id = branch_id
        if branch_name is not SENTINEL:
            self.branch_name = branch_name
        if component_id is not SENTINEL:
            self.component_id = component_id
        if copied_from_component_id is not SENTINEL:
            self.copied_from_component_id = copied_from_component_id
        if copied_from_component_version is not SENTINEL:
            self.copied_from_component_version = copied_from_component_version
        if created_by is not SENTINEL:
            self.created_by = created_by
        if created_date is not SENTINEL:
            self.created_date = created_date
        if current_version is not SENTINEL:
            self.current_version = current_version
        if deleted is not SENTINEL:
            self.deleted = deleted
        if folder_id is not SENTINEL:
            self.folder_id = folder_id
        if folder_name is not SENTINEL:
            self.folder_name = folder_name
        if modified_by is not SENTINEL:
            self.modified_by = modified_by
        if modified_date is not SENTINEL:
            self.modified_date = modified_date
        if name is not SENTINEL:
            self.name = name
        if sub_type is not SENTINEL:
            self.sub_type = sub_type
        if type_ is not SENTINEL:
            self.type_ = self._enum_matching(
                type_, ComponentMetadataType.list(), "type_"
            )
        if version is not SENTINEL:
            self.version = version
        self._kwargs = kwargs
