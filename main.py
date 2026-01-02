import asyncio
from aiohttp import web
from datetime import datetime

async def task(target):
    await asyncio.sleep(1)
    print(target)

async def add_task(target):
    asyncio.create_task(task(target.json()))
    return web.json_response({"status": "ok"})

async def main():
    app = web.Application()
    app.add_routes([web.post("/add_task", add_task)])

    runner = web.AppRunner(app)
    await runner.setup()

    site = web.TCPSite(runner, "0.0.0.0", 8080)
    await site.start()

    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())