# RosettaNetMessageOptions

**Properties**

| Name                       | Type                                        | Required | Description |
| :------------------------- | :------------------------------------------ | :------- | :---------- |
| attachment_cache           | str                                         | ❌       |             |
| compressed                 | bool                                        | ❌       |             |
| content_transfer_encoding  | ContentTransferEncoding                     | ❌       |             |
| encrypt_service_header     | bool                                        | ❌       |             |
| encrypted                  | bool                                        | ❌       |             |
| encryption_algorithm       | RosettaNetMessageOptionsEncryptionAlgorithm | ❌       |             |
| signature_digest_algorithm | SignatureDigestAlgorithm                    | ❌       |             |
| signed                     | bool                                        | ❌       |             |

# ContentTransferEncoding

**Properties**

| Name   | Type | Required | Description |
| :----- | :--- | :------- | :---------- |
| BINARY | str  | ✅       | "binary"    |
| BASE64 | str  | ✅       | "base64"    |

# RosettaNetMessageOptionsEncryptionAlgorithm

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

# SignatureDigestAlgorithm

**Properties**

| Name   | Type | Required | Description |
| :----- | :--- | :------- | :---------- |
| SHA1   | str  | ✅       | "SHA1"      |
| SHA224 | str  | ✅       | "SHA224"    |
| SHA256 | str  | ✅       | "SHA256"    |
| SHA384 | str  | ✅       | "SHA384"    |
| SHA512 | str  | ✅       | "SHA512"    |

