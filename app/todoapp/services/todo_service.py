from typing import Iterator

from todoapp.repositories.todo_repository import TodoRepository
from todoapp.models.todo import Todo


class TodoService:
    """Todo service class."""

    def __init__(self, todo_repository: TodoRepository) -> None:
        self._repository: TodoRepository = todo_repository

    def get_todos(self) -> Iterator[Todo]:
        return self._repository.get_all()

    def get_todo_by_id(self, todo_id: int) -> Todo:
        return self._repository.get_by_id(todo_id)

    def create_todo(self, title: str, is_completed: bool) -> Todo:
        return self._repository.add(
            title=title,
            is_completed=is_completed,
        )

    def delete_todo_by_id(self, todo_id: int) -> None:
        return self._repository.delete_by_id(todo_id)
