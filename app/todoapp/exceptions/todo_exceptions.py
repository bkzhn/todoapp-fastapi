from todoapp.exceptions.base_exceptions import NotFoundError


class TodoNotFoundError(NotFoundError):
    """Todo not found error."""

    entity_name: str = "Todo"
