import json

from fastapi import FastAPI
from models import TodoItem

app = FastAPI()


with open('todos.json') as f:
    TODOS = json.load(f)


@app.get('/todos')
async def get_todos(limit: int = 10):
    """Get a list of things to do"""
    return TODOS[0:limit]


@app.get('/todos/{todo_id}')
async def get_todo(todo_id: int):
    """Get a single to do item"""
    return TODOS[todo_id - 1]


@app.post('/todos', status_code=201)
async def create_todo(todo: TodoItem):
    item = todo.dict()
    item['id'] = len(TODOS) + 1
    return item
