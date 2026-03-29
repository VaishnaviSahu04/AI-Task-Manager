from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

from database import (
    create_table,
    insert_task,
    get_all_tasks,
    update_task_status,
    delete_task,
    clear_tasks
)

from utils.extractor import extract_tasks

app = FastAPI()
create_table()


class MeetingInput(BaseModel):
    text: str


@app.get("/")
def home():
    return {"message": "AI Workflow System Running 🚀"}


# 🔥 ADD MEETING
@app.post("/add_meeting")
def add_meeting(data: MeetingInput):
    tasks = extract_tasks(data.text)

    # 🔥 Remove duplicates (important for competition)
    clear_tasks()

    priority_order = {"High": 1, "Medium": 2, "Low": 3}
    tasks = sorted(tasks, key=lambda x: priority_order[x["priority"]])

    today = datetime.today().date()

    for t in tasks:
        deadline_date = datetime.strptime(t["deadline"], "%Y-%m-%d").date()

        if deadline_date < today:
            status = "Overdue"
        else:
            status = "Pending"

        insert_task(
            t["task"],
            t["owner"],
            t["deadline"],
            t["priority"],
            status
        )

    return {
        "message": "Tasks extracted successfully",
        "tasks": tasks
    }


# 🔍 GET TASKS
@app.get("/get_tasks")
def get_tasks(owner: str = None, status: str = None):
    tasks = get_all_tasks()
    result = []

    for t in tasks:
        if owner and t[2] != owner:
            continue
        if status and t[5] != status:
            continue

        result.append({
            "id": t[0],
            "task": t[1],
            "owner": t[2],
            "deadline": t[3],
            "priority": t[4],
            "status": t[5]
        })

    return {"tasks": result}


# ✅ UPDATE STATUS
@app.put("/update_status/{task_id}")
def update_status(task_id: int, status: str):
    update_task_status(task_id, status)
    return {"message": "Task updated successfully"}


# ❌ DELETE TASK
@app.delete("/delete_task/{task_id}")
def delete(task_id: int):
    delete_task(task_id)
    return {"message": "Task deleted"}