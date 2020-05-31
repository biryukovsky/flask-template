from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from {{ cookiecutter.project_slug }}.config import Config


db_engine = create_engine(Config.DATABASE_URI)

db_session = scoped_session(sessionmaker(autoflush=False,
                                         autocommit=False,
                                         bind=db_engine))

Base = declarative_base()
Base.query = db_session.query_property()
