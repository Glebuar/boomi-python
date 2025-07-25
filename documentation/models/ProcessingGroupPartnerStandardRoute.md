# ProcessingGroupPartnerStandardRoute

**Properties**

| Name                | Type                                        | Required | Description |
| :------------------ | :------------------------------------------ | :------- | :---------- |
| document_type_route | List[ProcessingGroupPartnerDocumentRoute]   | ❌       |             |
| process_id          | str                                         | ❌       |             |
| standard            | ProcessingGroupPartnerStandardRouteStandard | ❌       |             |

# ProcessingGroupPartnerStandardRouteStandard

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

