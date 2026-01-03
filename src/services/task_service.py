import asyncio

from datetime import datetime
from src.database.manager import db_manager
from src.services.discord import discord_service

class TaskService:
    @staticmethod
    async def create_task(data: dict):
        await db_manager.add_task(data)
        
        asyncio.create_task(TaskService._deferred_send(data))
        
        return {"status": "success", "message": "任務已排定延遲發送"}

    @staticmethod
    async def _deferred_send(data: dict):
        try:
            delay = data.get("time") - datetime.now().timestamp()
            print(f"Delay: {delay}")

            await asyncio.sleep(delay)

            print(f"Sending message to channel {data.get('channel')}")
            
            await discord_service.send_message(
                data.get("channel"),
                data.get("message")
            )
                
        except Exception as e:
            print(f"Error in deferred send: {e}")
    
    @staticmethod
    async def list_tasks():
        return await db_manager.get_tasks()

    @staticmethod
    async def remove_task(task_id: int):
        await db_manager.delete_task(task_id)
        return {"status": "success", "id": task_id}
