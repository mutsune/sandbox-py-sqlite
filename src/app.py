import sqlite3
from sqlite3 import Connection, Cursor

def create_connection() -> Connection:
    connection: Connection = sqlite3.connect(':memory:')
    return connection

def create_table(connection: Connection) -> None:
    cursor: Cursor = connection.cursor()
    cursor.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT)''')
    connection.commit()

def add_user(connection: Connection, username: str) -> int:
    cursor: Cursor = connection.cursor()
    cursor.execute('''INSERT INTO users (username) VALUES (?)''', (username,))
    connection.commit()
    return cursor.lastrowid

def get_user(connection: Connection, user_id: int) -> tuple:
    cursor: Cursor = connection.cursor()
    cursor.execute('''SELECT * FROM users WHERE id=?''', (user_id,))
    return cursor.fetchone()
