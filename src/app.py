import sqlite3
from sqlite3 import Connection, Cursor

DATABASE_PATH = "my_database.db"


def create_connection() -> Connection:
    connection: Connection = sqlite3.connect(DATABASE_PATH)
    return connection


def add_user(connection: Connection, username: str) -> int:
    cursor: Cursor = connection.cursor()
    cursor.execute("""INSERT INTO users (username) VALUES (?)""", (username,))
    connection.commit()
    return cursor.lastrowid


def get_user(connection: Connection, user_id: int) -> tuple:
    cursor: Cursor = connection.cursor()
    cursor.execute("""SELECT * FROM users WHERE id=?""", (user_id,))
    return cursor.fetchone()


if __name__ == "__main__":
    with create_connection() as connection:
        user_id = add_user(connection, "John Doe")
        print(f"Added user with ID {user_id}")

        user = get_user(connection, user_id)
        print(f"Got user: {user}")
