import json

from typing import List

from fastapi import FastAPI, Query, Path
from models import TodoItem

app = FastAPI()

# temporary until a real DB is in place
with open('todos.json') as f:
    TODOS = json.load(f)


@app.get('/todos', response_model=List[TodoItem], summary='Get a list of todo items')
async def get_todos(
    limit: int = Query(None, description='Limit the number of items returned', le=100)
):
    """Get a list of things to do"""
    return TODOS[0:limit]


@app.get('/todos/{todo_id}', response_model=TodoItem, summary='Get a single todo item')
async def get_todo(
    todo_id: int = Path(..., description='A todo item ID number to lookup')
):
    """Get a single to do item"""
    return TODOS[todo_id - 1]


@app.post('/todos', status_code=201, response_model=TodoItem, summary='Add a todo item')
async def create_todo(todo: TodoItem):
    item = todo.dict()
    item['id'] = len(TODOS) + 1
    return item
