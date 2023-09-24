from pathlib import Path
import sqlite3
import os

# 正しいパスを構築
ddl_file_path = os.path.join(os.path.dirname(__file__), 'ddl', 'ddl.sql')

def execute_sql_file(filepath: str, connection: sqlite3.Connection) -> None:
    sql_script = Path(filepath).read_text()

    cursor = connection.cursor()
    cursor.executescript(sql_script)
    connection.commit()

if __name__ == "__main__":
    conn = sqlite3.connect('my_database.db')
    execute_sql_file(ddl_file_path, conn)  # 更新されたパスを使用
    conn.close()
