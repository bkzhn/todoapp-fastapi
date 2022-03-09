from sqlalchemy import Column, String, Boolean, Integer

from todoapp.database import Base


class Todo(Base):
    """Todo model."""

    __tablename__ = "todos"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    is_completed = Column(Boolean, default=False)

    def __repr__(self):
        return f"<Todo(id={self.id}, " \
                f"title=\"{self.title}\, " \
                f"is_completed={self.is_completed})>"
