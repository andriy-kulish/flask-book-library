import os
from app import app
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


basedir = os.path.abspath(os.path.dirname(__file__))
exists = os.path.isfile(app.config['DATABASE'])
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + app.config['DATABASE']

engine = create_engine(SQLALCHEMY_DATABASE_URI, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    import models
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
