import asyncio

from datetime import datetime
from src.database.manager import db_manager
from src.services.discord import discord_service

class TaskService:
    @staticmethod
    async def create_task(data: dict):
        id = await db_manager.add_task(data)
        
        asyncio.create_task(TaskService._deferred_send(id, data))
        
        return {"status": "success", "message": "任務已排定延遲發送", "id": id}

    @staticmethod
    async def _deferred_send(id: int, data: dict):
        try:
            delay = max(0, data.get("time") - datetime.now().timestamp())
            await asyncio.sleep(delay)
            
            result = await discord_service.send_message(
                data.get("channel"),
                data.get("message")
            )

            if result and "error" not in result:
                await db_manager.updateStatus(id)

            else:
                print(f"Failed to send task {id}: {result}")

        except Exception as e:
            print(f"Error in deferred send: {e}")

    @staticmethod
    async def init_tasks():
        tasks = await db_manager.get_tasks()

        for task in tasks:
            if task["status"] == 0:
                asyncio.create_task(TaskService._deferred_send(task["id"], task["task"]))
    
    @staticmethod
    async def list_tasks():
        return await db_manager.get_tasks()

    @staticmethod
    async def remove_task(id: int):
        await db_manager.delete_task(id)
        return {"status": "success", "id": id}
