# X12Options

**Properties**

| Name                            | Type                               | Required | Description |
| :------------------------------ | :--------------------------------- | :------- | :---------- |
| element_delimiter               | EdiDelimiter                       | ✅       |             |
| segment_terminator              | EdiSegmentTerminator               | ✅       |             |
| acknowledgementoption           | X12OptionsAcknowledgementoption    | ❌       |             |
| envelopeoption                  | X12OptionsEnvelopeoption           | ❌       |             |
| filteracknowledgements          | bool                               | ❌       |             |
| outbound_interchange_validation | bool                               | ❌       |             |
| outbound_validation_option      | X12OptionsOutboundValidationOption | ❌       |             |
| reject_duplicate_interchange    | bool                               | ❌       |             |

# X12OptionsAcknowledgementoption

**Properties**

| Name         | Type | Required | Description    |
| :----------- | :--- | :------- | :------------- |
| DONOTACKITEM | str  | ✅       | "donotackitem" |
| ACKFUNCITEM  | str  | ✅       | "ackfuncitem"  |
| ACKTRANITEM  | str  | ✅       | "acktranitem"  |

# X12OptionsEnvelopeoption

**Properties**

| Name     | Type | Required | Description |
| :------- | :--- | :------- | :---------- |
| GROUPALL | str  | ✅       | "groupall"  |
| GROUPFG  | str  | ✅       | "groupfg"   |
| GROUPST  | str  | ✅       | "groupst"   |

# X12OptionsOutboundValidationOption

**Properties**

| Name        | Type | Required | Description   |
| :---------- | :--- | :------- | :------------ |
| FILTERERROR | str  | ✅       | "filterError" |
| FAILALL     | str  | ✅       | "failAll"     |

