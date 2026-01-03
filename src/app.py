from aiohttp import web
from src.api.routes import setup_routes
from src.database.manager import db_manager
from src.services.task_service import TaskService

async def create_app():
    await db_manager.init_db()
    
    await TaskService.init_tasks()
    
    app = web.Application()
    setup_routes(app)
    
    return app