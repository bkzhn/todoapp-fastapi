"""TodoApp."""

from fastapi import FastAPI 

from todoapp.containers import Container
from todoapp import endpoints


def create_app() -> FastAPI:
    container = Container()

    db = container.db()
    db.create_database()

    app = FastAPI()
    app.container = container
    app.include_router(endpoints.v1.v1)
    
    return app

app = create_app()
