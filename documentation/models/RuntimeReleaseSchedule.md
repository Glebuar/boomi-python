# RuntimeReleaseSchedule

**Properties**

| Name          | Type         | Required | Description                                                                                                                                                                                                                                                                                                                                                           |
| :------------ | :----------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| atom_id       | str          | ✅       | The ID of the container for which you want to set a schedule.                                                                                                                                                                                                                                                                                                         |
| day_of_week   | str          | ✅       | The day of the week that you want to receive updates on the Runtime, Runtime cluster, or Runtime cloud. \<br /\> 1. Required if scheduleType is set to FIRST or LAST                                                                                                                                                                                                  |
| schedule_type | ScheduleType | ✅       | Required. Determines whether you want to receive the updates when available, and if so, whether you receive them in the first or second \(last\) week they are available prior to the .- FIRST - Update within the first week that updates are available\<br /\> 1. LAST - Update within the second week that updates are available\<br /\>2. NEVER - Update with the |
| time_zone     | str          | ✅       | The time zone of your set schedule. \<br /\>1. Must be a [valid time zone](/api/platformapi#section/Introduction/Valid-time-zones) \<br /\>2. Required if scheduleType is set to FIRST or LAST                                                                                                                                                                        |
| hour_of_day   | int          | ❌       | The hour of the day that you want to receive updates on the Runtime, Runtime cluster, or Runtime cloud. 1. Must be between 0-23\<br /\> 2. Required if scheduleType is set to FIRST or LAST                                                                                                                                                                           |

# ScheduleType

Required. Determines whether you want to receive the updates when available, and if so, whether you receive them in the first or second \(last\) week they are available prior to the .- FIRST - Update within the first week that updates are available\<br /\> 1. LAST - Update within the second week that updates are available\<br /\>2. NEVER - Update with the

**Properties**

| Name  | Type | Required | Description |
| :---- | :--- | :------- | :---------- |
| NEVER | str  | ✅       | "NEVER"     |
| FIRST | str  | ✅       | "FIRST"     |
| LAST  | str  | ✅       | "LAST"      |

