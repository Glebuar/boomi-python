# UnhControlInfo

**Properties**

| Name                | Type                            | Required | Description |
| :------------------ | :------------------------------ | :------- | :---------- |
| assoc_assigned_code | str                             | ❌       |             |
| common_access_ref   | str                             | ❌       |             |
| controlling_agency  | UnhControlInfoControllingAgency | ❌       |             |
| release             | UnhControlInfoRelease           | ❌       |             |
| version             | UnhControlInfoVersion           | ❌       |             |

# UnhControlInfoControllingAgency

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AA   | str  | ✅       | "AA"        |
| AB   | str  | ✅       | "AB"        |
| AC   | str  | ✅       | "AC"        |
| AD   | str  | ✅       | "AD"        |
| AE   | str  | ✅       | "AE"        |
| CC   | str  | ✅       | "CC"        |
| CE   | str  | ✅       | "CE"        |
| EC   | str  | ✅       | "EC"        |
| ED   | str  | ✅       | "ED"        |
| EE   | str  | ✅       | "EE"        |
| EN   | str  | ✅       | "EN"        |
| ER   | str  | ✅       | "ER"        |
| EU   | str  | ✅       | "EU"        |
| EX   | str  | ✅       | "EX"        |
| IA   | str  | ✅       | "IA"        |
| KE   | str  | ✅       | "KE"        |
| LI   | str  | ✅       | "LI"        |
| OD   | str  | ✅       | "OD"        |
| RI   | str  | ✅       | "RI"        |
| RT   | str  | ✅       | "RT"        |
| UN   | str  | ✅       | "UN"        |

# UnhControlInfoRelease

**Properties**

| Name              | Type | Required | Description          |
| :---------------- | :--- | :------- | :------------------- |
| EDIFACTRELEASE1   | str  | ✅       | "EDIFACTRELEASE_1"   |
| EDIFACTRELEASE2   | str  | ✅       | "EDIFACTRELEASE_2"   |
| EDIFACTRELEASE902 | str  | ✅       | "EDIFACTRELEASE_902" |
| EDIFACTRELEASE911 | str  | ✅       | "EDIFACTRELEASE_911" |
| EDIFACTRELEASE912 | str  | ✅       | "EDIFACTRELEASE_912" |
| EDIFACTRELEASE921 | str  | ✅       | "EDIFACTRELEASE_921" |
| EDIFACTRELEASE932 | str  | ✅       | "EDIFACTRELEASE_932" |
| EDIFACTRELEASE93A | str  | ✅       | "EDIFACTRELEASE_93A" |
| EDIFACTRELEASE94A | str  | ✅       | "EDIFACTRELEASE_94A" |
| EDIFACTRELEASE94B | str  | ✅       | "EDIFACTRELEASE_94B" |
| EDIFACTRELEASE95A | str  | ✅       | "EDIFACTRELEASE_95A" |
| EDIFACTRELEASE95B | str  | ✅       | "EDIFACTRELEASE_95B" |
| EDIFACTRELEASE96A | str  | ✅       | "EDIFACTRELEASE_96A" |
| EDIFACTRELEASE96B | str  | ✅       | "EDIFACTRELEASE_96B" |
| EDIFACTRELEASE97A | str  | ✅       | "EDIFACTRELEASE_97A" |
| EDIFACTRELEASE97B | str  | ✅       | "EDIFACTRELEASE_97B" |
| EDIFACTRELEASE98A | str  | ✅       | "EDIFACTRELEASE_98A" |
| EDIFACTRELEASE98B | str  | ✅       | "EDIFACTRELEASE_98B" |
| EDIFACTRELEASE99A | str  | ✅       | "EDIFACTRELEASE_99A" |
| EDIFACTRELEASE99B | str  | ✅       | "EDIFACTRELEASE_99B" |
| EDIFACTRELEASE00A | str  | ✅       | "EDIFACTRELEASE_00A" |
| EDIFACTRELEASE00B | str  | ✅       | "EDIFACTRELEASE_00B" |
| EDIFACTRELEASE01A | str  | ✅       | "EDIFACTRELEASE_01A" |
| EDIFACTRELEASE01B | str  | ✅       | "EDIFACTRELEASE_01B" |
| EDIFACTRELEASE02A | str  | ✅       | "EDIFACTRELEASE_02A" |
| EDIFACTRELEASE02B | str  | ✅       | "EDIFACTRELEASE_02B" |
| EDIFACTRELEASE03A | str  | ✅       | "EDIFACTRELEASE_03A" |
| EDIFACTRELEASE03B | str  | ✅       | "EDIFACTRELEASE_03B" |
| EDIFACTRELEASE04A | str  | ✅       | "EDIFACTRELEASE_04A" |
| EDIFACTRELEASE04B | str  | ✅       | "EDIFACTRELEASE_04B" |
| EDIFACTRELEASE05A | str  | ✅       | "EDIFACTRELEASE_05A" |
| EDIFACTRELEASE05B | str  | ✅       | "EDIFACTRELEASE_05B" |
| EDIFACTRELEASE06A | str  | ✅       | "EDIFACTRELEASE_06A" |
| EDIFACTRELEASE06B | str  | ✅       | "EDIFACTRELEASE_06B" |
| EDIFACTRELEASE07A | str  | ✅       | "EDIFACTRELEASE_07A" |
| EDIFACTRELEASE07B | str  | ✅       | "EDIFACTRELEASE_07B" |
| EDIFACTRELEASE08A | str  | ✅       | "EDIFACTRELEASE_08A" |
| EDIFACTRELEASE08B | str  | ✅       | "EDIFACTRELEASE_08B" |
| EDIFACTRELEASE09A | str  | ✅       | "EDIFACTRELEASE_09A" |
| EDIFACTRELEASE09B | str  | ✅       | "EDIFACTRELEASE_09B" |

# UnhControlInfoVersion

**Properties**

| Name             | Type | Required | Description         |
| :--------------- | :--- | :------- | :------------------ |
| EDIFACTVERSION1  | str  | ✅       | "EDIFACTVERSION_1"  |
| EDIFACTVERSION2  | str  | ✅       | "EDIFACTVERSION_2"  |
| EDIFACTVERSION4  | str  | ✅       | "EDIFACTVERSION_4"  |
| EDIFACTVERSION88 | str  | ✅       | "EDIFACTVERSION_88" |
| EDIFACTVERSION89 | str  | ✅       | "EDIFACTVERSION_89" |
| EDIFACTVERSION90 | str  | ✅       | "EDIFACTVERSION_90" |
| EDIFACTVERSIOND  | str  | ✅       | "EDIFACTVERSION_D"  |
| EDIFACTVERSIONS  | str  | ✅       | "EDIFACTVERSION_S"  |

