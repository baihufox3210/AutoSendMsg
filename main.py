import asyncio
from aiohttp import web
from src.app import create_app

if __name__ == "__main__":
    app = asyncio.run(create_app())
    web.run_app(app, host="0.0.0.0", port=8000)