# IsaControlInfo

**Properties**

| Name                                | Type                              | Required | Description |
| :---------------------------------- | :-------------------------------- | :------- | :---------- |
| ackrequested                        | bool                              | ❌       |             |
| authorization_information           | str                               | ❌       |             |
| authorization_information_qualifier | AuthorizationInformationQualifier | ❌       |             |
| component_element_separator         | str                               | ❌       |             |
| interchange_id                      | str                               | ❌       |             |
| interchange_id_qualifier            | InterchangeIdQualifier            | ❌       |             |
| security_information                | str                               | ❌       |             |
| security_information_qualifier      | SecurityInformationQualifier      | ❌       |             |
| standard_identification             | str                               | ❌       |             |
| testindicator                       | Testindicator                     | ❌       |             |
| version                             | str                               | ❌       |             |

# AuthorizationInformationQualifier

**Properties**

| Name          | Type | Required | Description      |
| :------------ | :--- | :------- | :--------------- |
| X12AUTHQUAL00 | str  | ✅       | "X12AUTHQUAL_00" |
| X12AUTHQUAL01 | str  | ✅       | "X12AUTHQUAL_01" |
| X12AUTHQUAL02 | str  | ✅       | "X12AUTHQUAL_02" |
| X12AUTHQUAL03 | str  | ✅       | "X12AUTHQUAL_03" |
| X12AUTHQUAL04 | str  | ✅       | "X12AUTHQUAL_04" |
| X12AUTHQUAL05 | str  | ✅       | "X12AUTHQUAL_05" |

# InterchangeIdQualifier

**Properties**

| Name        | Type | Required | Description    |
| :---------- | :--- | :------- | :------------- |
| X12IDQUAL01 | str  | ✅       | "X12IDQUAL_01" |
| X12IDQUAL02 | str  | ✅       | "X12IDQUAL_02" |
| X12IDQUAL03 | str  | ✅       | "X12IDQUAL_03" |
| X12IDQUAL04 | str  | ✅       | "X12IDQUAL_04" |
| X12IDQUAL07 | str  | ✅       | "X12IDQUAL_07" |
| X12IDQUAL08 | str  | ✅       | "X12IDQUAL_08" |
| X12IDQUAL09 | str  | ✅       | "X12IDQUAL_09" |
| X12IDQUAL10 | str  | ✅       | "X12IDQUAL_10" |
| X12IDQUAL11 | str  | ✅       | "X12IDQUAL_11" |
| X12IDQUAL12 | str  | ✅       | "X12IDQUAL_12" |
| X12IDQUAL13 | str  | ✅       | "X12IDQUAL_13" |
| X12IDQUAL14 | str  | ✅       | "X12IDQUAL_14" |
| X12IDQUAL15 | str  | ✅       | "X12IDQUAL_15" |
| X12IDQUAL16 | str  | ✅       | "X12IDQUAL_16" |
| X12IDQUAL17 | str  | ✅       | "X12IDQUAL_17" |
| X12IDQUAL18 | str  | ✅       | "X12IDQUAL_18" |
| X12IDQUAL19 | str  | ✅       | "X12IDQUAL_19" |
| X12IDQUAL20 | str  | ✅       | "X12IDQUAL_20" |
| X12IDQUAL21 | str  | ✅       | "X12IDQUAL_21" |
| X12IDQUAL22 | str  | ✅       | "X12IDQUAL_22" |
| X12IDQUAL23 | str  | ✅       | "X12IDQUAL_23" |
| X12IDQUAL24 | str  | ✅       | "X12IDQUAL_24" |
| X12IDQUAL25 | str  | ✅       | "X12IDQUAL_25" |
| X12IDQUAL26 | str  | ✅       | "X12IDQUAL_26" |
| X12IDQUAL27 | str  | ✅       | "X12IDQUAL_27" |
| X12IDQUAL28 | str  | ✅       | "X12IDQUAL_28" |
| X12IDQUAL29 | str  | ✅       | "X12IDQUAL_29" |
| X12IDQUAL30 | str  | ✅       | "X12IDQUAL_30" |
| X12IDQUAL31 | str  | ✅       | "X12IDQUAL_31" |
| X12IDQUAL32 | str  | ✅       | "X12IDQUAL_32" |
| X12IDQUAL33 | str  | ✅       | "X12IDQUAL_33" |
| X12IDQUAL34 | str  | ✅       | "X12IDQUAL_34" |
| X12IDQUALNR | str  | ✅       | "X12IDQUAL_NR" |
| X12IDQUALZZ | str  | ✅       | "X12IDQUAL_ZZ" |

# SecurityInformationQualifier

**Properties**

| Name         | Type | Required | Description     |
| :----------- | :--- | :------- | :-------------- |
| X12SECQUAL00 | str  | ✅       | "X12SECQUAL_00" |
| X12SECQUAL01 | str  | ✅       | "X12SECQUAL_01" |

# Testindicator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| P    | str  | ✅       | "P"         |
| T    | str  | ✅       | "T"         |

