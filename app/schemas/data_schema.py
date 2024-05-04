# app/schemas/data_schema.py

from pydantic import BaseModel
from typing import Tuple, List, Optional

class TaskList(BaseModel):
    task_list: List

class SetupUserQuery(BaseModel):
    user_id: str
    device_resolution: Tuple[int, int]
    app_list: List[str]

class FetchConvQuery(BaseModel):
    user_id: str
    conv_id: str

class FetchAllConvPreviewQuery(BaseModel):
    user_id: str

class FetchAllTaskQuery(BaseModel):
    user_id: str

class FetchAppListQuery(BaseModel):
    app_list: List

class ConversationResponse(BaseModel):
    user_id: str
    conv_id: str
    conversation: List

class AllConversationPreviewResponse(BaseModel):
    user_id: str
    conversation: List

class AllTaskResponse(BaseModel):
    user_id: str
    task: List

class SetAppRecommendTaskResponse(BaseModel):
    app_tasks: List