
from __future__ import annotations
from enum import Enum
from xml.etree import ElementTree as ET
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .encrypted_values import EncryptedValues
import warnings


class ComponentType(Enum):
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
        return list(map(lambda x: x.value, ComponentType._member_map_.values()))


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
        "encrypted_values": "encryptedValues",
        "process_overrides": "processOverrides",
        "folder_full_path": "folderFullPath",
    }
)
class Component(BaseModel):
    """Component

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
    :type type_: ComponentType, optional
    :param version: Read only., defaults to None
    :type version: int, optional
    :param encrypted_values: encrypted_values, defaults to None
    :type encrypted_values: EncryptedValues, optional
    :param description: If specified, the text description that appears at the top of an opened component.Optional for CREATE and UPDATE., defaults to None
    :type description: str, optional
    :param object: The XML structure of the component object. The structure of the object contents vary by component type. Required. Object name for specific component type. Determines the type of component to create and update. Recommend exporting existing components to determine values.   \>**Note:** These values are slightly different from Component/@type values (reference the [Component Metadata object](/api/platformapi#tag/ComponentMetadata) topic for more information)., defaults to None
    :type object: dict, optional
    :param process_overrides: For process type components, specifies overridden values (for example, variables overridden by environment extensions)., defaults to None
    :type process_overrides: dict, optional
    :param folder_full_path: \<br/\>version \<br/\>type \<br/\>createdDate \<br/\>createdBy \<br/\>modifiedDate \<br/\>modifiedBy \<br/\>Deleted \<br/\>currentVersion \<br/\>folderName \<br/\>folderFullPath.   Read-only system-generated values returned in the response. If included in the response, values for these fields are ignored., defaults to None
    :type folder_full_path: str, optional
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
        type_: ComponentType = SENTINEL,
        version: int = SENTINEL,
        encrypted_values: EncryptedValues = SENTINEL,
        description: str = SENTINEL,
        object: dict = SENTINEL,
        process_overrides: dict = SENTINEL,
        folder_full_path: str = SENTINEL,
        # Phase 2: XML preservation fields
        object_xml: str = SENTINEL,
        _object_element: ET.Element = SENTINEL,
        _original_xml: str = SENTINEL,
        **kwargs,
    ):
        """Component

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
        :type type_: ComponentType, optional
        :param version: Read only., defaults to None
        :type version: int, optional
        :param encrypted_values: encrypted_values, defaults to None
        :type encrypted_values: EncryptedValues, optional
        :param description: If specified, the text description that appears at the top of an opened component.Optional for CREATE and UPDATE., defaults to None
        :type description: str, optional
        :param object: The XML structure of the component object. The structure of the object contents vary by component type. Required. Object name for specific component type. Determines the type of component to create and update. Recommend exporting existing components to determine values.   \>**Note:** These values are slightly different from Component/@type values (reference the [Component Metadata object](/api/platformapi#tag/ComponentMetadata) topic for more information)., defaults to None
        :type object: dict, optional
        :param process_overrides: For process type components, specifies overridden values (for example, variables overridden by environment extensions)., defaults to None
        :type process_overrides: dict, optional
        :param folder_full_path: \<br/\>version \<br/\>type \<br/\>createdDate \<br/\>createdBy \<br/\>modifiedDate \<br/\>modifiedBy \<br/\>Deleted \<br/\>currentVersion \<br/\>folderName \<br/\>folderFullPath.   Read-only system-generated values returned in the response. If included in the response, values for these fields are ignored., defaults to None
        :type folder_full_path: str, optional
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
            self.current_version = self._define_bool("current_version", current_version, nullable=True)
        if deleted is not SENTINEL:
            self.deleted = self._define_bool("deleted", deleted, nullable=True)
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
            self.type_ = self._enum_matching(type_, ComponentType.list(), "type_")
        if version is not SENTINEL:
            self.version = version
        if encrypted_values is not SENTINEL:
            self.encrypted_values = self._define_object(
                encrypted_values, EncryptedValues
            )
        if description is not SENTINEL:
            self.description = description
        if object is not SENTINEL:
            self.object = object
        if process_overrides is not SENTINEL:
            self.process_overrides = process_overrides
        if folder_full_path is not SENTINEL:
            self.folder_full_path = folder_full_path
        
        # Phase 2: XML preservation fields
        if object_xml is not SENTINEL:
            self.object_xml = object_xml
        if _object_element is not SENTINEL:
            self._object_element = _object_element
        if _original_xml is not SENTINEL:
            self._original_xml = _original_xml
        
        self._kwargs = kwargs

    # ========== Phase 2: XML Preservation Methods ==========
    
    def to_xml(self) -> str:
        """Generate XML from Component model with preserved structure.
        
        This method creates a valid XML representation of the component by:
        1. Starting with the original XML structure (if available)
        2. Updating only the changed fields (name, description, etc.)
        3. Preserving the <object> structure exactly
        
        :return: Valid XML ready to send to the Boomi API
        :rtype: str
        """
        # If we have the original XML, use it as the base
        if hasattr(self, '_original_xml') and self._original_xml:
            root = ET.fromstring(self._original_xml)
        elif hasattr(self, '_object_element') and self._object_element:
            # Create from stored element (this is less common)
            root = self._object_element
        else:
            # Fallback: create minimal XML structure
            ns = "http://api.platform.boomi.com/"
            root = ET.Element(f"{{{ns}}}Component")
            root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
            root.set("xmlns:bns", ns)
        
        # Update component metadata fields
        if hasattr(self, 'component_id') and self.component_id:
            root.set('componentId', self.component_id)
        if hasattr(self, 'name') and self.name:
            root.set('name', self.name)
        if hasattr(self, 'type_') and self.type_:
            type_value = self.type_.value if hasattr(self.type_, 'value') else str(self.type_)
            root.set('type', type_value)
        if hasattr(self, 'folder_id') and self.folder_id:
            root.set('folderId', self.folder_id)
        if hasattr(self, 'folder_name') and self.folder_name:
            root.set('folderName', self.folder_name)
        if hasattr(self, 'folder_full_path') and self.folder_full_path:
            root.set('folderFullPath', self.folder_full_path)
        if hasattr(self, 'version') and self.version:
            root.set('version', str(self.version))
        if hasattr(self, 'created_date') and self.created_date:
            root.set('createdDate', self.created_date)
        if hasattr(self, 'created_by') and self.created_by:
            root.set('createdBy', self.created_by)
        if hasattr(self, 'modified_date') and self.modified_date:
            root.set('modifiedDate', self.modified_date)
        if hasattr(self, 'modified_by') and self.modified_by:
            root.set('modifiedBy', self.modified_by)
        if hasattr(self, 'deleted') and self.deleted is not None:
            root.set('deleted', str(self.deleted).lower())
        if hasattr(self, 'current_version') and self.current_version is not None:
            root.set('currentVersion', str(self.current_version).lower())
        if hasattr(self, 'branch_name') and self.branch_name:
            root.set('branchName', self.branch_name)
        if hasattr(self, 'branch_id') and self.branch_id:
            root.set('branchId', self.branch_id)
        
        # Handle description element
        if hasattr(self, 'description') and self.description:
            ns = "http://api.platform.boomi.com/"
            desc_elem = root.find(f"{{{ns}}}description")
            if desc_elem is None:
                # Create description element after encryptedValues
                encrypted_elem = root.find(f"{{{ns}}}encryptedValues")
                if encrypted_elem is not None:
                    idx = list(root).index(encrypted_elem) + 1
                    desc_elem = ET.Element(f"{{{ns}}}description")
                    root.insert(idx, desc_elem)
                else:
                    desc_elem = ET.SubElement(root, f"{{{ns}}}description")
            desc_elem.text = self.description
        
        # Preserve object XML if available
        if hasattr(self, 'object_xml') and self.object_xml:
            ns = "http://api.platform.boomi.com/"
            # Remove existing object element if present
            obj_elem = root.find(f"{{{ns}}}object")
            if obj_elem is not None:
                root.remove(obj_elem)
            
            # Parse and insert the stored object XML
            try:
                obj_root = ET.fromstring(f'<bns:object xmlns:bns="{ns}">{self.object_xml}</bns:object>')
                # Find the right position (after description, before processOverrides)
                process_overrides = root.find(f"{{{ns}}}processOverrides")
                if process_overrides is not None:
                    idx = list(root).index(process_overrides)
                    root.insert(idx, obj_root)
                else:
                    root.append(obj_root)
            except ET.ParseError:
                # If parsing fails, skip object XML
                pass
        
        # Ensure processOverrides element exists (even if empty)
        ns = "http://api.platform.boomi.com/"
        if root.find(f"{{{ns}}}processOverrides") is None:
            ET.SubElement(root, f"{{{ns}}}processOverrides")
        
        # Register namespaces for proper serialization
        ET.register_namespace("", "http://api.platform.boomi.com/")
        ET.register_namespace("bns", "http://api.platform.boomi.com/")
        
        return ET.tostring(root, encoding='unicode', xml_declaration=True)
    
    @property
    def object_deprecated(self) -> dict:
        """Access to object dict (deprecated).
        
        This property provides backward compatibility but warns users
        that dict-based object access is deprecated in favor of XML preservation.
        
        :return: Object dict for backward compatibility
        :rtype: dict
        """
        if hasattr(self, 'object') and self.object:
            warnings.warn(
                "Component.object as dict is deprecated. "
                "Use object_xml or raw XML methods for reliable updates.",
                DeprecationWarning,
                stacklevel=2
            )
            return self.object
        return {}
    
    def set_object_xml(self, xml: str):
        """Set the object XML content directly.
        
        This method allows you to set the object XML content while
        maintaining the XML structure exactly as provided.
        
        :param xml: XML string for the object content
        :type xml: str
        """
        self.object_xml = xml
        # Also try to parse as ElementTree for potential DOM operations
        try:
            if xml:
                # Store the inner content (without the wrapper)
                if xml.startswith('<') and '>' in xml:
                    self._object_element = ET.fromstring(xml)
        except ET.ParseError:
            # If parsing fails, just store the string
            self._object_element = None
