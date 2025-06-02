# EdiSegmentTerminator

**Properties**

| Name                       | Type                   | Required | Description |
| :------------------------- | :--------------------- | :------- | :---------- |
| segment_terminator_special | str                    | ❌       |             |
| segment_terminator_value   | SegmentTerminatorValue | ❌       |             |

# SegmentTerminatorValue

**Properties**

| Name           | Type | Required | Description      |
| :------------- | :--- | :------- | :--------------- |
| NEWLINE        | str  | ✅       | "newline"        |
| SINGLEQUOTE    | str  | ✅       | "singlequote"    |
| TILDE          | str  | ✅       | "tilde"          |
| CARRIAGERETURN | str  | ✅       | "carriagereturn" |
| BYTECHARACTER  | str  | ✅       | "bytecharacter"  |
| OTHERCHARACTER | str  | ✅       | "othercharacter" |

