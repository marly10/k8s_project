from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

plants = []
tasks = []

class Plant(BaseModel):
    name: str
    type: str
    age: int

class Task(BaseModel):
    title: str
    description: str
    done: bool

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/plants")
async def create_plant(plant: Plant):
    plants.append(plant)
    return plant

@app.get("/plants")
async def read_plants():
    return plants

@app.get("/plants/{plant_id}")
async def read_plant(plant_id: int):
    return plants[plant_id]

@app.put("/plants/{plant_id}")
async def update_plant(plant_id: int, plant: Plant):
    plants[plant_id] = plant
    return plant

@app.delete("/plants/{plant_id}")
async def delete_plant(plant_id: int):
    plants.pop(plant_id)
    return {"message": "Plant deleted"}

@app.post("/tasks")
async def create_task(task: Task):
    tasks.append(task)
    return task

@app.get("/tasks")
async def read_tasks():
    return tasks

@app.get("/tasks/{task_id}")
async def read_task(task_id: int):
    return tasks[task_id]

@app.put("/tasks/{task_id}")
async def update_task(task_id: int, task: Task):
    tasks[task_id] = task
    return task

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    tasks.pop(task_id)
    return {"message": "Task deleted"}
