# UnbControlInfo

**Properties**

| Name                         | Type                                     | Required | Description |
| :--------------------------- | :--------------------------------------- | :------- | :---------- |
| ack_request                  | bool                                     | ❌       |             |
| app_reference                | str                                      | ❌       |             |
| comm_agreement               | str                                      | ❌       |             |
| interchange_address          | str                                      | ❌       |             |
| interchange_id               | str                                      | ❌       |             |
| interchange_id_qual          | UnbControlInfoInterchangeIdQual          | ❌       |             |
| interchange_sub_address      | str                                      | ❌       |             |
| priority                     | UnbControlInfoPriority                   | ❌       |             |
| reference_password           | str                                      | ❌       |             |
| reference_password_qualifier | UnbControlInfoReferencePasswordQualifier | ❌       |             |
| syntax_id                    | UnbControlInfoSyntaxId                   | ❌       |             |
| syntax_version               | UnbControlInfoSyntaxVersion              | ❌       |             |
| test_indicator               | UnbControlInfoTestIndicator              | ❌       |             |

# UnbControlInfoInterchangeIdQual

**Properties**

| Name             | Type | Required | Description         |
| :--------------- | :--- | :------- | :------------------ |
| EDIFACTIDQUALNA  | str  | ✅       | "EDIFACTIDQUAL_NA"  |
| EDIFACTIDQUAL1   | str  | ✅       | "EDIFACTIDQUAL_1"   |
| EDIFACTIDQUAL4   | str  | ✅       | "EDIFACTIDQUAL_4"   |
| EDIFACTIDQUAL5   | str  | ✅       | "EDIFACTIDQUAL_5"   |
| EDIFACTIDQUAL8   | str  | ✅       | "EDIFACTIDQUAL_8"   |
| EDIFACTIDQUAL9   | str  | ✅       | "EDIFACTIDQUAL_9"   |
| EDIFACTIDQUAL12  | str  | ✅       | "EDIFACTIDQUAL_12"  |
| EDIFACTIDQUAL14  | str  | ✅       | "EDIFACTIDQUAL_14"  |
| EDIFACTIDQUAL18  | str  | ✅       | "EDIFACTIDQUAL_18"  |
| EDIFACTIDQUAL22  | str  | ✅       | "EDIFACTIDQUAL_22"  |
| EDIFACTIDQUAL30  | str  | ✅       | "EDIFACTIDQUAL_30"  |
| EDIFACTIDQUAL31  | str  | ✅       | "EDIFACTIDQUAL_31"  |
| EDIFACTIDQUAL33  | str  | ✅       | "EDIFACTIDQUAL_33"  |
| EDIFACTIDQUAL34  | str  | ✅       | "EDIFACTIDQUAL_34"  |
| EDIFACTIDQUAL51  | str  | ✅       | "EDIFACTIDQUAL_51"  |
| EDIFACTIDQUAL52  | str  | ✅       | "EDIFACTIDQUAL_52"  |
| EDIFACTIDQUAL53  | str  | ✅       | "EDIFACTIDQUAL_53"  |
| EDIFACTIDQUAL54  | str  | ✅       | "EDIFACTIDQUAL_54"  |
| EDIFACTIDQUAL55  | str  | ✅       | "EDIFACTIDQUAL_55"  |
| EDIFACTIDQUAL57  | str  | ✅       | "EDIFACTIDQUAL_57"  |
| EDIFACTIDQUAL58  | str  | ✅       | "EDIFACTIDQUAL_58"  |
| EDIFACTIDQUAL59  | str  | ✅       | "EDIFACTIDQUAL_59"  |
| EDIFACTIDQUAL61  | str  | ✅       | "EDIFACTIDQUAL_61"  |
| EDIFACTIDQUAL63  | str  | ✅       | "EDIFACTIDQUAL_63"  |
| EDIFACTIDQUAL65  | str  | ✅       | "EDIFACTIDQUAL_65"  |
| EDIFACTIDQUAL80  | str  | ✅       | "EDIFACTIDQUAL_80"  |
| EDIFACTIDQUAL82  | str  | ✅       | "EDIFACTIDQUAL_82"  |
| EDIFACTIDQUAL84  | str  | ✅       | "EDIFACTIDQUAL_84"  |
| EDIFACTIDQUAL85  | str  | ✅       | "EDIFACTIDQUAL_85"  |
| EDIFACTIDQUAL86  | str  | ✅       | "EDIFACTIDQUAL_86"  |
| EDIFACTIDQUAL87  | str  | ✅       | "EDIFACTIDQUAL_87"  |
| EDIFACTIDQUAL89  | str  | ✅       | "EDIFACTIDQUAL_89"  |
| EDIFACTIDQUAL90  | str  | ✅       | "EDIFACTIDQUAL_90"  |
| EDIFACTIDQUAL91  | str  | ✅       | "EDIFACTIDQUAL_91"  |
| EDIFACTIDQUAL92  | str  | ✅       | "EDIFACTIDQUAL_92"  |
| EDIFACTIDQUAL103 | str  | ✅       | "EDIFACTIDQUAL_103" |
| EDIFACTIDQUAL128 | str  | ✅       | "EDIFACTIDQUAL_128" |
| EDIFACTIDQUAL129 | str  | ✅       | "EDIFACTIDQUAL_129" |
| EDIFACTIDQUAL144 | str  | ✅       | "EDIFACTIDQUAL_144" |
| EDIFACTIDQUAL145 | str  | ✅       | "EDIFACTIDQUAL_145" |
| EDIFACTIDQUAL146 | str  | ✅       | "EDIFACTIDQUAL_146" |
| EDIFACTIDQUAL147 | str  | ✅       | "EDIFACTIDQUAL_147" |
| EDIFACTIDQUAL148 | str  | ✅       | "EDIFACTIDQUAL_148" |
| EDIFACTIDQUALZ01 | str  | ✅       | "EDIFACTIDQUAL_Z01" |
| EDIFACTIDQUALZZZ | str  | ✅       | "EDIFACTIDQUAL_ZZZ" |
| EDIFACTIDQUALZZ  | str  | ✅       | "EDIFACTIDQUAL_ZZ"  |

