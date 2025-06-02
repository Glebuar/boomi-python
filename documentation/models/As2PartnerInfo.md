# As2PartnerInfo

**Properties**

| Name                             | Type              | Required | Description |
| :------------------------------- | :---------------- | :------- | :---------- |
| as2_id                           | str               | ✅       |             |
| client_ssl_certificate           | PublicCertificate | ✅       |             |
| encryption_public_certificate    | PublicCertificate | ✅       |             |
| mdn_signature_public_certificate | PublicCertificate | ✅       |             |
| signing_public_certificate       | PublicCertificate | ✅       |             |
| listen_attachment_settings       | AttachmentInfo    | ❌       |             |
| listen_auth_settings             | As2BasicAuthInfo  | ❌       |             |
| basic_auth_enabled               | bool              | ❌       |             |
| enabled_legacy_smime             | bool              | ❌       |             |
| messages_to_check_for_duplicates | int               | ❌       |             |
| reject_duplicate_messages        | bool              | ❌       |             |

