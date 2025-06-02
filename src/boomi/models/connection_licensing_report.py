
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .query_filter import QueryFilter


@JsonMap({"query_filter": "QueryFilter"})
class ConnectionLicensingReport(BaseModel):
    """ConnectionLicensingReport

    :param query_filter: query_filter
    :type query_filter: QueryFilter
    """

    def __init__(self, query_filter: QueryFilter, **kwargs):
        """ConnectionLicensingReport

        :param query_filter: query_filter
        :type query_filter: QueryFilter
        """
        self.query_filter = self._define_object(query_filter, QueryFilter)
        self._kwargs = kwargs
