import argparse
import sqlite3
from pathlib import Path


def exec_ddl(connection: sqlite3.Connection, ddl: str) -> None:
    cursor = connection.cursor()
    cursor.executescript(ddl)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create tables in a SQLite database.")
    parser.add_argument("--db", required=True, help="Path to the SQLite database file.")
    parser.add_argument("--ddl", required=True, help="Path to the DDL file.")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    db_file = args.db
    ddl_file = args.ddl

    ddl = Path(ddl_file).read_text()
    with sqlite3.connect(db_file) as connection:
        exec_ddl(connection, ddl)
