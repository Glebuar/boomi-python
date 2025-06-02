# Hl7Options

**Properties**

| Name                            | Type                               | Required | Description |
| :------------------------------ | :--------------------------------- | :------- | :---------- |
| composite_delimiter             | EdiDelimiter                       | ✅       |             |
| element_delimiter               | EdiDelimiter                       | ✅       |             |
| segment_terminator              | EdiSegmentTerminator               | ✅       |             |
| sub_composite_delimiter         | EdiDelimiter                       | ✅       |             |
| acceptackoption                 | Acceptackoption                    | ❌       |             |
| appackoption                    | Appackoption                       | ❌       |             |
| batchoption                     | Batchoption                        | ❌       |             |
| filteracknowledgements          | bool                               | ❌       |             |
| outbound_interchange_validation | bool                               | ❌       |             |
| outbound_validation_option      | Hl7OptionsOutboundValidationOption | ❌       |             |
| reject_duplicates               | bool                               | ❌       |             |

# Acceptackoption

**Properties**

| Name       | Type | Required | Description   |
| :--------- | :--- | :------- | :------------ |
| AL         | str  | ✅       | "AL"          |
| NE         | str  | ✅       | "NE"          |
| ER         | str  | ✅       | "ER"          |
| SU         | str  | ✅       | "SU"          |
| NOTDEFINED | str  | ✅       | "NOT_DEFINED" |

# Appackoption

**Properties**

| Name       | Type | Required | Description   |
| :--------- | :--- | :------- | :------------ |
| AL         | str  | ✅       | "AL"          |
| NE         | str  | ✅       | "NE"          |
| ER         | str  | ✅       | "ER"          |
| SU         | str  | ✅       | "SU"          |
| NOTDEFINED | str  | ✅       | "NOT_DEFINED" |

# Batchoption

**Properties**

| Name  | Type | Required | Description |
| :---- | :--- | :------- | :---------- |
| NONE  | str  | ✅       | "none"      |
| BATCH | str  | ✅       | "batch"     |

# Hl7OptionsOutboundValidationOption

**Properties**

| Name        | Type | Required | Description   |
| :---------- | :--- | :------- | :------------ |
| FILTERERROR | str  | ✅       | "filterError" |
| FAILALL     | str  | ✅       | "failAll"     |

