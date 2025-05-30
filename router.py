from fastapi import APIRouter
from typing import Annotated
from fastapi import Depends

from repository import TaskRepository
from schemas import STaskAdd, STask, STaskId

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.post("/task")
async def add_task(task: Annotated[STaskAdd, Depends()]) -> STaskId:
    task_id = await TaskRepository.add_one(task)
    return {"add_task": True, "task_id": task_id}


@router.get("/task")
async def get_task() -> list[STask]:
    tasks = await TaskRepository.find_all()
    return tasks