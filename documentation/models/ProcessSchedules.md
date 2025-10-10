# ProcessSchedules

**Properties**

| Name       | Type           | Required | Description                                                                        |
| :--------- | :------------- | :------- | :--------------------------------------------------------------------------------- |
| retry      | ScheduleRetry  | ❌       |                                                                                    |
| schedule   | List[Schedule] | ❌       |                                                                                    |
| atom_id    | str            | ❌       | A unique ID assigned by the system to the Runtime.                                 |
| id\_       | str            | ❌       | The object’s conceptual ID, which is synthesized from the process and Runtime IDs. |
| process_id | str            | ❌       | A unique ID assigned by the system to the process. Must not be a listener process. |

