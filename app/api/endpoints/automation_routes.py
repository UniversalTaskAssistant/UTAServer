from fastapi import APIRouter, WebSocket
from ...services.database import SessionLocal
from ...services.UTA_services.automation import Automation, QueryRAI, CheckAction
from ...services.UTA_services.chat import Chat
from ...services.user_service import validate_token 
import os

router = APIRouter()

@router.websocket("/ws/automation")
async def automation_endpoint(websocket: WebSocket):
    async with SessionLocal() as db:
        uuid = await validate_token(db, websocket.query_params.get('token'))  
        if not uuid:
            await websocket.close(code=1008)
            return 
        Automation_instance = await Automation.create() 
    await websocket.accept()
    while True:
        # Receive file metadata
        metadata = await websocket.receive_json()
        file_size = metadata.get("file_size", 0)
        xml = metadata.get("xml", "")
        
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
        data.update({"ui_img_file": image_file, "ui_xml_file": xml_file})
        async for response in Automation_instance.automation(**data):
            try:
                await websocket.send_json(response)
            except:
                await websocket.send_text(response)

@router.websocket("/ws/checkaction")
async def automation_endpoint(websocket: WebSocket):
    async with SessionLocal() as db:
        uuid = await validate_token(db, websocket.query_params.get('token'))  
        if not uuid:
            await websocket.close(code=1008)
            return 
        CheckAction_instance = await CheckAction.create() 
    await websocket.accept()
    while True:
        # Receive file metadata
        metadata = await websocket.receive_json()
        file_size = metadata.get("file_size", 0)
        xml = metadata.get("xml", "")
        
        image_file = os.path.join("data", uuid, uuid + "_checkaction.png")
        xml_file = os.path.join("data", uuid, uuid + "_checkaction.xml")

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
        data.update({"ui_img_file": image_file, "ui_xml_file": xml_file})
        async for response in CheckAction_instance.checkaction(**data):
            await websocket.send_json(response)

@router.websocket("/ws/chat")
async def chat_endpoint(websocket: WebSocket):
    async with SessionLocal() as db:
        uuid = await validate_token(db, websocket.query_params.get('token'))  
        if not uuid:
            await websocket.close(code=1008)
            return 
        Chat_instance = await Chat.create() 
    await websocket.accept()
    while True:
        # Receive file metadata
        metadata = await websocket.receive_json()
        file_size = metadata.get("file_size", 0)
        if file_size: 
            image_file = os.path.join("data", uuid, uuid + "_chat.png")
            with open(image_file, "wb") as file:
                bytes_received = 0
                while bytes_received < file_size:
                    data = await websocket.receive_bytes()
                    file.write(data)
                    bytes_received += len(data)
                    progress = (bytes_received / file_size) * 100
                    await websocket.send_json({"type": "progress", "value": progress})

            # Process user message
            data = await websocket.receive_json()
            data.update({"ui_img_file": image_file})
        else:
            data = await websocket.receive_json()
        async for response in Chat_instance.chat(**data):
            await websocket.send_json(response)

@router.websocket("/ws/queryrai")
async def queryrai_endpoint(websocket: WebSocket):
    async with SessionLocal() as db:
        uuid = await validate_token(db, websocket.query_params.get('token'))  
        if not uuid:
            await websocket.close(code=1008)
            return 
        QueryRAI_instance = await QueryRAI.create() 
    await websocket.accept()
    while True:
        # Receive file metadata
        metadata = await websocket.receive_json()
        file_size = metadata.get("file_size", 0)
        
        image_file = os.path.join("data", uuid, uuid + "_rai.png")

        # Receive the file in chunks
        with open(image_file, "wb") as file:
            bytes_received = 0
            while bytes_received < file_size:
                data = await websocket.receive_bytes()
                file.write(data)
                bytes_received += len(data)
                progress = (bytes_received / file_size) * 100
                await websocket.send_json({"type": "progress", "value": progress})

        # Process user message
        data = await websocket.receive_json()
        data.update({"ui_img_file": image_file})
        async for response in QueryRAI_instance.queryrai(**data):
            await websocket.send_json(response)