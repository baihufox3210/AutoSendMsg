from aiohttp import web
from src.api.routes import setup_routes
from src.database.manager import db_manager

async def create_app():
    await db_manager.init_db()
    
    app = web.Application()
    setup_routes(app)
    
    return app