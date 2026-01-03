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

def test_tasks():
    print("=== 開始測試 ===")

    # 清空資料表，確保測試乾淨
    cursor = connection.cursor()
    cursor.execute("DELETE FROM tasks")
    connection.commit()

    # 新增測試資料
    add_task({"title": "test task 1", "done": False})
    add_task({"title": "test task 2", "done": True})

    # 取得資料
    result_json = get_task()
    print("取得資料（JSON）：")
    print(result_json)

    # 解析 JSON 驗證內容
    data = json.loads(result_json)
    assert len(data) == 2, "資料筆數應為 2"
    assert data[0]["task"]["title"] == "test task 1"

    # 刪除其中一筆
    delete_task(data[0]["id"])

    # 再次取得資料
    result_json = get_task()
    data = json.loads(result_json)
    assert len(data) == 1, "刪除後資料筆數應為 1"

    print("=== 測試通過 ===")

if __name__ == "__main__":
    test_tasks()