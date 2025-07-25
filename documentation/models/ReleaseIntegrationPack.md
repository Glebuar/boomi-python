# ReleaseIntegrationPack

**Properties**

| Name                        | Type                                   | Required | Description                                                                                                                                                                                        |
| :-------------------------- | :------------------------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| release_packaged_components | ReleasePackagedComponents              | ❌       |                                                                                                                                                                                                    |
| id\_                        | str                                    | ❌       | The ID of the integration pack.                                                                                                                                                                    |
| installation_type           | ReleaseIntegrationPackInstallationType | ❌       | The type of integration pack. Possible values: - SINGLE — single attachment - MULTI — multiple attachment                                                                                          |
| name                        | str                                    | ❌       | The name of the integration pack.                                                                                                                                                                  |
| release_on_date             | str                                    | ❌       | Date for future release of integration pack. Date Format: yyyy-MM-dd                                                                                                                               |
| release_schedule            | ReleaseIntegrationPackReleaseSchedule  | ❌       | Specify the type of release schedule for the integration pack. Possible values: - IMMEDIATELY — for immediate release - RELEASE_ON_SPECIFIED_DATE — for future release                             |
| release_status_url          | str                                    | ❌       | The complete endpoint URL used to make a second call to the ReleaseIntegrationPackStatus object. It is provided for your convenience in the `releaseStatusUrl` field of the initial POST response. |
| request_id                  | str                                    | ❌       | A unique ID assigned by the system to the integration pack release request.                                                                                                                        |

# ReleaseIntegrationPackInstallationType

The type of integration pack. Possible values: - SINGLE — single attachment - MULTI — multiple attachment

**Properties**

| Name   | Type | Required | Description |
| :----- | :--- | :------- | :---------- |
| SINGLE | str  | ✅       | "SINGLE"    |
| MULTI  | str  | ✅       | "MULTI"     |

# ReleaseIntegrationPackReleaseSchedule

Specify the type of release schedule for the integration pack. Possible values: - IMMEDIATELY — for immediate release - RELEASE_ON_SPECIFIED_DATE — for future release

**Properties**

| Name                   | Type | Required | Description                 |
| :--------------------- | :--- | :------- | :-------------------------- |
| IMMEDIATELY            | str  | ✅       | "IMMEDIATELY"               |
| RELEASEONSPECIFIEDDATE | str  | ✅       | "RELEASE_ON_SPECIFIED_DATE" |

