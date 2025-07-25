# AtomDiskSpace

**Properties**

| Name                 | Type                         | Required | Description                                                                  |
| :------------------- | :--------------------------- | :------- | :--------------------------------------------------------------------------- |
| disk_space_directory | List[AtomDiskSpaceDirectory] | ❌       |                                                                              |
| quota_limit          | str                          | ❌       | The total amount of disk space available for consumption by this attachment. |
| raw_quota_limit      | int                          | ❌       | The total number of bytes available for consumption by this attachment.      |
| raw_total_size       | int                          | ❌       | The disk space in bytes that is already consumed by the given attachment.    |
| total_size           | str                          | ❌       | The size of disk space already consumed by the given attachment.             |

