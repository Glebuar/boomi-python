# ExecutionRequest

**Properties**

| Name                       | Type                                     | Required | Description                                                                                                                                                                                                              |
| :------------------------- | :--------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| dynamic_process_properties | ExecutionRequestDynamicProcessProperties | ✅       | The full list of Dynamic Process properties within the specified Runtime, Runtime cluster, or cloud, where each property is defined by their name and value.                                                             |
| process_properties         | ExecutionRequestProcessProperties        | ✅       | The full list of Process properties within the specified Runtime, Runtime cluster, or cloud, where each property is defined by their name and value.                                                                     |
| atom_id                    | str                                      | ✅       | The ID of the Runtime on which to run the process. Locate the Runtime ID by navigating to **Manage** \\> **Runtime Management** on the user interface, and viewing the Runtime Information panel for a selected Runtime. |
| process_id                 | str                                      | ❌       | The ID of the process to run. You can find ID of a process by locating the process' **Component ID** in the **Revision History** dialog on the user interface.                                                           |
| process_name               | str                                      | ❌       |                                                                                                                                                                                                                          |
| record_url                 | str                                      | ❌       | \(Response-only field\) The ID of the process run. This field is returned in the initial POST response and is used in the subsequent call to find the corresponding run record.                                          |
| request_id                 | str                                      | ❌       |                                                                                                                                                                                                                          |

