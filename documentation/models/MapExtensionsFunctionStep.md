# MapExtensionsFunctionStep

**Properties**

| Name          | Type                               | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                               |
| :------------ | :--------------------------------- | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| configuration | MapExtensionsConfiguration         | ✅       |                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| inputs        | MapExtensionsInputs                | ✅       | Lists the function's input and outputs according to their user-given names and keys. You must list inputs and outputs sequentially in order according to their key values. When creating or updating functions, it requires all input and output values in the request regardless if they are to be mapped or populated with a default value. The maximum number of inputs or outputs is 100.                                             |
| outputs       | MapExtensionsOutputs               | ✅       | Lists the function's input and outputs according to their user-given names and keys. You must list inputs and outputs sequentially in order according to their key values. See the following row for more information. When creating or updating functions, it requires all input and output values in the request regardless if they are to be mapped or populated with a default value. The maximum number of inputs or outputs is 100. |
| cache_type    | MapExtensionsFunctionStepCacheType | ❌       |                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| id\_          | str                                | ❌       |                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| position      | int                                | ❌       |                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| type\_        | MapExtensionsFunctionStepType      | ❌       |                                                                                                                                                                                                                                                                                                                                                                                                                                           |

# MapExtensionsFunctionStepCacheType

**Properties**

| Name       | Type | Required | Description  |
| :--------- | :--- | :------- | :----------- |
| NONE       | str  | ✅       | "None"       |
| BYDOCUMENT | str  | ✅       | "ByDocument" |
| BYMAP      | str  | ✅       | "ByMap"      |

# MapExtensionsFunctionStepType

**Properties**

| Name                        | Type | Required | Description                   |
| :-------------------------- | :--- | :------- | :---------------------------- |
| COUNT                       | str  | ✅       | "Count"                       |
| CURRENTDATE                 | str  | ✅       | "CurrentDate"                 |
| DATEFORMAT                  | str  | ✅       | "DateFormat"                  |
| LEFTTRIM                    | str  | ✅       | "LeftTrim"                    |
| LINEITEMINCREMENT           | str  | ✅       | "LineItemIncrement"           |
| MATHABS                     | str  | ✅       | "MathABS"                     |
| MATHADD                     | str  | ✅       | "MathAdd"                     |
| MATHCEIL                    | str  | ✅       | "MathCeil"                    |
| MATHDIVIDE                  | str  | ✅       | "MathDivide"                  |
| MATHFLOOR                   | str  | ✅       | "MathFloor"                   |
| MATHMULTIPLY                | str  | ✅       | "MathMultiply"                |
| MATHSETPRECISION            | str  | ✅       | "MathSetPrecision"            |
| MATHSUBTRACT                | str  | ✅       | "MathSubtract"                |
| NUMBERFORMAT                | str  | ✅       | "NumberFormat"                |
| PROPERTYGET                 | str  | ✅       | "PropertyGet"                 |
| PROPERTYSET                 | str  | ✅       | "PropertySet"                 |
| RIGHTTRIM                   | str  | ✅       | "RightTrim"                   |
| RUNNINGTOTAL                | str  | ✅       | "RunningTotal"                |
| STRINGAPPEND                | str  | ✅       | "StringAppend"                |
| STRINGPREPEND               | str  | ✅       | "StringPrepend"               |
| STRINGREMOVE                | str  | ✅       | "StringRemove"                |
| STRINGREPLACE               | str  | ✅       | "StringReplace"               |
| STRINGTOLOWER               | str  | ✅       | "StringToLower"               |
| STRINGTOUPPER               | str  | ✅       | "StringToUpper"               |
| SUM                         | str  | ✅       | "Sum"                         |
| TRIMWHITESPACE              | str  | ✅       | "TrimWhitespace"              |
| STRINGCONCAT                | str  | ✅       | "StringConcat"                |
| STRINGSPLIT                 | str  | ✅       | "StringSplit"                 |
| SEQUENTIALVALUE             | str  | ✅       | "SequentialValue"             |
| SIMPLELOOKUP                | str  | ✅       | "SimpleLookup"                |
| DOCUMENTPROPERTYGET         | str  | ✅       | "DocumentPropertyGet"         |
| DOCUMENTPROPERTYSET         | str  | ✅       | "DocumentPropertySet"         |
| CROSSREFLOOKUP              | str  | ✅       | "CrossRefLookup"              |
| DOCUMENTCACHELOOKUP         | str  | ✅       | "DocumentCacheLookup"         |
| CUSTOMSCRIPTING             | str  | ✅       | "CustomScripting"             |
| USERDEFINED                 | str  | ✅       | "UserDefined"                 |
| JAPANESECHARACTERCONVERSION | str  | ✅       | "JapaneseCharacterConversion" |

