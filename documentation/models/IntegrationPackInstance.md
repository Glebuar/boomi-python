# IntegrationPackInstance

**Properties**

| Name                           | Type            | Required | Description                                                                                                                                                                              |
| :----------------------------- | :-------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| process_id                     | List[ProcessId] | ❌       | A list of process IDs associated with the integration pack instance                                                                                                                      |
| id\_                           | str             | ❌       | A unique ID assigned by the system to the installed instance of the integration pack. This field populates only if you install the integration pack in the requesting account.           |
| integration_pack_id            | str             | ❌       | A unique ID assigned by the system to the integration pack.                                                                                                                              |
| integration_pack_override_name | str             | ❌       | The name of the installed instance of the integration pack. You can set this value only in the case of multi-install integration packs; its purpose is to distinguish between instances. |

