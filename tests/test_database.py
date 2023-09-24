import pytest
from sqlite3 import Connection
from src.app import create_connection, create_table, add_user, get_user


@pytest.fixture
def db_connection() -> Connection:
    connection: Connection = create_connection()
    create_table(connection)
    yield connection
    connection.close()


def test_add_and_get_user(db_connection: Connection) -> None:
    user_id: int = add_user(db_connection, "testuser")
    user: tuple = get_user(db_connection, user_id)
    assert user is not None
    assert user[0] == user_id
    assert user[1] == "testuser"
