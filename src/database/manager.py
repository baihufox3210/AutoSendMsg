import aiosqlite
import json
import os

class DatabaseManager:
    def __init__(self):
        self.db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "database.db")

    async def init_db(self):
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT NOT NULL)")
            await db.commit()

    async def add_task(self, task_data: dict):
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute("INSERT INTO tasks (task) VALUES (?)", (json.dumps(task_data, ensure_ascii=False),))
            await db.commit()

    async def get_tasks(self):
        async with aiosqlite.connect(self.db_path) as db:
            async with db.execute("SELECT id, task FROM tasks") as cursor:
                rows = await cursor.fetchall()
                return [{"id": row[0], "task": json.loads(row[1])} for row in rows]

    async def delete_task(self, task_id: int):
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
            await db.commit()

db_manager = DatabaseManager()