# CompDiffConfig

**Properties**

| Name              | Type                        | Required | Description                                     |
| :---------------- | :-------------------------- | :------- | :---------------------------------------------- |
| comp_diff_element | List[CompDiffElement]       | ❌       |                                                 |
| component_type    | CompDiffConfigComponentType | ❌       | The type of component that you want to compare. |

# CompDiffConfigComponentType

The type of component that you want to compare.

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

