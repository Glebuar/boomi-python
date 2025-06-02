# OdetteOptions

**Properties**

| Name                            | Type                                  | Required | Description |
| :------------------------------ | :------------------------------------ | :------- | :---------- |
| composite_delimiter             | EdiDelimiter                          | ✅       |             |
| element_delimiter               | EdiDelimiter                          | ✅       |             |
| segment_terminator              | EdiSegmentTerminator                  | ✅       |             |
| acknowledgementoption           | OdetteOptionsAcknowledgementoption    | ❌       |             |
| envelopeoption                  | OdetteOptionsEnvelopeoption           | ❌       |             |
| filteracknowledgements          | bool                                  | ❌       |             |
| include_una                     | bool                                  | ❌       |             |
| outbound_interchange_validation | bool                                  | ❌       |             |
| outbound_validation_option      | OdetteOptionsOutboundValidationOption | ❌       |             |
| reject_duplicate_unb            | bool                                  | ❌       |             |

# OdetteOptionsAcknowledgementoption

**Properties**

| Name         | Type | Required | Description    |
| :----------- | :--- | :------- | :------------- |
| DONOTACKITEM | str  | ✅       | "donotackitem" |
| ACKITEM      | str  | ✅       | "ackitem"      |

# OdetteOptionsEnvelopeoption

**Properties**

| Name         | Type | Required | Description    |
| :----------- | :--- | :------- | :------------- |
| GROUPALL     | str  | ✅       | "groupall"     |
| GROUPMESSAGE | str  | ✅       | "groupmessage" |

# OdetteOptionsOutboundValidationOption

**Properties**

| Name        | Type | Required | Description   |
| :---------- | :--- | :------- | :------------ |
| FILTERERROR | str  | ✅       | "filterError" |
| FAILALL     | str  | ✅       | "failAll"     |

