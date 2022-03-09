from fastapi import APIRouter, Depends, status
from dependency_injector.wiring import inject, Provide

from todoapp.containers import Container
from todoapp.services.todo_service import TodoService
from todoapp.exceptions.base_exceptions import NotFoundError
from todoapp.models.vo.todo import TodoVO


v1 = APIRouter()


@v1.get("/todos")
@inject
def get_list(
        todo_service: TodoService = Depends(Provide[Container.todo_service]),
    ):
    return todo_service.get_todos()

@v1.get("/todos/{todo_id}")
@inject
def get_by_id(
        todo_id: int,
        todo_service: TodoService = Depends(Provide[Container.todo_service]),
    ):
    try:
        return todo_service.get_todo_by_id(todo_id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)

@v1.post("/todos", status_code=status.HTTP_201_CREATED)
@inject
def add(
        todo: TodoVO,
        todo_service: TodoService = Depends(Provide[Container.todo_service]),
    ):
    return todo_service.create_todo(
        title=todo.title,
        is_completed=todo.is_completed,
    )

@v1.delete("/todos", status_code=status.HTTP_204_NO_CONTENT)
@inject
def remove(
        todo_id: int,
        todo_service: TodoService = Depends(Provide[Container.todo_service]),
    ):
    try:
        todo_service.delete_todo_by_id(todo_id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

@v1.get("/status")
def get_status():
    return {
        "status": "OK"
    }
