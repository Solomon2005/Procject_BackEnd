import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
folder_path = BASE_DIR / ".." / ".." / "data" / "my_database.sqlite"
folder_path = folder_path.resolve()


#Создание связи и подключение к ней
def BD_connect_table():
    connection = sqlite3.connect(folder_path)
    connection.row_factory=sqlite3.Row
    return connection

#Создание БД если её нет
def BD_create_table():
    conn = BD_connect_table()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            gender TEXT NOT NULL,
            age INTEGER NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()

#Добовляем пидора
def BD_create_user_table(first_name: str, last_name: str, gender: str, age: int):
    conn = BD_connect_table()
    cursor = conn.execute(
        "INSERT INTO users (first_name, last_name, gender, age) VALUES (?, ?, ?, ?)",
        (first_name, last_name, gender, age),
    )
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return {
        "id": new_id,
        "first_name": first_name,
        "last_name": last_name,
        "gender": gender,
        "age": age,
    }

#Возвращаем определёного пользователя
def BD_get_user_by_id(user_id: int):
    conn = BD_connect_table()
    row = conn.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
    print(row)
    conn.close()
    return dict(row) if row else None

#Возвращаем всех пользователей
def BD_get_all_users():
    conn = BD_connect_table()
    rows = conn.execute("SELECT * FROM users").fetchall()
    conn.close()
    return [dict(row) for row in rows]

#Проверка работоспособности
if __name__ == "__main__":
    BD_create_table()

    if not BD_get_all_users():
        BD_create_user_table(
            first_name="ван", last_name="ванов", gender="М", age=25
        )
        BD_create_user_table(
            first_name="Bван", last_name="ванов", gender="М", age=25
        )

    users = BD_get_all_users()
    print(users)