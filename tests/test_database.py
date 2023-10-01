from pathlib import Path

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from db import setup_db
from src.app import Base, add_user, find_user


@pytest.fixture
def db_session() -> Session:
    engine = create_engine("sqlite:///:memory:")
    session_maker = sessionmaker(bind=engine)
    ddl = Path("db/ddl/ddl.sql").read_text()
    with session_maker() as session:
        Base.metadata.drop_all(bind=engine)
        setup_db.exec_ddl(session, ddl)
        yield session


def test_add_and_get_user(db_session: Session) -> None:
    user_id: int = add_user(db_session, "testuser")
    user: tuple = find_user(db_session, user_id)
    assert user is not None
    assert user.user_id == user_id
    assert user.username == "testuser"
