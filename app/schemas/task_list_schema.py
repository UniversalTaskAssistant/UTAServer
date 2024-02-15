# app/schemas/task_list_schema.py

from pydantic import BaseModel
from typing import List

class TaskList(BaseModel):
    task_list: List