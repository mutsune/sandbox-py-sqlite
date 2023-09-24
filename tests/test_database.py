import sqlite3
from pathlib import Path
from sqlite3 import Connection

import pytest

from db import setup_db
from src.app import add_user, get_user


@pytest.fixture
def db_connection() -> Connection:
    ddl_file = "db/ddl/ddl.sql"
    ddl = Path(ddl_file).read_text()
    with sqlite3.connect(":memory:") as connection:
        setup_db.exec_ddl(connection, ddl)
        yield connection


def test_add_and_get_user(db_connection: Connection) -> None:
    user_id: int = add_user(db_connection, "testuser")
    user: tuple = get_user(db_connection, user_id)
    assert user is not None
    assert user[0] == user_id
    assert user[1] == "testuser"
