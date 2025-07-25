# ReleaseIntegrationPackStatus

**Properties**

| Name                        | Type                                         | Required | Description                                                                                                                                                                                                                                                    |
| :-------------------------- | :------------------------------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| response_status_code        | int                                          | ✅       |                                                                                                                                                                                                                                                                |
| release_packaged_components | ReleasePackagedComponents                    | ❌       |                                                                                                                                                                                                                                                                |
| installation_type           | ReleaseIntegrationPackStatusInstallationType | ❌       | The type of integration pack. Possible values: - SINGLE — single attachment - MULTI — multiple attachment                                                                                                                                                      |
| integration_pack_id         | str                                          | ❌       | A unique ID assigned by the system to the integration pack.                                                                                                                                                                                                    |
| name                        | str                                          | ❌       | The name of the integration pack.                                                                                                                                                                                                                              |
| release_on_date             | str                                          | ❌       | Date for future release of integration pack. Date Format: yyyy-MM-dd                                                                                                                                                                                           |
| release_schedule            | ReleaseIntegrationPackStatusReleaseSchedule  | ❌       | Specify the type of release schedule for the integration pack. Possible values: - IMMEDIATELY — for immediate release - RELEASE_ON_SPECIFIED_DATE — for future release                                                                                         |
| release_status              | ReleaseStatus                                | ❌       | The type of release Status. Possible values: - INPROGRESS — for currently releasing integration pack - SUCCESS — for successfully released integration pack - SCHEDULED — for future release integration pack - ERROR — for any error resulting in the release |
| request_id                  | str                                          | ❌       | A unique ID assigned by the system to the integration pack release request.                                                                                                                                                                                    |

# ReleaseIntegrationPackStatusInstallationType

The type of integration pack. Possible values: - SINGLE — single attachment - MULTI — multiple attachment

**Properties**

| Name   | Type | Required | Description |
| :----- | :--- | :------- | :---------- |
| SINGLE | str  | ✅       | "SINGLE"    |
| MULTI  | str  | ✅       | "MULTI"     |

# ReleaseIntegrationPackStatusReleaseSchedule

Specify the type of release schedule for the integration pack. Possible values: - IMMEDIATELY — for immediate release - RELEASE_ON_SPECIFIED_DATE — for future release

**Properties**

| Name                   | Type | Required | Description                 |
| :--------------------- | :--- | :------- | :-------------------------- |
| IMMEDIATELY            | str  | ✅       | "IMMEDIATELY"               |
| RELEASEONSPECIFIEDDATE | str  | ✅       | "RELEASE_ON_SPECIFIED_DATE" |

# ReleaseStatus

The type of release Status. Possible values: - INPROGRESS — for currently releasing integration pack - SUCCESS — for successfully released integration pack - SCHEDULED — for future release integration pack - ERROR — for any error resulting in the release

**Properties**

| Name       | Type | Required | Description   |
| :--------- | :--- | :------- | :------------ |
| INPROGRESS | str  | ✅       | "IN_PROGRESS" |
| SUCCESS    | str  | ✅       | "SUCCESS"     |
| SCHEDULED  | str  | ✅       | "SCHEDULED"   |
| ERROR      | str  | ✅       | "ERROR"       |

