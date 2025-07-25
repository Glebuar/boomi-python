# RosettaNetControlInfo

**Properties**

| Name                               | Type              | Required | Description |
| :--------------------------------- | :---------------- | :------- | :---------- |
| encryption_public_certificate      | PublicCertificate | ❌       |             |
| global_partner_classification_code | str               | ❌       |             |
| global_usage_code                  | GlobalUsageCode   | ❌       |             |
| partner_id                         | str               | ❌       |             |
| partner_id_type                    | PartnerIdType     | ❌       |             |
| partner_location                   | str               | ❌       |             |
| signing_public_certificate         | PublicCertificate | ❌       |             |
| supply_chain_code                  | str               | ❌       |             |

# GlobalUsageCode

**Properties**

| Name       | Type | Required | Description  |
| :--------- | :--- | :------- | :----------- |
| TEST       | str  | ✅       | "Test"       |
| PRODUCTION | str  | ✅       | "Production" |

# PartnerIdType

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| DUNS | str  | ✅       | "DUNS"      |

