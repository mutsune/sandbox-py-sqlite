import argparse
from pathlib import Path

from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session, sessionmaker


def exec_ddl(session: Session, ddl: str) -> None:
    sql_text = text(ddl)
    session.execute(sql_text)
    session.commit()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create tables in a SQLite database.")
    parser.add_argument("--db", required=True, help="Path to the SQLite database file.")
    parser.add_argument("--ddl", required=True, help="Path to the DDL file.")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    db_file = f"sqlite:///{args.db}"
    ddl_file = args.ddl

    engine = create_engine(db_file)
    session_maker = sessionmaker(bind=engine)
    ddl = Path(ddl_file).read_text()
    with session_maker() as session:
        exec_ddl(session, ddl)
