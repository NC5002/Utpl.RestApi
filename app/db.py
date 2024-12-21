import os

from sqlmodel import create_engine, SQLModel, Session

DATABASE_URL = "postgresql://usercomeencasa:87R7bCambVMT3EgTvVs6t4nu9Njsdh1e@dpg-cth2obhu0jms73fv33bg-a.oregon-postgres.render.com/dbapicomeencasa"

engine = create_engine(DATABASE_URL, echo=True)


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session