# UnbControlInfoPriority

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| NA   | str  | ✅       | "NA"        |
| A    | str  | ✅       | "A"         |

# UnbControlInfoReferencePasswordQualifier

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| NA   | str  | ✅       | "NA"        |
| AA   | str  | ✅       | "AA"        |
| BB   | str  | ✅       | "BB"        |

# UnbControlInfoSyntaxId

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| UNOA | str  | ✅       | "UNOA"      |
| UNOB | str  | ✅       | "UNOB"      |
| UNOC | str  | ✅       | "UNOC"      |
| UNOD | str  | ✅       | "UNOD"      |
| UNOE | str  | ✅       | "UNOE"      |
| UNOF | str  | ✅       | "UNOF"      |

# UnbControlInfoSyntaxVersion

**Properties**

| Name                  | Type | Required | Description              |
| :-------------------- | :--- | :------- | :----------------------- |
| EDIFACTSYNTAXVERSION1 | str  | ✅       | "EDIFACTSYNTAXVERSION_1" |
| EDIFACTSYNTAXVERSION2 | str  | ✅       | "EDIFACTSYNTAXVERSION_2" |
| EDIFACTSYNTAXVERSION3 | str  | ✅       | "EDIFACTSYNTAXVERSION_3" |

# UnbControlInfoTestIndicator

**Properties**

| Name          | Type | Required | Description      |
| :------------ | :--- | :------- | :--------------- |
| EDIFACTTESTNA | str  | ✅       | "EDIFACTTEST_NA" |
| EDIFACTTEST1  | str  | ✅       | "EDIFACTTEST_1"  |

