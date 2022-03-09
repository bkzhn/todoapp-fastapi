from typing import Optional
from pydantic import BaseModel


class TodoVO(BaseModel):
    title: str
    is_completed: bool
    id: Optional[int] = None
