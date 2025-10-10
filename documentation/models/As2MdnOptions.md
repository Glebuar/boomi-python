# As2MdnOptions

**Properties**

| Name                | Type               | Required | Description |
| :------------------ | :----------------- | :------- | :---------- |
| external_url        | str                | ✅       |             |
| mdn_client_ssl_cert | PrivateCertificate | ✅       |             |
| mdn_ssl_cert        | PublicCertificate  | ✅       |             |
| mdn_digest_alg      | MdnDigestAlg       | ❌       |             |
| request_mdn         | bool               | ❌       |             |
| signed              | bool               | ❌       |             |
| synchronous         | Synchronous        | ❌       |             |
| use_external_url    | bool               | ❌       |             |
| use_ssl             | bool               | ❌       |             |

# MdnDigestAlg

**Properties**

| Name   | Type | Required | Description |
| :----- | :--- | :------- | :---------- |
| SHA1   | str  | ✅       | "SHA1"      |
| SHA224 | str  | ✅       | "SHA224"    |
| SHA256 | str  | ✅       | "SHA256"    |
| SHA384 | str  | ✅       | "SHA384"    |
| SHA512 | str  | ✅       | "SHA512"    |

# Synchronous

**Properties**

| Name  | Type | Required | Description |
| :---- | :--- | :------- | :---------- |
| SYNC  | str  | ✅       | "sync"      |
| ASYNC | str  | ✅       | "async"     |

