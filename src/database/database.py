import sqlite3
import json

connection = sqlite3.connect("src\database\database.db")

def init_db():
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS tasks ( id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT NOT NULL )")
    connection.commit()


def add_task(task: dict):
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO tasks (task) VALUES (?)",
        (json.dumps(task),)
    )
    connection.commit()


def get_task():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()

    return json.dumps(
        [{"id": row[0], "task": json.loads(row[1])} for row in rows],
        ensure_ascii=False
    )


def delete_task(task_id: int):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    connection.commit()

init_db()