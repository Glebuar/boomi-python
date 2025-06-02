# EdifactOptions

**Properties**

| Name                            | Type                                   | Required | Description |
| :------------------------------ | :------------------------------------- | :------- | :---------- |
| composite_delimiter             | EdiDelimiter                           | ✅       |             |
| element_delimiter               | EdiDelimiter                           | ✅       |             |
| segment_terminator              | EdiSegmentTerminator                   | ✅       |             |
| acknowledgementoption           | EdifactOptionsAcknowledgementoption    | ❌       |             |
| envelopeoption                  | EdifactOptionsEnvelopeoption           | ❌       |             |
| filteracknowledgements          | bool                                   | ❌       |             |
| include_una                     | bool                                   | ❌       |             |
| outbound_interchange_validation | bool                                   | ❌       |             |
| outbound_validation_option      | EdifactOptionsOutboundValidationOption | ❌       |             |
| reject_duplicate_unb            | bool                                   | ❌       |             |

# EdifactOptionsAcknowledgementoption

**Properties**

| Name         | Type | Required | Description    |
| :----------- | :--- | :------- | :------------- |
| DONOTACKITEM | str  | ✅       | "donotackitem" |
| ACKITEM      | str  | ✅       | "ackitem"      |

# EdifactOptionsEnvelopeoption

**Properties**

| Name         | Type | Required | Description    |
| :----------- | :--- | :------- | :------------- |
| GROUPALL     | str  | ✅       | "groupall"     |
| GROUPFG      | str  | ✅       | "groupfg"      |
| GROUPMESSAGE | str  | ✅       | "groupmessage" |

# EdifactOptionsOutboundValidationOption

**Properties**

| Name        | Type | Required | Description   |
| :---------- | :--- | :------- | :------------ |
| FILTERERROR | str  | ✅       | "filterError" |
| FAILALL     | str  | ✅       | "failAll"     |

