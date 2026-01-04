import json
from aiohttp import web
from src.services.task_service import TaskService

class Routes:
    @staticmethod
    async def add_task(request):
        try:
            data = await request.json()
            result = await TaskService.create_task(data)
            return web.json_response({"status": "200", "result": result})

        except Exception as e:
            return web.json_response({"status": "error", "message": str(e)}, status=500)

    @staticmethod
    async def get_tasks(request):
        try:
            tasks = await TaskService.list_tasks()
            return web.json_response({"status": "200", "data": tasks})

        except Exception as e:
            return web.json_response({"status": "error", "message": str(e)}, status=500)

    @staticmethod
    async def delete_task(request):
        try:
            task_id = request.query.get("id")
            if not task_id:
                return web.json_response({"status": "400", "error": "Missing id parameter"}, status=400)

            result = await TaskService.remove_task(int(task_id))
            return web.json_response({"status": "200", "result": result})

        except Exception as e:
            return web.json_response({"status": "error", "message": str(e)}, status=500)

def setup_routes(app):
    app.add_routes([
        web.post("/add_task", Routes.add_task),
        web.get("/get_tasks", Routes.get_tasks),
        web.get("/delete_task", Routes.delete_task)
    ])
