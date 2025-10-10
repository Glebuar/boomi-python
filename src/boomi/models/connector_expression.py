
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .connector_simple_expression import ConnectorSimpleExpression
from .connector_grouping_expression import ConnectorGroupingExpression


class ConnectorExpressionGuard(OneOfBaseModel):
    class_list = {
        "ConnectorSimpleExpression": ConnectorSimpleExpression,
        "ConnectorGroupingExpression": ConnectorGroupingExpression,
    }


ConnectorExpression = Union[ConnectorSimpleExpression, ConnectorGroupingExpression]
