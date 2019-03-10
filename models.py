from pydantic import BaseModel, Schema


class TodoItem(BaseModel):
    title: str = Schema(..., description='The name of the todo item', max_length=100)
    completed: bool = False
