class NotFoundError(Exception):
    """Not Found Error."""

    entity_name: str

    def __init__(self, entity_id: int):
        super().__init__(f"{self.entity_name} not found, id: {entity_id}")

