from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String)


def create_session(database_url: str):
    engine = create_engine(database_url)
    session = sessionmaker(bind=engine)
    return session()


def add_user(session: Session, username: str) -> int:
    user = User(username=username)
    session.add(user)
    session.commit()
    return user.id


def get_user(session: Session, user_id: int) -> User:
    result = session.query(User)
    return result.filter_by(id=user_id).first()


def main(database_url: str):
    with create_session(database_url) as session:
        user_id = add_user(session, "John Doe")
        print(f"Added user with ID {user_id}")

        user = get_user(session, user_id)
        print(f"Got user: {user.id}, {user.username}")


if __name__ == "__main__":
    main("sqlite:///my_database.db")
