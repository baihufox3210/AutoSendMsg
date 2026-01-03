import sqlite3
import json

def init_db():
    connection = sqlite3.connect(r"src\database\database.db")

    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS tasks ( id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT NOT NULL )")
    connection.commit()
    connection.close()


def add_task(task: dict):
    connection = sqlite3.connect(r"src\database\database.db")
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO tasks (task) VALUES (?)",
        (json.dumps(task),)
    )
    connection.commit()
    connection.close()


def get_task():
    connection = sqlite3.connect(r"src\database\database.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()
    connection.close()

    return json.dumps(
        [{"id": row[0], "task": json.loads(row[1])} for row in rows],
        ensure_ascii=False
    )


def delete_task(task_id: int):
    connection = sqlite3.connect(r"src\database\database.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    connection.commit()
    connection.close()

init_db()