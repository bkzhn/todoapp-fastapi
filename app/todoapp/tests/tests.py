import pytest
from unittest import mock
from fastapi.testclient import TestClient

from todoapp.exceptions.todo_exceptions import TodoNotFoundError
from todoapp.repositories.todo_repository import TodoRepository
from todoapp.models.todo import Todo
from todoapp.models.vo.todo import TodoVO
from todoapp.application import app


@pytest.fixture
def client():
    yield TestClient(app)


def test_get_list(client):
    repository_mock = mock.Mock(spec=TodoRepository)
    repository_mock.get_all.return_value = [
        Todo(id=1, title="First task", is_completed=False),
        Todo(id=2, title="Second task", is_completed=True),
        Todo(id=3, title="Third task", is_completed=False),
    ]

    with app.container.todo_repository.override(repository_mock):
        response = client.get("/todos")

    assert response.status_code == 200
    data = response.json()

    assert data == [
        {"id": 1, "title": "First task", "is_completed": False},
        {"id": 2, "title": "Second task", "is_completed": True},
        {"id": 3, "title": "Third task", "is_completed": False},
    ]


def test_get_by_id(client):
    repository_mock = mock.Mock(spec=TodoRepository)
    repository_mock.get_by_id.return_value = Todo(
        id=1,
        title="First task",
        is_completed=False,
    )

    with app.container.todo_repository.override(repository_mock):
        response = client.get("/todos/1")

    assert response.status_code == 200
    data = response.json()

    assert data == {"id": 1, "title": "First task", "is_completed": False}
    repository_mock.get_by_id.assert_called_once_with(1)



def test_get_by_id_404(client):
    repository_mock = mock.Mock(spec=TodoRepository)
    repository_mock.get_by_id.side_effect = TodoNotFoundError(1)

    with app.container.todo_repository.override(repository_mock):
        response = client.get("/todos/1")

    assert response.status_code == 404


#@mock.patch("todoapp.services.uuid4", return_value="xyz")
def test_add(_, client):
    repository_mock = mock.Mock(spec=TodoRepository)
    repository_mock.add.return_value = Todo(
        title="First task",
        is_completed=False,
    )

    with app.container.todo_repository.override(repository_mock):
        response = client.post(
            "/todos",
            json=TodoVO(title="First task", is_completed=False).dict(),
        )

    assert response.status_code == 201
    data = response.json()

    assert data == {"id": 1, "title": "First task", "is_completed": False}
    repository_mock.add.assert_called_once_with(title="First task", is_completed=False)


def test_remove(client):
    repository_mock = mock.Mock(spec=TodoRepository)

    with app.container.todo_repository.override(repository_mock):
        response = client.delete("/todos/1")

    assert response.status_code == 404


def test_status(client):
    response = client.get("/status")
    assert response.status_code == 200
    data = response.json()
    assert data == {"status": "OK"}
