import aiosqlite
import json
import os

class DatabaseManager:
    def __init__(self):
        self.db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "database.db")

    async def init_db(self):
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT NOT NULL, status INTEGER DEFAULT 0)")
            await db.commit()

    async def add_task(self, task_data: dict):
        async with aiosqlite.connect(self.db_path) as db:
            cursor = await db.execute("INSERT INTO tasks (task, status) VALUES (?, ?)", (json.dumps(task_data, ensure_ascii=False), 0))
            task_id = cursor.lastrowid
            await db.commit()
            return task_id

    async def get_tasks(self):
        async with aiosqlite.connect(self.db_path) as db:
            async with db.execute("SELECT id, task, status FROM tasks") as cursor:
                rows = await cursor.fetchall()
                return [{"id": row[0], "task": json.loads(row[1]), "status": bool(row[2])} for row in rows]

    async def updateStatus(self, id: int):
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute("UPDATE tasks SET status = ? WHERE id = ?", (1, id))
            await db.commit()

    async def delete_task(self, id: int):
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute("DELETE FROM tasks WHERE id = ?", (id,))
            await db.commit()

db_manager = DatabaseManager()