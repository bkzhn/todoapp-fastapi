from dependency_injector import containers, providers

from todoapp.database import Database
from todoapp.repositories.todo_repository import TodoRepository
from todoapp.services.todo_service import TodoService


class Container(containers.DeclarativeContainer):
    """Container class."""

    wiring_config = containers.WiringConfiguration(modules=[".endpoints.v1"])

    config = providers.Configuration(yaml_files=["config.yaml"])

    #db = providers.Singleton(Database, db_url=config.db.url)
    db = providers.Singleton(Database, db_url="sqlite:///test.sqlite3")

    todo_repository = providers.Factory(
        TodoRepository,
        session_factory=db.provided.session,
    )

    todo_service = providers.Factory(
        TodoService,
        todo_repository=todo_repository,
    )
