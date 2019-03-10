import json

from fastapi import FastAPI, Query, Path
from models import TodoItem

app = FastAPI()

# temporary until a real DB is in place
with open('todos.json') as f:
    TODOS = json.load(f)


@app.get('/todos')
async def get_todos(
    limit: int = Query(None, description='Limit the number of items returned', le=100)
):
    """Get a list of things to do"""
    print(limit)
    return TODOS[0:limit]


@app.get('/todos/{todo_id}')
async def get_todo(
    todo_id: int = Path(..., description='A todo item ID number to lookup')
):
    """Get a single to do item"""
    return TODOS[todo_id - 1]


@app.post('/todos', status_code=201)
async def create_todo(todo: TodoItem):
    item = todo.dict()
    item['id'] = len(TODOS) + 1
    return item
