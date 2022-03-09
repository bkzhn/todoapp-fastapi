from contextlib import AbstractContextManager
from typing import Callable, Iterator
from sqlalchemy.orm import Session

from todoapp.exceptions.todo_exceptions import TodoNotFoundError
from todoapp.models.todo import Todo


class TodoRepository:
    """Todo repository class."""

    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    def get_all(self) -> Iterator[Todo]:
        with self.session_factory() as session:
            return session.query(Todo).all()

    def get_by_id(self, todo_id: int) -> Todo:
        with self.session_factory() as session:
            todo = (
                session.query(Todo)
                .filter(Todo.id == todo_id)
                .one_or_none()
            )

            if not todo:
                raise TodoNotFoundError(todo_id)

            return todo

    def add(self, title: str, is_completed: bool = False) -> Todo:
        with self.session_factory() as session:
            todo = Todo(
                title=title,
                is_completed=is_completed,
            )

            session.add(todo)
            session.commit()
            session.refresh(todo)

            return todo

    def delete_by_id(self, todo_id: int) -> None:
        with self.session_factory() as session:
            todo = Todo(
                title=title,
                is_completed=is_completed,
            )

            if not todo:
                raise TodoNotFoundError(todo_id)

            session.delete(todo)
            session.commit()

