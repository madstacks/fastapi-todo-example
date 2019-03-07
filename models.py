from pydantic import BaseModel


class TodoItem(BaseModel):
    title: str
    completed: bool = False
