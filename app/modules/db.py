import os
from sqlmodel import Session, create_engine


def get_session() -> Session:
    conn_config = {
        "user" : "postgres",
        "pwd": "password",
        "host": "localhost",
        "port": 5433,
        "db": "db1"
    }
    # conn_config = {
    #     "user": os.environ["POSTGRES_USER"],
    #     "pwd": os.environ["POSTGRES_PASSWORD"],
    #     "host": os.environ["POSTGRES_HOST"],
    #     "port": os.environ["POSTGRES_PORT"],
    #     "db": os.environ["POSTGRES_DB"],
    # }
    # conn_string = "postgresql://{user}:{pwd}@{host}:{port}/{db}"
    conn_string = "postgresql://postgres:password@localhost:5433/db1"
    engine = create_engine(conn_string.format(**conn_config), echo=True)
    return Session(engine)
