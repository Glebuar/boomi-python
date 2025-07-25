# NodeDetails

**Properties**

| Name            | Type | Required | Description                                                                                                                                                                                                            |
| :-------------- | :--- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| cluster_problem | str  | ✅       | Lists any issues reported for nodes.                                                                                                                                                                                   |
| host_name       | str  | ✅       | Displays the external host name or IP of the machine where the node currently lives.                                                                                                                                   |
| node_id         | str  | ✅       | Displays the unique identifier associated with a particular node in the Runtime cluster or Runtime cloud. A star icon indicates the cluster's head node.                                                               |
| status          | str  | ✅       | Lists the nodes in the Runtime cluster or Runtime cloud and displays some basic information about each node. By default, the nodes are sorted by `status`. You can sort the list by `status`, `nodeId`, or `hostName`. |

