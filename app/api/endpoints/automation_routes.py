from fastapi import APIRouter, WebSocket
from ...services.database import SessionLocal
from ...services.UTA_services.automation import Automation
from ...services.UTA_services.declaration import Declaration
from ...services.user_service import validate_token 

router = APIRouter()

@router.websocket("/ws/automation")
async def automation_endpoint(websocket: WebSocket):
    async with SessionLocal() as db:
        await validate_token(db, websocket.query_params.get('token'))   
        Automation_instance = await Automation.create(db) 
    await websocket.accept()
    while True:
        # Receive file metadata
        metadata = await websocket.receive_json()
        file_size = metadata['size']
        file_name = metadata['name']
        
        # Receive the file in chunks
        with open(file_name, "wb") as file:
            bytes_received = 0
            while bytes_received < file_size:
                data = await websocket.receive_bytes()
                file.write(data)
                bytes_received += len(data)

        # Receive task message
        data = await websocket.receive_text()
        async with SessionLocal() as db:
            async for response in Automation_instance.automation(db, data):
                await websocket.send_json(response)
    
@router.websocket("/ws/declaration")
async def declaration_endpoint(websocket: WebSocket):
    async with SessionLocal() as db:
        await validate_token(db, websocket.query_params.get('token'))   
        Declaration_instance = await Declaration.create() 
    await websocket.accept()
    while True:
        data = await websocket.receive_json()
        async for response in Declaration_instance.declaration(data):
            await websocket.send_json(response)