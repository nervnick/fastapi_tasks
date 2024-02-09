from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Task(BaseModel):
    title: str
    description: str
    completed: Optional[bool] = False

tasks = []

@app.get("/tasks")
def read_tasks():
    return tasks

@app.get("/tasks/{task_id}")
def read_task(task_id: int):
    return tasks[task_id]

@app.post("/tasks")
def create_task(task: Task):
    tasks.append(task)
    return tasks[-1]

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    tasks[task_id] = task
    return tasks[task_id]

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    return tasks.pop(task_id)
