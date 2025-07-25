
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap(
    {"cluster_problem": "clusterProblem", "host_name": "hostName", "node_id": "nodeId"}
)
class NodeDetails(BaseModel):
    """NodeDetails

    :param cluster_problem: Lists any issues reported for nodes.
    :type cluster_problem: str
    :param host_name: Displays the external host name or IP of the machine where the node currently lives.
    :type host_name: str
    :param node_id: Displays the unique identifier associated with a particular node in the Runtime cluster or Runtime cloud. A star icon indicates the cluster's head node.
    :type node_id: str
    :param status: Lists the nodes in the Runtime cluster or Runtime cloud and displays some basic information about each node. By default, the nodes are sorted by `status`. You can sort the list by `status`, `nodeId`, or `hostName`.
    :type status: str
    """

    def __init__(
        self, cluster_problem: str, host_name: str, node_id: str, status: str, **kwargs
    ):
        """NodeDetails

        :param cluster_problem: Lists any issues reported for nodes.
        :type cluster_problem: str
        :param host_name: Displays the external host name or IP of the machine where the node currently lives.
        :type host_name: str
        :param node_id: Displays the unique identifier associated with a particular node in the Runtime cluster or Runtime cloud. A star icon indicates the cluster's head node.
        :type node_id: str
        :param status: Lists the nodes in the Runtime cluster or Runtime cloud and displays some basic information about each node. By default, the nodes are sorted by `status`. You can sort the list by `status`, `nodeId`, or `hostName`.
        :type status: str
        """
        self.cluster_problem = cluster_problem
        self.host_name = host_name
        self.node_id = node_id
        self.status = status
        self._kwargs = kwargs
