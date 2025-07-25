# ComponentMetadata

**Properties**

| Name                          | Type                  | Required | Description                                                                                                                                                                                                                                                                                                                                                                |
| :---------------------------- | :-------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| branch_id                     | str                   | ❌       | If specified, the branch on which you want to manage the component.                                                                                                                                                                                                                                                                                                        |
| branch_name                   | str                   | ❌       |                                                                                                                                                                                                                                                                                                                                                                            |
| component_id                  | str                   | ❌       | Required. Read only. The ID of the component. The component ID is available on the Revision History dialog, which you can access from the Build page in the service.                                                                                                                                                                                                       |
| copied_from_component_id      | str                   | ❌       | Read only. If you copied the component, this field is the ID of the original component from where you copied the component.                                                                                                                                                                                                                                                |
| copied_from_component_version | int                   | ❌       | Read only. If you copied the component, this field is the revision number of the original component you copied.                                                                                                                                                                                                                                                            |
| created_by                    | str                   | ❌       | Read only. User name of the user who created the component.                                                                                                                                                                                                                                                                                                                |
| created_date                  | str                   | ❌       | Read only. Date and time.                                                                                                                                                                                                                                                                                                                                                  |
| current_version               | bool                  | ❌       | Read only. Indicates if the value specified in the version field is the most current and latest revision number created for the component on the **Build** tab. A value of True indicates that the revision number is the most current revision number on the **Build** tab, whereas False indicates that the version field value is not the most current revision number. |
| deleted                       | bool                  | ❌       | Read only. Indicates if the component is deleted. A value of True indicates a deleted status, whereas False indicates an active status.                                                                                                                                                                                                                                    |
| folder_id                     | str                   | ❌       | The ID of the folder where the component currently resides.                                                                                                                                                                                                                                                                                                                |
| folder_name                   | str                   | ❌       | Read only. The folder location of the component within Component Explorer.                                                                                                                                                                                                                                                                                                 |
| modified_by                   | str                   | ❌       | Read only. User name of the user who last modified the component.                                                                                                                                                                                                                                                                                                          |
| modified_date                 | str                   | ❌       | Read only. Date and time.                                                                                                                                                                                                                                                                                                                                                  |
| name                          | str                   | ❌       | Read only.                                                                                                                                                                                                                                                                                                                                                                 |
| sub_type                      | str                   | ❌       | Read only. Used by connector-related components \(connections and operations\) to identify the connector type. Subtype values are the internal connector ID, not the user-facing name.See [Connector object](/api/platformapi#tag/Connector).                                                                                                                              |
| type\_                        | ComponentMetadataType | ❌       | Read only. The type of component. See the section **Component Types** later in this topic for a complete list of component type values                                                                                                                                                                                                                                     |
| version                       | int                   | ❌       | Read only.                                                                                                                                                                                                                                                                                                                                                                 |

# ComponentMetadataType

Read only. The type of component. See the section **Component Types** later in this topic for a complete list of component type values

**Properties**

| Name               | Type | Required | Description           |
| :----------------- | :--- | :------- | :-------------------- |
| CERTIFICATE        | str  | ✅       | "certificate"         |
| CONNECTORACTION    | str  | ✅       | "connector-action"    |
| CONNECTORSETTINGS  | str  | ✅       | "connector-settings"  |
| CROSSREF           | str  | ✅       | "crossref"            |
| DOCUMENTCACHE      | str  | ✅       | "documentcache"       |
| TRANSFORMMAP       | str  | ✅       | "transform.map"       |
| TRANSFORMFUNCTION  | str  | ✅       | "transform.function"  |
| CERTIFICATEPGP     | str  | ✅       | "certificate.pgp"     |
| PROCESS            | str  | ✅       | "process"             |
| PROCESSPROPERTY    | str  | ✅       | "processproperty"     |
| PROFILEDB          | str  | ✅       | "profile.db"          |
| PROFILEEDI         | str  | ✅       | "profile.edi"         |
| PROFILEFLATFILE    | str  | ✅       | "profile.flatfile"    |
| PROFILEXML         | str  | ✅       | "profile.xml"         |
| PROFILEJSON        | str  | ✅       | "profile.json"        |
| QUEUE              | str  | ✅       | "queue"               |
| TRADINGPARTNER     | str  | ✅       | "tradingpartner"      |
| TPGROUP            | str  | ✅       | "tpgroup"             |
| TPORGANIZATION     | str  | ✅       | "tporganization"      |
| TPCOMMOPTIONS      | str  | ✅       | "tpcommoptions"       |
| WEBSERVICE         | str  | ✅       | "webservice"          |
| WEBSERVICEEXTERNAL | str  | ✅       | "webservice.external" |
| PROCESSROUTE       | str  | ✅       | "processroute"        |
| CUSTOMLIBRARY      | str  | ✅       | "customlibrary"       |
| EDISTANDARD        | str  | ✅       | "edistandard"         |
| FLOWSERVICE        | str  | ✅       | "flowservice"         |
| SCRIPTPROCESSING   | str  | ✅       | "script.processing"   |
| SCRIPTMAPPING      | str  | ✅       | "script.mapping"      |
| XSLT               | str  | ✅       | "xslt"                |

