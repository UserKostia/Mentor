from datetime import datetime
from fastapi import HTTPException
from typing import Optional, List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Task(BaseModel):
    name: str
    description: Optional[str] = "descripton"
    status: str = "not completed"
    date: datetime = datetime.now()


DATABASE = {}
id_counter = 1


# GET - read all tasks
@app.get("/tasks/", response_model=List[Task])
async def read_all_tasks():
    return list(DATABASE.values())


# GET - read task by id
@app.get("/tasks/{task_id}")
async def read_task_by_id(task_id: int):
    if task_id not in DATABASE:
        raise HTTPException(detail=f"Task with id = {task_id} not found", status_code=404)
    return DATABASE[task_id]


# POST - create task
@app.post("/task/", response_model=Task)
async def create_task(task: Task):
    global id_counter
    key = id_counter
    id_counter += 1
    DATABASE[key] = task.dict()
    return DATABASE[key]


# PATCH - update status task
@app.patch("/task/{task_id}", response_model=Task)
async def update_task_status(task_id: int, status: str):
    if task_id not in DATABASE:
        raise HTTPException(detail=f"Task with id = {task_id} not found", status_code=404)
    DATABASE[task_id]["status"] = status
    return DATABASE[task_id]


# DELETE - delete task by id
@app.delete("/task/{task_id}")
async def pop_task_by_id(task_id: int):
    if task_id not in DATABASE:
        raise HTTPException(detail=f"Task with id = {task_id} not found", status_code=404)
    del DATABASE[task_id]
    return {"message": f"Task with {task_id = } was deleted"}
