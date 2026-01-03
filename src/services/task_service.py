from src.database.manager import db_manager
from src.services.discord import discord_service

class TaskService:
    @staticmethod
    async def create_task(data: dict):
        await db_manager.add_task(data)
        
        channel = data.get("channel_id")
        message = data.get("message")
        
        return await discord_service.send_message(channel, message)
    
    @staticmethod
    async def list_tasks():
        return await db_manager.get_tasks()

    @staticmethod
    async def remove_task(task_id: int):
        await db_manager.delete_task(task_id)
        return {"status": "success", "id": task_id}
