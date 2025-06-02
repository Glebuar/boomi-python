# TradingPartnerComponent

**Properties**

| Name                        | Type                                  | Required | Description |
| :-------------------------- | :------------------------------------ | :------- | :---------- |
| contact_info                | ContactInfo                           | ✅       |             |
| partner_communication       | PartnerCommunication                  | ✅       |             |
| partner_document_types      | PartnerDocumentTypes                  | ✅       |             |
| partner_info                | PartnerInfo                           | ✅       |             |
| partner_communication_types | List[str]                             | ❌       |             |
| classification              | TradingPartnerComponentClassification | ❌       |             |
| component_id                | str                                   | ❌       |             |
| component_name              | str                                   | ❌       |             |
| deleted                     | bool                                  | ❌       |             |
| description                 | str                                   | ❌       |             |
| folder_id                   | int                                   | ❌       |             |
| folder_name                 | str                                   | ❌       |             |
| identifier                  | str                                   | ❌       |             |
| organization_id             | str                                   | ❌       |             |
| standard                    | TradingPartnerComponentStandard       | ❌       |             |

# TradingPartnerComponentClassification

**Properties**

| Name           | Type | Required | Description      |
| :------------- | :--- | :------- | :--------------- |
| TRADINGPARTNER | str  | ✅       | "tradingpartner" |
| MYCOMPANY      | str  | ✅       | "mycompany"      |

# TradingPartnerComponentStandard

**Properties**

| Name       | Type | Required | Description  |
| :--------- | :--- | :------- | :----------- |
| X12        | str  | ✅       | "x12"        |
| EDIFACT    | str  | ✅       | "edifact"    |
| HL7        | str  | ✅       | "hl7"        |
| CUSTOM     | str  | ✅       | "custom"     |
| ROSETTANET | str  | ✅       | "rosettanet" |
| TRADACOMS  | str  | ✅       | "tradacoms"  |
| ODETTE     | str  | ✅       | "odette"     |

