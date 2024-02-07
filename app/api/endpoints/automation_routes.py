from fastapi import APIRouter, WebSocket
from ...services.database import SessionLocal
from ...services.UTA_services.automation import Automation
from ...services.UTA_services.declaration import Declaration
from ...services.user_service import validate_token 
import os

router = APIRouter()

@router.websocket("/ws/automation")
async def automation_endpoint(websocket: WebSocket):
    async with SessionLocal() as db:
        uuid = await validate_token(db, websocket.query_params.get('token'))   
        Automation_instance = await Automation.create() 
    await websocket.accept()
    while True:
        # Receive file metadata
        metadata = await websocket.receive_json()
        file_size = metadata.get('file_size')
        xml = metadata.get('xml')
        
        image_file = os.path.join("data", uuid, uuid + ".png")
        xml_file = os.path.join("data", uuid, uuid + ".xml")

        # Receive the file in chunks
        with open(image_file, "wb") as file:
            bytes_received = 0
            while bytes_received < file_size:
                data = await websocket.receive_bytes()
                file.write(data)
                bytes_received += len(data)
                progress = (bytes_received / file_size) * 100
                await websocket.send_json({"type": "progress", "value": progress})
        
        # Save XML file
        with open(xml_file, "w", encoding='utf-8') as file:
            file.write(xml)

        # Process user message
        data = await websocket.receive_json()
        data.update({"ui_img": image_file, "ui_xml": xml_file})
        async for response in Automation_instance.automation(data):
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