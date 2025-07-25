# OdetteUnbControlInfo

**Properties**

| Name                         | Type                                           | Required | Description |
| :--------------------------- | :--------------------------------------------- | :------- | :---------- |
| ack_request                  | bool                                           | ❌       |             |
| app_reference                | str                                            | ❌       |             |
| comm_agreement               | str                                            | ❌       |             |
| interchange_address          | str                                            | ❌       |             |
| interchange_id               | str                                            | ❌       |             |
| interchange_id_qual          | OdetteUnbControlInfoInterchangeIdQual          | ❌       |             |
| interchange_sub_address      | str                                            | ❌       |             |
| priority                     | OdetteUnbControlInfoPriority                   | ❌       |             |
| reference_password           | str                                            | ❌       |             |
| reference_password_qualifier | OdetteUnbControlInfoReferencePasswordQualifier | ❌       |             |
| syntax_id                    | OdetteUnbControlInfoSyntaxId                   | ❌       |             |
| syntax_version               | OdetteUnbControlInfoSyntaxVersion              | ❌       |             |
| test_indicator               | OdetteUnbControlInfoTestIndicator              | ❌       |             |

# OdetteUnbControlInfoInterchangeIdQual

**Properties**

| Name            | Type | Required | Description        |
| :-------------- | :--- | :------- | :----------------- |
| ODETTEIDQUALNA  | str  | ✅       | "ODETTEIDQUAL_NA"  |
| ODETTEIDQUAL1   | str  | ✅       | "ODETTEIDQUAL_1"   |
| ODETTEIDQUAL4   | str  | ✅       | "ODETTEIDQUAL_4"   |
| ODETTEIDQUAL5   | str  | ✅       | "ODETTEIDQUAL_5"   |
| ODETTEIDQUAL8   | str  | ✅       | "ODETTEIDQUAL_8"   |
| ODETTEIDQUAL9   | str  | ✅       | "ODETTEIDQUAL_9"   |
| ODETTEIDQUAL12  | str  | ✅       | "ODETTEIDQUAL_12"  |
| ODETTEIDQUAL14  | str  | ✅       | "ODETTEIDQUAL_14"  |
| ODETTEIDQUAL18  | str  | ✅       | "ODETTEIDQUAL_18"  |
| ODETTEIDQUAL22  | str  | ✅       | "ODETTEIDQUAL_22"  |
| ODETTEIDQUAL30  | str  | ✅       | "ODETTEIDQUAL_30"  |
| ODETTEIDQUAL31  | str  | ✅       | "ODETTEIDQUAL_31"  |
| ODETTEIDQUAL33  | str  | ✅       | "ODETTEIDQUAL_33"  |
| ODETTEIDQUAL34  | str  | ✅       | "ODETTEIDQUAL_34"  |
| ODETTEIDQUAL51  | str  | ✅       | "ODETTEIDQUAL_51"  |
| ODETTEIDQUAL52  | str  | ✅       | "ODETTEIDQUAL_52"  |
| ODETTEIDQUAL53  | str  | ✅       | "ODETTEIDQUAL_53"  |
| ODETTEIDQUAL54  | str  | ✅       | "ODETTEIDQUAL_54"  |
| ODETTEIDQUAL55  | str  | ✅       | "ODETTEIDQUAL_55"  |
| ODETTEIDQUAL57  | str  | ✅       | "ODETTEIDQUAL_57"  |
| ODETTEIDQUAL58  | str  | ✅       | "ODETTEIDQUAL_58"  |
| ODETTEIDQUAL59  | str  | ✅       | "ODETTEIDQUAL_59"  |
| ODETTEIDQUAL61  | str  | ✅       | "ODETTEIDQUAL_61"  |
| ODETTEIDQUAL63  | str  | ✅       | "ODETTEIDQUAL_63"  |
| ODETTEIDQUAL65  | str  | ✅       | "ODETTEIDQUAL_65"  |
| ODETTEIDQUAL80  | str  | ✅       | "ODETTEIDQUAL_80"  |
| ODETTEIDQUAL82  | str  | ✅       | "ODETTEIDQUAL_82"  |
| ODETTEIDQUAL84  | str  | ✅       | "ODETTEIDQUAL_84"  |
| ODETTEIDQUAL85  | str  | ✅       | "ODETTEIDQUAL_85"  |
| ODETTEIDQUAL86  | str  | ✅       | "ODETTEIDQUAL_86"  |
| ODETTEIDQUAL87  | str  | ✅       | "ODETTEIDQUAL_87"  |
| ODETTEIDQUAL89  | str  | ✅       | "ODETTEIDQUAL_89"  |
| ODETTEIDQUAL90  | str  | ✅       | "ODETTEIDQUAL_90"  |
| ODETTEIDQUAL91  | str  | ✅       | "ODETTEIDQUAL_91"  |
| ODETTEIDQUAL92  | str  | ✅       | "ODETTEIDQUAL_92"  |
| ODETTEIDQUAL103 | str  | ✅       | "ODETTEIDQUAL_103" |
| ODETTEIDQUAL128 | str  | ✅       | "ODETTEIDQUAL_128" |
| ODETTEIDQUAL129 | str  | ✅       | "ODETTEIDQUAL_129" |
| ODETTEIDQUAL144 | str  | ✅       | "ODETTEIDQUAL_144" |
| ODETTEIDQUAL145 | str  | ✅       | "ODETTEIDQUAL_145" |
| ODETTEIDQUAL146 | str  | ✅       | "ODETTEIDQUAL_146" |
| ODETTEIDQUAL147 | str  | ✅       | "ODETTEIDQUAL_147" |
| ODETTEIDQUAL148 | str  | ✅       | "ODETTEIDQUAL_148" |
| ODETTEIDQUALZ01 | str  | ✅       | "ODETTEIDQUAL_Z01" |
| ODETTEIDQUALZZZ | str  | ✅       | "ODETTEIDQUAL_ZZZ" |
| ODETTEIDQUALZZ  | str  | ✅       | "ODETTEIDQUAL_ZZ"  |

# OdetteUnbControlInfoPriority

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| NA   | str  | ✅       | "NA"        |
| A    | str  | ✅       | "A"         |

# OdetteUnbControlInfoReferencePasswordQualifier

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| NA   | str  | ✅       | "NA"        |
| AA   | str  | ✅       | "AA"        |
| BB   | str  | ✅       | "BB"        |

# OdetteUnbControlInfoSyntaxId

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| UNOA | str  | ✅       | "UNOA"      |
| UNOB | str  | ✅       | "UNOB"      |
| UNOC | str  | ✅       | "UNOC"      |
| UNOD | str  | ✅       | "UNOD"      |
| UNOE | str  | ✅       | "UNOE"      |
| UNOF | str  | ✅       | "UNOF"      |

# OdetteUnbControlInfoSyntaxVersion

**Properties**

| Name                 | Type | Required | Description             |
| :------------------- | :--- | :------- | :---------------------- |
| ODETTESYNTAXVERSION1 | str  | ✅       | "ODETTESYNTAXVERSION_1" |
| ODETTESYNTAXVERSION2 | str  | ✅       | "ODETTESYNTAXVERSION_2" |
| ODETTESYNTAXVERSION3 | str  | ✅       | "ODETTESYNTAXVERSION_3" |

# OdetteUnbControlInfoTestIndicator

**Properties**

| Name         | Type | Required | Description     |
| :----------- | :--- | :------- | :-------------- |
| ODETTETESTNA | str  | ✅       | "ODETTETEST_NA" |
| ODETTETEST1  | str  | ✅       | "ODETTETEST_1"  |

