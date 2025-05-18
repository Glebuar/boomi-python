from typing import Callable, Dict, Any, Iterable, Optional


def paginate_query(
    first_call: Callable[[dict], Dict[str, Any]],
    more_call: Callable[[str], Dict[str, Any]],
    body: dict,
    *,
    parse_item: Optional[Callable[[Dict[str, Any]], Any]] = None,
    parse: bool = True,
) -> Iterable[Any]:
    """Yield items from a paginated query.

    Parameters
    ----------
    first_call:
        Function performing the initial query. It accepts the request body
        and returns the raw JSON response.
    more_call:
        Function performing subsequent ``queryMore`` calls given a token.
    body:
        Initial query payload.
    parse_item:
        Optional callable used to convert each result item into a model.
    parse:
        When ``True`` the ``parse_item`` callable is applied to each item.
    """
    data = first_call(body)
    while True:
        items = data.get("result", [])
        if parse and parse_item:
            for item in items:
                yield parse_item(item)
        else:
            for item in items:
                yield item
        token = data.get("queryToken")
        if not token:
            break
        data = more_call(token)
