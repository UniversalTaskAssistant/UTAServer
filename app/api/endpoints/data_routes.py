# app/api/v1/endpoints/data_routes.py
from fastapi import APIRouter, Depends, HTTPException, status, Body
from sqlalchemy.ext.asyncio import AsyncSession
from ...services.database import get_db_session
from fastapi.responses import JSONResponse
from ..dependencies import get_current_user
from ...services.UTA_services.fetch_data import (
    fetch_tasks,
    setup_user, 
    fetch_conversation,
    fetch_all_previouse_conversation_preview,
    fetch_all_previouse_task
)
from ...schemas.data_schema import (
    TaskList, 
    SetupUserQuery, 
    FetchConvQuery, 
    FetchAllConvPreviewQuery, 
    FetchAllTaskQuery, 
    ConversationResponse,
    AllConversationPreviewResponse,
    AllTaskResponse
)
router = APIRouter()

# Setup user
@router.post("/users/setup", response_model=SetupUserQuery)
async def setup_user_endpoint(setup_data: SetupUserQuery = Body(...), _: None = Depends(get_current_user)):
    try:
        user = await setup_user(**setup_data.model_dump())
        response = SetupUserQuery(**user.to_dict())
        return JSONResponse(content=response.model_dump()) 
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

# Fetch task list 
@router.get("/tasklist", response_model=TaskList)
async def fetch_task_list_endpoint(_: None = Depends(get_current_user)):
    try: 
        return await fetch_tasks()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
# Fetch conversation
@router.post("/conversation", response_model=ConversationResponse)
async def fetch_conversation_endpoint(fetch_query: FetchConvQuery = Body(...), _: None = Depends(get_current_user)):
    try: 
        result = await fetch_conversation(**fetch_query.model_dump())
        response = ConversationResponse(**result.to_dict())
        return JSONResponse(content=response.model_dump()) 
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
# Fetch all previous conversation previews
@router.post("/allconversationpreview", response_model=AllConversationPreviewResponse)
async def fetch_all_previouse_conversation_preview_endpoint(fetch_query: FetchAllConvPreviewQuery = Body(...), _: None = Depends(get_current_user)):
    try: 
        result = await fetch_all_previouse_conversation_preview(**fetch_query.model_dump())
        response = AllConversationPreviewResponse(**result)
        return JSONResponse(content=response.model_dump()) 
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
# Fetch all previous tasks
@router.post("/allprevioustask", response_model=AllTaskResponse)
async def fetch_conversation_endpoint(fetch_query: FetchAllTaskQuery = Body(...), _: None = Depends(get_current_user)):
    try: 
        result = await fetch_all_previouse_task(**fetch_query.model_dump())
        response = AllTaskResponse(**result)
        return JSONResponse(content=response.model_dump()) 
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))