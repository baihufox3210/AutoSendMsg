import json
import asyncio

from aiohttp import web
from datetime import datetime

from src.database import database

async def task(target):
    await asyncio.to_thread(database.add_task, target)

async def add_task(request):
    try:
        data = await request.json()
        await task(data)
        return web.json_response({"status": "200"})

    except Exception as e:
        return web.json_response({"status": "500", "error": str(e)})

async def get_task(request):
    return web.json_response(
        {
            "status": "200",
            "data": json.loads(database.get_task())
        }
    )

async def delete_task(request):
    try:
        id = request.query.get("id")
        await asyncio.to_thread(database.delete_task, id)
        return web.json_response({"status": "200"})

    except Exception as e:
        return web.json_response({"status": "500", "error": str(e)})

async def main():
    app = web.Application()
    app.add_routes([
        web.post("/add_task", add_task),
        web.get("/get_task", get_task),
        web.get("/delete_task", delete_task)
    ])

    runner = web.AppRunner(app)
    await runner.setup()

    site = web.TCPSite(runner, "0.0.0.0", 8000)
    await site.start()

    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())