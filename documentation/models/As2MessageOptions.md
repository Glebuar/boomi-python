# As2MessageOptions

**Properties**

| Name                 | Type                                 | Required | Description |
| :------------------- | :----------------------------------- | :------- | :---------- |
| subject              | str                                  | ✅       |             |
| attachment_cache     | str                                  | ❌       |             |
| attachment_option    | AttachmentOption                     | ❌       |             |
| compressed           | bool                                 | ❌       |             |
| data_content_type    | DataContentType                      | ❌       |             |
| encrypted            | bool                                 | ❌       |             |
| encryption_algorithm | As2MessageOptionsEncryptionAlgorithm | ❌       |             |
| max_document_count   | int                                  | ❌       |             |
| multiple_attachments | bool                                 | ❌       |             |
| signed               | bool                                 | ❌       |             |
| signing_digest_alg   | SigningDigestAlg                     | ❌       |             |

# AttachmentOption

**Properties**

| Name          | Type | Required | Description      |
| :------------ | :--- | :------- | :--------------- |
| BATCH         | str  | ✅       | "BATCH"          |
| DOCUMENTCACHE | str  | ✅       | "DOCUMENT_CACHE" |

# DataContentType

**Properties**

| Name           | Type | Required | Description      |
| :------------- | :--- | :------- | :--------------- |
| TEXTPLAIN      | str  | ✅       | "textplain"      |
| BINARY         | str  | ✅       | "binary"         |
| EDIFACT        | str  | ✅       | "edifact"        |
| EDIX12         | str  | ✅       | "edix12"         |
| APPLICATIONXML | str  | ✅       | "applicationxml" |
| TEXTXML        | str  | ✅       | "textxml"        |

# As2MessageOptionsEncryptionAlgorithm

**Properties**

| Name      | Type | Required | Description |
| :-------- | :--- | :------- | :---------- |
| NA        | str  | ✅       | "na"        |
| TRIPLEDES | str  | ✅       | "tripledes" |
| DES       | str  | ✅       | "des"       |
| RC2_128   | str  | ✅       | "rc2-128"   |
| RC2_64    | str  | ✅       | "rc2-64"    |
| RC2_40    | str  | ✅       | "rc2-40"    |
| AES128    | str  | ✅       | "aes-128"   |
| AES192    | str  | ✅       | "aes-192"   |
| AES256    | str  | ✅       | "aes-256"   |

# SigningDigestAlg

**Properties**

| Name   | Type | Required | Description |
| :----- | :--- | :------- | :---------- |
| SHA1   | str  | ✅       | "SHA1"      |
| SHA224 | str  | ✅       | "SHA224"    |
| SHA256 | str  | ✅       | "SHA256"    |
| SHA384 | str  | ✅       | "SHA384"    |
| SHA512 | str  | ✅       | "SHA512"    |

